from SoundcloudClient import SoundcloudClient

class SoundcloudMe(SoundcloudClient):

    def __init__(self):

        self.access = []
        self.limit = None


    def generate_queries(self):

        body = {}

        if len(self.access) > 0:
            body['acces'] = self.access
        if self.limit != None:
            body['limit'] = self.limit
        return body

    def clear_queries(self):

        self.access = []
        self.limit = None