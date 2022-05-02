from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    expected = 0
    
    # Act
    simple_storage = SimpleStorage.deploy({"from":account})
    age = simple_storage.getPersonAge("Peter")
    
    # Assert
    assert expected == age

def test_deploy_update():
    # Arrange
    account = accounts[0]
    name = "Peter"
    expectedAge = 13
    simple_storage = SimpleStorage.deploy({"from":account})
    
    # Act
    simple_storage.addPerson(expectedAge, name, {"from": account})
    
    # Assert
    assert expectedAge == simple_storage.getPersonAge(name)