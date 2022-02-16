from stellar_sdk import Server, Keypair, Network, TransactionBuilder, Asset, ClaimPredicate, Claimant

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret("[QUEST_SECRET]")
source_account = server.load_account(source.public_key)

predicate_left = ClaimPredicate.predicate_before_relative_time(60 * 60 * 24 * 7)
predicate_right = ClaimPredicate.predicate_not(
    ClaimPredicate.predicate_before_relative_time(60 * 3)
)

predicate = ClaimPredicate.predicate_and(predicate_left, predicate_right)
claimant = Claimant(destination=source.public_key, predicate=predicate)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,

    ).append_create_claimable_balance_op(
        asset=Asset.native(),
        amount="100",
        claimants=[claimant],
        source=source.public_key
    )
    .build()
)

transaction.sign(source.secret)
response = server.submit_transaction(transaction)

if response:
    print(response)
else:
    print("Failed")
