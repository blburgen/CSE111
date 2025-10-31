from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("number and street, city, state zipcode") == "city"
    assert extract_city("525 S. Center Street, Rexburg, ID 83460") == "Rexburg"

def test_extract_state():
    assert extract_state("number and street, city, state zipcode") == "state"
    assert extract_state("525 S. Center Street, Rexburg, ID 83460") == "ID"

def test_extract_zipcode():
    assert extract_zipcode("number and street, city, state zipcode") == "zipcode"
    assert extract_zipcode("525 S. Center Street, Rexburg, ID 83460") == "83460"

pytest.main(["-v", "--tb=line", "-rN", __file__])