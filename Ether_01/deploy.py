from solcx import compile_standard, install_solc # Solidity compiler
from web3 import Web3 # A Python library built for interacting with the blockchain (eg.Ethereum)
from dotenv import load_dotenv
import os

# Prepare env
load_dotenv()
install_solc("0.7.0")

# Read contract
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version = "0.7.0"
)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Add provider
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/10aeae3fc5b0458c9490252e6c363fa1"))
chain_id = 4 # Rinkeby
my_address = os.getenv("Test_Account_Address_01")
private_key = os.getenv("PRIVATE_KEY")

# Construct contract
SimpleStorage = w3.eth.contract(abi = abi, bytecode = bytecode)
nonce = w3.eth.getTransactionCount(my_address)

# Create transaction
transaction = SimpleStorage.constructor().buildTransaction({"chainId": chain_id, "from":my_address, "nonce":nonce, "gasPrice": w3.eth.gas_price})
print("trans create")

# Sign contract
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
print("trans signed")

# Public transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("trans sent")

# Waiting transaction complete
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("trans complete")