import re
import verbose as v

def simply(equa):

    # splitter en 2 avec le "="
    splitted = re.split("=", equa)
    #### Creation de variables ###
    #liste ou on stocque les nombres (valeur) en fonction de leur puissance (cle)
    numbers = {} 
    #pattern pour recuperer les differents polynomes
    pattern = re.compile("(\-?\s*\d+(?:\.\d+)?)\s*\*\s*X\^(\d+)")

    #recuperation et symplification des polynomes cote gauche du "="
    match = re.findall(pattern, splitted[0])
    for polynome in match:
        try :
            numbers[int(polynome[1].replace(' ', ''))] += float(polynome[0].replace(' ', ''))
        except KeyError:
            numbers[int(polynome[1].replace(' ', ''))] = float(polynome[0].replace(' ', ''))

    #recuperation et symplification des polynomes cote droit du "="
    match = re.findall(pattern, splitted[1])
    for polynome in match:
        try :
            numbers[int(polynome[1])] -= float(polynome[0].replace(' ', ''))
        except KeyError:
            numbers[int(polynome[1])] = -float(polynome[0].replace(' ', ''))
    return(numbers)
