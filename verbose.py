import sys
import tools
import globale

def verbose(message):
    if globale.verbose == 1:
        print("\033[1;30m" + message + "\033[0m")

def ft_usage():
    print ("\n\t---------- Usage ---------- \n\n python3 main.py \"equation\" [-v]\n\t\t\"equation\": valid input, some bonus like double spaces, min x\n\t\t-v: optional, shows details of resolution\n\t\t-h: help\n")
    sys.exit()

def ft_missing_equal():
    print ("There is no \"=\" in your equation... actually it's not even an equation ><'")
    sys.exit()

def too_much_equal():
    print ("There is too much \"=\" in your equation... actually it's not even an equation ><'")
    sys.exit()

def no_sign():
    print ("Please don't use signed powers")
    sys.exit()

def no_float():
    print ("Please don't use float powers")
    sys.exit()

def ft_simplyprint(numbers):

    #cree un tableau contenant toutes les puissances trie dans l'ordre decroissant
    table = sorted(numbers, reverse=True)
    #Cree la chaine a afficher avec l'equation simplifie
    to_print = "Reduced form: "
    printed = 0
    sign = ""
    higest = 0


    for degree in table:
         if numbers[degree] != 0:
            if numbers[degree] < 0:
                sign = " - "
                numbers[degree] = -numbers[degree]
            else:
                sign = " + "
            if printed == 0:
                if sign == " - ":
                    to_print = to_print + "-"
                to_print = to_print + tools.ft_ftoa(numbers[degree]) + " * X^"+ str(degree)
                printed = 1
            else:
                if degree != 0:
                    to_print = to_print + sign + tools.ft_ftoa(numbers[degree]) + " * X^"+ str(degree)
                else:
                    to_print = to_print + sign + tools.ft_ftoa(numbers[degree])
            if sign == " - ":
                numbers[degree] = -numbers[degree]

    if to_print != "Reduced form: ":
        to_print = to_print + " = 0"
    else:
        to_print += "0"
    print(to_print)
    try : 
        for n in numbers:
            if numbers[n] != 0:
                return n
        return table[0]
    except:    
        print("An error occured simply")
        sys.exit()
