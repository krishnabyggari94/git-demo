from logic.app import add, div, get_weather
from langchain_core.tools import tool

def test_add()->int:
    """
    tests the add function
    """
    res = add(3,4)
    assert res==7

def test_div()->float:
    """
    tests the div function
    """
    res = div(10,2)
    assert res==5

def test_get_weather()->str:
    """
    tests the get_weather function
    """
    res = get_weather.invoke('Hyd')
    assert 'sunny' in res