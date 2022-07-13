from brownie import accounts, network, config, HelloWorld

def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.from_mnemonic(config["wallets"]["from_mnemonic"])

def deploy_voting_escrow():
    account = get_account()
    print('Deploying from account %s' % account)

    hello_world = HelloWorld.deploy(10, {'from': account})

    print(hello_world.counter())

def main():
    deploy_voting_escrow()
