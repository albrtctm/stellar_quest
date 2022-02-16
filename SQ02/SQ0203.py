import requests
from stellar_sdk import Server, Keypair, Network, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
random_keypair = Keypair.random()
source_account = server.load_account(source.public_key)
random_account = server.load_account(random_keypair.public_key)

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': random_keypair.public_key})

inner_transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
        v1=True
    ).append_bump_sequence_op(
        bump_to=1
    )
    .build()
)

inner_transaction.sign(source.secret)
bump_tx = TransactionBuilder.build_fee_bump_transaction(
    fee_source=random_keypair,
    base_fee=100,
    inner_transaction_envelope=inner_transaction,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
)

bump_tx.sign(random_keypair.secret)
response = server.submit_transaction(bump_tx)

if response:
    print(response)
else:
    print("Failed")
