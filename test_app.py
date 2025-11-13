from app import adicionar, subtrair, multiplicar


def test_adicionar():
    """Verifica se a função adicionar funciona corretamente."""
    assert adicionar(1, 2) == 3
    assert adicionar(-1, 1) == 0
    assert adicionar(0, 0) == 0


def test_subtrair():
    """Verifica se a função subtrair funciona corretamente."""
    assert subtrair(5, 3) == 2
    assert subtrair(10, 20) == -10


# Vamos introduzir um bug neste teste para vermos a pipeline falhar.
def test_multiplicar_com_bug():
    """Verifica se a função multiplicar funciona corretamente."""
    # O correto seria assert multiplicar(4, 5) == 20
    # Mas vamos colocar 21 para o teste falhar!
    assert multiplicar(4, 5) == 21
