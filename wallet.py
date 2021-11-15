# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
from bit import *
from web3 import Web3

BTC

# Load and set environment variables
load_dotenv('mnemonic.env')
mnemonic=os.getenv("mnemonic")

mnemonic

# Create a function called `derive_wallets`
def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --cols=all --coin={coin} --numderive={depth} --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

derive_wallets()

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = coins = {
    ETH: derive_wallets(coin = ETH),
    BTCTEST: derive_wallets(coin = BTCTEST),
}
print(coins)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    elif coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    
Eth_PrivateKey = coins["eth"][0]['privkey']
Btc_PrivateKey = coins['btc-test'][1]['privkey']
print(Eth_PrivateKey)
print(Btc_PrivateKey)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin,account,to,amount):
    if coin == ETH:
        value= w3.toWei(amount,"ether")
        gas_estimate=w3.eth.estimateGas({'to':to,
                                        'from':account.address,
                                        'amount':value})
        gas_price=w3.eth.generateGasPrice()
        nonce=w3.eth.getTransactionCount(account.address)
        chainID=w3.eth.chain_id
        return {"to":to,
               'from':account.address,
               "value":value,
               "gas":gas_estimate,
               "gasPrice":gas_price,
               "nonce":nonce,
               "chainID":chainID}
            
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
    # Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin,account,to,amount):
    raw_tx = create_tx(coin,account,to,amount)
    if coin == ETH:
        signedtx=account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signedtx.rawTransaction)
                
                
    if coin== BTC:
        signedtx=account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signedtx)