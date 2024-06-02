# import datetime

# ma_date = datetime.datetime(2024, 5, 29)

# date_today = 'Aujourdhui est le {}'.format(ma_date)

# print (date_today)


# date_today = 'Aujourdhui est le {:%d %B %Y}'.format(ma_date)

# date_today = 'Aujourdhui est {0:%A} et le {0:%j} jour de lannée'.format(ma_date)

# print (date_today)


# def find_index(chercher, cible):
#     for i, value in enumerate(chercher):
#         if value == cible:
#             break
#     else:
#         return -1
#     return i

# '''return -1 si lindice nest pas dans le module indiqué'''

# names = ['Yann', 'Grace', 'Oceane']

# indice = find_index(names, 'Franck')

# print ('Lindice est situé a: {}   '.format(indice))


# list_ = {'name' : 'yann', 'school' : 'UFHB', 'taille' : 176}
# print ('hello {0[name]} , votre école est {0[school]}, et votre taille est {0[taille]}'.format(list_))


# print ('Je veux un salaire de {:,}'.format(100**2))

# for x in range (10):
#     print ('{:02}'.format(x))

# x = 1

# for i in range (10):
#     i+= x
#     print (x)
#     # if i == 6:
#     #     break
# else:
#     print ('Good !')

students = ['Yann', 'Sephora', 'Abraham', 'Christ', 'Sami']
average =  [16.43, 15.85, 15.10, 14.9, 14.4]

status = {pupil : moy for pupil , moy in zip (students, average)}

any = sorted(status.values(), reverse=True)
ano = sorted(status.keys(),reverse=True)

statut = {eleve : point for eleve , point in zip (ano, any)}

print (statut)
















# medicament_palu  = ['paracetamol', 'efferalgan', 'CA-c1000']

# medicament_diabete  = ['Gicofat', 'Balurine', 'thermmos']

# def consultation(maladie):
#     x = input("De quoi souffrez-vous : ")
#     match (x):
#         case("palu"):
#           print ("Votre ordonnance : ")
#         case ("Diabete"):
#             print ("Votre ordonnance :")
#         case _:
#             print ("Patientez un peu pour votre ordonnance!")
#     return maladie

# def process_data(data):
#     processed = []
#     while data:
#         processed.append(data.pop())
#     return processed

# #medicament_diabete.append(' ')
# medicament_diabete.insert(2, "solurre")
# medicament_diabete.extend(medicament_palu)
# medicament_diabete.sort()
# print (medicament_diabete)



# class Car:
#     def __init__(self, nom, prénom, age):
#         self.nom = nom
#         self.prénom = prénom
#         self.age = age
       
    
    # def other(self):
    #     print ('hello {}. {}'.format(self.nom, self.prénom))
        
# x1 = Car('yann', 'Gohi', 24)
# x1 = {'name' : 'Gohi', 'age' : 25, 'classe' : 'Tle A2'}

# # phrase = 'Mon nom est {0.nom}, jai {0.age} et mon prenom est {0.prénom}.'.format(x1)
# # phrase = 'Mon nom est {name}, jai {age} ans, et je suis en classe de {classe}'.format (name='yann', age= 25, classe = 'Tle A2')
# phrase = 'Mon nom est {name}, jai {age} ans, et je suis en classe de {classe}'.format (**x1)
# print (phrase)


# x2 = Car('Kwamé', 'Adams', 34, 192, "Real madrid")
# x3 = Car('Ngotta', 'aimé', 27, 187, "Chelsea")

# attr_ = ['UFHB', 'Bac + 4']
# # attr = {'school' : 'UFHB', 'niveau' : 'Bac+4'}
# phrase = 'Mon école est {0[0]}, avec un niveau {0[1]}'.format(attr_)

# print (phrase)

# balise = 'footer'
# text = 'This a footer'
# texture = '<{0}> {1} </{1}>'.format(balise, text)
# print (texture)

# for x in range(1,12):
#     phrase = 'La valeur est {:}'.format(x)
#     print (phrase)

# x = 12.344354
# phrase = 'x est écrit a 3 chiffres apres la virgule {:.f}'.format(x)
# print (phrase)

# print ('Je veux un salaire de {:,.3f} frs'.format(134**3))

