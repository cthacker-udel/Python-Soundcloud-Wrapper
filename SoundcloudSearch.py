from SoundcloudClient import SoundcloudClient

class SoundcloudSearch(SoundcloudClient):

    def __init__(self):
        self.q = None
        self.ids = []
        self.genres = []
        self.tags = []
        self.bpm = None
        self.duration = None
        self.created_at = None
        self.access = []
        self.limit = None
        self.offset = None
        self.linked_partitioning = None
        self.show_tracks = None

    def generate_queries(self):

        body = {}

        if self.show_tracks != None:
            body['show_tracks'] = self.show_tracks
        if self.q != None:
            body['q'] = self.q
        if len(self.ids) > 0:
            body['ids'] = ','.join(self.ids)
        if len(self.genres) > 0:
            body['genres'] = ','.join(self.genres)
        if len(self.tags) > 0:
            body['tags'] = ','.join(self.tags)
        if self.bpm != None:
            body['bpm'] = self.bpm
        if self.duration != None:
            body['duration'] = self.duration
        if self.created_at != None:
            body['created_at'] = self.created_at
        if len(self.access) != None:
            body['access'] = self.access
        if self.limit != None:
            body['limit'] = self.limit
        if self.offset != None:
            body['offset'] = self.offset
        if self.linked_partitioning != None:
            body['linked_partitioning'] = self.linked_partitioning
        return body

    def clear_queries(self):

        self.q = None
        self.ids = []
        self.genres = []
        self.tags = []
        self.bpm = None
        self.duration = None
        self.created_at = None
        self.access = []
        self.limit = None
        self.offset = None
        self.linked_partitioning = None
        self.show_tracks = None