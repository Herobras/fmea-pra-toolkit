# tests/test_hello.py
from fmea_pra_toolkit import hello

def test_hello():
    result = hello()
    assert result == "Hello from fmea-pra-toolkit!"