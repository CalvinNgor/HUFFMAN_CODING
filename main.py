import os

from Node import Node


def getData(fileName):
    """
    Fonction qui permet de récupérer les données d'un fichier.
    :param fileName: Nom du fichier.
    :return: La lecture d'un fichier.
    """
    file = open(fileName, "r")
    fileSize = os.fstat(file.fileno()).st_size

    return file.read(fileSize)


def run():
    """
    Fonction qui permet de ranger tous les caractères d'un fichier texte afin de les ranger dans une liste de tuples de manière ordonnée.
    :return: Liste de tuples rangés en fonction de la fréquence puis des lettres.
    """
    letterFreq = {}  # initialise le dico a partir de l'alphabet avec une valeur par défaut 0
    data = getData("./textesimple.txt")

    for character in data:  # parcours les char du fichier
        if character in letterFreq:  # .lower() pour convertir en minuscule
            letterFreq[character] += 1  # value +1
        else:
            letterFreq[character] = 1

    # letterFreq = {k: v for k, v in sorted(letterFreq.items(), key=lambda item: item[1])} # trie la value de chaque key et recréer le dico
    # letterFreq = collections.OrderedDict(sorted(letterFreq.items()))

    letterFreq = sorted(letterFreq.items(), key=lambda x: (x[1], x[0]))
    return letterFreq


def createTree(sortedListOfTuple):
    """
    Fonction qui permet de créer l'arbre.
    :param sortedListOfTuple:  Liste de tuples rangés.
    :return: L'arbre.
    """
    createSubTree(travelList(sortedListOfTuple))


def travelList(sortedListTuple):
    """
    Fonction qui permet de parcourir une liste de tuple afin de créer une liste d'arbre feuilles.
    :param sortedListTuple: Liste de tuples rangés.
    :return: Liste des arbres feuilles.
    """
    # parcourir liste de tuple pour cree liste d'arbre feuille
    list_tree_leaf = []
    for element in sortedListTuple:
        label = element[0]
        freq = element[1]
        nod = Node(label, freq)
        list_tree_leaf.append(nod)
    return list_tree_leaf


def createSubTree(listNode):
    """
    Fonction qui récupère des 2 premiers éléments de la liste de tuples et construire des sous-arbres
    :param listNode: liste de noeuds
    :return: Arbre fini
    """
    # tant que taille liste d'arbre > 1 :
    # prendre les 2 1er et créer nouvel arbre
    # réinjecter dans liste de nœuds a la bonne place (trié)

    while len(listNode) > 1:
        n1 = listNode[0]
        n2 = listNode[1]
        newNode = Node(n1.label + n2.label, n1.freq + n2.freq, n1, n2)
        listNode.pop(0)
        listNode.pop(0)
        listNode.append(newNode).sort()

    return listNode[0]


fileName = input("Fichier ?")
initialVolume = (os.path.getsize(fileName[:-4] + '_comp.bin'))
finalVolume = tailleArrivee = (os.path.getsize(fileName))

compRate = (1 - (finalVolume / initialVolume))

if __name__ == '__main__':
    list1 = run()
    list2 = travelList(list1)
    list3 = travelList(createSubTree(list2))
    print(list3)
