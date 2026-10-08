import os
from datetime import datetime

vstupni_soubor = "postavy.txt"
vystupni_soubor = "oblibene-postavy.txt"

with open(vstupni_soubor, "r", encoding="utf-8") as soubor:
    radky = soubor.readlines()

with open(vystupni_soubor, "w", encoding="utf-8") as vystup:
    for radek in radky:
        radek = radek.strip()
        if not radek:
            continue

        jmeno, vek, pohlavi, zvire, datum, oblibenost = radek.split("#")

        try:
            vek = int(vek)
            oblibenost = float(oblibenost.replace(",", "."))
        except ValueError:
            continue

        if oblibenost > 2.5:
            print(f"Jméno: {jmeno}, Věk: {vek}, Pohlaví: {pohlavi}, Zvíře: {zvire}, Datum: {datum}, Oblíbenost: {oblibenost}")
            vystup.write(f"{jmeno}\t{vek}\t{pohlavi}\t{zvire}\t{datum}\t{str(oblibenost)}\n")