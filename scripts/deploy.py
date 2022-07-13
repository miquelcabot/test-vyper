from brownie import accounts, network, config, ERC20CRV, VotingEscrow

def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.from_mnemonic(config["wallets"]["from_mnemonic"])

def deploy_voting_escrow():
    account = get_account()
    print('Deploying from account %s' % account)

    erc20 = ERC20CRV.deploy('Ocean token', 'OCEAN', 18, {'from': account})

    voting_escrow = VotingEscrow.deploy(
        erc20, 'Ocean', 'OCEAN', '1.2', {'from': account})

    print(voting_escrow.name())
    print(voting_escrow.symbol())
    print(voting_escrow.version())

def main():
    deploy_voting_escrow()
