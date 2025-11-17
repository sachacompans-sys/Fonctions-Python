def fizzbuzz(x:int):
    seuil = 0
    while seuil < x :
        seuil += 1
        if seuil % 3 == 0 and seuil % 5 == 0 :
            print("fizzbuzz")
        elif seuil % 3 == 0 :
            print("fizz")
        elif seuil % 5 == 0 :
            print("buzz")
        else :
            print(seuil)

fizzbuzz(16)