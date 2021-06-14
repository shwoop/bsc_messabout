from web3 import Web3
import json
import pathlib
import requests

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
contract = '0x27ae27110350b98d564b9a3eed31baebc82d878d'
client_address = '0x110ba088d85505bd0818275f7b30693d397f0248'


abi_file = pathlib.Path('cummies.abi.json')
if not abi_file.exists():
    resp = requests.get(f'https://api.bscscan.com/api?module=contract&action=getabi&address={contract}')
    if not resp.status_code == 200:
        print('fucked getting abi')
        exit(1)
    abi_file.write_text(resp.json()['result'])
abi = json.loads(abi_file.read_text())


c = w3.eth.contract(Web3.toChecksumAddress(contract), abi=abi)
print(f'cummies @ {c.address}')
balance = c.functions.balanceOf(Web3.toChecksumAddress(client_address)).call()
print(f'balance for {client_address} is {balance}')

