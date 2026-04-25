from langchain_core.tools import tool

def add(a:int, b:int)->int:
    return a+b

def div(a:int, b:int)->float:
    return a/b

@tool
def get_weather(city: str)->str:
    """
    Args:
        city (str): name of the city

    Returns:
        str: the weather details of given city
    """
    return f"weather in {city} is sunny"