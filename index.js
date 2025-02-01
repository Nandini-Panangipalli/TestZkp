import Web3 from 'web3';

// Initialize Web3 with Ganache's RPC endpoint
const web3 = new Web3('http://127.0.0.1:7545');

web3.eth.getAccounts()
  .then(accounts => {
    console.log('Accounts:', accounts);
  })
  .catch(err => {
    console.error('Error connecting to Ganache:', err);
  });
