from brownie import accounts, config, FundMe, MockV3Aggregator, network
from scripts.utils import get_account, deploy_mocks
from web3 import web3

def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}
    ) 


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    
    transaction = simple_storage.addPerson(13, "Peter", {"from": account})
    transaction.wait(1)

    person_age = simple_storage.getPersonAge("Peter")

    print(person_age)

def main():
    deploy_fund_me()