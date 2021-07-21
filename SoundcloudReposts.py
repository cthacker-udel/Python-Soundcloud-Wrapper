from SoundcloudClient import SoundcloudClient

class SoundcloudReposts(SoundcloudClient):

    def __init__(self):
        self.track_id = None
        self.playlist_id = None


    def generate_queries(self):
        return None

    def clear_queries(self):
        return None