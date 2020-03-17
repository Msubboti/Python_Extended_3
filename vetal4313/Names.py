import random
n = ['Mary', 'Max', 'Lera', 'Alex', 'Anton']
s = ['Grey', 'Black', "Green", 'McFly', 'Stone']

i = 0
names = []

x = random.randint(0, 5)
y = random.randint(0, 5)
while i < 25:
    names.append(random.choice(n) + " " + random.choice(s))
    i += 1

count_names = []
for n in names:
    count = names.count(n)
    count_names.append(f"We've met {n}, {str(count)} times.")
persons_met = set(count_names)
print(persons_met)