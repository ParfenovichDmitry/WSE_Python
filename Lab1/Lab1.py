## Język python jest językiem wysokiego poziomu, typowanie danych w Pythonie jest dynamiczne (interpreter sam rozpoznaje typ zmiennej na podstawie jej wartości)
## You should always use camelCase for class names, snake_case for everything else in Python (you could to use UPPER_CASE_SNAKE for constants).
############ Zmienne; typ prosty (klasy): string, integer, float,double, bool ###############
# print('Hello world')
#
# var_string = 'mercedes'
# print(type(var_string)) # funkcja type sprawdzenie typu zmiennej
#
# var_bool = True
# print(type(var_bool))
#
# var_integer = 1
# print(type(var_integer))
#
# var_float = 2.2324234
# print(type(var_float))
#
# var_float = 2.2324234
# print(type(var_float))
import subprocess

#### przypisanie wielu wartości do wielu zmiennych
# a, b, c = 1, 2, 1+2
# print(a,b,c)
# print('a = ', a, '; b = ', b, '; c =', c)
# print('a = ' + str(a) + ', b = ' + str(b) + ', c =' + str (c))   # str - konwersja zmiennej na typ string
# print('a = {}; b = {}; c = {}'.format(a,b,c))
# print('zmienna %s \n2 jako float: %f' % ('a', a))  # \n2 - newline
# print('zmienna %s jako int: %i' % ('a', a))
# print('zmienna %s jako float: %.2f' % ('a', a))  # 2f - zaokrąglij do 2 miejsc po przecinku
# print('zmienna %s jako int: %i' % ('a', a))
########################### Importowanie pakietów/bibliotek w Python
# Sposób 1
# import math   # importuje wszystkie funkcje i metody dostępne w bibliotece math
# x = 30*pi/180
# print(math.sin(x))

# Sposób 2
# from math import pi, sin
# x = 30*pi/180
# print('30*pi/180 =', sin(x))

############ strukturalny vs funkcyjny
## Oblicz pierwiastek z liczby 4
# p1 = 4**(1/2)  # paradygmat programowania strukturalnego
# print(p1)
#
# # from math import sqrt
# import math
# p2 = math.sqrt(4) # paradygmat programowania funkcyjnego
# print(p2)

## Komunikacja z użytkownikiem, wczytanie danych z konsoli
# name = input('Podaj imię: ')
# print(name)
# age = int(input('Podaj wiek: '))   # int - konwersja typu zmiennej string (str, łańcuch) na integer (int, liczba całkowita)
# print(name + ' ' + str(age))    # str - konwersja typu zmiennej str na int
#
# print("Twoje imię to: {} masz {} lat.".format(name, age))

###### Zmienne; typy złożone
# W Pythonie nie ma tablic
# # ################## Lista  ####################
# Tworzenie listy i odwoływanie się do jej elementów
# list_empty1 = list()  # pusta lista
# list_empty2 = []      # też pusta lista
# list1 = ['Informatyka', 1, True]  # to jest lista o nazwie cars
# print(list1)
# print(list1[0]) # uwaga numeracja wektora/listy itd. jest od 0
# print(list1[2]) # tu element nr 3 listy
########################### metody dla klasy lista ##########################
####### metody (okreslone operacje) wykonujemy na obiektach, obiektem może być np. nasza zmienna
# # # Zapoznaj się z kilkoma poniższymi podstawowymi i użytecznymi metodami dla list
# # # append(x) - Dodaje element do końca listy,
# # # extend(L) rozszerza listę poprzez dołączenie wszystkich elementów podanej listy L,
# # # insert(i, x) - umieszcza element x na podaną pozycję listy i, np. nazwaLista.insert(0,'Ala')
# # # remove(x) - usuwa pierwszy napotkany element z listy, którego wartością jest x.
# # # pop([i]) - usuwa element z podanej pozycji na liście i zwraca go jako wynik.
# # # index(x) - zwraca indeks pierwszego elementu listy, którego wartością jest x, np. cars.index('BMW')
# # # count(x) - zwraca liczbę wystąpień elementu x na liście.
# # # sort() - sortuje elementy na liście, w niej samej
# # # reverse() - odwraca porządek elementów listy.
##########################################################################
# # # Zapoznaj się przykładami zastosowania w/w metod ###############################################
# cars = ['Audi', 'BMW', 'Mercedes','BMW', 'BMW']
# print(cars)
# cars.append('Porsche') # na obiekcie o nazwie cars wywołana została metoda o nazwie append
# print(cars)

# cars = ['Audi', 'BMW', 'Mercedes','BMW']
# print(cars)
# cars.insert(2,'Porsche')
# cars2 = cars
# print(cars2)

#######  Użycie metody index na obiekcie cars, sprawdzamy index elementu listy
# cars = ['Audi', 'BMW', 'Mercedes','BMW']
# print(cars)
# ind = cars.index('BMW') # na obiekcie cars stosujemy metodę index, 1-sza pozycja elementu
# print(ind)
# ind2 = cars.count('BMW') # na obiekcie cars stosujemy metodę count liczba wystąpień elementu
# print(ind2)

# # Usuwanie wybranego elementu z listy
# numbers = [1, 2, 3, 10, 18, 10, 13, 10]
# print(numbers)
# numbers.remove(10)
# print(numbers)

### Łączenie list
# list1 = ["Ala", "Zosia"]
# list2 = ["Janek", "Tomek"]
# merge_list = list1 + list2
# print(merge_list)
#
# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy

print("Zadanie 1")
print()
list_name =['Anna', 'Magdalena', 'Rafał', 'Michał', 'Anna', 'Alex', 'Alex', 'Martin',
            'Roman', 'Adam']
print('Podaj imię')
user_name = input()
if user_name in list_name:
    print('Pirwszy index: \n',list_name.index(user_name))
    print('Ilość imion: \n',list_name.count(user_name))
    list_name.append(user_name)
else:
    list_name.append(user_name)
print('Dodanie do końca listy: \n', list_name)
print('Dołącz nowe imię jako 3 pozycję')
list_name.insert(2,input())
print('Imię na 3 pozycję: \n',list_name)
list_name.sort()
print('Sortowanie tablicy: \n', list_name)
print('Usunieńcie ostatniego elementu: ',list_name.pop(len(list_name)-1))
print(list_name)

nowa_lista = ['Piotr', 'Aga', 'Lech']
print('Nowa lista:\n', nowa_lista)
list_name.extend(nowa_lista)
print('List ogólny: \n', list_name)
print("_______________________________________________________")

# # ################# Klasa: Krotka (Tuple)
# print('To moja pierwsza krotka')
# cars2 = ('A', 'B')  # krotka = tuple
# print(cars2)
# #cars2.append('aaaaa')   # w krotce nie mogę zmieniać wartości, elementów
# print(cars2, type(cars2))

# ################  Klasa: Słownik
# dict_empty1 = dict()    # pusty słownik
# print(dict_empty1)
# print(type(dict_empty1))

# słownik = {klucz1: wartość klucza1, klucz2: wartość klucza2, itd}
# slownik1 = {'wojenne': 'Medal od honor, Call of Duty',
#            'romans ': 'Romeo i Julia',
#            'komiksy ': 'Kaczor Donald'}
# print(slownik1)

# cars_countries = {
#       'Germany': ['Audi', 'BMW'],
#       'Asia': {'Japan': ['Toyota', 'Honda']}
# }
# print(cars_countries)
#### Przykład: Zwróć uwagę na odwoływanie się do elementów słownika, po nazwie klucza, a
##### następnie po elementach listy (wartość klucza)
# print(cars_countries['Germany'])
# print(cars_countries['Germany'][1])
# print(cars_countries['Asia']['Japan'][0])
# print(cars_countries['Korea'])  # nas slownik nie ma takiego klucza

######################Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

###Przykład: dodawanie nowego klucza do słownika##########################
# cars_countries['Korea'] = 'Kia' # 1 sposób dodawanie nowego klucza do słownika
# print(cars_countries)
# print(cars_countries['Korea'])

# 2 sposób dodawanie nowego/ch klucza/kluczy do słownika
# cars_countries.update({
#     'France': 'Citroen',
#     'Spain': 'Seat'
#    })
# print(cars_countries)
# print()
print("Zaadanie 2")
print()
osoby = {
    'imię':['Anna','Lena', 'Piotr'],
    'nazwisko':['Lech','Ivanova','Petrov'],
    'wiek':[18,25,34]
}
print('List osob: \n',osoby.items())
osoby.update(
    {'kraj':['Polska','Rosja','Bełarus'],
     'miasto':['Warszawa','Moskwa','Mińsk'],
     'telefon':[1234567,4897978,798894]}
)
print('Modyfikowany list osób:\n', osoby)
print("Wprowadź numer użytkownika od 1 do 3")
i=int(input())
for key in osoby:
   print(osoby[key][i-1], end=" ")
print()

print("__________________________________________________")

######################Zadanie 3
# Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "kierunek_studiów", wartość w/w klucza dowolna
# wskazana przez użytkownika

################# Metody dla klasy słownik:
### var_dict.clear() - usuwa wszystkie klucze ze słownika var_dict
### var_dict.get(klucz) - zwraca wartość dla podanego klucza, gdy klucza nie ma w słowniku zwraca None
### var_dict.has_key(klucz) - zwraca True gdy klucz jest w słowniku, False w przeciwnym razie,
### var_dict.items() - zwraca listę dwuelementowych krotek (klucz, wartość)
### var_dict.keys() - zwraca listę wszystkich kluczy
### var_dict.values() - zwraca listę wszystkich wartości

################# Przykłady
# cars_countries = {
#       'Germany': ['Audi', 'BMW'],
#       'Asia': {'Japan': ['Toyota', 'Honda']}
# }

# del cars_countries['Germany'] # funkcja del usuwa klucz 'Germany' z słownika cars_countries
# print(cars_countries)
# keys = cars_countries.keys()
# print(keys)
# l = len(keys) # funkcja len liczy długość, ilość elementów
# print(l)
# print(len(cars_countries))
######################Zadanie 4
# Wyświetl nazwy kluczy poprzednio utworzonego słownika, oraz ilość jego elementów
# ###########################################
############ Typ złożony (klasa) Zbiory ###############
# my_list = [5, 1, 1, 2, 3]
# a = set(my_list)
# b = set([4, 5, 6, 7, 8])
# #### wybrane operacje na zbiorach
# print(a & b)
# print(a.intersection(b)) # operacja równoważna do powyższej
#
# print(a | b)
# print(a.union(b))   # operacja równoważna do powyższej
#
# print(a - b)
# print(a.difference(b))   # operacja równoważna do powyższej
#
# print(b - a)
# print(b.difference(a))   # operacja równoważna do powyższej

#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?

set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
                'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
                'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
print()
print("Zadanie 3")
print("Wspólne geny dla wszystkich pacjentów:")
general_gene=set_gene1.intersection(set_gene2).intersection(set_gene3)
print(set_gene1.intersection(set_gene2).intersection(set_gene3))
print("Wspólne geny dla 1go i 3go pacjentów:")
print(set_gene1.intersection(set_gene3))
print("Geny chroby 1go pacjenta: ")
print(set_gene1.difference(general_gene))
print("Geny chroby 2go pacjenta: ")
print(set_gene2.difference(general_gene))
print("Geny chroby 3go pacjenta: ")
print(set_gene3.difference(general_gene))
print("_____________________________________")


######### Operatory porównania lokalnego i globalne
####################Przykład
### Sprawdź wynik działania następujących operacji:
# l1 = [5,10]
# l2 = [5,11]
#
# print(l1,l2)
# print('l1 == l2 wynik:',l1 == l2)
# print('l1 is l2 wynik:',l1 is l2)
# print('l1 != l2 wynik: ',l1 != l2)
# print('l1 is not l2 wynik:',l1 is not l2)
# print('l1 >= l2 wynik:', l1 >= l2)

## x or y	jeżeli x == False, to y, w przeciwnym razie x
## w przybliżeniu alternatywa
## x and y	jeżeli x == False, to x, w przeciwnym razie y
## w przybliżeniu koniunkcja
## not x	negacja

## Sprawdź wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
####################Przykład
# a = False
# b = 2
# c = True
#
# print(a or b)
# print(b or a)
# print(c or a)
# print(a or c)
# print(b and a)
# print(a and b)
# print(a and c)

###### Przykład
# list1 = [1,2,3,4,5,6,7,6,5,6,5]
# for element in list1:
#     print(element is 5)

# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
print("Zadanie")
lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
if "FGFR4" in lista_gene1 or "FGERA4" in lista_gene1:
    for i in range(0, len(lista_gene1)):
        if lista_gene1[i] == "FGFR4":
            print("Numer genu FGFR4: ", i)
        if lista_gene1[i] == "FGERA4":
            print("Numer genu FGERA4: ",i)
else:
    print("Nie ma takich genów")
print("____________________________________")

####################Łańcuchy znaków
## Zapoznaj się z wybranymi metodami dla typu string
## więcej metod znajdziesz tu: https://pl.python.org/docs/lib/string-methods.html
## s.endswith(przyrostek[, początek[, koniec]]) - sprawdzenia, czy napis jest zakończony napisem przyrostek
## s.index(napis[, początek[, koniec]]) - indeks wystąpienia napisu
## s.isalpha() - czy wszystkie znaki napisu są literami i napis składa się przynajmniej z jednego znaku.
# s.capitalize() - zmienia pierwszą literę na dużą\\
# s.center(długość) - Centruje napis w polu o podanej długości\\
# s.count(sub) - zlicza wystąpienie podciągu sub w napisie s\\
# s.encode(kodowanie) - zwraca zakodowaną wersję napisu ('utf-8', 'ascii', 'utf-16')\\
# s.isalnum() - sprawdza czy wszystkie znaki są znakami alfanumerycznymi\\
# s.isdigit() - sprawdza czy wszystkie znaki są cyframi\\
# s.islower() - sprawdza czy wszystkie litery są małe\\
# s.isspace() - sprawdza czy wszystkie znaki są białymi znakami\\
# s.isupper() - sprawdza czy wszystkie litery są duże\\
# s.join(t) - łączy wszystkie napisy na liście t używając s jako separatora\\
# s.lstrip() - usuwa początkowe białe znaki\\
# s.replace(old, new) - zastępuje stary podciąg nowym\\
# s.rstrip() - usuwa końcowe białe znaki\\
# s.split(separator) - dzieli napis używają podanego separatora\\
# s.strip() - usuwa początkowe i końcowe białe znaki\\
# s.upper() - Zwraca kopię napisu z wszystkimi literami zamienionymi na wielkie litery.

#### Przykład
# word = 'Python jest super, każdy to wie'
# print(word.capitalize())
# print(word.count('super'))
# print(word.endswith('per'))
# print(word.index('super'))
# print('-'.join(word))
# print(word.split(' '))
# print(word.upper())

##############  Zadania do wykonania
## 1. Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) Ile zdań jest w analizowanym tekście?


print("Zadanie  ")
text = "A co z Emmą? Kryje się na nią jakiś człowiek? " \
       "Shaunak Khire, współtwórca Stealth, twierdzi, że choć " \
       "Emma posiada zespół ludzkich trenerów, efekty jej pracy " \
       "są wyłącznie jej zasługą. Zawsze ciężko będzie laikom korzystającym" \
       " z tych usług wiedzieć na pewno, czy chodzi o maszynę czy o człowieka. "

print("Słowo \"Emma\" występuje ",text.count("Emma"), "razy.")
print(text.upper())
list_text  = text.split(" ")
print(list_text)
count = text.count(".")
count+=text.count("!")
count+=text.count("?")
count+=text.count("...")
print("Iłość zdań w tekście: ",count)
print("_______________________________________")


## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

print("Zadanie 2")
print("Wprowadź x:")
x = int(input())
print("Wprowadź x:")
y = int(input())
print("2x + 5y =",2*x+5*y)
print("____________________________________")

## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)
#
print("Zadanie 3")
print("Wprowadż imię")
a=input()
print("Wprowadź nazwisko")
b=input()
print("Ile lat masz?")
c=int(input())
print("Na jakim jest kierunku studyj?")
d=input()
print("Jestem", a, b, "mam", c, "lat studiuję", d)
print("____________________________________________")


## 4. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646

print("Zadanie 4")

if 1+2+10+20000001+4+347586970885 == 321784560456434534646:
    print("Tak")
else:
    print("Nie")
print("___________________________________________")


## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
##  użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0

print("Zadanie 5")
print("Wprowadź pierwszą liczbę")
a=int(input())
print("Wprowadź drugą liczbę")
b=int(input())
if (a+b)%2 == 0:
    print("Summa liczb jest", a+b,"- parzysta")
else:
    print("Summa liczb jest", a+b,"- nieparzysta")
print("____________________________________________")

## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
print("Zadanie 6")
print("Wprowadź pierwszą liczbę")
a=float(input())
print("Wybierz operacią: +, -, *, /, pot")
znak = input()
print("Wprowadź drugą liczbę")
b=float(input())


match znak:
    case "+": print(a,"+",b, "=",a+b)
    case "-": print(a,"-",b, "=",a-b)
    case "*": print(a,"*",b, "=",a*b)
    case "/":
        if b != 0:
            print(a,"/",b, "=",a/b)
        else:
            print("Nie wolno dzielić na 0")
    case "pot": print(a,"**",b, "=",a**b)
print("______________________________________")


## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)
print("Zadanie 7")
print("Wprowadź x")
x=int(input())
if 1<x<13 and (x!=5 or x < 0):
    print("X jest zgodny z warumkami")
else:
    print("X nie jest zgodny z warumkami")
print("_____________________________________________")


# Zadania dodatkowe:
# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania:
# "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.

print("Zadanie dodatkowe 1")
print("Wprowadż imię")
imie = input()
print("Wprowadż nazwisko")
nazwisko = input()
print("Wprowadż  wiek")
wiek = int(input())
pytania = [
    'Czy zdrowo się odżywiasz?',
    'Czy lubisz sport?',
    'Czy palisz?',
    'Czy lubisz pływać?',
    'Czy chcesz pracować?'
]
odpowiedzi = []
for i in pytania:
    print(i)
    odpowiedzi.append(input())

print(imie, nazwisko, "ma", wiek, "lat. odpowiedział/ła na następny pytania:")

for i in range (len(pytania)):
    print(pytania[i])
    print(odpowiedzi[i])
print("_________________________________________________________________")


# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.

print("Zadanie dodatkowe 2")
print("Wprowadż imie")
imie = input()
print("Wprowadż nazwisko")
nazwisko = input()
print("Wprowadż wiek")
wiek = int(input())
print("Jaki masz zawód?")
zawod = input()
print("Gdzie jest miejsce urodzenia?")
urodzenie = input()
print("Jakie masz zainteresowania?")
interes = input()
print(imie, nazwisko, "ma", wiek, "lat. Z zawodu jest", zawod,"Lubie", interes)
print("_______________________________________________________")


# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie
print("Zadanie 3")
samogloski = ["a","ą","e","ę","i","o","ó","u","y"]

print("Wprowadź spółgłoskę")
sp = input()

if sp not in samogloski and sp.isalpha():
    for a in samogloski:
        print(sp+a)
else:
    print("Bląd")
print("_________________________________________")

# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna
print("Zadanie 4")
print("Wprowadź imie")
imie = input()
list = ["Janusz","Grażyna"]
if imie in list:
    print("Dzień dobry ",imie)
else:
    print("Niestety nie jesteś Janusz lub Grażyna")