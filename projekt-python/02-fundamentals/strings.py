# Znakové řetězce mohou být uvozeny jednoduchými i dvojitými uvozovkami
course_name = "Python programming"

'''
Mnohdy programátor potřebuje řetězec, který je rozložen přes více řádků. Dosáhnout toho opět můžeme několika způsoby. 
První z nich, který se neváže pouze na řetězce, je spojení dvou po sobě jdoucích řádků znakem zpětného lomítka:
'''
# Obrácené lomítka - použití escape sekvence
hello = 'Toto je dlouhý řetězec obsahující mnoho\n\
řádek textu, stejně jej zapisujete i v C.\n\
    "Bílé" znaky na začátku řádku se samozřejmě\
 berou v úvahu.'

# print(hello)

'''
Python podporuje i tzv. raw řetězce (cosi jak ryzí, syrové řetězce), u nichž se řídící (escape) sekvence 
nepřevádí na odpovídající znaky.3.2. Raw řetězce charakterizuje předpona r. 
Potom řetězec r'\n' odpovídá dvěma znakům - zpětnému lomítku a znaku n, kdežto řetězec '\n' je jediný znak nového řádku:
'''

hello = r'Toto je dlouhý řetězec obsahující mnoho\n\
řádek textu, stejně jej zapisujete i v C.'

# print(hello)

'''
Další možností, jak vytvořit víceřádkový řetězec je jeho uzavření mezi odpovídající pár trojitých uvozovek. 
To má tu výhodu, že nemusíme explicitně zapisovat konce řádků, ty bude řetězec obsahovat přesně tak, 
jak jsou zapsány ve zdrojovém kódu
'''
# Předformátovaný text je uvozen trojími uvozovkami
message = '''
    Krásný pozdrav z výletu do \"přírody\"

    posílá 

       Andrej
'''
# print(message)

# Funkce len vrací délku řetězce
# print(len(message))

'''
Řetězce můžeme (podobně jako v jazyce C) indexovat. První znak řetězce pak má index 0. 
Poněvadž je Python velice uživatelsky přítulný, nekomplikuje život programátora speciálním typem určeným pro jediný znak - 
každý znak řetězce je opět řetězec s délkou 1. 
Na získání podřetězce nepotřebujeme žádné speciální funkce, samotný jazyk podporuje indexování subsekvencí. 
Subsekvenci indexujeme podobně jako jednotlivé znaky, pouze potřebuje dva indexy (začátek a konec subsekvence), 
které oddělíme dvojtečkou:
'''

# Vypíše 4. znak z řetězce
# print(course_name[3])

'''
Důležité je si zapamatovat, že slice indexy ukazují mezi znaky, přičemž levá hrana prvního znaku má číslo 0 
a pravá hrana posledního znaku řetězce o n znacích má index n:

 +---+---+---+---+---+ 
 | H | e | l | p | A |
 +---+---+---+---+---+ 
 0   1   2   3   4   5 
-5  -4  -3  -2  -1
Na prvním řádku jsou uvedeny všechny možné slice-indexy 0...5 v řetězci 'HelpA', na druhém pak odpovídající záporné hodnoty. 
Řez od i do j je tedy tvořen všemi znaky mezi hranami označenými mezi hranami označenými i a j.
'''

# Vypíše poslední znak z řetězce
# print(course_name[-1])
# Vypíše vše od 2. do 4. znaku (bez něj)
# print(course_name[1:3])

'''
Slice indexy mají specifické vlastnosti. Vynecháme-li první index, je za něj automaticky dosazena nula (začátek řetězce). 
Při neuvedení druhého indexu se použije délka řetězce (čili konec řetězce). 
'''

# Vypíše vše od 2. znaku
# print(course_name[1:])
# Vypíše vše od 2. znaku do předposledního
# print(course_name[1:-1])
# Vypíše 3 znaky od začátku
# print(course_name[:3])

'''
Další vlastností slice indexů je jejich automatické "zarovnávání" na rozměr řetězce. 
Je-li totiž index použitý ve slice konstrukci příliš velký, je nahrazen délkou řetězce. 
'''
# print(course_name[1:50])
# Pokud je dolní index větší než horní, je výsledkem prázdný řetězec:
# print(course_name[2:1])

first_name = "Donald  "
second_name = "  Trump"
# Spojování řetězců
# print(first_name + second_name)

# Opakování řetězců
# print(first_name + second_name * 3)

'''
Řetězce v jazyce Python nelze měnit. Pokusíme-li se změnit určitou pozici v řetězci, dojde k chybě.
'''
# first_name[0] = 'R'
'''
Proto jedinou cestou, jak vytvářet nové řetězce, je jejich kombinování, které je velice jednoduché a přitom efektivní:
'''
# print('R' + first_name[1:])

# Formátovaný výstup, použití řetězcových funkcí
# print(f"{first_name.upper().rstrip()} {second_name.lower().lstrip()} {5 * 4} {len(message)}")

# Nalezení pozice podřetězce v řetězci
# print(first_name.find("na"))

# Nahrazení podřetězce v řetězci
# print(first_name.upper().replace("D", "*"))

# Zjištění výskytu podřetězce
# print("na" not in first_name)

'''
Python umí pracovat s Unicode řetězci úplně stejným způsobem jako s obyčejnými řetězci. 
Dokonce je možné díky konverzním funkcím snadno převádět obyčejné řetězce na Unicode a zpět.
Unicode řetězce můžeme zapisovat přímo ve zdrojovém kódu programu. 
Pouze před samotný řetězec vložíme prefix u (podobně jako u raw řetězců prefix r):
'''

# print(u'\xe4\xf6\xfc')

'''Pro konverzi znaků můžeme použít interní funkci encode(), 
která umožňuje přístup ke všem registrovaným kodekům (např. Latin-1, ASCII, UTF-8 nebo UTF-16). '''

# print(u'äöü'.encode('utf-8'))
# print(u'čřž'.encode('latin2'))

'''Opačnou konverzi umožňuje funkce decode(), které lze opět předat jediný argument - jméno kódování, 
ve kterém je původní osmibitový řetězec.
'''

# print(b'\xc3\xa4\xc3\xb6\xc3\xbc'.decode('utf-8'))
# print(b'\xe8\xf8\xbe'.decode('windows-1250'))

''' 
Programátorská výzva:
Použijte kombinaci různý možností pro práci s řetězci (včetně různých funkcí) i jiných prvků jazyka Python 
(ternární operátor, matematické funkce atd.) k co nejefektivnějšímu řešení následujících cvičení (čím kratší
funkční kód, tím lepší).

1. Převeďte "česky" zadané datum - např. 12. 10. 2020 - do podoby "databázové" podoby - např. 2020-10-12
2. Vytvořte funkci, která vyrobí ze zadaného sousloví:
   a) identifikátor pro proměnné používané v Pythonu - např. To je proměnná v Pythonu = to_je_promenna_v_pythonu
   b) identifikátor pro camel syntax v JS - např. To je proměnná v Pythonu = toJePromennaVPythonu 
   Obě možnosti by měly být vyřešeny v jedné funkci s využitím parametrů.
   Kdo si chce úkol trochu zjednodušit, nemusí řešit znaky s českou diakritikou. 
3. Vytvořte funkci, která vygeneruje náhodná hesla pro počet osob zadaný v parametru tak, aby heslo začínalo
   3 velkými písmeny, pokračovalo 3 malými písmeny, jedním speciálním znakem (-/+*) a končilo 3 náhodnými číslicemi.
'''

def cz_date_to_db(date_str: str) -> str:
   """Převede datum z formátu 'DD. MM. YYYY' (mezery a oddělovače volitelné) na 'YYYY-MM-DD'.
   Příklad: '12. 10. 2020' -> '2020-10-12'
   """
   m = re.match(r'^\s*(\d{1,2})\s*[.\-/]\s*(\d{1,2})\s*[.\-/]\s*(\d{2,4})\s*$', date_str)
   if not m:
      raise ValueError("Neplatný formát data")
   day, month, year = map(int, m.groups())
   if year < 100:
      year += 2000
   if not (1 <= month <= 12 and 1 <= day <= 31):
      raise ValueError("Neplatný den nebo měsíc")
   return f"{year:04d}-{month:02d}-{day:02d}"
print(cz_date_to_db("12. 10. 2020"))

import re, unicodedata
import random
import string

def make_identifier(text: str, style: str = "snake") -> str:
    """Vytvoří identifikátor ve stylu snake_case, camelCase."""

    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))

    words = re.findall(r"[A-Za-z0-9]+", text)
    if not words:
        return ""

    style = style.lower()
    if style == "snake":
        ident = "_".join(w.lower() for w in words)
    elif style == "camel":
        ident = words[0].lower() + "".join(w.capitalize() for w in words[1:])
    else:
        raise ValueError(f"Neznámý styl: {style}")

    return ident

print(make_identifier("To je proměnná v Pythonu", "snake"))
print(make_identifier("To je proměnná v Pythonu", "camel"))

def generate_passwords(count: int) -> list:
   """Vygeneruje náhodná hesla pro zadaný počet osob.
   Formát hesla: 3 velká písmena + 3 malá písmena + 1 speciální znak (-/+*) + 3 číslice
   """
   passwords = []
   special_chars = "-/+*"
   
   for _ in range(count):
      password = (
         ''.join(random.choices(string.ascii_uppercase, k=3)) +
         ''.join(random.choices(string.ascii_lowercase, k=3)) +
         random.choice(special_chars) +
         ''.join(random.choices(string.digits, k=3))
      )
      passwords.append(password)
   
   return passwords

passwords = generate_passwords(5)
for i, password in enumerate(passwords, 1):
   print(f"Osoba {i}: {password}")
