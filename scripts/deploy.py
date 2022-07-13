from brownie import accounts, ERC20CRV, VotingEscrow


def deploy_voting_escrow():
    account = accounts[0]
    print('Deploying from account %s' % account)

    erc20 = ERC20CRV.deploy('Ocean token', 'OCEAN', 18, {'from': account})

    voting_escrow = VotingEscrow.deploy(
        erc20, 'Ocean', 'OCEAN', '1.2', {'from': account})

    print(voting_escrow.name())
    print(voting_escrow.symbol())
    print(voting_escrow.version())

def main():
    deploy_voting_escrow()
