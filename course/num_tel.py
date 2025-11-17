
num_tel = input("Veuillez entrer votre numéro de téléphone (068974...) : ")

dict_chiffres = {
    "0" : "zero",
    "1" : "un",
    "2" : "deux",
    "3" : "trois",
    "4" : "quatre",
    "5" : "cinq",
    "6" : "six",
    "7" : "sept",
    "8" : "huit",
    "9" : "neuf"
}

inter = ""
result_fin = ""

for digit in num_tel:  #parcours du num
    for cle, value in dict_chiffres.items(): #parcours du dict
        inter += digit #ajout du chiffre itéré dans une variable intermediaire 
        if inter == cle: #comparaison entre num et dict par clés
            result_fin += value + " " #ajout du chiffre en lettre dans la variable de retour
        inter = inter[:-1] #suppression du digit dans la variable inter pour passé a la comparaison du chiffre suivant
print(result_fin) #affichage du resultat dans la console

