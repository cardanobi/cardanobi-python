import aiohttp
import base64
from urllib.parse import urlencode
from .constants import NETWORKS, API_BASE_URLS, IDS_BASE_URLS
from .misc import handleError

class APIClient:
    def __init__(self, apiKey=None, apiSecret=None, network='mainnet', baseURL=None, idsBaseURL=None, timeout=0, proxy=None, httpsAgent=None):
        self.apiKey = apiKey or 'onlypublic'
        self.apiSecret = apiSecret
        self.network = network or 'mainnet'
        # Assuming constants are defined elsewhere and imported
        self.baseURL = baseURL or API_BASE_URLS.get(self.network, '')
        self.idsBaseURL = idsBaseURL or IDS_BASE_URLS.get(self.network, '')
        self.timeout = timeout
        self.proxy = proxy
        self.httpsAgent = httpsAgent
        self.session = aiohttp.ClientSession()
        self.auth_token = base64.b64encode(f"{self.apiKey}:{self.apiSecret}".encode('utf-8')).decode('utf-8')
        self.accessToken = None

        # print(f"APIClient.__init__, apiKey: {self.apiKey}, network: {self.network}, baseURL: {self.baseURL}, idsBaseURL: {self.idsBaseURL}")

    async def init(self):
        if self.apiKey and self.apiSecret:
            await self.getAccessToken()

    async def getAccessToken(self):
        data = {'grant_type': 'client_credentials'}
        headers = {
            'Authorization': f'Basic {self.auth_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # print(f"APIClient.getAccessToken, baseURL: {self.baseURL}")

        async with self.session.post(f'{self.idsBaseURL}/connect/token', data=urlencode(data), headers=headers) as response:
            if response.status == 200:
                resp_json = await response.json()
                self.accessToken = resp_json.get('access_token')
                # print(f"APIClient.getAccessToken, accessToken: {self.accessToken}")

    async def getRequest(self, url, private=False):
        headers = self.prepare_headers(private)

        # print(f"APIClient.getRequest, url: {url}")
        
        async with self.session.get(url, headers=headers) as response:
            if response.status != 200:
                # Try to extract the JSON body, which might contain error details
                try:
                    error_details = await response.json()  # This is where you get the JSON content
                    # Assuming the JSON structure has an 'errors' key
                    errors = error_details.get('errors', 'No error details found.')
                except Exception as e:
                    # In case the response is not JSON or another error occurs
                    errors = f"Failed to parse error details: {str(e)}"

                return handleError(errors, response)
                # raise ApiError(f"API request failed with status {response.status}, URL: {url}")
            return await response.json()

    def prepare_headers(self, private):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Client-Api-Key': self.apiKey
        }
        if private and self.accessToken:
            headers['Authorization'] = f'Bearer {self.accessToken}'
        else:
            headers['Authorization'] = f'Basic {self.auth_token}'

        return headers
    
    async def getPrivate(self, path, params={}):
        if self.accessToken is None:
            await self.getAccessToken()

        url = f"{self.baseURL}{path}"

        print(f"APIClient.getPrivate, url: {url}")

        return await self.getRequest(url, private=True)

    async def getPublic(self, path, params={}):
        url = f"{self.baseURL}{path}"
        return await self.getRequest(url)

    async def close(self):
        await self.session.close()  # Remember to close the session when done
