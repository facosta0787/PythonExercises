# -*- coding: utf-8 -*-
amigos = list()

def printList():
    amigos.append('Alejandro')
    amigos.append('Felipe')
    amigos.reverse() # Invierte el orden de los elementos
    for amigo in amigos:
        print(amigo)

def addLists():
    friendsBoys = ['Alejandro','Brujo','Simon','Anderson']
    friendsGirls = ['Daniela','Angela','Nana']
    BoysGirls = friendsBoys + friendsGirls # Concatena 2 listas
    BoysGirls.remove('Brujo') # Borra un Elemento
    del BoysGirls[0] #Borra un Elemento por su indice
    print(BoysGirls)

def run():
    printList()
    addLists()

if __name__ == '__main__':
    run()
    # amigos.__dict__
