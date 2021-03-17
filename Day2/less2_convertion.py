weight=input('weight:')
unit=input('unit:')
if unit.upper()=="L":
    print(int(weight)*0.45)
elif unit.upper()=="K":
    print(int(weight)*2.2)