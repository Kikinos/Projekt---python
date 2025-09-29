def ask(question, options, correct):
    print("\n" + question)
    i = 1                      
    for opt in options:        
        print(i, opt)          
        i += 1
    while True:
        try:
            choice = int(input("Tvoje volba (1-4): "))
            if 1 <= choice <= 4:
                return choice == correct
            else:
                print("Zadej číslo 1–4.")
        except ValueError:
            print("Zadej číslo 1–4.")

def main():
    print("=" * 40)
    print("   🎬 VÍTEJ V MALÉM FILMOVÉM KVÍZU 🎬")
    print("=" * 40)

    score = 0
    questions = [
        ("Kdo je režisérem filmu Pán prstenů?", 
         ["James Cameron", "Peter Jackson", "Christopher Nolan", "Steven Spielberg"], 2),

        ("Který film získal Oscara za nejlepší film roku 1994?", 
         ["Forrest Gump", "Pulp Fiction", "Lví král", "Titanic"], 1),

        ("Jak se jmenuje robot z Hvězdných válek, který mluví pípáním?", 
         ["C-3PO", "BB-8", "Wall-E", "R2-D2"], 4),

        ("Který herec hraje Iron Mana v Marvel filmech?", 
         ["Chris Hemsworth", "Robert Downey Jr.", "Tom Holland", "Mark Ruffalo"], 2),

        ("Který český film získal Oscara?", 
         ["Tmavomodrý svět", "Obecná škola", "Kolja", "Pelíšky"], 3),
    ]

    for q, opts, correct in questions:
        if ask(q, opts, correct):
            print("✅ Správně!")
            score += 1
        else:
            print("❌ Špatně!")

    print("\n" + "=" * 40)
    print(f"Tvůj výsledek: {score}/{len(questions)} bodů")

    if score == 5:
        print("🎉 Jsi filmový expert!")
    elif score >= 3:
        print("🍿 Dobrá práce, ale je co dohánět.")
    else:
        print("😅 Asi radši koukej na víc filmů!")
    print("=" * 40)

if __name__ == "__main__":
    main()
