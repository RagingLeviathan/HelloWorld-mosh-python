import random
# print(random.random())
for i in range(3):
    print(random.randint(10, 20))

members = ['john', 'joe', 'warwick', 'lurcher']
leader = random.choice(members)
print('The leader is: ' + leader)


