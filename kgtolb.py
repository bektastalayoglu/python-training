weight = input("weight:")
unit = input("(K) or (L)bs:")

if unit.upper()=='K':
    converted = float(weight) / 0.45
    print("weight in Lbs : {}".format(converted))
else:
   converted = float(weight) * 0.45
   print("weight in kg : {}".format(converted))    