from agora_rest_client.core import response
from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.web_recording.api_acquire import web_recording_acquire
from agora_rest_client.services.cloud_recording.v1.web_recording.api_query import web_recording_query
from agora_rest_client.services.cloud_recording.v1.web_recording.api_start import web_recording_start
from agora_rest_client.services.cloud_recording.v1.web_recording.api_stop import web_recording_stop
from agora_rest_client.services.cloud_recording.v1.web_recording.api_update import web_recording_update

class WebRecordingClient(CloudRecordingClient):
    """
    Web recording client
    """
    
    def __init__(self):
        super(WebRecordingClient, self).__init__()

    def new_builder():
        return WebRecordingClient()

    def acquire(self, cname, uid, resource_expired_hour=72, exclude_resource_ids=[], region_affinity=0):
        return web_recording_acquire(self, cname, uid, resource_expired_hour=resource_expired_hour, exclude_resource_ids=exclude_resource_ids, region_affinity=region_affinity)

    def query(self, resource_id, sid):
        return web_recording_query(self, resource_id, sid)

    def start(self, resource_id, cname, uid, storageConfig, extensionServiceConfig):
        return web_recording_start(self, resource_id, cname, uid, storageConfig, extensionServiceConfig)

    def stop(self, resource_id, sid, cname, uid, async_stop=False):
        return web_recording_stop(self, resource_id, sid, cname, uid, async_stop=async_stop)

    def update(self, resource_id, sid, cname, uid, web_recording_config=None, rtmp_publish_config=None):
        return web_recording_update(self, resource_id, sid, cname, uid, web_recording_config=web_recording_config, rtmp_publish_config=rtmp_publish_config)
