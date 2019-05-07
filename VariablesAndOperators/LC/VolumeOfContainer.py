volOfCargo = float(input())
NoOfCargos = float(input())

sideOfCargo = round(volOfCargo**(1/3))
cargoArr = round(NoOfCargos**(1/3))

sideLength = sideOfCargo*cargoArr

volOfContainer = sideLength**3

print (volOfContainer)