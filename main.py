"""Bingo"""
import random
from termcolor import colored

def imprimir_cartones(carton,color,valores_tachados,valores_bolillas)-> None:
    """Imprimir cartones.
    Pre: Recibe los cartones,el color,los valores que deben ser tachados,
    y los valores de las bolillas, se necesita que el carton tenga 3 filas y 9 columnas,
    el color tiene que ser un string que su valor sea 'red' o cualquier otro,
    valores_tachados y valores_bolillas deben ser listas y ambas listas deben contener str.
    Post: Imprime los cartones con el color correspondiente, y los valores que pertenecian
    a la lista valores_tachados reemplazados por XX para los cartones con codigo de color 'red'
    para los cartones con codigo de color distinto a 'red' reemplaza los valores que coincidan
    en valores_bolillas con XX para ambos casos si el valor es igual a '0' lo reemplaza con '**'
    """
    print("---------------------------------------------")
    for i in range(3):
        for j in range (9):
            numero : str = str(carton[i][j])
            if color == 'red':
                if numero in valores_tachados or '-'+numero in valores_tachados:
                    numero = 'XX'
            else:
                if numero in valores_bolillas:
                    numero = 'XX'
            if numero == '0':
                numero = '**'
            elif len(numero) == 1:
                numero = '0' + numero
            print(colored(" " + numero+" ", color),end = ' ')
        print()
        print("---------------------------------------------")


def generar_cartones()-> list:
    """Generar cartones.
    Pre: No recibe nada, toma 1 valor de cada lista de las que estan
    adentro de matriz_valores_posibles de forma aleatoria,
    reemplaza por cero 4 posiciones aleatorias que son usadas
    como espacio
    Post: Genera los cartones , retorna un carton  de 3 filas y 9 coumnas
    """
    carton :list = []
    matriz_valores_posibles = [
    [1,2,3,4,5,6,7,8,9,10,11],
    [12,13,14,15,16,17,18,19,20,21,22],
    [23,24,25,26,27,28,29,30,31,32,33],
    [34,35,36,37,38,39,40,41,42,43,44],
    [45,46,47,48,49,50,51,52,53,54,55],
    [56,57,58,59,60,61,62,63,64,65,66],
    [67,68,69,70,71,72,73,74,75,76,77],
    [78,79,80,81,82,83,84,85,86,87,88],
    [89,90,91,92,93,94,95,96,97,98,99],
    ]
    for _ in range(3):
        fila :list = []
        for j in range (9):
            posicion : int = random.randrange(len(matriz_valores_posibles[j]))
            valores = matriz_valores_posibles[j][posicion]
            matriz_valores_posibles[j].remove(valores)
            fila.append(valores)
            fila.sort()
        for _ in range (4):
            valores_nulos : int = 0
            valores_cambiados : int = random.randrange(1,9)
            while fila[valores_cambiados] == 0:
                valores_cambiados=random.randrange(1,9)
            fila[valores_cambiados] = valores_nulos
        carton.append(fila)
    return carton

def sorteador_bolillas(valores_bolilla:list)->list:
    """Sortea las bolillas.
    Pre: Recibe un array vacio valores_bolilla, y lo va llenando con valores aleatorios
    entre el 1 y el 99, comprueba si ese valor no esta ya en el array y en el caso de que
    ya este cambia el valor aleatoriamente nuevamente entre 1 y 99, en el caso que el
    valor de la bolilla tenga una longitud de 1 le concatena un 0 adelente.
    Post: asigna valor a las bolillas y retorna un array valores_bolillas lleno de los
    valores aleatorios de las bolillas
    """
    bolilla : str = ''
    bolilla = random.randrange(1,100)
    bolilla = str(bolilla)
    while bolilla in valores_bolilla:
        bolilla = str(random.randrange(1,100))
    bolilla = str(bolilla)
    valores_bolilla.append(bolilla)
    if len(bolilla) == 1:
        bolilla = '0' + bolilla
    print("Salio el numero:",bolilla)
    return valores_bolilla

def validacion_tachar_numeros(cartones, valores_tachados:list[list])-> list:
    """Guarda los valores tachados.
    Pre: Recibe una lista de cartones y una lista de los valores que tiene que tachar,
    la lista de valores_tachados puede tener valores ya adentro, y tiene que haber por lo
    menos un carton dentro del array de cartones, pide un numero y lo guarda.
    Post: Compara el valor que pide para que sea un numero entre 1 y 99, luego recorre el
    carton buscando un valor que sea igual a ese numero, si lo encuentra castea el numero a
    str y le concatena un '-' y lo appendea a valores_tachados. Si no entra avisa al usuario
    que ese numero no pertenece al carton. Luego retorna valores_tachados.
    """
    numero_a_tachar: int = int(input("Que numero desea tachar?: "))
    numero_tachado : bool = False
    while 1 > numero_a_tachar > 99:
        numero_a_tachar: int = int(input("Ingrese un numero valida por favor: "))
    for i,carton in enumerate(cartones):
        for j in range(3):
            for k in range (9):
                numero : str = str(carton[j][k])
                if numero == str(numero_a_tachar):
                    valores_tachados[i].append(numero)
                    numero_tachado = True
    if numero_tachado is False:
        print("ese numero no se encuentra en ningun carton")
    return valores_tachados

def cantar_linea(carton,fila,valores_tachados,valores_bolilla)-> bool:
    """Se fija si la linea es valida.
    Pre: Recibe una carton el cual es una lista de listas, una fila la cual
    es un entrero la lista valores_tachados y la lista valores_bolillas.
    Post: Compara cada valor de la fila del carton que forme parte de la lista
    valores_tachados y comprueba si estan tambien en la lista valores_bolillas
    en el caso que coincidan suma 1 vuelta a un contador , tambien verifica si
    el valor que esta comparando es negativo, retorna un booleano,
    retorna true si la cantidad de valores en el contador es igual a 5 y false
    en el caso contrario.
    """
    cantidad_valores_validos: int = 0
    for valor in carton[fila]:
        if(str(valor) in valores_tachados and str(valor) in valores_bolilla) or str(valor)[0]== '-':
            cantidad_valores_validos += 1
            print(cantidad_valores_validos)
    return cantidad_valores_validos == 5

def jugada_especial(argumentos)->list:
    """Tira la moneda.
    Pre: Recibe una lista argumentos que tiene en su interio dos lista
    cartones_usuarios y valores_tachados
    Post: Guarda un valor aleatorio entre 1 y 0,
    en caso de que salga 1 genera un nuevo carton y reemplaza el primer carton
    de la lista cartones_usuarios por el nuevo carton, en caso de que el valor sea
    0 , da al usuario la opcion de elegir un numero luego compara si ese numero
    esta en los cartones del ususario y lo appendea a valores_tachados remplazando
    el numero por su negativo.retona dos listas cartones_usuarios y valores_tachados
    """
    cartones_usuarios: list = argumentos [0]
    valores_tachados : list[list] = argumentos [1]
    moneda = str(random.randrange(2))
    if moneda == '1':
        print("Salio ceca uno de sus cartones sera cambiado")
        carton = generar_cartones()
        cartones_usuarios[0] = carton
        valores_tachados[0] = []
    else:
        print("Uf que suerte, salio cara elija un numero para tachar")
        numero_a_tachar: int = int(input("Que numero desea tachar?: "))
        for i,carton in enumerate(argumentos[0]):
            for fila in carton:
                for valor in fila:
                    if valor == numero_a_tachar:
                        numero_a_tachar = str(numero_a_tachar)
                        numero_a_tachar = '-'+ numero_a_tachar
                        valores_tachados[i].append(numero_a_tachar)
    return [cartones_usuarios,valores_tachados]

def bingo_pc(cartones_pc,valores_bolillas)-> bool:
    """Valida el bingo para la pc.
    Pre: Recibe dos lista cartones_pc y valores_bolillas.
    Post: Recorre las filas de los cartones y verifica que cada valor
    este tambien en la lista valores_bolillas. Retorna un booleano
    """
    for carton in cartones_pc:
        bingo : bool = True
        for fila in carton:
            for i in fila:
                i = str(i)
                if i not in str(valores_bolillas):
                    bingo = False
    return bingo

def menu()->None:
    """Despliega un menu
    Pre: No recibe nada, da una lista de opciones la cual el usuario puede elegir
    depende que elija el usuario llama a diferentes funciones.
    Post: No retorna nada.
    """
    color_pc : str = 'blue'
    color_usuario : str = 'red'
    valores_tachados :list[list] = []
    premio : int = 0

    print("0)	Salir del programa")
    print("1)	Jugar")
    terminar_programa: int =int(input("Ingrese la opcion que desea: "))
    while terminar_programa not in range(2):
        print("Ingrese un numero dentro de las opciones validas!")
        terminar_programa=int(input("Ingrese la opcion que desea: "))

    if terminar_programa==0:
        return
    cant_cartones:int=int(input("Elija la cantidad de cartones con la que quiere jugar: "))
    while cant_cartones not in range(1,6):
        print("La cantidad maxima es de 5 cartones por persona")
        cant_cartones =int(input("Elija la cantidad de cartones con la que quiere jugar:"))
    cartones_usuarios: list = []
    cartones_pc: list = []
    valores_bolilla : list = []
    for l in range(1,95):
        valores_bolilla.append(str(l))
    for i in range(cant_cartones):
        carton_usuario = generar_cartones()
        valores_tachados.append([])
        imprimir_cartones(carton_usuario, color_usuario,valores_tachados[i],valores_bolilla)
        cartones_usuarios.append(carton_usuario)
    for _ in range(10-cant_cartones):
        carton_pc= generar_cartones()
        imprimir_cartones(carton_pc, color_pc,valores_tachados,valores_bolilla)
        cartones_pc.append(carton_pc)
    terminar_programa = -1
    while terminar_programa != 0:
        print("0)	Salir del programa")
        print("1)	Si desea tachar algun numero")
        print("2)	Si desea pasar a la proxima ronda")
        print("3)	Cantar linea")
        print("4)	Cantar bingo")
        terminar_programa = int(input("Que quiere hacer?: "))

        if terminar_programa == 1:
            valores_tachados = validacion_tachar_numeros(cartones_usuarios,valores_tachados)
            for i,carton in enumerate(cartones_usuarios):
                imprimir_cartones(carton,color_usuario,valores_tachados[i],valores_bolilla)
        elif terminar_programa == 2:
            if (len(valores_bolilla)+1) % 4 != 0:
                valores_bolilla = sorteador_bolillas(valores_bolilla)
                for i,carton in enumerate(cartones_usuarios):
                    imprimir_cartones(carton,color_usuario,valores_tachados[i],valores_bolilla)
                for carton_pc in cartones_pc:
                    imprimir_cartones(carton_pc,color_pc,valores_tachados,valores_bolilla)
                bingo_confirmado_pc= bingo_pc(cartones_pc,valores_bolilla)
                if bingo_confirmado_pc:
                    print("La PC tiene bingo en el carton numero: ",
                            cartones_pc.index(carton_pc),
                            ", has perdido")
                    terminar_programa = 0
            else:
                valores_bolilla.append('-1')
                print("Es momento de la jugada especial!!!!!!")
                argumentos = jugada_especial([cartones_usuarios,valores_tachados])
                cartones_usuarios = argumentos[0]
                valores_tachados = argumentos[1]
                for i,carton in enumerate(cartones_usuarios):
                    imprimir_cartones(carton,color_usuario,valores_tachados[i],valores_bolilla)
        elif terminar_programa == 3:
            carton_con_linea : int = int(input("En que carton desea cantar linea?: "))
            fila_con_linea : int = int(input("En que fila desea cantar linea?: "))
            if cantar_linea(cartones_usuarios[carton_con_linea - 1],
                            fila_con_linea - 1,
                            valores_tachados[carton_con_linea - 1],
                            valores_bolilla):
                premio = premio + 2000
                print("Usted a ganado " , premio , "$")
            else:
                print("Ha sido descalificado, el cartón  nro ",carton_con_linea,"no tiene linea")
                terminar_programa = 0
        elif terminar_programa == 4:
            fila_tachada: bool = True
            carton_con_bingo : int = int(input("En que carton desea cantar bingo?: "))
            i : int = 0
            while i < 3 and fila_tachada:
                fila_tachada = cantar_linea(cartones_usuarios[carton_con_bingo - 1],
                                            i,
                                            valores_tachados[carton_con_bingo - 1],
                                             valores_bolilla)
                i = i + 1
            if fila_tachada:
                premio = premio + 58000
                print("Usted a ganado " , premio , "$")
            else:
                print("“Ud. Ha sido descalificado, posee el cartón  nro ",carton_con_bingo)
            terminar_programa = 0
        else:
            print("Seleccione una opcion valida")

def main()->None:
    """Main.
    Pre: No recibe nada
    Post: Llama a la funcion menu
    """
    menu()

main()
