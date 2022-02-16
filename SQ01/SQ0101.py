from stellar_sdk import Keypair, Network, TransactionBuilder, Server

server = Server(horizon_url="https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
destination = Keypair.random()

source_account = server.load_account(account_id=source.public_key)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_create_account_op(
        destination=destination.public_key, starting_balance='1000'
    )
    .build()
)

transaction.sign(source)
response = server.submit_transaction(transaction)

if response:
    print(response['hash'])
else:
    print("Failed")
