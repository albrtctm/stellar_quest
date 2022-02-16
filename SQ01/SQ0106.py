from stellar_sdk import Server, Keypair, Network, TransactionBuilder, Asset

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)

issuer = "[PUB_KEY_FROM_LAST]"
asset = Asset("jcatama", issuer)
lumen = Asset("XLM", issuer=None)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_manage_sell_offer_op(
        selling=asset,
        buying=lumen,
        amount="69",
        price="10",
        offer_id=0
    )
    .build()
)

transaction.sign(source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
