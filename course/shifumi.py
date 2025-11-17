import random
print(f'{"-"*25} Bienvenue dans le Shifumi {"-"*25}')
Choices = ["Pierre", "Feuille", "Ciseaux"]
Computer = random.choice(Choices)
nb_win = 0
nb_win_computer = 0

while nb_win < 2 and nb_win_computer <2 :
    user = input("Entrer votre objet pour la prochaine manche ! : ")
    if user == 'Pierre':
        if Computer == 'Ciseaux':
            nb_win += 1
            print(f'Manche gagnée {nb_win}-{nb_win_computer}')
        elif Computer == 'Pierre':
            print(f'égalité pour cette manche {nb_win}-{nb_win_computer}')
        else:
            nb_win_computer += 1
            print(f'Manche perdue {nb_win}-{nb_win_computer}')
        
    if user == 'Feuille':
        if Computer == 'Pierre':
            nb_win += 1
            print(f'Manche gagnée {nb_win}-{nb_win_computer}')
        elif Computer == 'Feuille':
            print(f'égalité pour cette manche {nb_win}-{nb_win_computer}')
        else:
            nb_win_computer += 1
            print(f'Manche perdue {nb_win}-{nb_win_computer}')

    if user == 'Ciseaux':
        if Computer == 'Feuille':
            nb_win += 1
            print(f'Manche gagnée {nb_win}-{nb_win_computer}')
        elif Computer == 'Ciseaux':
            print(f'égalité pour cette manche {nb_win}-{nb_win_computer}')
        else:
            nb_win_computer += 1
            print(f'Manche perdue {nb_win}-{nb_win_computer}')
    
    if nb_win == 2:
        print(f'{"-"*25} Partie Gagné Bravo !!! {"-"*25}')
    elif nb_win_computer == 2:
        print(f'{"-"*25} Partie Perdue aïe... {"-"*25}')
