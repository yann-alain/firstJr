
'''
LEGB
Local, Enclosing , Global, Built-in

'''
# prompt = 'Bienvenue a emploi-jeune !'
# prompt__= 'Entrez votre diplome :'
# agés = ['21 ans', '34 ans', '48 ans']
# yann,ami,fanny,*vieux   = ['yann', 'ami', 'fanny','sylvain', 'christian', 'augustin']

# salaire = ['150,000', '200,000', '250,000', '300,000', '350,000', '400,000', '450,000', '500,000']

# designation = ["Gardien", "Assistant", "Sécrétaire", "Technicien", "Directeur R-H", "CTO", "PDG"]

# diplomes = ['Bac + *', 'Bac + 2', 'Bac + 3', 'Bac + 5', 'master']

# for diplome, fonction, revenu in zip (diplomes, designation, salaire):
#     print (f'Diplome : {diplome}, \t Désignation : {fonction}, \t Salaire : {revenu} \n')




# def fun():
#     print (prompt)
#     input('Entrez vos coordonnées : ')
#     x = input (prompt__)

#     if x == diplomes[0]:
#         for work, money in zip(designation, salaire):
#             print (f'{work [0]}, avec un salaire de {money[0]}')
#     elif x == diplomes[1]:
#         for work, money in zip(designation, salaire):
#             print (f'{work [1]}, avec un salaire de {money[1]}')
#     elif x == diplomes[2]:
#         for work, money in zip(designation, salaire):
#             print (f'{work [2]}, avec un salaire de {money[2]}')
#     elif x == diplomes[3]:
#         for work, money in zip(designation, salaire):
#             print (f'{work [3]}, avec un salaire de {money[3]}')
#     elif x == diplomes[4]:
#         for work, money in zip(designation, salaire):
#             print (f'{work [4]}, avec un salaire de {money[4]}')
#     else:
#         for work, money in zip(designation, salaire):
#             print (f'{work [0]}, avec un salaire de {money[0]}')


# print (diplomes[0])
      


# class People():
#     pass

# people = People()

# one = 'Gohi'
# two = 'yann'
# three = 'alain'

# setattr(people, one, three)

# any = getattr(people,one)

# print (any)
    
'''Python Object-Oriented- Programming'''

# class Fonctionnaire:
    
#     taux_interet = 1.05
    
#     def __init__(self, first, last, pay):
#       self.first = first
#       self.last = last
#       self.pay = pay
#       self.email = first + '.' + last + '@company.com'
    
#     def coord(fonc_1):
#       return 'Les coordonnées du premier fonctionnaire sont : {} {},{}'.format(fonc_1.first, fonc_1.last, fonc_1.email)
    
#     def apply_raise(self):
#        self.pay = int(self.pay * Fonctionnaire.taux_interet)
   

# fonc_1 = Fonctionnaire('yann', 'Gohi', 250000)
# fonc_2 = Fonctionnaire('alain', 'kouao', 350000)

# print (fonc_1.pay)
# fonc_1.apply_raise()
# print (fonc_1.pay)



# print (fonc_1)
# print (fonc_2)


# fonc_1.first = 'yann'
# fonc_1.last = 'Gohi'
# fonc_1.pay = '250000'


# fonc_2.first = 'alain'
# fonc_2.last = 'kouao'
# fonc_2.pay = '350000'

# class Pays:

#     pourcentage = 0.1
#     def __init__(attribut, président, population, pib, ethnnie_populaire):
#         attribut.président = président
#         attribut.population = population
#         attribut.pib = pib
#         attribut.ethnnie_populaire = ethnnie_populaire

#     def portrait(attribut):
#         print ('{} est le président de la Cote d"Ivoire avec une population estimée a {:,}, et un pib de {}, et une ethnie majoritairement {}'.format(attribut.président, attribut.population, attribut.pib, attribut.ethnnie_populaire))

#     def richesse(attribut):
#         x = attribut.population * Pays.pourcentage
#         print ('{:,} est le nombre de personnnes les plus riches avec une fortune concentrée a 60 pour100 du PIB'.format(x))



# Cote_d_Ivoire = Pays("Alassane Dramane Ouattara", 23_000_000, '7,414 000 000 000', "Dioula")

# print (Cote_d_Ivoire.richesse())

# class Data:
#     def __init__(self, nom, prénom, birthday, numéro, statut_marital, casier_judiciare):
#         self.nom = nom
#         self.prénom = prénom
#         self.birthday = birthday
#         self.numéro = numéro
#         self.statut_marital = statut_marital
#         self.casier_judiciare = casier_judiciare
    
#     def data(self):
#         print ('\nnom : \t {} \nprénom : \t {} \nbirthday : \t {} \nnuméro : \t {} \nstatut_marital : \t {} \ncasier_judiciare : \t {}'.format(self.nom ,
#         self.prénom,
#         self.birthday,
#         self.numéro,
#         self.statut_marital,
#         self.casier_judiciare ,))


# personne1 = Data('Gohi', 'Yannick Alain Junior', '2000_28_04', '07-03-78-84-27', 'Marié', 'Vide')

# print (personne1.data())

# class Club:
#     pass

# club = Club()

# one = 'Réal'
# L_one = '14 ligues'

# two = 'Barcelone'
# L_two = '5 ligues'

# three = 'Milan'
# L_three = '7 ligues'

# four= 'Liverpool'
# L_four = '6 ligues'

# one = setattr(club ,one, L_one)
# two = setattr(club ,two, L_two)
# three = setattr(club ,three, L_three)
# four = setattr(club ,four, L_four)

# x1 = getattr(club, 'Réal')
# x2 = getattr(club, 'Barcelone')
# x3 = getattr(club, 'Milan')
# x4 = getattr(club, 'Liverpool')

# def In(equipe):
#     if equipe == 'Réal':
#         print (x1)
#     elif equipe == 'Barcelone':
#         print (x2)
#     elif equipe == 'Milan':
#         print (x3)
#     elif equipe == 'Liverpool':
#         print (x4)
#     else:
#         print ('No such a club inside !')

# x = True
# def Sport():
#     print ('Bienvenue sur le site e-Sport Africa')
#     x = input ('Que voulez vous?')
#     if x:
#       y = input('Votre équipe \t : ')
#       print (In(y))#

# Sport()

















# o_list = sorted(ages, reverse=True)
# print ('La liste des enfants du plus grand au plus petit ! \n {}'.format(o_list))

# for x , i in zip (vieux, agés):
#     print (f'{x} a {i}')
# nums = [1,1,2,3,2,2,3,4,5,2,1,6,8,6,8,9,7]
# #fisrt_nber = [n for n in numbers if n%2 == 0]
# #print (fisrt_nber)
# #for n in numbers:
#     #first_list.append(n)
# #print (first_list)

# #a_dict = {number:name for name , number in zip(names, numbers) if name != 'fanny'}
# my_set = (n*n for n in nums)
# print (my_set)


# x, i, *b, y = (10, 20, 30, 40, 50, 60)
# print (x)
# print (i)
# print (b)
# print (y)




