'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343.2 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  

'''

def calculate_weight_earth(mass):
    """
    Vypočítá váhu objektu na Zemi na základě hmotnosti a gravitačního zrychlení.
    """
    return mass * EARTH_GRAVITY

def calculate_weight_moon(mass):
    """
    Vypočítá váhu objektu na Měsíci na základě hmotnosti a gravitačního zrychlení.
    """
    return mass * MOON_GRAVITY

def light_travel_time(distance):
    """
    Vypočítá čas, za který světlo urazí danou vzdálenost.
    """
    return distance / SPEED_OF_LIGHT

def sound_travel_time(distance):
    """
    Vypočítá čas, za který zvuk urazí danou vzdálenost.
    """
    return distance / SPEED_OF_SOUND

if __name__ == "__main__":
        print(f"Tíha na Zemi: {calculate_weight_earth(70)} N")
        print(f"Tíha na Měsíci: {calculate_weight_moon(70)} N")
        print(f"Čas světla: {light_travel_time(1_000_000_000)} s")
        print(f"Čas zvuku: {sound_travel_time(1_000_000_000)} s")
        
        __all__ = [
            'EARTH_GRAVITY',
            'MOON_GRAVITY', 
            'SPEED_OF_LIGHT',
            'SPEED_OF_SOUND',
            'calculate_weight_earth',
            'calculate_weight_moon',
            'light_travel_time',
            'sound_travel_time'
        ]

        __version__ = "1.0.0"
        __author__ = "Kryštof Halška"
        __description__ = "Fyzikální konstanty a výpočetní funkce"        
