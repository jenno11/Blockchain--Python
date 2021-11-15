# Blockchain--Python

##Derive a HD Wallet
wallet.py pf function 'derive_wallet':

command = f'./derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{num}" --cols=index,path,address,privkey,pubkey,pubkeyhash,xprv,xpub --format=json'

## Executing

from wallet import *
BTCTEST: derive_wallets(coin = BTCTEST)
ETH: derive_wallets(coin = ETH)
send_tx(BTCTEST, btc_acc, derive_wallets(mnemonic, BTCTEST, 5)[1]['address'], 0.001)
send_tx(ETH, eth_acc, derive_wallets(mnemonic, ETH, 5)[1]['address'], 0.1)

## Proof of Transactions

<img width="507" alt="Screen Shot 2021-11-15 at 4 55 05 pm" src="https://user-images.githubusercontent.com/84065878/141762330-d8123cf0-9bdb-4efd-8f83-f1e03534479f.png">
