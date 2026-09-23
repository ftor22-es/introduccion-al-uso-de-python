def main():
    lista = ["Manzana", "Pera", "Melocotón"] # 5.2
    listaDos = ["Kiwi", "Sandia", "Melon"] # 5.3

    lista.extend(listaDos) # 5.4

    print(lista[-1]) # 5.5

    tupla = (3,5,7) # 5.6
    print(tupla[0]) # 5.7

    inicio = int(input("Inicio:")) # 5.8
    fin = int(input("Fin:")) # 5.8
    salto = int(input("Salto:")) # 5.8
    rango = range(inicio, fin, salto) # 5.8

    print(rango) # 5.9
    print(len(rango)) # 5.9
if __name__ == "__main__":
    main()