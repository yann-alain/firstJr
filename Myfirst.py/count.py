# clubs = ['Barca', 'Real', 'ATM', 'Séville', 'Malaga', 'Deportivo', 'Valence', 'Grenade', 'Villareal', 'Real Sociedad']

# terminaleC = ['yann', 'oceane', 'bolou', 'christian', 'firmin', 'saviola', 'brice']
# diplomes = ['Bac-E', 'Bac-D', 'Bac-C', 'Bac-A2', 'Bac-C', 'Bac-F1', 'Bac-A2']

# classement = [-7, -3, 1, -9, 4, 5, -6, 2, 8]
# #classement = (7, 3, 1, 9, 4, 5, 6, 2, 8)
# s_classement = sorted(classement, key=abs)
# classs = sorted(classement, reverse=True)
# #print ('La classe :\t', s_classement)

# school = {termo:dip for termo, dip in zip(terminaleC, diplomes)}
# my_school = sorted(school)


#print (my_school)
# class Workers():
#     def __init__(self, nom, age, salaire):
#         self.nom = nom
#         self.age = age
#         self.salaire = salaire

#     def __repr__(self):
#         return '{}, {} ans, ${}'.format(self.nom, self.age, self.salaire)
    
# w1 = Workers('yann', 25, 350000)
# w2 = Workers ('sephora', 22, 250000 )
# w3 = Workers ('eric', 32 , 150000)
# worker = [w1, w2, w3]

# université = {name:dip for name, dip in zip (terminaleC, diplomes)}

# my_list = [(I, X) for X in range(3) for I in 'abc' ]
# #print (my_list)

# def any(emp):
#     return emp.age

# anything = [x for x in range(5)]
# #print (anything)

#print ("La liste des 10 meilleurs clubs espagnols !")
#for item, i in enumerate(clubs, start=1):
    #print (item, i)

#def fidels(*name, **datas):
    #print (*name)
    #print (datas)


# prompt = '\n Entrez vos coordonnées (Nom, Prénom, Age, Niveau, Salaire, Statut)'
# prompt+= '\n Appuyez sur valider lorsque toutes vos coordonnées demandées'
# prompt_question = '\n Entrez : \t'


# coord = ''
# valider = ""

# while coord != 'valider':
#     coordonée = []
#     print (prompt)
#     coord = input(prompt_question)
#     if coord == 'valider':
#       print ('Merci d''avoir entré toutes vos coordonnées''')
#     else:
#        print ('{}  est  entré'.format(coord.title()))
#        print (coordonée.append(coord.title()))



# prompt = '\n Entrez les ingredients que vous voulez pour votre pizza : '
# prompt+= '\n (Entrez stop si vos ingrédients sont tous entrés):'
# ingrédients = ""
# while ingrédients != 'stop':
#     ingrédients = input(prompt)
#     if ingrédients == 'stop':
#        print ('Votre pizza est en cuisine et vous sera livrée tres bientot !')
#     else:
#        print (f'{ingrédients.title()} est ajouté aux ingrédients de votre pizza...')

# while True:
#     ingrédients == input(prompt)
#     if ingrédients.lower() == 'stop':
#       break
#     else:
#        print (f"{ingrédients.title()} est ajouté aux ingrédients de votre pizza ...")




# while ingrédients == input(prompt):
#     if ingrédients.lower() == 'stop':
#        appel_stop = True

    #else:
      #  print (f"{ingrédients.title()} est ajouté a votre pizza !")


# print (help(str.isalnum))



# admis_et_non_admis_2017 = {'Yohan', 'Yannick', 'Tio', 'Ahoun', 'Messou', 'Suzy', 'Doumbia', 'Bonfo', 'Cissé'
# }

# doublants_2017 = {'Bonfo', 'Cissé', 'Tio', 'Kouao', 'Franck', 'Messou'}

# print ('\t'.join(admis_et_non_admis_2017))


# classement_by_name = sorted(admis_et_non_admis_2017)
# for x in enumerate(admis_et_non_admis_2017):
#     print(x)



# for liste in range(10):
#     print ('{:02}'.format(liste))

# def féli(*names):
#     print ('Félicitations mesdames et messieurs : {}'.format(names))

# féli(admis)












# def point(points):
    
#     '''Return nombres de points exacts !'''
#     return points * 2 >= 250

# def moy(moy_class):

#     return moy_class * 2 >= 24

# def check_resultat(points, name, moy_class):
#     if not 200 <= points <= 400 and name not in admis and moy_class < 12:
#         print ('Desolé {nom}, vous n etes pas admis !'.format(nom = name))
#     if points > 200 and name in admis:
#         print ('Félicitations {}, vous etes admis !'.format(name))
#     if points > 200 and name in admis and moy_class >= 12:
#         print ('Vous avez eu également votre affectation !')
    
# check_resultat(280, 'Bonfo', 15)




# boisson_sucrée = ['orange nature', 'limonade', 'bissap', 'perrier', 'mandarine_liquide', 'gnanmankou']

# plats.extend(boisson_sucrée)

# print ('\n '.join(plats))

# print (boisson_sucrée.insert(plats)) 
# boisson_alcolisée = {'bock', 'heineken', 'ivoire-black', 'beaufort', 'despé'
# }

# prompt = '\n Bienvenue au Restuarant "Chez Yanno" !'
# prompt+= '\n Voici nos menus'
# prompt_= '\n Que voulez-vous qu"on vous offre : '

# choix = ""

# def choice(plat):
#     print (prompt)
#     print (plat)
#     choix = input(prompt_)
    
# while choix != 'Stop':
#             print (prompt)
#             print (plats)
#             choix = input(prompt_)
#             if choix == 'Stop' and choix in plats:
#                print ('Votre commande est passée !' + '\n veuillez patienter un instant ! Merci')
#                break
#             #   x = liste.append(choix)
#             #   print (x)
#             else:
#                 print ('Noté ! : {}'.format(choix)) 
                
                
                 
            
            
            

# if 'sandwich-fromage' in plats:
#        print (plats)
# else :
#        print ('Error !')


# numb = 1_000_000_000
# numb1 = 10_000_000

# tot = numb + numb1
# print (f'{tot:,}')


plats = ['salade bourgeois','frites au poulet', 'riz au pattéo', 'creme aderntéé', 'attiéké sauce-claire', 'sandwich-poulet', 'sandwich-fromage', 'sandwich-viande', 'riz sauce tomate']
boisson_sucrée = ['orange nature', 'limonade', 'bissap', 'perrier', 'mandarine_liquide', 'gnanmankou']
prix = ['1000fr', '1500fr', '500fr', '2000fr', '1500fr', '1000fr']
collation = ['avec pipette', 'sans-sucre', 'light', 'gazeux', 'non-sucré', 'gimgimbre']

# for x , i, o  in zip (boisson_sucrée, collation, prix ):
#     print (f'{x} {i} est a : {o}')

# for x in zip (boisson_sucrée, collation, prix):
#     print (x)



# for i, x in enumerate(boisson_sucrée):
#     price = i
#     price = prix[i]
#     print (f'{x} est a : {price}')
#     print (x, price)




# numb1 = 1_000_000_000
# numb2 = 1_000_000
# som = numb1 + numb2
# print ('{:,}'.format(som))

# cond = False
# x = 1 if cond else print ('None')

# print (x)








# i = 0
# for x in plats:
#     print (i, x)
#     i += 1

# for i , x in enumerate(plats, start = 1):
#     print(i, x)








    
    


























       
































# jour_du_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
    
#     """return True for leap years, False for non-loop years."""

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year, month):
    
#     """Return number of days in that month in that year"""

#     if not 1 <= month <= 12:
#         return 'Mois invalide'
    
#     if month == 2 and is_leap(year):
#         return 29
    
#     return jour_du_mois[month]

# print  (jour_du_mois[0])