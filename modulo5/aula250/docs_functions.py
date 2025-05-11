"""Descrição do modulo - documentando funções

Aqui pode ter um texto longo com descrição detalhada para a documentação
"""

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma x e y

    Este modulo contem funções e exemplos de documentação
    """
    return x + y

def multiplica(
    x: int | float, 
    y: int | float, 
    z: int | float | None = None
) -> int | float:
    """
    Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y, z
    """
    if z is None:
        return x*y
    return x*y*z