from typing import List, Dict

# Seznam pro ukládání úkolů: každý úkol je slovník s 'nazev' a 'popis'

ukoly: List[Dict[str, str]] = []

def pridat_ukol() -> None:
    """Umožní uživateli přidat úkol – název a popis. Kontroluje prázdné vstupy."""
    while True:
        nazev: str = input("Zadejte název úkolu: Úkol ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis: str = input("Zadejte popis úkolu: Popis pro úkol ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.\n")
        break

def zobrazit_ukoly() -> None:
    """Zobrazí všechny úkoly v seznamu s jejich názvy a popisy."""
    if not ukoly:
        print("Seznam úkolů je prázdný.\n")
        return

    print("Seznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. Úkol {ukol['nazev']} - Popis pro úkol {ukol['popis']}")
    print()

def odstranit_ukol() -> None:
    """Zobrazí úkoly a umožní uživateli vybrat jeden k odstranění."""
    if not ukoly:
        print("Žádné úkoly k odstranění.\n")
        return

    zobrazit_ukoly()

    try:
        cislo: int = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odebrany: Dict[str, str] = ukoly.pop(cislo - 1)
            print(f"Úkol '{odebrany['nazev']}' byl odstraněn.\n")
        else:
            print("Neplatné číslo úkolu. Zkuste to znovu.\n")
    except ValueError:
        print("Zadejte platné číslo.\n")

def hlavni_menu() -> None:
    """Hlavní nabídka programu. Nabízí volby pro práci se seznamem úkolů."""
    while True:
        print("Spravce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba: str = input("Vyberte možnost (1–4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zadejte prosím číslo od 1 do 4.\n")

# Spuštění pouze při přímém spuštění skriptu
if __name__ == "__main__":
    hlavni_menu()