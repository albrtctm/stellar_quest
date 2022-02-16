from stellar_sdk import Keypair, Network, TransactionBuilder, Server

server = Server(horizon_url="https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_keypair = Keypair.from_secret(source.secret)
source_account = server.load_account(account_id=source.public_key)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_manage_data_op(
        data_name='Hello',
        data_value='World'
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
