<center>
    <h1>Python Basis</h1>
    <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png"/>
    <br>
    <h4> Cursus dag 1</h4>
    <img width=180px src="https://www.nieuwlandgeo.nl/wp-content/themes/nieuwland/img/nieuwland-geo-informatie.png"/>
</center>



# Overzicht dag 1
## Dag 1
   * Python console
   * Variabelen 
   * IDEs & Debugging
   * Functies oproepen
   * Scripts schrijven en uitvoeren
   * Loops & if-else
   * Lists
   * Methoden

# Python opdrachtprompt
* Open je systeem opdrachtprompt en run command: `python3`

```python
$ python3
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

* gebruik `quit()` of `Cntrl-D` om de pythonprompt te aftesluiten.
* The python opdrachtprompt wordt ook _python REPL_ (Read-Eval-Print Loop), _python interactive shell_ of _python console_ genoemd
* Warom python**3**? Op veel compters is ook nog een oudere python2 geinstelleerd. Python2 is veroudert, probeer altijd python3 te gebruiken

# Variabelen
* Voorbeeld: oppervlakte berekenen: `Area = width * height`


```python
13.41 * 4.75
```




    63.6975




```python
width = 13.41
height = 4.75
width * height
```




    63.6975



Een waarde aanpassen:


```python
13.41 * 2
```




    26.82




```python
height = 2
width * height
```




    26.82



Resultaat hergebruiken:


```python
13.41 * 2
```




    26.82




```python
area = width * height
area
```




    26.82



## Variabelen (2)
* “opberglocaties” voor gegevens in een programma.
* Specifiek en hoofdlettergevoelig naam, conventie voor namen: `kleine_letters_laag_streepje`
* __Geen automatische updates!__
* `=` is toewijzing operator, **niet** gelijkteken
* Python berekend eerst het resultaat berekend, en wijst dan aan de variabele toe.


```python
height = 1.433
print(area)
```

    26.82



```python
area = width * height
print(area)
```


```python
volume
```

# Variabelen: Oefeningen

[IntroducingVariables](https://futurecoder.io/course/#IntroducingVariables)

De links naar de oefeningen staan op:

### [github.com/latlon-dev](https://github.com/latlon-dev)
`->` _Cursus_Python_Basis_

# Scripts schrijven en uitvoeren
* Om dezelfde code meerdere keren uit te voeren, sla je hem als script.
* Je slaat je script dan op als `.py`-bestand. Deze bestanden worden ook Pyhton **modules** genoemd.
* In de systeem opdrachtprompt kan je scripts uitvoeren met  `python mijn_script_naam.py`

# Commentaar
* Annotaties in het script
* Beschrijft het __waarom__
* `python` ignoreert commentaar!


```python
print('a') # hier volgt commentaar
# code tijdelijk ""uitcommentariëren"": 
# print('b') 
print('c') # commentaar helpt jij en anderen je script te begrijpen 
```

# Python Software-ontwikkelomgevingen (IDEs) 
Voordelen van een IDE:

* Project organiseren
* Debugging:
    * stap voor stap door je code
    * overzicht over alle variabelen
* Gemak en efficiëntie: autocompletion, formatting, linting


# Veel gebruikte IDEs voor Python:
* __`Python` specific__
    * PyCharm
    * WingIDE
    * [Thonny](https://thonny.org/) (voor beginners, gebruikt in deze cursus)
    * Online: [futurecoder.io](https://futurecoder.io/course/#ide)
* __Universele IDEs__:
    * [VSCode](https://code.visualstudio.com/docs/python/python-tutorial)
    * Online: [replit.com](https://replit.com/join/mgjvvgnpnw-latlondev) 
* __Jupyter Notebooks__
    * Vermengen van text en code, zoals deze presentatie.
    * Online: [kaggle.com](https://www.kaggle.com/code), [Google colab](https://colab.research.google.com/), [mybinder.org](mybinder.org) (voor notebooks op github)

# Debuging in een IDE
* __Breakpoints__ en stap voor stap uitvoeren
* __Variabelen lijst__: waarde van alle varaiblen tijdens het uitvoeren
* __Debug console__: je kan tijdens het debuggen interactief commandos gebruiken!

## Oefen in Thonny
* Schrijf een script en zet een breakpoint
* Let goed op de variabelen lijst!
* Schrijf een script met een foutje!


```python
# hello.py
name  = "Abby"
greeting = "hello " + name + "!"
print(greeting)
print(other_greeting)
```

# For loops


```python
name = 'Bob'
for letter in name: 
    print(letter) 
```

 * een __blok__ van aanweizingen __voor een vast aantal keren uit te voeren__, bijvoorbeeld voor het aantal
letters in een woord.

## For loops (2): inspringing
* Python leidt af waar het blok begint en eindigt door inspectie van de __inspringing__, 
    * Je moet een zelfde aantal spaties plaatsen voor iedere regel in het blok.
    * (Andere talen gebruiken hiervoor vaak accoladen { }.)


```python
name = 'Bob'
for i in name: 
    print(i)
    print('!')
x = 0

```


```python
name = 'Bob'
for i in name: 
    print(i)
print('!')
```

## For loops
[Oefenigen](https://futurecoder.io/course/#IntroducingForLoops)

# Als - dan Beslissingen
* Soms wil je keuzes maken in je programma. Als dit, dan dat.
* `if`: een voorwaarde nagaan (is leeftijd groter dan 65?) en bepaalde opdrachten uitvoeren
* net als bij `for` worden inspringen gebruikt
* `=` toewijsings operator,  `==`, `<`, `!=`, ... vergelijkings operatoren!


```python
geboorteJaar = 1912
huidigJaar = 2022
leeftijd = huidigJaar - geboorteJaar
if leeftijd == 36:
    print("je bent even oud als ik!")
```

# Else en elif 


```python
leeftijd = 27
if leeftijd > 65:
    print('Geniet van uw pensioen!')
    print('Jij bent', leeftijd, 'jaar')
else:
    jaren_tot_pensioen = 65 - leeftijd
    print("Nog ", jaren_tot_pensioen, " jaren werken!")
```

    Nog  38  jaren werken!



```python
# check who is older:
my_age = 35
your_age = 40
if my_age == your_age: print("We're share the same age.")
elif my_age < your_age: print("I'm younger.")
else: print("I'm older.")
```

    I'm younger.


[Oefeningen](https://futurecoder.io/course/#IntroducingIfStatements)

# Waarheidswaarde: Boolean Variabelen
Waarheidswaarde (ja, klopt of nee, fout) wordt in variable opgeslagen als `True` of `False`



```python
my_age = 35
your_age = 40
my_age < your_age
```




    True




```python
younger = my_age < your_age
older = my_age > your_age
print(older)
```

    False



## Waarheidswaarde en Beslissingen


```python
younger = True
if younger:
    print("I'm younger!")
```


```python
if False:
    print("This line never gets printed!")
```

# Functies oproepen


```python
len('Text')
```


```python
round(2.16, 1)
```


```python
round
```

* Functies zijn __herbruikbare__ stukjes code
* Aantal __argumenten__ die tussen haakjes staan: `round(2.15, 1)`
* Vergelijkbaar met Excel functies `=AFRONDEN(A2;1)` 

## Functies oproepen (2): hulp en argumenten


```python
help(round)
```


```python
rounded_number = round(2.16)
print(rounded_number)
```

    2



```python
round(222.16, -2)
```




    200.0



## Functies oproepen: extra oefeningen
[Extra oefeningen (NL)](https://cscircles.cemc.uwaterloo.ca/2-functions-nl/)

# Lijsten
* Data Science, GIS: vaak reeks van waarden
* Python: `list` (In vele andere programmeertalen : `array`)


```python
measurement0 = 0.01
measurement1 = 11.1
measurement2 = 12.2
measurement3 = 13.3
measurement4 = 14.4
```


```python
measurements = [0.01, 11.1, 12.2, 13.3, 14.4]   
print(measurements)
```


```python
# loop over the the list and print one element per line:
for i in measurements:
    print(i)
```

## Lijsten (2): index
* Lijst element oproepen met idex `measurements[0]` 
* __het eerste element heeft index 0!__


```python
measurements[0]
```


```python
measurements[2] = 2222.2
measurements
```

## Lijsten (3): Slicing & lengte
* bereik van een lijst "selecteren":  `measurements[1:2]` verglijkbaar met Excel bereik (A1:A4)


```python
print(measurements[0:3])
```


```python
print(measurements[-2:])
```


```python
print(len(measurements))
```

### Lijsten (4)
* Lijstem samenvoegen: `+`


```python
more_measurements = measurements + [15.5, 16.6]
print(more_measurements)
```

* Twee namen voor een lijst (__!= kopiëren__)
* Elk naam is een __verwijzing naar de zelfde lijst__


```python
m2 = measurements
print(m2)
```


```python
measurements[0] = 0.9999
print(m2)
```

# Python Types
Elk variable heeft een "type". Wij zijn nu al verschillende types tegen gekomen:

| Data type       | Voorbeeld               | Variable Type (en afkorting) |
|-----------------|-------------------------|------------------------------|
| Hele getal      | `age = 32`              | __Integer__  (`int`)         |
| Kommagetal      | `decimal_number = 1.33` | __Float__ (`float`)          |
| Waarheidswaarde | `younger = True`        | __Boolean__ (`bool`)         |
| Tekenreeks      | `text = 'abc'`          | __String__ (`str`)           |
| Lijst _         | `m2 =[1,2,3]`           | __List__ (`list`)            |


```python
age = 32
type(age)
```

## Python Types (3)
* Gedrag van python verschilt per type:


```python
1 + 1
```


```python
"1" + "1"
```


```python
# Verschillende types combineren?
1 + "1"  
```

## Python Types (5) extra oefeningen
[Extra oefeningen types (NL)](https://cscircles.cemc.uwaterloo.ca/4-types-nl/)

# Methoden

* Alle Variabelen in Python zijn `objects`
* Python `objects` hebben 
    * een `type`
    * `attributes` en `methods`: eigenschappen en functies 

* __String__ `text = 'abc'`:   
    * `.replace()`
    * `.upper()` 
    * ...
* __Float__: `decimal_number = '1.33'`
    * `.as_integer_ratio()`, ...
* __List__: `m2 =[1,2,3]'`
    * `.append()`
    * `.reverse()`
    * ...  

|Data type |     Voorbeeld                |Variable Type (en afkorting)          | Methoden|
|-----------|-------------------------|--------------|--|
|Hele getal |`age = 32`             |  __Integer__  (`int`)      | `.to_bytes()` ...|
|Kommagetal |`decimal_number = 1.33`|  __Float__ (`float`)|  `.as_integger_ratio()`, ...  |
|Waarheidswaarde |`younger = True`|  __Boolean__ (`bool`)   |   |
|Tekenreeks |`text = 'abc'`           |  __String__ (`str`)     |  `.replace()`, `.upper()`, ...    |
|Lijst _|`m2 =[1,2,3]`           | __List__ (`list`)  |  `.append()`, `.reverse()`, ...        |

## Methoden (2): dir(): alle methodes van een object 


```python
text = "Arnhem is de hoofdstad van Gelderland."
print(dir(text)) # get all attributes and methods of an object
    
```


```python
text.upper()
```


```python
text.split()
```


```python
text.__class__
```

## Methoden (3): string methoden



```python
text = "Arnhem is de hoofdstad van Gelderland."
print(text.replace('Arnhem', 'Bemmel'))
print(text.index('is'))
print(text)
```

# Strings vs Lists
* _Index_ & _slice_ (net als met lijsten)
* Anders dan lijsten kunnen _strings_ __niet verandert__ worden! (strings zijn niet _mutuable_)


```python
print(text[0:9]) 
```


```python
text[4] = 'a' # -> TypeError!
```

* Lijts __kunnen__ verandert worden, ook door methoden:


```python
my_list = [0,1,2]
my_list.reverse()
print(my_list)
```

[Oefeningen lijsten & methoden](https://futurecoder.io/course/#IntroducingLists)

[Extra oefeningen methoden (NL)](https://cscircles.cemc.uwaterloo.ca/14-methods-nl/)

# Huiswerk 1: decimal degrees

Schrijf een script dat een lijst met strings met coördinaten in  `"ddd°mm′ss′N, ddd′mm′ss′W"` formaat omwandelt in een genestelde lijst met decimaal onderverdeelde graden `ddd,dddd`.


```python
# input
coordinates = ["52°22′23″N, 4°53′36″E", "33°27′0″S, 70°40′0″W"]

# ... jouw code! ...

# expected output:
decimal_degrees =[[52.3731, 4.8933], [-33.45, -70.6667]]
```

Je zal `for` loops, `if` beslissingen, de string methjods [`.strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip), [`.split()`](https://docs.python.org/3/library/stdtypes.html#str.split), [`.find()`](https://docs.python.org/3/library/stdtypes.html#str.find) kunnen gebruiken, misschine ook de [`in`](https://docs.python.org/3/reference/expressions.html#in) operator en [string indexing](https://cscircles.cemc.uwaterloo.ca/7a-strings-nl/#:~:text=Het%20bewerken%20van%20een%20string%20door%20deze%20te%20zien%20als%20een%20rij%20karakters%3A%20S%5B%5D).
Om een string "0.45" om te wandelen in een kommagetal kan je de ingebouwde function `float()` gebruiken. Andere oplossingen zijn ook goed, maar gebruik alleen "built-in" functies en methoden, geen packages (geen `import`). Probeer zo min mogelijk code te gebruiken en niet op stack-overflow te zoeken. Je kan je script naar mij mailen, ook als het nog niet helemaal werkt!

# Huiswerk 2: optioneel

[Caesar's JVTIVK JRCRU IVTZGV](https://cscircles.cemc.uwaterloo.ca/15c-nl/): schrijf een simple code decrypting script!
 
Doe eerst [deze oefening](https://cscircles.cemc.uwaterloo.ca/7a-strings-nl/#:~:text=Codes%20voor%20karakters).
