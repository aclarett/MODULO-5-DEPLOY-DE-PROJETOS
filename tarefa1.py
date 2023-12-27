def verifica_numero(numero):
    if numero % 5 == 0 and numero % 7 == 0:
        return "fizzbuzz"
    elif numero % 5 == 0:
        return "fizz"
    elif numero % 7 == 0:
        return "buzz"
    else:
        return "miss"