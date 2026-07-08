# tests/test_hello.py
from fmea_pra_toolkit.get_data import get_data

def test_nureg2020():
    df = get_data("NUREG_CR_6928_2020")
    ## Check que no hay ninguna fila none
    assert df.isnull().sum().sum() == 0