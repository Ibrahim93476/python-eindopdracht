player_class = "Warrior"

match player_class:
    case "Warrior":
        health = 150
        damage = 20

    case "Mage":
        health = 80
        damage = 35

    case "Archer":
        health = 100
        damage = 25

    case "Rogue":
        health = 90
        damage = 30

    # Bonus classes

    case "Paladin":
        health = 180
        damage = 15

    case "Necromancer":
        health = 70
        damage = 40

    case _:
        health = 0
        damage = 0
        print("Unknown character class!")

if health > 0:
    print("Character class:", player_class)
    print("Health:", health)
    print("Damage:", damage)
