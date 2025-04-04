def lista_de_numeros_pares(lista: list) -> list:
    lista_retorno = []
    for item in lista:
        try:
            valor = int(item)
            if valor % 2 == 0:
                lista_retorno.append(valor)
        except ValueError:
            continue
    return lista_retorno


if __name__ == "__main__":
    lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Numeros pares na lista 1: ", lista_de_numeros_pares(lista_exemplo))
    lista_exemplo_2 = [1, '2', 3, 'Numero 4', 5, 6, 7, 8]
    print("Numeros pares na lista 2: ", lista_de_numeros_pares(lista_exemplo_2))
