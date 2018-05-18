import re
from collections import Counter

def mix(s1, s2):
    sol = []
    regex = r"[a-z]"
    s1, s2 = re.findall(regex, s1), re.findall(regex, s2)
    s1, s2 = Counter(s1), Counter(s2)
    print(s1)
    print(s2)
    for key, value in s1.items():
        if((s2[key] == 0 or s1[key] > s2[key]) and (s1[key] > 1)):
            sol.append((1, str(key * value)))
        elif ((s2[key] > s1[key]) and (s2[key] > 1)):
            sol.append((2, str(key * value)))
        elif ((s2[key] == s1[key]) and (s2[key] > 1)):
            sol.append(("=", str(key * value)))
    return sol


print(mix("A aaaa bb c", "& aaaa bbb c d"))
