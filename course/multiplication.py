

answer = int(input("Quelle table voulez-vous afficher ? : "))
table = []

for i in range(1,11):
    if (i*answer) % 3 == 0 :
        table.append(f'{i*answer}*')
    else :
        table.append(i*answer)
print(table)