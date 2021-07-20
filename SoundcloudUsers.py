from SoundcloudClient import SoundcloudClient

class SoundcloudUsers(SoundcloudClient):

    def __init__(self):

        self.user_id = None
        self.limit = None
        self.offset = None

    def generate_queries(self):

        body = {}

        if self.limit != None:
            body['limit'] = self.limit
        if self.offset != None:
            body['offset'] = self.offset
        return body


    def clear_queries(self):

        self.limit = None
        self.offset = None
        self.user_id = None