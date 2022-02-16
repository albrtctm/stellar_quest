import requests
import hashlib
from stellar_sdk import Server, Keypair, Network, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
random_keypair = Keypair.random()
random_account = server.load_account(random_keypair.public_key)

response = requests.get(
    "https://friendbot.stellar.org",
    params={'addr': random_keypair.public_key}
)

memo_hash = hashlib.sha256()
memo_hash.update(b"[ADD MEMO]")

transaction = (
    TransactionBuilder(
        source_account=random_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_create_account_op(
    	destination=source.public_key,
    	starting_balance="5000",
    )
    .add_hash_memo(memo_hash.hexdigest())
    .build()
)

transaction.sign(random_keypair)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
