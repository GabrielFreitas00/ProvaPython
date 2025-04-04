def multiliplicar_numeros_inteiros(_num1: int, _num2: int) -> int:
    try:
        _num1 , _num2 = (int(_num1), int(_num2))  # Logica no try, caso não consiga converter em um int, o python ira
# lançar um ValueError, assim não sendo um numero e passando pelo nosso tratamento de erros.
        return _num1 * _num2
    except ValueError:
        raise ValueError("Não são numeros")  # lançar um execeção para evitar um erro na multiplicação
        # print("Não são numeros impossivel realziar a operação")


if __name__ == "__main__":
    # Parte sem ser interativa.
    print("Multiplicação de um INT com FLOAT: ", multiliplicar_numeros_inteiros(2, 2.5))
    print("Multiplicação de um INT com STR de numeros: ", multiliplicar_numeros_inteiros(2, '4'))
    print("Multiplicação de um INT com INT: ", multiliplicar_numeros_inteiros(2, 5))
    try:  # Aplicando um bloco TRY para evitar a interrupção no codigo, ele prosseguir
        print("Multiplicação de um INT com STR: ", multiliplicar_numeros_inteiros(2, 'Abobora'))
    except ValueError as e:
        print("Não e possivel multilicar, deu o seguinte erro: ", e)
    # Parte interativa
    while True:
        try:  # Caso o usuario digite tudo certo, ira prosseguir com a multiplicaçãio, caso contrario, irá pedir para
            # digitar novamente os numeros.
            num1 = int(input("Digite o 1º numero inteiro: "))
            num2 = int(input("Digite o 2º numero inteiro: "))
            print("Multiplicação dos inteiros foi: ", multiliplicar_numeros_inteiros(num1, num2))
            break
        except ValueError:
            print("Favor digitar somente numeros")
