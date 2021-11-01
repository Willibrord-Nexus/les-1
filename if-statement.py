# Opdracht 4  --  if-statement
#   Maak een functie met daarin een if-statement
#   deze functie moet de parameter returnen mits deze even is. de functie hoeft geen vaste returnvalue te hebben, want als het niet even is kan je 'None' returnen.
#   in deze opdracht zit veel meer problem-solving, dus als je er niet uit komt doen we hem klassikaal.


# Uitleg

#
#
# Uitwerking

def return_even(x: int):
    if x % 2 == 0:
        return x
    return None
