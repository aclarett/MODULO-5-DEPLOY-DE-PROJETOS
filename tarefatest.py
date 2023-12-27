from tarefa1 import verifica_numero
def test_multiplo_de_5_e_7():
    resultado = verifica_numero(35)
    assert resultado == "fizzbuzz"
    
def test_multiplo_de_5():
    resultado = verifica_numero(5)
    assert resultado == "fizz"
    
def test_multiplo_de_7():
    resultado = verifica_numero(7)
    assert resultado == "buzz"
    
    
def test_nao_multiplo_de_5_ou_7():
    resultado = verifica_numero(1)
    assert resultado == "miss"
