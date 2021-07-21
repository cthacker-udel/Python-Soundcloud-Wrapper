from SoundcloudClient import SoundcloudClient

class SoundcloudMisc(SoundcloudClient):

    def __init__(self):

        self.url = None

    def generate_queries(self):

        body = {}

        if self.url != None:
            body['url'] = self.url

        return body

    def clear_queries(self):

        return None