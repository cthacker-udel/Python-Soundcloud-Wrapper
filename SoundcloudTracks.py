from SoundcloudClient import SoundcloudClient

class SoundcloudTracks(SoundcloudClient):

    def __init__(self):

        self.title = None
        self.asset_data = None
        self.permalink = None
        self.sharing = None
        self.embeddable_by = None
        self.purchase_url = None
        self.description = None
        self.genre = None
        self.tag_list = None
        self.label_name = None
        self.release = None
        self.release_date = None
        self.streamable = None
        self.downloadable = None
        self.license = None
        self.commentable = None
        self.isrc = None
        self.artwork_data = None
        self.secret_token = None
        self.track_id = None

    def generate_queries(self):

        body = {}

        if self.secret_token != None:
            body['secret_token'] = self.secret_token
        if self.title != None:
            body['track[title]'] = self.title
        if self.asset_data != None:
            body['track[asset_data]'] = self.asset_data
        if self.permalink != None:
            body['track[permalink]'] = self.permalink
        if self.sharing != None:
            body['track[sharing]'] = self.sharing
        if self.embeddable_by != None:
            body['track[embeddable_by]'] = self.embeddable_by
        if self.purchase_url != None:
            body['track[purchase_url]'] = self.purchase_url
        if self.description != None:
            body['track[description]'] = self.description
        if self.genre != None:
            body['track[genre]'] = self.genre
        if self.tag_list != None:
            body['track[tag_list]'] = self.tag_list
        if self.label_name != None:
            body['track[label_name]'] = self.label_name
        if self.release != None:
            body['track[release]'] = self.release
        if self.release_date != None:
            body['track[release_date]'] = self.release_date
        if self.streamable != None:
            body['track[streamable]'] = self.streamable
        if self.downloadable != None:
            body['track[downloadable]'] = self.downloadable
        if self.license != None:
            body['track[license]'] = self.license
        if self.commentable != None:
            body['track[commentable]'] = self.commentable
        if self.isrc != None:
            body['track[isrc]'] = self.isrc
        if self.artwork_data != None:
            body['track[artwork_data]'] = self.artwork_data
        return body

    def clear_queries(self):

        self.title = None
        self.asset_data = None
        self.permalink = None
        self.sharing = None
        self.embeddable_by = None
        self.purchase_url = None
        self.description = None
        self.genre = None
        self.tag_list = None
        self.label_name = None
        self.release = None
        self.release_date = None
        self.streamable = None
        self.downloadable = None
        self.license = None
        self.commentable = None
        self.isrc = None
        self.artwork_data = None
        self.secret_token = None
        self.track_id = None