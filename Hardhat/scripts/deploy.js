// What is Hardhat? Hardhat is an environment developers use to test, 
// compile, deploy and debug dApps based on the Ethereum blockchain.
const hre = require("hardhat");

const main = async () => {
    const [deployer] = await hre.ethers.getSigners();
    const accountBalance = await deployer.getBalance();
    console.log("Account balance: ", accountBalance.toString());

    // Compile contract by Solidity compiler
    const factory = await hre.ethers.getContractFactory("GiveMeBeer");

    // Create a local Ethereum network and deploy the contract. 
    const contract = await factory.deploy();

    // Waiting contract deploy
    await contract.deployed();

    // Log address of deployed contract in the local chain
    console.log(`Contract deployed to: ${contract.address}`);
    console.log(`Contract deployed by: ${deployer.address}`)

    // Invoke function from contract
    let beers = await contract.showTotalBeers();

    let transaction = await contract.takeBeer();
    await transaction.wait();

    waveCount = await contract.showTotalBeers();
};

const runMain = async() => {
    try {
        await main();
        process.exit(0);
    } catch (err) {
        console.log(err);
        process.exit(1);
    }
}

runMain();