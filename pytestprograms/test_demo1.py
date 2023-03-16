import pytest
@pytest.mark.login
def test_samp():
    x=10
    y=16
    assert x==y,"test failed samp"
@pytest.mark.login
def test_name():
    age=18
    assert age>=18

@pytest.mark.login
def test_hello():
     assert False


