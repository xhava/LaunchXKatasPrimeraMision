asteroidDiameter = 20 #expresed in meters
asteroidVelocity = 25#espresed in km/s

if asteroidDiameter > 25 and asteroidDiameter < 1000 :
    print("Peligro! un asteroide lo suficientemente grande impactará la tierra.  no importa a donde corras, el daño es inevitable.")
elif asteroidVelocity >= 25 :
    print("Advertencia! un asteroide se inpactará en la tierra a una velocidad de: " + str(asteroidVelocity) + "km/s")
    print("Puedes mirar al cielo y contemplar un rayo de luz! pero no olvides correr.")
elif asteroidVelocity >= 20 :
    print("Puedes mirar al cielo y contemplar un rayo de luz!.")
else: 
    print("No hay peligro")

