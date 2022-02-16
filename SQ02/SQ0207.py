from stellar_sdk import Server, Keypair, Network, TransactionBuilder, Asset

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)
source_other_account = Keypair.from_secret("[QUEST_OTHER_SECRET]")

asset = Asset("XLM", issuer=None)
transaction = TransactionBuilder(
    source_account=source_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=100,
).append_payment_op(
    destination=source_other_account.public_key,
    amount="69",
    asset=asset,
).append_revoke_account_sponsorship_op(
	account_id=source_other_account.public_key,
).build()

transaction.sign(source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
