#Exo 2

emails = ['pierre.dupont@yahoo.fr', 'marie.curie@gmail.com']
users = []

for email in emails:
    first_name = email.split("@")[0].split(".")[0]
    last_name = email.split("@")[0].split(".")[1]
    users.append({'first_name' : first_name, 'last_name' :  last_name})

print(users)

#Exo 3
fruits = ['Apple', 'Cherry', 'Mandarin', 'Banana', 'Pear','Clementine', 'Abricot']
voyelles = 'aeiouy'
fruits_result = []

for fruit in fruits:
    if fruit[-1] not in voyelles:
        fruits_result.append(fruit)

print(fruits_result)

#Exo 4
def word_count():
    sentence = "J'adore la langage de programmation Python et l'engagement"
    sentence_split = []
    num_word = 0
    sentence_split = sentence.split(" ")
    for element in sentence_split : 
        if "\'" in element :
            sentence_final_split = element.split("\'")
            sentence_split.append(sentence_final_split)
    num_word = len(sentence_split)
    print (num_word)

word_count()

#Exo 5
def get_largest_gap():
    marks = [8, 17.5, 6, 11, 15]
    minimum = marks[0]
    maximum = marks[0]
    for note in marks:
        if note < minimum :
            minimum = note
        if note > maximum : 
            maximum = note
    gap = (maximum - minimum)
    print (gap)        

get_largest_gap()

#Exo 6
def get_ages_average():
    users = [
        {
            'first_name': 'pierre', 
            'last_name': 'dupont',
            'age': 42
        },    
        {
            'first_name': 'marie', 
            'last_name': 'curie',
            'age': 18
        },
        {
            'first_name': 'marie', 
            'last_name': 'curie',
            'age': 35
        },
    ]
    age_user = []
    total = 0 
    for user in users:
        if 'age' in user:
            age_user.append(user['age'])
    
    for age in age_user:
        total += age
        average_final = total / len(age_user)
    print(average_final)

get_ages_average()