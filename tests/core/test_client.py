import logging
import os
import pytest
import requests
from agora_rest_client.core import exceptions
from agora_rest_client.core import errors
from agora_rest_client.core.client import Client
from agora_rest_client.core.domain import Domain
from agora_rest_client.core.domain import EndpointRegion
from agora_rest_client.core.domain import ServiceRegion

class TestClient:
    def setup_class(self):
        self._app_id = os.environ.get('AGORA_APP_ID')
        self._credential_basic_auth_user_name = os.environ.get('AGORA_CREDENTIAL_BASIC_AUTH_USER_NAME')
        self._credential_basic_auth_password = os.environ.get('AGORA_CREDENTIAL_BASIC_AUTH_PASSWORD')

    def test_init(self):
        client = Client \
            .new_builder() \
            .with_app_id(self._app_id) \
            .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
            .with_domain(Domain(EndpointRegion.CN.value, service_region=ServiceRegion.AP.value)) \
            .with_http_retry_count(2) \
            .with_http_timeout_seconds(15) \
            .build()

        assert client.app_id == self._app_id
        assert client.credential_basic_auth == (self._credential_basic_auth_user_name, self._credential_basic_auth_password)
        assert client.domain.get_endpoint_region() == EndpointRegion.CN.value
        assert client.domain.get_service_region() == ServiceRegion.AP.value
        assert client.http_retry_count == 2
        assert client.http_timeout_seconds == 15

    def test_build_error_app_id(self):
        with pytest.raises(exceptions.ClientBuildException) as e:
            client = Client \
                .new_builder() \
                .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
                .with_domain(Domain(EndpointRegion.CN.value)) \
                .build()

        assert e.value.__str__() == 'ClientBuildException - {status_code:[None],error_code:[None],error_msg:[app id is required]}'
        assert e.value.error_msg == errors.APP_ID_REQUIRED

    def test_build_error_basic_auth(self):
        with pytest.raises(exceptions.ClientBuildException) as e:
            client = Client \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_domain(Domain(EndpointRegion.CN.value)) \
                .build()

        assert e.value.__str__() == 'ClientBuildException - {status_code:[None],error_code:[None],error_msg:[credential basic auth is required]}'
        assert e.value.error_msg == errors.CREDENTIAL_BASIC_AUTH_REQUIRED

    def test_build_error_domain(self):
        with pytest.raises(exceptions.ClientBuildException) as e:
            client = Client \
                .new_builder() \
                .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
                .with_app_id(self._app_id) \
                .build()

        assert e.value.__str__() == 'ClientBuildException - {status_code:[None],error_code:[None],error_msg:[domain is required]}'
        assert e.value.error_msg == errors.DOMAIN_REQUIRED

    def test_build_error_endpoint_region(self):
        with pytest.raises(exceptions.ClientBuildException) as e:
            client = Client \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
                .with_domain(Domain(None)) \
                .build()

        assert e.value.__str__() == 'ClientBuildException - {status_code:[None],error_code:[None],error_msg:[endpoint region is required]}'
        assert e.value.error_msg == errors.ENDPOINT_REGION_REQUIRED

        with pytest.raises(exceptions.ClientBuildException) as e:
            client = Client \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
                .with_domain(Domain(-1)) \
                .build()

        assert e.value.__str__() == 'ClientBuildException - {status_code:[None],error_code:[None],error_msg:[endpoint region invalid]}'
        assert e.value.error_msg == errors.ENDPOINT_REGION_INVALID

    def test_call_api_error_404(self, mocker):
        fake_resp = mocker.Mock()
        fake_resp.status_code = 404

        client = Client \
            .new_builder() \
            .with_app_id(self._app_id) \
            .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
            .with_domain(Domain(EndpointRegion.CN.value)) \
            .with_stream_log(log_level=logging.DEBUG) \
            .build()

        mocker.patch("requests.request", return_value=fake_resp)
        resp = client.call_api('GET', '/')

        assert resp.status_code == 404

    def test_call_api_error_timeout(self, mocker):
        fake_resp = mocker.Mock()
        fake_resp.status_code = 404

        with pytest.raises(exceptions.ClientTimeoutException) as e:
            client = Client \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
                .with_domain(Domain(EndpointRegion.CN.value)) \
                .with_stream_log(log_level=logging.DEBUG) \
                .with_http_timeout_seconds(2) \
                .build()

            mocker.patch("requests.request", return_value=fake_resp, side_effect=requests.exceptions.HTTPError('mock http error'))
            resp = client.call_api('GET', '/')

        assert e.value.error_msg == "Function do_http_request (args=('GET', '/')) (kwargs={'params': None, 'post_data': None, 'post_json': None, 'headers': None, 'timeout_seconds': 10, 'trace_id': None}) timed out after 2.000000 seconds.\n"

    def test_do_http_request_error_404(self, mocker):
        fake_resp = mocker.Mock()
        fake_resp.status_code = 404

        client = Client \
            .new_builder() \
            .with_app_id(self._app_id) \
            .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
            .with_domain(Domain(EndpointRegion.CN.value)) \
            .with_stream_log(log_level=logging.DEBUG) \
            .build()

        mocker.patch("requests.request", return_value=fake_resp)
        resp = client.do_http_request('GET', '/')

        assert resp.status_code == 404

    def test_get_api_url(self):
        client = Client \
            .new_builder() \
            .with_app_id(self._app_id) \
            .with_credential_basic_auth(self._credential_basic_auth_user_name, self._credential_basic_auth_password) \
            .with_domain(Domain(EndpointRegion.CN.value)) \
            .with_stream_log(log_level=logging.DEBUG) \
            .build()

        assert client.get_api_url('api-cn-east-1.sd-rtn.com', '/v1') == 'https://api-cn-east-1.sd-rtn.com/v1'
        assert client.get_api_url('api-cn-east-1.sd-rtn.com', '/v1', ServiceRegion.NA.value) == 'https://api-cn-east-1.sd-rtn.com/na/v1'
        assert client.get_api_url('api-cn-east-1.sd-rtn.com', '/v1', ServiceRegion.AP.value) == 'https://api-cn-east-1.sd-rtn.com/ap/v1'

