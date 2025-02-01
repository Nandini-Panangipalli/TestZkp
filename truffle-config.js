module.exports = {
    networks: {
        development: {
            host: "127.0.0.1",
            port: 7545,
            network_id: "5777", // Must match the Ganache network ID
            from: "0x6F96319B9234fb2bd73887F1B204FAe410B7D783", // Deployment account
            gas: 5000000, // Set a custom gas limit
            gasPrice: 20000000000, // Set a custom gas price (20 Gwei)
        },
    },
    compilers: {
        solc: {
            version: "0.8.0", // Match the Solidity version used in your contracts
        },
    },
};
