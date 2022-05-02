from brownie import accounts, config, network, MockV3Aggregator
from web3 import web3

DECIMALS = 8
STARTING_PRICE = 20000000000

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mocks():
    if (len(MockV3Aggregator) <= 0):
            MockV3Aggregator.deploy(
                DECIMALS, 
                web3.toWei(STARTING_PRICE, "ether"), 
                {"from": get_account()}
            )