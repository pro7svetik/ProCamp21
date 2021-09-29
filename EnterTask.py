import re

inp = open('number.txt', 'r')
out = open('output.txt', 'a')
suma = 0

numbers = inp.read()
numbers = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', numbers)
numbers = [float(x) for x in numbers]
for x in numbers:
    suma += x
out.write(str(suma))

inp.close()
out.close()
