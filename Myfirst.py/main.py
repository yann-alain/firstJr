

# def talk(sentence):
#     def say(word):
#         print (word)

#     mots = sentence.split(', ')
#     for dires in mots:
#         say(dires)

# print (talk("Je suis pret a affronter les situations de la vie."))


class Accessoires:
    
    def __init__(self, phone, montre, chaussure, lunettes):
        self.phone = phone
        self.montre = montre
        self.chaussure = chaussure
        self.lunettes = lunettes
    

    def tendance(self):  #méthode d'instance
        return 'Téléphone : \t {}\n Montre : \t {} \n Chaussure : \t {} \n lunettes : \t {}'.format(self.phone, self.montre, self.chaussure, self.lunettes)
    @classmethod   #méthode de classe -o Accessoires.from_string(var)
    
    
    def from_string (cls, access):
       phone, montre, chaussure, lunettes = access.split('-')
       return cls(phone, montre, chaussure, lunettes) #return avec la classe (cls)
    
    @staticmethod #méthode statique 
    def is_workday(day):
        return False if day.weekday() == 5 or day.weekday == 6 else True
    
class Objets(Accessoires):
    pass                   #sous-classe















pers_1 = Objets('Motorola', 'Balenciaga', 'Puma', 'Zara')

print (help(Accessoires))
# print (pers_1.chaussure)

import datetime
ma_date = datetime.date(2024, 7, 1)

#print (Accessoires.is_workday(ma_date))



# person_1 = Accessoires('Iphone 14', 'Mont-Blanc', 'Jordan', 'Gucci')

# access = 'Samsung-Permont-Nike-Lapaire'
# access2 = 'Huawei-Mont_Blanc-Ballerine-Glass'
# access3 = 'Samsung-Permont-Nike-Lapaire'

# phone, montre, chaussure, lunettes = access.split('-')

# new_person = Accessoires.from_string(access)
# other_person = Accessoires.from_string(access2) #méthode de classe

# print (new_person.chaussure)
# print (other_person.chaussure)




# Day = []
# Activities = []

# name = 'Yann'
# word = 'Bienvenue'
# message = '{}, {}. Enchantée!'.format(word, name)

# print ()


