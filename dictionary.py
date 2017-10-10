notas = {}
notas['algoritmos'] = 5
notas['bases de datos'] = 4
notas['programacion'] = 4

acum = 0
prom = 0.0
for value in notas.values():
    acum += value

prom = float(acum / len(notas))
print('{:0.2f}'.format(prom))
