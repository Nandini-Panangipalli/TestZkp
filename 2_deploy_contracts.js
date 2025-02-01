const ZKPAuth = artifacts.require("ZKPAuth");

module.exports = function (deployer) {
  deployer.deploy(ZKPAuth);
};
