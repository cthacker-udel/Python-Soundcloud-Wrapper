from SoundcloudClient import SoundcloudClient

class SoundcloudMe(SoundcloudClient):

    def __init__(self):

        self.access = []
        self.limit = None
        self.offset = None
        self.connection_id = None


    def generate_queries(self):

        body = {}

        if len(self.access) > 0:
            body['acces'] = self.access
        if self.limit != None:
            body['limit'] = self.limit
        if self.offest != None:
            body['offset'] = self.offset
        return body

    def clear_queries(self):

        self.access = []
        self.limit = None
        self.offset = None
        self.connection_id = None