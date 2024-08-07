# CardanoBI Python SDK

## Getting Started

To use this SDK you will first need to log in to [cardanobi.io](https://cardanobi.io).

Once logged in, create a new project and copy both the API Key and the API Secret.

You will need both of them to authenticate your API requests.

For more information please check out our [Quick Start Tutorial](https://docs.cardanobi.io/docs/getting-started/quick-start).

## Installation

```
$ git clone https://github.com/cardanobi/cardanobi-python.git
```

## Example

Let's get the details for the latest block on mainnet:
```python
import asyncio
import json
from cardanobi import CardanoBI

async def main():
    CBI = CardanoBI(apiKey="YOUR_API_KEY", apiSecret="YOUR_API_SECRET")
    latest = await CBI.core.blocks.latest_()
    print(json.dumps(latest, indent=4))
    await CBI.client.session.close()

asyncio.run(main())

```

Output
```js
{
  id: 8992460,
  hash: 'o9B9KPkKLxQnh3nHi2llQPe0IOr/pfaKJMv+gtVkv/s=',
  epoch_no: 421,
  slot_no: 96814945,
  epoch_slot_no: 306145,
  block_no: 8981926,
  previous_id: 8992459,
  slot_leader_id: 5512499,
  size: 17464,
  time: '2023-07-03T10:47:16',
  tx_count: 4,
  proto_major: 8,
  proto_minor: 0,
  vrf_key: 'vrf_vk1ys9nhj9yzzd7lwpgthrc2rrtekkaal7frdv86em07exn84vd658svuuk2x',
  op_cert: 't60ywMG+7Avgt3LobrmfvmvNVfC/6OBrEMHCe/C7OIY=',
  op_cert_counter: 9,
  hash_hex: 'a3d07d28f90a2f14278779c78b696540f7b420eaffa5f68a24cbfe82d564bffb',
  op_cert_hex: 'b7ad32c0c1beec0be0b772e86eb99fbe6bcd55f0bfe8e06b10c1c27bf0bb3886'
}
```

## API Reference Documentation

Please visit our [API Reference Documentation](https://docs.cardanobi.io/docs/introduction) for information about all our Domains and Endpoints.

## Tutorial

Please try one of our [Tutorials](https://docs.cardanobi.io/docs/category/tutorials) to get to know more about CardanoBI's capabilities.

## Contributions

CardanoBI is fully open-source and everyone is welcome to contribute. Please reach out to us via twitter (@CardanoBI), email (info@cardanobi.io) or by submitting a PR. :heart: