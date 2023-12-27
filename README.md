ELECTION SCRAPER

Vypracovaný třetjí projekt v rámci Engeto Python Akademie.

Popis projektu:

Třetí projekt má za úkol prověřit znalosti získané z celého kurzu. Cílem zde je zvytvořt scraper výsledků voleb z roku 2017, které jsou umístěny na webu. Napiš takový skript, který vybere jakýkoliv územní celek z tohoto odkazu: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ např. X u Benešov odkazuje sem: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101. Z tohoto odkazu chcete vyscrapovat výsledky hlasování pro všechny obce (resp. pomocí X ve sloupci Výběr okrsku).

Použíté knihovny

Knihovny, které jsou potřeba pro funkci programu jsou obsažené v souboru requirements.txt. Z tohoto souboru se instalují za pomocí příkazu v příkazovém řádku: $ pip install -r requirements.txt

Spuštění projektu

Hlavní soubor projektu projekt_3.py se spouští z příkazového řádku a požaduje dva argumenty (odkaz uzemního celku ke scrapování a druhý název výstupního souboru CSV) a název hlavního souboru projektu viz níže.

Příklad: python projekt_3.py "odkaz_uzemniho_celku" "nazev_vystupni_soubor"
