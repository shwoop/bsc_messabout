from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
contract = '0x27ae27110350b98d564b9a3eed31baebc82d878d'
client_address = '0x110ba088d85505bd0818275f7b30693d397f0248'

with open('cummies.abi.json', 'r') as f:
    abi = json.loads(f.read())

c = w3.eth.contract(Web3.toChecksumAddress(contract), abi=abi)
print('cummies @ %s' % c.address)
balance = c.functions.balanceOf(Web3.toChecksumAddress(client_address)).call()
print('balance = %s' % balance)

import pdb; pdb.set_trace()
print(1)
