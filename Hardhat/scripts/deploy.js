// What is Hardhat? Hardhat is an environment developers use to test, 
// compile, deploy and debug dApps based on the Ethereum blockchain.
const hre = require("hardhat");

const main = async () => {
    const [deployer, randomPerson] = await hre.ethers.getSigners();
    const accountBalance = await deployer.getBalance();
    console.log("Account balance: ", accountBalance.toString());

    // Compile contract by Solidity compiler
    const factory = await hre.ethers.getContractFactory("TuesdayCafe");

    // Create a local Ethereum network and deploy the contract.
    // Generaete ABI(Application Binary Interface) and deployed bytes
    const contract = await factory.deploy();

    // Waiting contract deploy
    await contract.deployed();

    // Log address of deployed contract in the local chain
    console.log(`Contract deployed to: ${contract.address}`);
    console.log(`Contract deployed by: ${deployer.address}`)
    
    // Seeding
    await contract.seedReviews();

    // // Testing code in local net
    // await contract.addReview("Marius","5");
    // let reviews = await contract.getReviews();
    // console.log(reviews);

    // let pay =  {
    //     value: ethers.utils.parseEther("0.00001")
    // }

    // let txn = await contract.placeOrder("Peter", "Latte", pay);
    // await txn.wait();

    // contractBalance = await hre.ethers.provider.getBalance(contract.address);
    // console.log(
    //   "Contract balance:",
    //   hre.ethers.utils.formatEther(contractBalance)
    // );

    // let count = await contract.getOrderNumber();
    // console.log(`Order Count`, count);  
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