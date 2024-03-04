import logging
import os
import pytest
from agora_rest_client.core import exceptions
from agora_rest_client.core.domain import EndpointRegion
from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient

class TestCloudRecordingClient:
    def setup_class(self):
        self._app_id = os.environ.get('AGORA_APP_ID')
        self._basic_auth_user_name = os.environ.get('AGORA_BASIC_AUTH_USER_NAME')
        self._basic_auth_password = os.environ.get('AGORA_BASIC_AUTH_PASSWORD')

    def test_init(self):
        cloud_recording_client = CloudRecordingClient \
            .new_builder() \
            .with_app_id(self._app_id) \
            .with_basic_auth(self._basic_auth_user_name, self._basic_auth_password) \
            .with_endpoint_region(EndpointRegion.CN.value) \
            .build()

        assert cloud_recording_client.app_id == self._app_id

    def test_call_api_error_404_json(self, mocker):
        fake_resp = mocker.Mock()
        fake_resp.json = mocker.Mock(return_value={'code': 'mock code', 'reason': 'mock reason'})
        fake_resp.status_code = 404

        with pytest.raises(exceptions.ServiceResponseException) as e:
            cloud_recording_client = CloudRecordingClient \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_basic_auth(self._basic_auth_user_name, self._basic_auth_password) \
                .with_endpoint_region(EndpointRegion.CN.value) \
                .with_stream_log(log_level=logging.DEBUG) \
                .build()

            mocker.patch("requests.request", return_value=fake_resp)
            resp = cloud_recording_client.call_api('GET', '/')

        assert e.value.status_code == 404
        assert e.value.error_code == 'mock code'
        assert e.value.error_msg == 'mock reason'

        fake_resp.json = mocker.Mock(return_value={'code': 'mock code', 'msg': 'mock reason'})
        fake_resp.text = "{'code': 'mock code', 'msg': 'mock reason'}"
        fake_resp.status_code = 404

        with pytest.raises(exceptions.ServiceResponseException) as e:
            cloud_recording_client = CloudRecordingClient \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_basic_auth(self._basic_auth_user_name, self._basic_auth_password) \
                .with_endpoint_region(EndpointRegion.CN.value) \
                .with_stream_log(log_level=logging.DEBUG) \
                .build()

            mocker.patch("requests.request", return_value=fake_resp)
            resp = cloud_recording_client.call_api('GET', '/')

        assert e.value.status_code == 404
        assert e.value.error_code == 'mock code'
        assert e.value.error_msg == "{'code': 'mock code', 'msg': 'mock reason'}"

    def test_call_api_error_404_text(self, mocker):
        fake_resp = mocker.Mock()
        fake_resp.json = mocker.Mock(return_value=None)
        fake_resp.text = 'code: mock code, reason: mock reason'
        fake_resp.status_code = 404

        with pytest.raises(exceptions.ServiceResponseException) as e:
            cloud_recording_client = CloudRecordingClient \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_basic_auth(self._basic_auth_user_name, self._basic_auth_password) \
                .with_endpoint_region(EndpointRegion.CN.value) \
                .with_stream_log(log_level=logging.DEBUG) \
                .build()

            mocker.patch("requests.request", return_value=fake_resp)
            resp = cloud_recording_client.call_api('GET', '/')

        assert e.value.status_code == 404
        assert e.value.error_code == None
        assert e.value.error_msg == 'code: mock code, reason: mock reason'

    def test_call_api_error_retry(self, mocker):
        fake_resp = mocker.Mock()
        fake_resp.json = mocker.Mock(return_value={'code': 'mock code', 'reason': 'mock reason'})
        fake_resp.status_code = 500

        with pytest.raises(exceptions.ClientRequestException) as e:
            cloud_recording_client = CloudRecordingClient \
                .new_builder() \
                .with_app_id(self._app_id) \
                .with_basic_auth(self._basic_auth_user_name, self._basic_auth_password) \
                .with_endpoint_region(EndpointRegion.CN.value) \
                .with_stream_log(log_level=logging.DEBUG) \
                .build()

            mocker.patch("requests.request", return_value=fake_resp)
            resp = cloud_recording_client.call_api('GET', '/', is_retry=True)

        assert e.value.status_code == 500
        assert e.value.error_code == 'mock code'
        assert e.value.error_msg == 'mock reason'
