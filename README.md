# AZTEC connect

## How to setup

Add a mainnet fork on the development network

If a mainnet-fork exist you will have to remove it with this command

```sh
$ brownie networks delete mainnet-fork
```

Then create a mainnet-fork and then replace MAINNET_ALCHEMY_URL_API with your mainnet api url from `https://dashboard.alchemyapi.io/`

```sh
$ brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=MAINNET_ALCHEMY_URL_API accounts=10 mnemonic=brownie port=8545
```

## How to deploy contract

```sh
$ brownie run scripts/deploy_and_create.py --network mainnet-fork
```

## How to test contract

```sh
$ brownie test
```
