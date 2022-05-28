// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface ISafeManager {
    function openSAFE(bytes32 collateralType, address usr)
        external
        returns (uint256);

    function modifySafeCollateralization(
        uint256 safe,
        int256 deltaCollateral,
        int256 deltaDept
    ) external;

    function transferInternalCoins(
        uint256 safe,
        address dst,
        uint256 rad
    ) external;

    function safes(uint256 _safeId) external view returns (address);

    function transferCollateral(
        uint256 safe,
        address dst,
        uint256 wad
    ) external;
}
