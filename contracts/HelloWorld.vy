# @version 0.3.3

counter: public(uint256)

@external
def __init__(_counter: uint256):
    self.counter = _counter

@external
def increment() -> uint256:
    self.counter += 1
    return self.counter

@external
@view
def get_counter() -> uint256:
    return self.counter
