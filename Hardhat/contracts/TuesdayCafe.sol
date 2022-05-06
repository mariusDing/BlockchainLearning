// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.9;

import "hardhat/console.sol";

// Similar as C# class
contract TuesdayCafe {
    address private ownerAccountAddress = 0xDF7Bc6c78A29895c3AC9D7c47ef15cFfc88a72F3;

    mapping(uint256 => Order) orders;

    struct Order {
        string customerName;
        string coffeeName;
        address customerAddress;
        uint256 orderDate;
    }

    event OrderPlaced(uint256 orderId, uint256 timestamp, string customerName, string coffeeName);

    struct Review {
        string customerName;
        string rating;
    }

     Review[] public reviews;

    event ReviewAdded(string reviewerName, string rating);

    constructor() payable {
        console.log("Welcome Tuesday Cafe");
    }
    
    function placeOrder(string memory _customerName, string memory _coffee) payable public {
        console.log("%s buy a coffee", msg.sender);
        console.log("%s money", msg.value);

        // Hardcode price for coffee
        uint256 unitOfPrice = 0.000001 ether;

        // check if send $ is over coffee price
        require(
            msg.value >= unitOfPrice, 
            "Not enough $ to buy"
        );

        // Transfer money
        payable(ownerAccountAddress).transfer(unitOfPrice);    
    
        // Create order
        uint256 orderId = random(1000);
        
        orders[orderId] = Order(_customerName, _coffee, msg.sender, block.timestamp);   

        // Dispatch event
        emit OrderPlaced(orderId, block.timestamp, _customerName, _coffee);
    }

    function getReviews() public view returns (Review[] memory) {
        return reviews;
    }

    function addReview(string memory _customerName, string memory _rating) public {
        reviews.push(Review(_customerName, _rating));

        // Dispatch event
        emit ReviewAdded(_customerName, _rating);
    }
    
    function seedReviews() public {
        reviews.push(Review("Peter", "4.5"));
        reviews.push(Review("Steven", "5"));
        reviews.push(Review("Thor", "3.5"));
        reviews.push(Review("Groot", "4"));
    }

    function random(uint number) public view returns(uint){
        return uint(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % number;
    }
}