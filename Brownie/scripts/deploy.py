from brownie import accounts, config, SimpleStorage, network

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    
    transaction = simple_storage.addPerson(13, "Peter", {"from": account})
    transaction.wait(1)

    person_age = simple_storage.getPersonAge("Peter")

    print(person_age)

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
def main():
    deploy_simple_storage()