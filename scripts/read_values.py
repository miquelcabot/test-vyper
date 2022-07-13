from brownie import accounts, config, network, HelloWorld

def read_contract():
    # -1 --> read the latest deployment
    hello_world = HelloWorld[-1]
    print("HellowWorld deployed on %s" % network.show_active())
    print("Address %s" % hello_world)
    print("Counter: %s" % hello_world.counter())

def main():
    read_contract()