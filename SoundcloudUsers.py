from SoundcloudClient import SoundcloudClient

class SoundcloudUsers(SoundcloudClient):

    def __init__(self):

        self.user_id = None
        self.limit = None
        self.offset = None
        self.linked_partitioning = None
        self.following_id = None

    def generate_queries(self):

        body = {}

        if self.limit != None:
            body['limit'] = self.limit
        if self.offset != None:
            body['offset'] = self.offset
        if self.linked_partitioning != None:
            body['linked_partitioning'] = self.linked_partitioning
        return body


    def clear_queries(self):

        self.limit = None
        self.offset = None
        self.user_id = None
        self.linked_partitioning = None
        self.following_id = None