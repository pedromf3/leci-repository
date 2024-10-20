import math

cateto1 = float(input("Cateto 1 (lado A)?"))
cateto2 = float(input("Cateto 2 (lado B)?"))

hipot = math.sqrt(math.pow(cateto1,2) + math.pow(cateto2,2))
angulo_r = math.acos(cateto1/hipot)
angulo_g = math.degrees(angulo_r)

print("O comprimento da hipotenusa (lado C) é", hipot , ". O ângulo entre o lado A e o lado C é de", angulo_g ,"graus.")
