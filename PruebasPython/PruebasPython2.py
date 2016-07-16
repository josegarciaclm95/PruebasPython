# from functools import reduce
from itertools import permutations
from itertools import combinations

def declare_winner(fighter1, fighter2, first_attacker):
    first = fighter1 if fighter1.name == first_attacker else fighter2
    victim = fighter2 if fighter1.name == first_attacker else fighter1
    while(1):
        victim.health -= first.damage_per_attack
        if(victim.health <= 0):
            return first.name
        else:
            first, victim = victim, first


def min_unfairness(arr,k):
    return min([max(x) - min(x) for x in permutations(arr,k)])


def min_unfairness2(arr,k):
    return reduce(min,[max(x)-min(x) for x in permutations(arr,k)], float("inf"))

print(min_unfairness([1,2,3,4,5,6],2))

def power(s):
   return [list(a) for a in sorted(set([y for x in range(len(s) + 1) for y in permutations(s,x)]))]

def power2(s):
    return [list(y) for x in range(len(s) + 1) for y in combinations(s,x)]

print(power2([1,2,3]))

def namelist(names):
    result = ''
    if len(names) == 0:
        return result
    result = names[0]['name']
    if len(names) == 1:
        return result
    for x in range(1,len(names)):
        if(x + 1 == len(names)):
            result += ' & ' + names[x]['name']
        else:
            result += ', ' + names[x]['name']
    return result
