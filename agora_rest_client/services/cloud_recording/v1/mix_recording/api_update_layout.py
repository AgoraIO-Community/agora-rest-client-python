from agora_rest_client.core import request
from agora_rest_client.services.cloud_recording.v1 import api_update_layout
from agora_rest_client.services.cloud_recording.v1.api import Mode

class LayoutConfig(api_update_layout.LayoutConfig):
    pass

class BackgroundConfig(api_update_layout.BackgroundConfig):
    pass

class ClientRequest(request.RequestObject):
    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.maxResolutionUid`
    """
    maxResolutionUid = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.mixedVideoLayout`
    """
    mixedVideoLayout = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundColor`
    """
    backgroundColor = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundImage`
    """
    backgroundImage = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.defaultUserBackgroundImage`
    """
    defaultUserBackgroundImage = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.layoutConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout.LayoutConfig`
    """
    layoutConfig = None

    """
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout.BackgroundConfig`
    """
    backgroundConfig = None

class RequestPathParamsApiUpdateLayout(api_update_layout.RequestPathParamsApiUpdateLayout):
    pass

class RequestBodyApiUpdateLayout(api_update_layout.RequestBodyApiUpdateLayout):
    pass

class ResponseApiUpdateLayout(api_update_layout.ResponseApiUpdateLayout):
    pass

def mix_recording_update_layout(client, resource_id, sid, cname, uid, max_resolution_uid=None, mixed_video_layout=None, background_color=None,
        background_image=None, default_user_background_image=None, layout_config=None, background_config=None, trace_id=None):
    """
    Mix recording update layout
    更新云端录制合流布局

    :type client: object
    :param client: MixRecordingClient object

    :type resource_id: str
    :param resource_id: resource id
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestPathParamsApiUpdate.resource_id`

    :type sid: str
    :param sid: sid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestPathParamsApiUpdate.sid`

    :type cname: str
    :param cname: cname
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestBodyApiUpdate.cname`

    :type uid: str
    :param uid: uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.RequestBodyApiUpdate.uid`

    :type max_resolution_uid: str
    :param max_resolution_uid: max resolution uid
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.maxResolutionUid`

    :type mixed_video_layout: int
    :param mixed_video_layout: mixed video layout
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.mixedVideoLayout`

    :type background_color: str
    :param background_color: background color
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundColor`

    :type background_image: str
    :param background_image: background image
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.backgroundImage`

    :type default_user_background_image: str
    :param default_user_background_image: default user background image
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.ClientRequest.defaultUserBackgroundImage`

    :type layout_config: object
    :param layout_config: layout config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.LayoutConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout.LayoutConfig`

    :type background_config: object
    :param background_config: background config
    :refer: `agora_rest_client.services.cloud_recording.v1.api_update_layout.BackgroundConfig`
    :value: instance of `agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout.BackgroundConfig`

    :type trace_id: string
    :param trace_id: trace id

    :return: response object ResponseApiUpdate
    """
    request_path_params_obj = RequestPathParamsApiUpdateLayout(
        mode=Mode.MIX.value,
        resource_id=resource_id,
        sid=sid
    )

    request_body_obj = RequestBodyApiUpdateLayout(
        cname=cname,
        uid=uid,
        clientRequest=ClientRequest()
    )

    if max_resolution_uid is not None:
        request_body_obj.clientRequest.maxResolutionUid = max_resolution_uid

    if mixed_video_layout is not None:
        request_body_obj.clientRequest.mixedVideoLayout = mixed_video_layout

    if background_color is not None:
        request_body_obj.clientRequest.backgroundColor = background_color

    if background_image is not None:
        request_body_obj.clientRequest.backgroundImage = background_image

    if default_user_background_image is not None:
        request_body_obj.clientRequest.defaultUserBackgroundImage = default_user_background_image

    if layout_config is not None:
        request_body_obj.clientRequest.layoutConfig = layout_config

    if background_config is not None:
        request_body_obj.clientRequest.backgroundConfig = background_config

    return api_update_layout.api_update_layout(client, request_path_params_obj=request_path_params_obj, request_body_obj=request_body_obj,
                                               response_obj=ResponseApiUpdateLayout, trace_id=trace_id)
