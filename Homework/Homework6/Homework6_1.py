""" Homework 6 - needs to be presented before exam day
O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse in ziua respectiva.
Seriile si loturile sunt numere intregi de tip int
Un lot este alcatuit din 20 de masini jumatate din lot sunt cu volan pe dreapta si jumatate cu volan pe stanga
Numerotarea loturilor incepe de la prima masina produsa cu seria 1 si lot 1
Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati produse in acea zi poate avea orice valoare
Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0
Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
1)Definire: 40p
 - Creati o clasa pentru un obiect iterabil
  a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (101, 41) 10p
  b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile cu volan pe stanga 15p
  c) iterator-ul returnat de object va comtine loturile din care fac parte seriile din obiectul curent  15p
2) Executie: 40p
- Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
- Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p
3) Documentatie: 20p
  a) adaugati type hints 5p
  a) documentati modulul 5p
  b) documentati clasele 5p
  c) documentati metodele 5p
"""
class Car :
   def _init_(self, series:list):
      self.series = series
   def _iter_ (self) :
       return self
   def _next_(self):
      if not self.series :
         raise StopIteration
      return self.series.pop(0)



class Factory:
     def _init_(self, date):
        self.date = date
        self.right = {}
        self.left = {}
     def add_lot(self, series: str , left:list , right:list):
        for series,  left, right in self.lot():
           for right in numbers:
              if right % 2 == 0 :
                 print(right)
           for left in numbers:
              if left % 2 != 0 :
                 print(left)
def __iter__(self):
   result = []
   for v in self.work.values():
      result.extend(v)
   return Car(result)
factory = Factory(date.fromisoformat('2021-05-11'))
factory.addwork("arg1", [101 , 41])
factory.addwork("arg2", [314 , 90])
print(Factory)



print(__doc__)
class Factory():
   pass
print(Factory.__doc__)











