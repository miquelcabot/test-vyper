from brownie import accounts, HelloWorld

def test_deploy():
    account = accounts[0]
    counter = 20

    hello_world = HelloWorld.deploy(counter, {'from': account})

    assert hello_world.counter() == counter
