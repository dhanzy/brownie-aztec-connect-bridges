import eth_abi
from brownie import (
    RaiBridge,
    DefiBridgeProxy,
    RollupProcessor,
    network,
    config,
    Contract,
    interface,
)

from scripts.helpful_scripts import get_account
from web3 import Web3 as w3
import eth_abi


def deploy_and_create():
    account = get_account()
    defiBridgeProxy = DefiBridgeProxy.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    rollupProcessor = RollupProcessor.deploy(
        defiBridgeProxy.address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    rai_bridge = RaiBridge.deploy(
        rollupProcessor.address,
        "Rai-Safe-Token",
        "RTK",
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    weth = interface.IERC20("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    rai = interface.IERC20("0x03ab458634910AaD20eF5f1C8ee96F1D6ac54919")
    vm = interface.Vm("0x7109709ECfa91a80626fF3989D68f67F5b1DD12D")
    vm.store(
        weth.address,
        w3.solidityKeccak(eth_abi.encode_abi(rollupProcessor, 3)),
        bytes(10**18),
    )
    print(interface.IERC20(weth.address).balanceOf(rollupProcessor))
    return defiBridgeProxy, rollupProcessor, rai_bridge


def deploy_weth():
    contract = Contract.from_explorer("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    print(contract.address)


def main():
    deploy_and_create()
