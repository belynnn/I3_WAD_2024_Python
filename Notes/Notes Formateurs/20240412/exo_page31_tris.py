ranks ={
    "Marie": 1,
    "Bernard" : 4,
    "François": 2,
    "Thomas": 12,
    "Hila": 15,}

for name, rank in list(ranks.items()):
    if rank >= 10:
        ranks.pop(name)

avg = sum(ranks.values())
avg /= len(ranks)

print(f"Moyenne des rangs du club: {avg}.")
