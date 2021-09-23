from random import randint


def read_file():
    
    with open('data.csv', 'r+') as f:
        list_nombres = f.read().split("\n")[:-1]
    return list_nombres


def lista_ganadores(total):

    i = 1
    nombres = read_file()
    ganadores = []
    ganador = None
    max_list = len(nombres) - 1
    if(total <= max_list):
        """
        Se valida un numero menor en 1 del total de usuarios para que no entre en ciclo infinito
        al ingresar un numero igual al total de usuario en el archivo
        """
        while(i <= total):
            # se ejecuta hasta tener n ganadores no repetidos
            random_n = randint(0, max_list)
            ganador = nombres[random_n]
            if ganador not in ganadores:
                ganadores.append(ganador)
                i += 1
        return ganadores
    else:
        return "El número dado excede al total de usuarios"


if __name__ == "__main__":
    ganadores = int(input("Cuantos Ganadores habrá: "))
    print(lista_ganadores(ganadores))
