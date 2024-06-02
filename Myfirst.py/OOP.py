###This programm is for OOP###$

# class Data:
#     def __init__(self, nom, prénom, birthday, numéro, statut_marital, casier_judiciare):
#         self.nom = nom
#         self.prénom = prénom
#         self.birthday = birthday
#         self.numéro = numéro
#         self.statut_marital = statut_marital
#         self.casier_judiciare = casier_judiciare
    
#     def data(self):
#         print ('\nnom : \t {} \nprénom : \t {} \nbirthday : \t {} \nnuméro : \t {} \nstatut_marital : \t {} \ncasier_judiciare : \t {}'.format(
#         self.nom ,
#         self.prénom,
#         self.birthday,
#         self.numéro,
#         self.statut_marital,
#         self.casier_judiciare ,))


class Fonctionnaire:
    
    taux_interet = 1.05 # class variable
    nombre_fonc = 0
    
    def __init__(self, first, last, pay): #self est une méthode réguliere!
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'
      Fonctionnaire.nombre_fonc += 1
    
    def coord(fonc_1):
      return 'Les coordonnées du premier fonctionnaire sont : {} {},{}'.format(fonc_1.first, fonc_1.last, fonc_1.email)
      
    def apply_raise(self):
       self.pay = int(self.pay * Fonctionnaire.taux_interet)
    
    @classmethod
    def taux_interet_imposé (cls, montant):
       cls.taux_interet = montant
    
    @classmethod
    def from_string (cls, emp_str):
       first, last, pay = emp_str.split('-')
       return cls(first, last, pay)
    
class Cadre(Fonctionnaire):  #subclass
#    taux_interet = 1.1
    
    def __init__(self,  first, last, pay, fonction):   #create a new instance methode
       super().__init__(first, last, pay)    #use super fun() for inheritance in order to calling method from parent classes within subclasses.
       self.fonction = fonction

class Manager (Fonctionnaire):
   
   def __init__(self,  first, last, pay, embauchés):   #create a new instance methode
      super().__init__(first, last, pay)    #use super fun() for inheritance in order to calling method from parent classes within subclasses.
   
   def __repr__(self):    #This dunder represente la classe Manager et va aider la variable d'instance de s'afficher littéralement sans données binaires.
      return "('{}', '{}', {})".format(self.first, self.last, self.pay)
    
   def __str__(self):     #this dunder affiche une chaine littérale d'office
      return '{} {} / {}'.format(self.first, self.last, self.email)
    
   def __add__(self, autre):
      return self.pay + autre.pay
   
   def __len__(self):
      return len(self.first)
   #     if embauchés is None:
   #        self.embauchés = []
   #     else:
   #        self.embauchés = embauchés

   #  def add_embauché (self, emp):
   #     if emp not in self.embauchés:
   #        self.embauchés.append(emp)
    
   #  def remove_embauché(self, emp):
   #     if emp in self.embauchés:
   #        self.embauchés.remove(emp)
    
   #  def print_emps(self):
   #     for em in self.embauchés:
   #        print ('-->',em.fullname())

travailleur = Cadre('Yannick', 'Gohi', 100000, 'CEO')
travailleur2 = Cadre('Seraphin', 'Gomé', 130000, 'Architecte')

manager_1 = Manager('Yao', 'Eric', 250000, [travailleur])
manager_2 = Manager('Gohi', 'Yannick', 350000, [travailleur])

# =====================================
# print (repr(manager_2))
# print (str (manager_2))
# =====================================
# print (manager_1.__repr__()) #same thing as before
# print (manager_1.__str__())
# =====================================
a = 2
b = 5
print (len(manager_1))
# print (manager_1 + manager_2)

# print (int.__add__(2,3))
# print (str.__add__('b', 'b'))









# print (travailleur.pay)
# travailleur.apply_raise()
# print (travailleur.pay)










# print (Fonctionnaire.nombre_fonc)


# crée une nouvelle variable avec les nouvelles variables en string.

# fonc_str1 = 'Grace-Gohi-600000'  #une variable crée en string
# fonc_str2 = 'Tania-Sissoko-700000'  #une variable crée en string
# fonc_str3 = 'Konaté-Elohim-800000'  #une variable crée en string
# new_emp1 = Fonctionnaire.from_string(fonc_str1) #la nouvelle variable prend la methode réguliere de la méthode de classe, et printe les valeurs de la variable assimilée.
# print (new_emp1.email)

# first, last, pay = fonc_str1.split('-') #le spilt ('-') permet de le decomposer avec les attributs de la méthode __init__(self)
# first, last, pay = fonc_str2.split('-') #le spilt ('-') permet de le decomposer avec les attributs de la méthode __init__(self)

# liste_key_value = [
#    {'name' : 'yann'}, 
#    {'age' : 25},
#    {'school' : 'UFHB'}
# ]

# coord = [x for x in liste_key_value]
# print (coord)

# fonc_1 = Fonctionnaire('yann', 'Gohi', 250000)
# fonc_2 = Fonctionnaire('alain', 'kouao', 350000)
# fonc_3 = Fonctionnaire('oce', 'uboi', 550000)

# print (new_emp1.email)
# print (new_emp2.first) #Va printer une seule valeur celle qui la derniere.

# print (Fonctionnaire.nombre_fonc)

# print (fonc_1.pay)
# fonc_1.apply_raise()
# print (fonc_1.pay)
# print (fonc_1.__dict__)

# fonc_1.taux_interet_imposé(1.04) #1.04 is montant in @classmethod

# print (fonc_1.taux_interet) #si on attribut une classe de méthode a la classe ou l'instance de classe, tous les éléments affectés changent automatiquement!

# print (Fonctionnaire.taux_interet)
# print (fonc_2.taux_interet)




