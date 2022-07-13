from brownie import accounts, config, network, VotingEscrow
from pyrsistent import v

def read_contract():
    # -1 --> read the latest deployment
    voting_escrow = VotingEscrow[-1]
    print("VotingEscrow deployed on %s" % network.show_active())
    print("Address %s" % voting_escrow)
    print("Name: %s" % voting_escrow.name())
    print("Symbol: %s" % voting_escrow.symbol())
    print("Version: %s" % voting_escrow.version())

def main():
    read_contract()