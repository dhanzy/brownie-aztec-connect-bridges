// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IRollUpProcesor {
    function defiBridgeProxy() external view returns (address);

    function processRollup(bytes calldata proofData) external payable;
}
