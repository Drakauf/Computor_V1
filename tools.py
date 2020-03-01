import re
import verbose as v

def simplifier(equation):
    equ = re.sub(r"([\+\-\=]|^)\s*[X|x]\s*($|[\+\-\=])", r"\1 1 * X^1 \2", equation) # X  => 1 * X^1
    equ = re.sub(r"(^|[+=-])\s*(\d+(?:(\.\d+)?))\s*($|[\+\-\=])", r"\1 \2 * X^0 \4", equ) # N => N * X^0
    equ = re.sub(r"(^|[+=\-])\s*(\d+(?:(\.\d+)?))\s*\*?\s*[x|X]\s*($|[\+\-\=])", r"\1 \2 * X^1 \4", equ) # N * X && NX => N * X ^ 1
    equ = re.sub(r"(^|[+=\-])\s*[x|X]\s*\^?\s*(\d+(?:(\.\d+)?))\s*([\+\-]?)\s*($|[\+\-\=])", r"\1 1 * X^\2 \4 \5", equ) # X ^ N && XN => 1 * X ^ N
    equ = re.sub(r"(^|[+=\-])\s*(\d+(?:(\.\d+)?))\s*\*?[x|X]\s*\^?\s*([\+\-]?)\s*(\d+(?:(\.\d+)?))\s*($|[\+\-\=])", r"\1 \2 * X^\4\5 \7", equ) # N * X ^ N && NXN => 1 * X ^ N
    return equ

def simplify(equation):

    # si il n'y a pas de "=" c'est pas une equation si il y en a plus d'un c'est pas bon aussi
    splitted = re.split("=", equation)
    if len(splitted) == 1 :
        v.ft_missing_equal()
    if len(splitted) > 2 :
        v.too_much_equal()
    
    pattern = re.compile("[\^xX]\s*([+-])\s*(\d+(?:(\.\d+)?))\s*($|[\+\-\=])")
    match = re.findall(pattern, equation)
    if len(match) != 0 :
        v.no_sign()

    pattern = re.compile("([\^xX])\s*(\d+?(\.(\d+)*?))\s*($|[\+\-\=])")
    match = re.findall(pattern, equation)
    if len(match) != 0 :
        v.no_float()


    tmp1 = re.sub(r"([,])", r".", equation) # change "," to "."
    tmp1 = re.sub(r"([^0-9.+\-*xX^=])", r"", tmp1) # remove unwanted caracteres and spaces
    tmp2 = ""
    while tmp1 != tmp2 :
        tmp2 = tmp1
        tmp1 = simplifier(tmp2)
    v.verbose("[Verbose]Formated: " + tmp2)
    return tmp2


def ft_ftoa(number):
    ret = str(number)
    ln = len(ret)
    check = ret[ln - 2:]
    if check == ".0":
        return ret[:ln - 2]
    return ret

def sqrt(x) :
    i = 0.00001
    if x == 0.0 :
        return 0.0
    while i * i < x :
        i += 0.00001
    s = str(i)
    j = s.find(".")
    k = s[:j + 5]
    return (float(k))
