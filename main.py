from utils import *
from logic import *
clauses = []
clauses.append(expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
clauses.append(expr("Enemy(Nono, America)"))
clauses.append(expr("Owns(Nono, M1)"))
clauses.append(expr("Missile(M1)"))
clauses.append(expr("(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)"))
clauses.append(expr("American(West)"))
clauses.append(expr("Missile(x) ==> Weapon(x)"))
clauses.append(expr("Enemy(x, America) ==> Hostile(x)"))
crime_kb = FolKB(clauses)
answer = fol_fc_ask(crime_kb, expr('Hostile(x)'))
print("List of hostile nations")
print(list(answer))
answer = fol_fc_ask(crime_kb, expr('Criminal(x)'))
print("List of criminals")
print(list(answer))