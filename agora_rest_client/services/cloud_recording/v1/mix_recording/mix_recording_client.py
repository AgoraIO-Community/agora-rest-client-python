from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_acquire import mix_recording_acquire
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_query import mix_recording_query
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_start import mix_recording_start
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_stop import mix_recording_stop
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_update_layout import mix_recording_update_layout
from agora_rest_client.services.cloud_recording.v1.mix_recording.api_update import mix_recording_update

class MixRecordingClient(CloudRecordingClient):
    """
    Mix recording client
    """
    
    def __init__(self):
        super(MixRecordingClient, self).__init__()

    def new_builder():
        return MixRecordingClient()

    def acquire(self, cname, uid, resource_expired_hour=72, exclude_resource_ids=[], region_affinity=0):
        return mix_recording_acquire(self, cname, uid, resource_expired_hour=resource_expired_hour, exclude_resource_ids=exclude_resource_ids, region_affinity=region_affinity)

    def query(self, resource_id, sid):
        return mix_recording_query(self, resource_id, sid)

    def start(self, resource_id, cname, uid, token, storage_config, recording_config=None):
        return mix_recording_start(self, resource_id, cname, uid, token, storage_config, recording_config=recording_config)

    def stop(self, resource_id, sid, cname, uid, async_stop=False):
        return mix_recording_stop(self, resource_id, sid, cname, uid, async_stop=async_stop)

    def update_layout(self, resource_id, sid, cname, uid, max_resolution_uid=None, mixed_video_layout=None, background_color=None,
        background_image=None, default_user_background_image=None, layout_config=None, background_config=None):
        return mix_recording_update_layout(self, resource_id, sid, cname, uid, max_resolution_uid=max_resolution_uid, mixed_video_layout=mixed_video_layout,
            background_color=background_color, background_image=background_image, default_user_background_image=default_user_background_image, 
            layout_config=layout_config, background_config=background_config)

    def update(self, resource_id, sid, cname, uid, stream_subscribe=None):
        return mix_recording_update(self, resource_id, sid, cname, uid, stream_subscribe=stream_subscribe)
