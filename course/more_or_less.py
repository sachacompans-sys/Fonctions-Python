import random

nb_tries = 1
difficulty = input("Entrer le niveau de difficulté (Facile/Moyen/Difficile) : ")

if difficulty == 'Facile':
    maximum = 10
elif difficulty == 'Moyen':
    maximum = 100
elif difficulty == 'Difficile':
    maximum = 1000

nb_random = random.randint(0, maximum)
nb_user = int(input(f'Veuillez entrer un nombre entre 0 et {maximum} : '))

while nb_user != nb_random :
    nb_tries += 1

    if nb_user > nb_random :
        print(f'Le nombre est plus petit que {nb_user}')
    else :
        print(f'Le nombre est plus grand que {nb_user}')

    nb_user = int(input("Entrer un nombre entre 0 et 10 : "))

print(f'Bravo tu a trouvé en {nb_tries} essais')