Stellar Quest
-
My stellar quest project.

Please don't just copy the code mindlessly without trying to solve the problems yourself, it's totally pointless if you actually wanna learn how to write software.

P.S I intetionally did not add code documentation ;)

Trophy
-
### SERIES 1
1. [SQ0101](https://stellar.expert/explorer/public/tx/af365461d274fbdfe7bf67755c18e94dfcd17059be09079989a0fac5bcc9ccb8)
    > In this challenge your task is to create and fund a brand new Stellar account (seen below) with 1000 XLM on the testnet.
    > You will be required to use the createAccount operation, so don't just rely on friendbot. Good luck!
2. [SQ0102](https://stellar.expert/explorer/public/tx/9447f3bfae00a6adbf549f983a4b6ed522daafc27b61b092657a026349147926)
    > In this challenge, your task is to make a 10 XLM payment from the Stellar account (seen below) you funded in challenge 1.
    > Use the payment operation to send the XLM payment to any other testnet account.
3. [SQ0103](https://stellar.expert/explorer/public/tx/3dbd85bd5b33c85cb9d149819011187af3e2a84949079c43c57600cabbc85a4d)
    > Stellar allows you to store arbitrary data in the form of key : value pairs. In this challenge, you're tasked with adding a key of Hello and a value of World as a data attribute on your account. (seen below).
    > Note this challenge is case sensitive, so ensure you've got your key and value properly capitalized before checking your answer.
4. [SQ0104](https://stellar.expert/explorer/public/tx/c4c5497f17cc66f9bc7b09bf099a4928a3316e2fd25e385bb3c4b3c6254d1eb4)
    > In this challenge, your task is to add and then make use of multisig on your account (seen below).

    > ⚠️ Please take your time with this one ⚠️
    > If you get it wrong you could lock yourself out of your account for the remainder of the series.
    > Nervous? Pop into our Discord and verify before submitting.

    > Multisig can be a little tricky to wrap your mind around at first, but it's an important and essential security feature of Stellar baked into the core of the protocol.
    > *HINT: When adding multisig use setOptions but only set Signer Type. Do not touch Master Weight or any Threshold settings unless you're sure you know what you're doing.
5. [SQ0105](https://stellar.expert/explorer/public/tx/67891232a8ad87974561bac28e4f5a2e9f7e97a378f5011faec391945dfd798a)
    > In this challenge, your task is to create and send a custom asset to your account (seen below).

    > Custom assets are a first-class citizen in Stellar, and while the concept of trustlines can be a little tricky, once you get it sorted it's quite intuitive and straightforward.
6. [SQ0106](https://stellar.expert/explorer/public/tx/8257ff66f53c4cc56b17f52628c00d3b91a2cebe996e87f4f9d6e71a26a4ae53)
    > In this challenge, your task is to create an offer to sell your custom asset for XLM.

    > Stellar's decentralized exchange is a powerful feature that is built into the core of the protocol. It allows for instant interoperability between all Stellar assets, including yours!
7. [SQ0107](https://stellar.expert/explorer/public/tx/6eb3ed7de55256dfa4824a9d9e7b3214c7dcf3139a2cfb7df36a4a8aaacfa5b0)
    > In this challenge, your task is to submit a payment operation from your account (seen below), but to use a separate source account to pay the fee and sequence number for the transaction.

    > This is known as a fee channel or a channel account. It's a great way to soak up fees for users in larger apps or achieve higher transaction throughput.
8. [SQ0108](https://stellar.expert/explorer/public/tx/3a8306ed9e80b6b0294d8061bd6c2535ca0640d367969a257e0ee1ed37561720)
    > In this challenge, your task is to acquire SRT from its issuing account XXXXXXX via a path payment operation.

    > By taking advantage of the decentralized exchange built in at the protocol level, a path payment combines the conversion and transfer of assets It's one of Stellar's most powerful features.

### SERIES 2
1. [SQ0201](https://stellar.expert/explorer/public/tx/7fc5544210987ca2a9874bfefd71a45e0e4bb5c9e1f0cae256c9cee51098184c)
    > In this challenge your task is to create and fund a brand new Stellar account (seen below) with 5000 XLM on the testnet.

    > Include the SHA256 hash of the string Stellar Quest Series 2 as the MEMO_HASH in the transaction memo field.

    > You will be required to use the createAccount operation, so don't just rely on friendbot. Good luck!
2. [SQ0202](https://stellar.expert/explorer/public/tx/ba6c42fa7bcc8a0666d300c7b8fc8307c8ee2d0fe3b79c8fa9569fcd25d0519c)
    > Did you know each Stellar transaction can include as many as 100 unique operations? 😱 This is an incredible feature as each transaction is atomic meaning either the whole group of operations succeeds or fails together.

    > In this challenge your task is to create a multi-operational transaction which creates a custom asset trustline on your account and pays that asset to your account from the issuing account all in the same transaction.

    > Fun fact: This is actually what we do here at Stellar Quest when issuing prizes. The claim transaction is a nice little multi-operational transaction adding and issuing the badge to your account all in a single transaction.
3. [SQ0203](https://stellar.expert/explorer/public/tx/4335c8cea9f1afaec54ea563a5ed3ec5009026e37ab27bdcd170971727cb590f)
    > Fee channels are a common best practice in Stellar development. Their goal is to delegate fee payments away from user accounts for an improved UX. Protocol 13 saw a huge improvement to this flow with the introduction of fee bump transactions.

    > In this challenge your task is to create and execute a fee bump transaction which consumes the sequence number from your account (seen below) but the transaction fee from some other account.

    > This is actually how Stellar Quest delivers your prizes to you. A multi-operational transaction wrapped in a fee bump transaction. You pay the sequence number but we pay the transaction fee. How nice!
4. [SQ0204](https://stellar.expert/explorer/public/tx/a5e8f9455ab47c7c9b0c4fcc253f8f9b2b83e8f191aad75affadc50694a3d1f0)
    > This one will be a bit tricky but I believe in you.

    > Today you've gotta sort out how to create a claimable balance that is only claimable by you and only claimable after the next challenge.

    > Additionally the claimable balance must be denoted in the native XLM asset for an exact amount of 100 XLM.
5. [SQ0205](https://stellar.expert/explorer/public/tx/aad6ecffdd3f0fddec49796a2714943c11ceb5faf33f93d4ff1e04c8732eb4d0)
    > Remember that claimable balance you setup in the last challenge?

    > This challenge is to "simply" claim that balance and get your XLM back.
6. [SQ0206](https://stellar.expert/explorer/public/tx/1275bdbee89fc77a9829947b4c54c40b26de979764a95acfd997257471adfed3)
    > Storing stateful data on the Stellar blockchain isn't free. Everything from data attributes, trustlines and offers all the way down to just creating an account all increase the minimum balance of the account in question.

    > Up until protocol 15 this minimum balance had to be paid for by the account itself which often makes sense. However there are instances where it would be more convenient or even essential for these fees to be staked by some other account, a "sponsor" account.

    > In this challenge your task is to create a brand new 0 XLM balance account with the absolute minimum balance sponsored by your account (seen below).
7. [SQ0207](https://stellar.expert/explorer/public/tx/dec4ffd1a15ab3d4ed31d1dd88145945cbb51d7d49e41af51246b3ee10adaf26)
    > Remember that account you sponsored in the last challenge? Well the winds of change are blowing and you no longer wish to sponsor their absolute minimum balance any longer.

    > In this challenge you need to revoke account sponsorship for the account you're currently sponsoring.
8. [SQ0208](https://stellar.expert/explorer/public/tx/2f2995a3ed3f1f351c141068f83c9322400dfb1a4a7f3db1d34f8f3eb8c2b4c4)
    > Not all digital info should be stored on a blockchain. Some information needs to be mutable and derives no benefit from maintaining a blockchain paper trail. For these requirements we must look outside Stellar.

    > Blockchain database software like IPFS, Torrent or Filecoin can store stuff in a decentralized manner but are overkill when simply storing basic, mutable metadata for a Stellar account. For that we'll use SEP 1.

    > SEPs, or Stellar Ecosystem Proposals are ecosystem initiatives aimed at providing consensus around common Stellar use cases. For SEP 1 that's providing a common format for Stellar account metadata.

    > In today's challenge your task is to create, host and link to a stellar.toml file with an SQ02_EASTER_EGG field containing the text:

    > Log into series 2 of Stellar Quest then visit quest.stellar.org/series2. Finally drag and drop your Stellar Quest series 2 badge PNG images onto the screen. Enjoy!
    > Note you won't be able to solve today's challenge using only the laboratory. You'll need to host a toml file and for that you'll need a basic server. Personally I love RunKit and CodeSandbox but feel free to use whatever works. Good luck!
