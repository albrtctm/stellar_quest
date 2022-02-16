import requests
from stellar_sdk import Server, Keypair, Network, Signer, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
random_source = Keypair.random()
source_account = server.load_account(source.public_key)

response = requests.get(
    'https://friendbot.stellar.org',
    params={
        'addr': random_source.public_key
    }
)

random_source_signer = Signer.ed25519_public_key(
    account_id=random_source.public_key,
    weight=1
)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_set_options_op(
        signer=random_source_signer
    )
    .build()
)
transaction.sign(source.secret)
response = server.submit_transaction(transaction)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_bump_sequence_op(
       bump_to=0
    )
    .build()
)
transaction.sign(random_source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
