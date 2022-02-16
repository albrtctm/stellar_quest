import sys
from stellar_sdk import Server, Keypair, Network, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)

balances = (server.claimable_balances()
    .for_claimant(source.public_key)
    .call())

balance_index = 0
try:
    balance_id = balances['_embedded']['records'][balance_index]['id']
except:
    print("balance_id not found")
    sys.exit()

transaction = TransactionBuilder(
    source_account=source_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
).append_claim_claimable_balance_op(
    balance_id=balance_id,
    source=source.public_key
).set_timeout(30).build()


transaction.sign(source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
