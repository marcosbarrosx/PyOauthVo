from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class OAuth2:
    def __init__(self, clientId, clientSecret, authCode):
        self.client_id = clientId
        self.client_secret = clientSecret
        self.code = authCode
        self.redirect_uri = 'http://localhost:13653/oauth/callback.aspx'
        self.token_url = 'https://erp.varejonline.com.br/apps/oauth/token'

    def AccessToken(self):
        json = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': self.code
        }
        response = self.OauthPost(json)

    def RefreshToken(self):
        json = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': ''
        }
        response = self.OauthPost(json)

    def OauthPost(self, json):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        return oauth.post(self.token_url, json)