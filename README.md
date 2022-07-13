# test-brownie
Test brownie framework

## venv

Activate the environment
```bash
python -m venv venv
source venv/bin/activate
```

Install packages in that environment:
```bash
pip install -r requirements.txt
```
or
```bash
pip install eth-brownie
```

Deactivate environment
```bash
deactivate
```

## Compile, deploy, test....
Compile:
```bash
brownie compile
```

Deploy:
```bash
brownie run scripts/deploy.py
```

Test:
```bash
brownie test
```