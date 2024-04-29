from utils import APIClient
from domains import Core
from domains import Bi

class CardanoBI:
    def __init__(self, apiKey=None, apiSecret=None, network='mainnet'):
        # Initialize APIClient and domain objects synchronously
        self.client = APIClient(apiKey=apiKey, apiSecret=apiSecret, network=network)
        self.core = Core(self.client)
        self.bi = Bi(self.client)
