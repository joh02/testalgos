from datetime import datetime

# Datumsangaben im Format Jahr, Monat, Tag (Jahr, Monat, Tag)
datum1 = datetime(1997, 8, 10)
datum2 = datetime(2023, 9, 28)

# Berechnung der Differenz
differenz = abs((datum2 - datum1).days)

print(f'Die Tagesdifferenz zwischen {datum1.strftime("%d.%m.%Y")} und {datum2.strftime("%d.%m.%Y")} beträgt {differenz} Tage.')
