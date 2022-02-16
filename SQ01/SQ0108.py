from stellar_sdk import Server, Keypair, Network, TransactionBuilder, Asset

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)

asset_to_buy = Asset("[QUEST_ASSET]", "[QUEST_ASSET_ADDR]")
stellar = Asset('XLM')
lumen = Asset("XLM", issuer=None)

payments = Server.strict_receive_paths(
    server,
    source=[stellar],
    destination_asset=asset_to_buy,
    destination_amount='100'
).call()

path = [
    Asset(asset['destination_asset_code'], asset['destination_asset_issuer']) for asset in payments['_embedded']['records']
]

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    ).append_change_trust_op(
        asset=asset_to_buy
    ).append_path_payment_strict_send_op(
        destination=source.public_key,
        send_asset=lumen,
        send_amount='69',
        dest_asset=asset_to_buy,
        dest_min='1',
        path=path
    )
).build()

transaction.sign(source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
