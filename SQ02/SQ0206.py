from stellar_sdk import Server, Keypair, Network, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)
other_source_account = Keypair.random()

transaction = TransactionBuilder(
    source_account=source_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=100,
).append_begin_sponsoring_future_reserves_op(
    sponsored_id=other_source_account.public_key,
    source=source.public_key
).append_create_account_op(
    destination=other_source_account.public_key,
    starting_balance="0",
    source=source.public_key
).append_end_sponsoring_future_reserves_op(
    source=other_source_account.public_key
).build()

transaction.sign(source.secret)
transaction.sign(other_source_account.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
