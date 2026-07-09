# tests/test_nureg2020.py
from fmea_pra_toolkit.catalog import get_data

def test_nureg2020():
    df = get_data("NUREG_CR_6928_2020")
    ## Check que no hay ninguna fila none
    assert df.isnull().sum().sum() == 0

def test_nureg2020_no_nulls():
    df = get_data("NUREG_CR_6928_2020")
    nulls = df.isnull().sum()
    assert nulls.sum() == 0, f"Nulls encontrados:\n{nulls[nulls > 0]}"

def test_nureg2020_no_empty_strings():
    df = get_data("NUREG_CR_6928_2020")
    for col in ["group", "component_type", "failure_mode", "failure_description"]:
        assert (df[col].str.strip() != "").all()

def test_nureg2020_row_count():
    df = get_data("NUREG_CR_6928_2020")
    assert len(df) == 306  # 307 líneas en CSV - 1 header

def test_nureg2020_columns():
    df = get_data("NUREG_CR_6928_2020")
    assert list(df.columns) == [
        "group", "component_type", "failure_mode", "failure_description"
    ]