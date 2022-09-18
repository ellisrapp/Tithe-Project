"""
Example of use:
If you earned $200 from one income source and $150 from another income source, type
tithes(200,150)

KEY:
i = total income
ff = firstfruits
t1 = first tithe (to the church)
t2 = second tithe (to the savings)
tp = poor tithe (to the needy)
"""

from math import ceil
from fnmatch import fnmatch

def round_up(number:float, decimals:int=2):
    """
    Returns a value rounded up to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return ceil(number)

    factor = 10 ** decimals
    return ceil(number * factor) / factor

def tithes(*incomes):
    i = sum(incomes)
    ff = str(round_up(0.03*i))
    t1 = str(round_up(0.097*i))
    t2 = str(round_up(0.0582*i))
    tp = str(round_up(0.0291*i))
    directions = []
    directions.append(f'Firstfruits:  $' + ff)
    directions.append(f'Church Tithe: $' + t1)
    directions.append(f'Second Tithe: $' + t2)
    directions.append(f'Poor Tithe:   $' + tp)
    for n in range(len(directions)):
        if fnmatch(directions[n],'*.??'):
            print(directions[n])
        elif fnmatch(directions[n],'*.?'):
            print(directions[n] + '0')
        elif '.' not in directions[n]:
            print(directions[n] + '.00')
        else: print('Something''s wrong with the output digits.')

tithes(2345678)