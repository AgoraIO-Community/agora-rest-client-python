from agora_rest_client.services.cloud_recording.v1.api import SnapshotType
from agora_rest_client.services.cloud_recording.v1.cloud_recording_client import CloudRecordingClient
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_acquire import individual_recording_acquire
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_query import individual_recording_query
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_start import individual_recording_start
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_stop import individual_recording_stop
from agora_rest_client.services.cloud_recording.v1.individual_recording.api_update import individual_recording_update

class IndividualRecordingClient(CloudRecordingClient):
    """
    Individual recording client
    """
    
    def __init__(self):
        super(IndividualRecordingClient, self).__init__()

    def new_builder():
        return IndividualRecordingClient()

    def acquire(self, cname, uid, enable_postpone_transcoding_mix=False, resource_expired_hour=72, exclude_resource_ids=[], region_affinity=0):
        return individual_recording_acquire(self, cname, uid, enable_postpone_transcoding_mix=enable_postpone_transcoding_mix, 
            resource_expired_hour=resource_expired_hour, exclude_resource_ids=exclude_resource_ids, region_affinity=region_affinity)

    def query(self, resource_id, sid):
        return individual_recording_query(self, resource_id, sid)

    def start(self, resource_id, cname, uid, token, storage_config, recording_config=None, snapshot_type=SnapshotType.SNAPSHOT_AND_RECORDING.value,
            snapshot_config=None, apps_collection=None, transcode_options=None):
        return individual_recording_start(self, resource_id, cname, uid, token, storage_config, recording_config=recording_config, 
            snapshot_type=snapshot_type, snapshot_config=snapshot_config, apps_collection=apps_collection, transcode_options=transcode_options)

    def stop(self, resource_id, sid, cname, uid, async_stop=False):
        return individual_recording_stop(self, resource_id, sid, cname, uid, async_stop=async_stop)

    def update(self, resource_id, sid, cname, uid, stream_subscribe=None):
        return individual_recording_update(self, resource_id, sid, cname, uid, stream_subscribe=stream_subscribe)
