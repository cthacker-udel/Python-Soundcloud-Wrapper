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



class MeRequests(SoundcloudClient):


    def __init__(self,client):
        self.client = client


    def return_user_info(self):



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










