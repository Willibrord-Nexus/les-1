# Opdracht 5  --  for-loop
#   Maak een functie met daarin een for-loop
#   deze functie moet x keer loopen en alle loops bij elkaar optellen. deze uitijndelijke waarde moet de returnvalue zijn.
#   in deze opdracht zit veel meer problem-solving, dus als je er niet uit komt doen we hem klassikaal.


# Uitleg

#
#
# Uitwerking

def return_all(x: int) -> int:
    temp: int = 0
    for y in range(x):
        temp += y
    return temp
