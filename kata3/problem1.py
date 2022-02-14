asteroidVelocity = 49 #expresed in km/s
maxAllowedVelocity = 25 #expresed in km/s

if asteroidVelocity > maxAllowedVelocity :
    print("Advertencia, se hacerca un asteroide demasiado rápido, correeeeeee!")
else:
    print("Asteroide dentro del rango de velocidad de " + str(maxAllowedVelocity) + " km/s")