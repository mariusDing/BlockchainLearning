// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.4;

import "hardhat/console.sol";

// Similar as C# class
contract GiveMeBeer {
    uint256 totalBeer;
    
    constructor() {
        console.log("Yo yo, I am a contract and I am smart");
    }

    function takeBeer() public {
        ++totalBeer;
        console.log("%s take a beer", msg.sender);
    }

    function showTotalBeers() public view returns (uint256) {
        console.log("We have %d total beers!", totalBeer);
        return totalBeer;
    }
}