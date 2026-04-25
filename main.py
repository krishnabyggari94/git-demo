print('starting app...')
from langchain_core.tools import tool

from logic.app import add
from logic.app import div
from logic.app import get_weather

def main()->None:
    a = add(1,2)
    b = div(25,10)
    c = get_weather.invoke('Hyd')
    print(f"a:{a}, b:{b}, c:{c}")

if __name__=='__main__':
    main()