"""
juego tipo slay the spire

1 cosa que creo que seran importantes saber para hacer este jueguito.

Primero saber que es un dicionario:
los dicionarios son resumidamente como listas pero al invez de solo guardar datos se guarda como el nombre lo dice, como dicionario.
y lo que se refiere con dicionario de que cada elemento en la lista tiene su llave y valor como por ejemplo dict = {"joao":200,"pedro":150,"buratti": 410 }
"""
dict = {"joao":200,"pedro":150,"buratti": 410 }
""" cada elemento de la lista tiene su valor
y si hacemos por ejemplos print(dict["joao"]) nos retornara el valor de 200"""
print(dict["joao"])
""" algunos metodos basicos de dicionarios"""

"""agregar al dicionario"""

print(dict)
dict['facundo'] = 300 
print(dict)
#como podes ver se agrego el el elemento facundo con valor 300, 
# para aclarar el valor del dicionario puede ser de cualquier tipo tanto una lista [] como una strin '' o otro dict {}
""" para aumentar el valor de una llave es simplemente la buscas y la reasignas o sumas haciendo por ejemplo """
dict["joao"] = dict["joao"] + 200 # O dict['joao'] += 200

# eliminar un elemento de un dicionario es 
dict.pop('facundo')
print(dict)

# para ver solo las llaves o  valores del dicionario es
print(dict.keys())
print(dict.values())

""" unas de las principales funciones de un dicionario es para la creacion de objetos,
 un objeto es lo que seria representado por un dicionario contendo el las informaciones de el, como por ejemplo"""
player = { 

    'vida':100,
    'energia':3,
    'cartas':{"golpe":[6,5,1],'defender':[5,5,1]},
    "proteccion": 0,
    'totens': [],
    'piso':0
    }
""" lo que ese dicionario seria las informaciones del jugador y sus valores y apartir de ahi las cambias, 
como por ejemplo si aparece un ogro q le da 6 de dano pones player['vida'] -=6 que seria player['vida']= player['vida'] - 6
y la lista de las cartas 
 """
print(player)
player['vida'] -=6
print(player)
# y lo que seria la lista despues de cada carta seria la la cantidad de esa carta que el player tiene, cuanto hace lo que hace (5 de dano) y el tercero su costo


# dependiendo que tan grande queres q sea el juego  va a tardar mucho y por eso podemos hacerlo juntos y entrenas tu trabajo en equipo
enemigos = []
cartas = []
#podes primero definiendo todas las cartas que quieras poner en el juego