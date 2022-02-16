from stellar_sdk import Server, Keypair, Network, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .append_set_options_op(
        home_domain = "[DOMAIN]" # i.e jcatama.pythonanywhere.com
    )
    .build()
)

transaction.sign(source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
