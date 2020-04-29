"""
Definieren Sie den Tag, den Monat und das Jahr Ihres Geburtstages als Integerkonstanten und geben Sie den Satz:
  Ich wurde am tt.mm.jjjj geboren.
auf dem Bildschirm aus, wobei tt, mm und jjjj durch die konkreten Integerkonstanten ihres Geburtstages zu ersetzen sind.
"""

tag = 2
monat = 9
jahr = 1981

# https://pyformat.info/ section Padding numbers
print("Ich wurde am {:02d}.{:02d}.{:04d} geboren.".format(tag, monat, jahr))
