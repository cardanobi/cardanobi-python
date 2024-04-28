import asyncio
from cardanobi import CardanoBI
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

apiKey = os.getenv('CBI_API_KEY')
apiSecret = os.getenv('CBI_API_SECRET')
network = os.getenv('CBI_ENV')

async def single():
    CBI = CardanoBI(apiKey=apiKey, apiSecret=apiSecret, network=network)
    # print(CBI.client.accessToken)

    # resp = await CBI.core.epochs.latest_()

    # resp = await CBI.core.epochs.epochsparams_()
    # resp = await CBI.core.epochs.epochsparams_(query="$count=true")
    # resp = await CBI.core.epochs.epochsparams_(query="$count=true&orderby=epoch_no desc&top=1")
    # resp = await CBI.core.epochs.epochsparams_(epoch_no=208)

    # resp = await CBI.core.epochs.params_()
    # resp = await CBI.core.epochs.params_(odata=1,query="$count=true")
    # resp = await CBI.core.epochs.params_(odata=1,query="$count=true")
    # resp = await CBI.core.epochs.params_(query="$count=true&orderby=epoch_no desc&top=2")
    # resp = await CBI.core.epochs.params_(epoch_no=208)

    # resp = await CBI.core.blocks.epochs.slots_(epoch_no=394, slot_no=85165743)
    # resp = await CBI.core.blocks.latest.pools_(pool_hash="pool1y24nj4qdkg35nvvnfawukauggsxrxuy74876cplmxsee29w5axc")
    # resp = await CBI.core.blocks.latest.transactions_()
    # resp = await CBI.core.blocks.pools.history_(pool_hash="pool1y24nj4qdkg35nvvnfawukauggsxrxuy74876cplmxsee29w5axc")

    # resp = await CBI.core.transactions_(transaction_hash="5f6f72b00ae982492823fb541153e6c2afc9cb7231687f2a5d82a994f61764a0")
    # resp = await CBI.core.transactions.utxos_(transaction_hash="5f6f72b00ae982492823fb541153e6c2afc9cb7231687f2a5d82a994f61764a0")
    resp = await CBI.core.transactions.utxos_(transaction_hash="e437901e028365c244b8e6d7afe2bada293a118bf6b3f5b3c3b24629593651be")
    

    print(json.dumps(resp, indent=4))
    
    await CBI.client.session.close()

async def multiple():
    CBI = CardanoBI(apiKey=apiKey, apiSecret=apiSecret, network=network)
    
    # Schedule the three calls to run concurrently
    results = await asyncio.gather(
        CBI.core.epochs.latest_(),
        CBI.core.epochs.latest_(),
        CBI.core.epochs.latest_()
    )
    
    for result in results:
        print(json.dumps(result, indent=4))

    await CBI.client.session.close()

if __name__ == '__main__':
    asyncio.run(single())
    # asyncio.run(multiple())
