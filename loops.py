monster_health = 150
player_damage = 25
attacks = 0

while monster_health > 0:
    monster_health -= player_damage
    attacks += 1

    if monster_health < 0:
        monster_health = 0

    print("Monster health:", monster_health)

print("Monster defeated!")
print("Total attacks:", attacks)

monsters = [150, 100, 75]

for monster_health in monsters:
    attacks = 0

    print("\nNew monster appeared!")

    while monster_health > 0:
        monster_health -= player_damage
        attacks += 1

        if monster_health < 0:
            monster_health = 0

        print("Monster health:", monster_health)

    print("Monster defeated!")
    print("Total attacks:", attacks)
