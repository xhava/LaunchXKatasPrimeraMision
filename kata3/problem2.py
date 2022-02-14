asteroidVelocity = 19 #expresed in km/s
maxAllowedVelocity = 20

if asteroidVelocity > maxAllowedVelocity :
    print('Se hacerca un asteroide, mira arriba para ver un rayo de luz')
elif asteroidVelocity == maxAllowedVelocity :
    print('Se hacerca un asteroide, mira arriba para ver un rayo de luz')
else :
    print("No hay peligro! Asteroide con velocidad de" + str(asteroidVelocity))

