from random import randint

list_monster = []

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
    for idx, monster in enumerate(list_monster, 1):
        print (
            f"{idx}. Name: {monster['name']} // Level: {monster['level']} // HP: {monster['hp']} // Damage: {monster['damage']} // XP: {monster['xp']}"
        )

def roll_dice(sides):
    return randint(1, sides)

def start_battle(player):
    while player["hp"] > 0 and any(monster["hp"] > 0 for monster in list_monster):
        print("Escolha um monstro para atacar:")
        display_monsters()
        action = input("Digite !atacar <número do monstro> para atacar: ")

        if action.startswith("!atacar"):
            try:
                _, monster_index = action.split()
                monster_index = int(monster_index) - 1
                if 0 <= monster_index < len(list_monster):
                    monster = list_monster[monster_index]
                    if monster["hp"] > 0:
                        print("Digite !dado<numero de lados> para rolar o dado e atacar:")
                        dice_action = input()
                        if dice_action.startswith("!dado"):
                            try:
                                sides = int(dice_action[5:])
                                player_damage = hit_monster(player, monster, sides)
                                print(f"Você causou {player_damage} de dano ao {monster['name']}!")
                                if monster["hp"] <= 0:
                                    print(f"Você derrotou {monster['name']}!")
                                    player['xp'] += monster['xp']
                                    if player['xp'] >= player['max_xp']:
                                        level_up_player(player)
                                if any(monster["hp"] > 0 for monster in list_monster):
                                    monster_damage = hit_player(player, monster)
                                    print(f"{monster['name']} causou {monster_damage} de dano a você!")
                                display_info_battle(player, monster)
                            except ValueError:
                                print("Número de lados inválido.")
                    else:
                        print(f"{monster['name']} já foi derrotado.")
                else:
                    print("Número do monstro inválido.")
            except ValueError:
                print("Comando inválido. Use !atacar <número do monstro>.")
        else:
            print("Comando inválido.")
        
        if player["hp"] <= 0:
            print("Você foi derrotado!")
            break

    if player['hp'] > 0:
        print(f"{player['name']} venceu todos os monstros e ganhou {player['xp']} de XP!")
        display_player(player)
    else:
        print("A batalha terminou.")

def hit_monster(player, monster, sides):
    roll = roll_dice(sides)
    damage = player['damage'] + roll
    monster['hp'] -= damage
    return damage

def hit_player(player, monster):
    roll = roll_dice(20)  # Monstro sempre rola um d20
    damage = monster['damage'] + roll
    player['hp'] -= damage
    return damage

def display_info_battle(player, monster):
    print(f"Player: {player['hp']}/{player['max_hp']}")
    print(f"Monstro: {monster['name']} {monster['hp']}/{monster['max_hp']}")
    print('--------------------\n')

def level_up_player(player):
    player['level'] += 1
    player['xp'] = 0
    player['max_xp'] *= 2
    player['max_hp'] += 20
    player['damage'] += 5
    reset_player(player)
    print(f"{player['name']} subiu para o nível {player['level']}!")

def reset_player(player):
    player['hp'] = player['max_hp']

def display_player(player):
    print(
        f"Name: {player['name']} // Level: {player['level']} // HP: {player['hp']}/{player['max_hp']} // Damage: {player['damage']} // XP: {player['xp']}/{player['max_xp']}"
    )

def create_player(name, hp, max_hp, level, xp, max_xp, damage):
    return {
        "name": name,
        "hp": hp,
        "max_hp": max_hp,
        "level": level,
        "xp": xp,
        "max_xp": max_xp,
        "damage": damage,
    }

# Cria o jogador
name = input("Digite o nome do seu personagem: ")
hp = int(input("Digite o HP inicial do seu personagem: "))
max_hp = hp
level = 1
xp = 0
max_xp = 50
damage = int(input("Digite o dano base do seu personagem: "))
player = create_player(name, hp, max_hp, level, xp, max_xp, damage)

# Reseta e cria novos monstros
reset_player(player)
new_monsters(5)

# Exibe a batalha
display_player(player)
start_battle(player)
