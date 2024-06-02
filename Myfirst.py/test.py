# # class Votants:
# #         def __init__(self, first, last, number, pays):
# #             self.first = first
# #             self.last = last
# #             self.number = number
# #             self.pays = pays

# #         def coord (self):
# #               return f'{self.first} \n {self.last} \n {self.number} \n {self.pays} \n Les coordonnes de {self()}'
        
# # villageois_1 = Votants('Gbahé', 'christian', '07-78-56-23-10', 'Cote d Ivoire')

# # print (Votants.coord(villageois_1))

# préfixe_moov = ['01', '02', '03']
# préfixe_orange = ['07', '08', '09']
# préfixe_mtn = ['04', '05', '06']


# # print (préfixe_moov[0:2])
# class Identifiant:
#     def __init__(self, numéro):
#         self.numéro = numéro

#     # def add_préfixe(self):
#     #     if self.numéro[0:2] in préfixe_moov:
#     #         print ('Moov')
#     #     elif self.numéro[0:2] in préfixe_mtn:
#     #         print ('Mtn')
#     #     elif self.numéro[0:2] in préfixe_orange:
#     #         print ('Orange')
#     #     else:
#     #         print ('None')

# id1 = Identifiant('02-03-05-05')
# id2 = Identifiant('07-78-84-27')
# id3 = Identifiant('05-33-98-13')

# prompt = 'Dans la zone UEMOA, les numéros sont passés a 10 chiffres'
# prompt+= '\nCommuniqué de la HACA'

# number = []

# def new_num(x):
#     print (prompt)
#     if x.numéro[0:2] in préfixe_moov:
#        number = [x.numéro]
#        x.numéro.__add__(préfixe_moov[0])
#        number.insert(0, préfixe_moov[0])
#        print ('Votre nouveau numéro est {}'.format('-'.join(number)))
#        print ('Moov vous remercie pour votre fidelité')
#     elif x.numéro[0:2] in préfixe_orange:
#        number = [x.numéro]
#        x.numéro.__add__(préfixe_orange[0])
#        number.insert(0, préfixe_orange[0])
#        print ('Votre nouveau numéro est {}'.format('-'.join(number)))
#        print ('Orange-CI vous remercie pour votre fidelité')
#     elif x.numéro[0:2] in préfixe_mtn:
#        number = [x.numéro]
#        x.numéro.__add__(préfixe_mtn[0])
#        number.insert(0, préfixe_mtn[0])
#        print ('Votre nouveau numéro est {}'.format('-'.join(number)))
#        print ('MTN vous remercie pour votre fidelité')
#     else:
#         print ('Numéro Invalide ! \n Veuillez entrer un nouveau contact.')


# new_num(id3)

class Identifiant:
    def __init__(self, numéro):
        self.numéro = numéro
    
    @classmethod
    def add_prefix(cls, user):
        for number in user:
          print (number)
        
    
user1 = ['02 03 04 05']
real_user = Identifiant.add_prefix(user1)

print (type(real_user))













