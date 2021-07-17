from SoundcloudClient import SoundcloudClient

class SoundcloudPlaylists(SoundcloudClient):

    def __init__(self):
        self.playlist_id = None
        self.secret_token = None
        self.access = []
        self.show_tracks = None
        self.title = None
        self.description = None
        self.sharing = None
        self.tracks = []


    def generate_queries(self):

        body = {}

        if self.title != None:
            body['title'] = self.title
        if self.description != None:
            body['description'] = self.description
        if self.sharing != None:
            body['sharing'] = self.sharing
        if len(self.tracks) > 0:
            body['tracks'] = self.tracks
        if self.secret_token != None:
            body['secret_token'] = self.secret_token
        if len(self.access) > 0:
            body['access'] = self.access
        if self.show_tracks != None:
            body['show_tracks'] = self.show_tracks
        return body

    def clear_queries(self):

        self.title = None
        self.description = None
        self.sharing = None
        self.tracks = []
        self.secret_token = None
        self.access = []
        self.show_tracks = None