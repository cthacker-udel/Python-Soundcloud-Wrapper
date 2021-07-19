from SoundcloudClient import SoundcloudClient

class SoundcloudTracks(SoundcloudClient):

    def __init__(self):

        self.track_title = None
        self.track_asset_data = None
        self.track_permalink = None
        self.track_sharing = None
        self.track_embeddable_by = None
        self.track_purchase_url = None
        self.track_description = None
        self.track_genre = None
        self.track_tag_list = None
        self.track_label_name = None
        self.track_release = None
        self.track_release_date = None
        self.track_streamable = None
        self.track_downloadable = None
        self.track_license = None
        self.track_commentable = None
        self.track_isrc = None
        self.track_artwork_data = None
        self.secret_token = None
        self.track_id = None

        self.title = None
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

        self.limit = None
        self.linked_partitioning = None

        self.access = []
        self.offset = None


    def generate_queries(self):

        body = {}

        if len(self.access) > 0:
            body['access'] = self.access
        if self.offset != None:
            body['offset'] = self.offset
        if self.limit != None:
            body['limit'] = self.limit
        if self.linked_partitioning != None:
            body['linked_partitioning'] = self.linked_partitioning
        if self.title != None:
            body['title'] = self.title
        if self.permalink != None:
            body['permalink'] = self.permalink
        if self.sharing != None:
            body['sharing'] = self.sharing
        if self.embeddable_by != None:
            body['embeddable_by'] = self.embeddable_by
        if self.purchase_url != None:
            body['purchase_url'] = self.purchase_url
        if self.description != None:
            body['description'] = self.description
        if self.genre != None:
            body['genre'] = self.genre
        if self.tag_list != None:
            body['tag_list'] = self.tag_list
        if self.label_name != None:
            body['label_name'] = self.label_name
        if self.release != None:
            body['release'] = self.release
        if self.release_date != None:
            body['release_date'] = self.release_date
        if self.streamable != None:
            body['streamable'] = self.streamable
        if self.downloadable != None:
            body['downloadable'] = self.downloadable
        if self.license != None:
            body['license'] = self.license
        if self.commentable != None:
            body['commentable'] = self.commentable
        if self.isrc != None:
            body['isrc'] = self.isrc
        if self.secret_token != None:
            body['secret_token'] = self.secret_token
        if self.title != None:
            body['track[title]'] = self.track_title
        if self.track_asset_data != None:
            body['track[asset_data]'] = self.track_asset_data
        if self.permalink != None:
            body['track[permalink]'] = self.track_permalink
        if self.sharing != None:
            body['track[sharing]'] = self.track_sharing
        if self.embeddable_by != None:
            body['track[embeddable_by]'] = self.track_embeddable_by
        if self.purchase_url != None:
            body['track[purchase_url]'] = self.track_purchase_url
        if self.description != None:
            body['track[description]'] = self.track_description
        if self.genre != None:
            body['track[genre]'] = self.track_genre
        if self.tag_list != None:
            body['track[tag_list]'] = self.track_tag_list
        if self.label_name != None:
            body['track[label_name]'] = self.track_label_name
        if self.release != None:
            body['track[release]'] = self.track_release
        if self.release_date != None:
            body['track[release_date]'] = self.track_release_date
        if self.streamable != None:
            body['track[streamable]'] = self.track_streamable
        if self.downloadable != None:
            body['track[downloadable]'] = self.track_downloadable
        if self.license != None:
            body['track[license]'] = self.track_license
        if self.commentable != None:
            body['track[commentable]'] = self.track_commentable
        if self.isrc != None:
            body['track[isrc]'] = self.track_isrc
        if self.track_artwork_data != None:
            body['track[artwork_data]'] = self.track_artwork_data
        return body

    def clear_queries(self):

        self.access = []
        self.offset = None
        self.track_title = None
        self.track_asset_data = None
        self.track_permalink = None
        self.track_sharing = None
        self.track_embeddable_by = None
        self.track_purchase_url = None
        self.track_description = None
        self.track_genre = None
        self.track_tag_list = None
        self.track_label_name = None
        self.track_release = None
        self.track_release_date = None
        self.track_streamable = None
        self.track_downloadable = None
        self.track_license = None
        self.track_commentable = None
        self.track_isrc = None
        self.track_artwork_data = None
        self.secret_token = None
        self.track_id = None
        self.title = None
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
        self.limit = None
        self.linked_partitioning = None