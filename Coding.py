import os

class Coding :
    def __init__(self):
        pass

    def convertText(self, fileName):
        f = open(fileName, "r")
        fileSize = os.fstat(f.fileno()).st_size
        res = f.read(fileSize)
        result = []

        for character in res:
            result.append(character)
            if result == reading()

    def reading(self,trees):
        """
        Fonction qui permet de parcourir l'arbre.
        :param: La liste qui compose l'arbre
        :return: Le code qui correspond au caractère.
        """
        #Parcours en profondeur de l'arbre
        char = []
        for chiffre in trees:
            char.append(chiffre)
        return char

    def concatChar(self,listChar1,listChar2):
        """
        Fonction qui permet de concaténer des chaines de caractères.
        :param listChar1:
        :param listChar2:
        :return:
        """
        res = listChar1 + [" "] + listChar2
        return res


