from random import randint

list_monster = []
player = {
    "name": "Stand",
    "hp": 100,
    "max_hp": 100,
    "level": 1,
    "xp": 0,
    "max_xp": 50,
    "damage": 20,
}

def create_monster():
    level = randint(3, 15)

    new_monster = {
        "name": f"Monster #{level}",
        "level": 2 * level,
        "damage": 2 * level,
        "hp": 100,
        "max_hp": 100,
        "xp": level // 2,
    }

    return new_monster

def new_monsters(n_npcs):
    for _ in range(n_npcs):
        new_monster = create_monster()
        list_monster.append(new_monster)

def display_monsters():
    for monster in list_monster:
        print (
            f"Name: {monster['name']} // Level: {monster['level']} // HP: {monster['hp']} // Damage: {monster['damage']} // XP: {monster['xp']}"
        )

def display_player():
    print(
        f"Name: {player['name']} // Level: {player['level']} // HP: {player['hp']}/{player['max_hp']} // Damage: {player['damage']} // XP: {player['xp']}/{player['max_xp']}"
    )

def reset_player():
    player['hp'] = player['max_hp']

def start_battle(monster):
    while player["hp"] > 0 and monster["hp"] > 0:
        hit_monster(monster)
        if monster["hp"] > 0:
            hit_player(monster)
        display_info_battle(monster)
    
    if player['hp'] > 0:
        print(f"{player['name']} venceu e ganhou {monster['xp']} de XP!")
        player['xp'] += monster['xp']
        if player['xp'] >= player['max_xp']:
            level_up_player()
        display_player()
    else:
        print(f"{monster['name']} venceu!")
        display_monster_info(monster)

def hit_monster(monster):
    monster['hp'] -= player['damage']

def hit_player(monster):
    player['hp'] -= monster['damage']

def display_info_battle(monster):
    print(f"Player: {player['hp']}/{player['max_hp']}")
    print(f"Monstro: {monster['name']} {monster['hp']}/{monster['max_hp']}")
    print('--------------------\n')

def level_up_player():
    player['level'] += 1
    player['xp'] = 0
    player['max_xp'] *= 2
    player['max_hp'] += 20
    player['damage'] += 5
    reset_player()
    print(f"{player['name']} subiu para o nível {player['level']}!")

def display_monster_info(monster):
    print (
        f"Name: {monster['name']} // Level: {monster['level']} // HP: {monster['hp']} // Damage: {monster['damage']} // XP: {monster['xp']}"
    )

# Reseta o player e cria novos monstros
reset_player()
new_monsters(5)

# Exibe a batalha
display_player()
display_monsters()
selected_monster = list_monster[1]
start_battle(selected_monster)
