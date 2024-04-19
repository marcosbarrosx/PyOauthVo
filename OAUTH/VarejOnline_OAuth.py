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
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        response = oauth.post(self.token_url, json)

    def RefreshToken(self):
        json = {
            'grant_type': 'refresh_token',
            'client_id': clientId,
            'client_secret': clientSecret,
            'refresh_token': ''
        }
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        response = oauth.post(self.token_url, json)

clientId = '661d332d84600b425d6e5703'
clientSecret = ''
authorizationCode = 'a8sd7fas87fd8a9s7d99'
redirect_uri = 'http://localhost:13653/oauth/callback.aspx'
token_url = 'https://erp.varejonline.com.br/apps/oauth/token'

token = ''
refreshToken = ''

client = BackendApplicationClient(client_id=clientId)
oauth = OAuth2Session(client=client)

token_request_data = {
    'grant_type' : 'authorization_code',
    'client_id' : clientId,
    'client_secret' : clientSecret,
    'redirect_uri' : redirect_uri,
    'code' : authorizationCode
}

token_refresh_data = {
    'grant_type': 'refresh_token',
    'client_id': clientId,
    'client_secret': clientSecret,
    'refresh_token': ''
}

# get token access
token_response = oauth.post(token_url, data=token_request_data)

# refresh token
token_response = oauth.post(token_url, data=token_refresh_data)

def GetToken():
    return token
def SetToken(value):
    token = value

