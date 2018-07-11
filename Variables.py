import Classes

n = 10
m = 10

board = ["_"] * int(n)

for i in range(int(n)):
    board[i] = ["_"] * int(m)

players_turn = 2
game_turn = 0
tot_moves = 0

sniper = Classes.Weapon("sniper", damage=50, range_=5, dropoff=1 / 4)
shotgun = Classes.Weapon("shotgun", damage=70, range_=2, dropoff=1 / 2)
assult_rifle = Classes.Weapon("assult_rifle", damage=40, range_=4, dropoff=3 / 10)
pistol = Classes.Weapon("pistol", damage=5, range_=1, dropoff=1 / 5)
A = Classes.Character("A", speed=4, health=220, team=1, move=0, shoot=0, weapon_1=shotgun, weapon_2=pistol)
B = Classes.Character("B", speed=3, health=280, team=1, move=0, shoot=0, weapon_1=assult_rifle, weapon_2=pistol)
C = Classes.Character("C", speed=2, health=180, team=1, move=0, shoot=0, weapon_1=sniper, weapon_2=pistol)
a = Classes.Character("a", speed=4, health=220, team=2, move=0, shoot=0, weapon_1=shotgun, weapon_2=pistol)
b = Classes.Character("b", speed=3, health=280, team=2, move=0, shoot=0, weapon_1=assult_rifle, weapon_2=pistol)
c = Classes.Character("c", speed=2, health=180, team=2, move=0, shoot=0, weapon_1=sniper, weapon_2=pistol)

characters_alive = [A, B, C, a, b, c]