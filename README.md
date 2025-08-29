# Projektna naloga za predmet Uvod v programiranje

V sledeči projektni nalogi, napisani v okviru predmeta Uvod v porgramiranje, je predstavljena analiza nekaterih podatkov s spletne strani https://archiveofourown.org/. Spletna stran služi kot arhiv krajših fiktivnih del in omogoča brezplačno branje in objavljanje le-teh vsem uporabnikom. Zaradi same količine del sem nalogo omejila na analiziranje različnih kategorij, pod katerimi so dela objavljena. V drugem delu sem nato natančneje analizirala 1000 najbolj priljubljenih del, objavljenih pod področje "Harry Potter".

Za prvi del naloge so v datoteki `zajem_fandomi.py` zapisane funkcije, s pomočjo katerih dostopamo do posameznih kategorij na spletni strani in pri vsaki izluščimo imena posameznih področij (angleško *fandomov*) in pripadajoče število del.

Za drugi del naloge so v datoteki `zajem_dela.py` funkcije, s pomočjo katerih iz posameznega objavljenega dela izluščimo osnovne podatke kot so naslov, avtor, število besed .... Da zajamemo več kot le 20 del, objavljenih na osnovni strani, se moramo premikati po različnih straneh. To naredimo s pomočjo funkcij definiranih v `pomozne.py`. Tam so prav tako definirane funkcije, ki nam podatke zajete v tem delu naloge pomagajo lepše predstaviti v slovarjih.

Za dostop do spletne strani in zapis podatkov v datoteke so funkcije definirane v `pisanje_datotek.py`.

Celotno kodo lahko poženemo z zagonom glavne datoteke `glavna_zagon.py`. Pri tem se bosta obe csv datoteki shranili v mapo `podatki`. Če mapa pred tem ne obstaja, jo funkcija ustvari sama.

Analiza podatkov obeh csv datotek je nato predstavljena v zvezku `analiza_podatkov.ipynb`. Tudi to datoteko lahko v celoti poženemo od začetka do konca, saj so funkcije urejene v primeren vrstni red. 

