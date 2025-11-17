side_one = int(input("Entrer la longueur du premier côté : "))
side_two = int(input("Entrer la longueur du deuxième côté : "))
side_three = int(input("Entrer la longueur du troisième côté : "))

if side_one == side_two == side_three :
    print(f'Votre triangle est équilatéral')
elif (side_one == side_two) or (side_one == side_three) or (side_three == side_two) :
    print(f'Votre triangle est isocèle')
else :
    print(f'Votre triangle est quelconque')