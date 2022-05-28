from brownie import (
    RaiBridge,
    RollupProcessor,
    DefiBridgeProxy,
    RollupProcessor,
    config,
    network,
    interface,
)
from scripts.helpful_scripts import get_account
from scripts.deploy_and_create import deploy_and_create


totalDepositAmount = 0


def _setTokenBalance(token, user, balance):
    slot = 3


def _initialize(depositAmount, collateralRatio):
    totalDepositAmount += depositAmount


def test_get_raibridge():
    account = get_account()
    defiBridgeProxy, rollupProcessor, rai_bridge = deploy_and_create()
    weth = interface.IERC20("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    rai = interface.IERC20("0x03ab458634910AaD20eF5f1C8ee96F1D6ac54919")
