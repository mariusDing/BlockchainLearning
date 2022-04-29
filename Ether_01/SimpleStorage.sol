// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract SimpleStorage {
    uint public favoriteNumber;

    struct Person {
        uint256 age;
        string name;
    }

    Person[] public people;

    mapping(string => uint) public nameMapping;

    function addPerson(uint _age, string memory _name) public {
        people.push(Person( _age, _name ));
        nameMapping[_name] = _age;
    }
}