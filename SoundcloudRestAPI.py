import time
from collections import OrderedDict
from urllib.parse import urlencode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
import requests
from requests.auth import HTTPBasicAuth
from SoundcloudClient import SoundcloudClient
from pprint import pprint

base_url = "https://api.soundcloud.com"


class OAuthRequests(SoundcloudClient):

    def __init__(self,client):
        self.client = client

    def server_side_oauth(self):

        body = {

            'response_type': self.client.response_type,
            'redirect_uri': self.client.redirect_uri,
            'client_id': self.client.client_id,
            'scope': self.client.scope,

        }

        try:
            br = webdriver.Firefox(FirefoxDriverManager().install())
        except Exception as e:
            try:
                br = webdriver.Chrome(ChromeDriverManager().install())
            except Exception as e:
                print('Unable to instantiate webdriver')
                return None

        query_string = []

        for eachkey in body.keys():
            query_string.append('{}={}'.format(eachkey,body[eachkey]))
        query_string = '&'.join(query_string)

        full_url = self.base_url + '?' + query_string

        br.get(full_url)

        time.sleep(5)

    def generateOAuth2Token(self):

        url = base_url + '/oauth2/token'

        body = {

            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': self.code

        }

        try:
            br = webdriver.Firefox(FirefoxDriverManager().install())
        except Exception as e:
            try:
                br = webdriver.Chrome(ChromeDriverManager().install())
            except Exception as e:
                print('unable to instantiate webdriver')
                return None

        request = requests.post(url,body=body)

        pprint(request)

    def generate_auth(self):

        str = 'OAuth {}'.format(self.access_token)

        return str



class MeRequests(SoundcloudClient):


    def __init__(self,client):
        self.client = client


    def return_user_info(self):

        url = base_url + '/me'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def return_user_activities(self):

        url = base_url + '/me/activities'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def get_recent_user_activities(self):

        url = base_url + '/me/activities/all/own'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def return_recent_track_activities(self):

        url = base_url + '/me/activities/tracks'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def list_user_connected_social_accounts(self):

        url = base_url + '/me/connections'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def get_users_connected_social_account(self):

        url = base_url + '/me/connections/{}'.format(self.client.SoundcloudMe.connection_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def get_favorited_liked_tracks(self):

        url = base_url + '/me/likes/tracks'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def get_favorited_liked_playlists(self):

        url = base_url + '/me/likes/playlists'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def get_user_follows(self):

        url = base_url + '/me/followings'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def get_user_followed_tracks(self):

        url = base_url + '/me/followings/tracks'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def follow_user(self):

        url = base_url + '/me/followings/{}'.format(self.client.SoundcloudMe.user_id)

        request = requests.put(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def delete_user(self):

        url = base_url + '/me/followings/{}'.format(self.client.SoundcloudMe.user_id)

        request = requests.delete(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def return_followers(self):

        url = base_url + '/me/followers'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def return_playlists(self):

        url = base_url + '/me/playlists'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

    def return_tracks(self):

        url = base_url + '/me/tracks'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudMe.generate_queries())

        pprint(request)

class SoundcloudSearch(SoundcloudClient):

    def __init__(self,client):
        self.client = client

    def track_search(self):

        url = base_url + '/tracks'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudSearch.generate_queries())

        pprint(request)

    def playlist_search(self):

        url = base_url + '/playlists'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudSearch.generate_queries())

        pprint(request)

    def user_search(self):

        url = base_url + '/users'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudSearch.generate_queries())

        pprint(request)

class SoundcloudPlaylists(SoundcloudClient):

    def __init__(self,client):
        self.client = client


    def create_playlist(self):

        url = base_url + '/playlists'

        request = requests.post(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def return_playlist(self):

        url = base_url + '/playlists/{}'.format(self.client.SoundcloudPlaylists.playlist_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudPlaylists.generate_queries())

        pprint(request)

    def update_playlist(self):

        url = base_url + '/playlists/{}'.format(self.client.SoundcloudPlaylists.playlist_id)

        request = requests.put(url,auth='OAuth {}'.format(self.access_token),body=self.client.SoundcloudPlaylists.generate_queries())

        pprint(request)

    def delete_playlist(self):

        url = base_url + '/playlists/{}'.format(self.client.SoundcloudPlaylists.playlist_id)

        request = requests.delete(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def get_playlist_tracks(self):

        url = base_url + '/playlists/{}/tracks'.format(self.client.SoundcloudPlaylists.playlist_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudPlaylists.generate_queries())

        pprint(request)

    def get_playlist_reposters(self):

        url = base_url + '/playlists/{}/reposters'.format(self.client.SoundcloudPlaylists.playlist_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudPlaylists.generate_queries())

        pprint(request)


class SoundcloudTracks(SoundcloudClient):

    def __init__(self,client):
        self.client = client

    def upload_track(self):

        url = base_url + '/tracks'

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

    def get_track(self):

        url = base_url + '/tracks/{}'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

    def update_track(self):

        url = base_url + '/tracks/{}'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

    def delete_track(self):

        url = base_url + '/tracks/{}'.format(self.client.SoundcloudTracks.track_id)

        request = requests.delete(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def get_track_streamable_urls(self):

        url = base_url + '/tracks/{}/streams'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

    def get_track_comments(self):

        url = base_url + '/tracks/{}/comments'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

    def get_track_new_comments(self):

        url = base_url + '/tracks/{}/comments'.format(self.client.SoundcloudTracks.track_id)

        request = requests.post(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def track_favoriters(self):

        url = base_url + '/tracks/{}/favoriters'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries)

        pprint(request)

    def get_track_reposters(self):

        url = base_url + '/tracks/{}/reposters'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

    def get_related_tracks(self):

        url = base_url + '/tracks/{}/related'.format(self.client.SoundcloudTracks.track_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudTracks.generate_queries())

        pprint(request)

class SoundcloudUsers(SoundcloudClient):

    def __init__(self,client):
        self.client = client

    def get_user(self):

        url = base_url + '/users/{}'.format(self.client.SoundcloudUsers.user_id);

        request = requests.get(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def get_users_comments(self):

        url = base_url + '/users/{}/comments'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.foramt(self.acces_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_liked_tracks(self):

        url = base_url + '/users/{}/favorites'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_followers(self):

        url = base_url + '/users/{}/followers'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_followings(self):

        url = base_url + '/users/{}/followings'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_specific_following(self):

        url = base_url + '/users/{}/followings/{}'.format(self.client.SoundcloudUsers.user_id,self.client.SoundcloudUsers.following_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token))

        pprint(request)

    def get_users_playlists(self):

        url = base_url + '/users/{}/playlists'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_tracks(self):

        url = base_url + '/users/{}/tracks'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_links(self):

        url = base_url + '/users/{}/web-profiles'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)

    def get_users_liked_tracks_v2(self):

        url = base_url + '/users/{}/likes/tracks'.format(self.client.SoundcloudUsers.user_id)

        request = requests.get(url,auth='OAuth {}'.format(self.access_token),params=self.client.SoundcloudUsers.generate_queries())

        pprint(request)






def main():

    client = SoundcloudClient()
    client.client_id = "iHyu48dtzozAdMNcWkh7jpfh9kY3V5YO"
    client.redirect_uri = "http://localhost:8888/callback/"
    client.response_type = "code"
    client.scope = "default"
    oAuth = OAuthRequests(client)
    oAuth.server_side_oauth()


if __name__ == '__main__':

    main()










