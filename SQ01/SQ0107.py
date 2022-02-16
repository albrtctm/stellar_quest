import requests
from stellar_sdk import Server, Keypair, Network, TransactionBuilder, Asset

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
random_keypair = Keypair.random()
other_keypair = Keypair.random()

source_account = server.load_account(source.public_key)
channel_account = server.load_account(random_keypair.public_key)

response = requests.get(
    "https://friendbot.stellar.org",
    params={'addr': random_keypair.public_key}
)

response = requests.get(
    "https://friendbot.stellar.org",
    params={'addr': random_keypair.public_key}
)

lumen = Asset("XLM", issuer=None)

transaction = (
    TransactionBuilder(
        source_account=channel_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_payment_op(
        destination=other_keypair.public_key,
        amount="10",
        asset=lumen,
        source=source.public_key,
    )
    .build()
)

transaction.sign(source.secret)
transaction.sign(random_keypair.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
