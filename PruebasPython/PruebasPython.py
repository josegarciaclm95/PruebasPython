from itertools import count
from math import pow
# Double char
def double_char(s):
    r = ""
    for char in s:
        r = r + char*2
    return r

# Test
print(double_char("Hola mundo"))


# from collections import Counter
def triple_double(num1, num2):
    tripleFound = []
    #Counter return a dictionary where key is "1","2" and so on, and the value is the times it appears in num
    # a = dict((int(k),v) for k,v in Counter(str(num1)).items() if v >= 3)
    # b = dict((int(k),v) for k,v in Counter(str(num2)).items() if v >= 2)
    a = [int(x) for x in str(num1)]
    b = [int(x) for x in str(num2)]
    occurences1 = lookForRepeated(a,3)
    occurences2 = lookForRepeated(b,2)
    print(occurences1)
    print(occurences2)
    if len(set(occurences1).intersection(occurences2)) == 0:
        return 0
    else:
        return 1 
    print(a)
    
def lookForRepeated(numList, occurrences):
    occurFound = []
    found = 0
    aux = numList[0]
    for digit in numList:
        if digit == aux:
            found += 1
            if found == occurrences :
                occurFound.append(aux)
                found = 0
        else:
            aux = digit
            found = 1
    return occurFound

#Solucion de usuario rewk
def triple_double2(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])
# Test triple doble
a = triple_double(200058880,4558587)
print(a)


def tribonacci(signature,n):
    resultado = []
    resultado.extend(signature[:n])
    if(len(resultado)<n):
        for i in range(len(resultado),n):
            resultado.append(resultado[i-1] + resultado[i-2] + resultado[i-3]) 
    return resultado
 
# Test  
print(tribonacci([1,1,1],10))

#Secuencia que hace tri, bi, cuatri...segun el numero de elementos que tenga signature
def Xbonacci(signature,n):
    resultado = signature[:n]
    for i in range(n - len(signature)):
        resultado.append(sum(resultado[-len(signature):])) 
    return resultado




class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age
# Modificamos la propia clase Dog
Dog.bark = lambda x : "Woof!"

apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

print(apollo.bark())

#Spin words with more than five letters
def spin_words(sentence):
    return " ".join(list(map(lambda x : x if len(x) < 5 else x[::-1],[x for x in sentence.split()])))
# return [ x[::-1] for x in [x for x in sentence.split()] if len(x)>=5]
#print(" ".join([x for x in "A ver que puedes hacer".split()]))
print(spin_words("Hola mundo"))

def valid_parentheses(string):
    string = remove_text(string)
    test_valid(string)
    return string

def test_valid(string):
    fine = False
    if string[0] == "(":
        fine = test_valid(string[1:])
    
        
def remove_text(string):
    string = filter(lambda x : x == ")" or x == "(", string)
    return "".join(list(string))

print(valid_parentheses("hola () )() )()( world )()"))

def reverse_words(str0):
    aux = str0
    rest = ""
    word = [False, -1, -1]
    for x in range(len(str0)):
        if str0[x] != " " and not word[0]:
            #print(aux[x] + " " + str(x))
            word[0] = True
            word[1] = x
        elif str0[x] == " ":
            if word[0]:
                word[2] = x
                rest = aux[0:word[1]-1] + aux[word[1]:word[2]][::-1] + aux[word[2]:]
                word = [False, -1, -1]
    return rest


print(reverse_words("hola  mundo!! jaja saludos!:"))

    #return " ".join(list(map(lambda x : x[::-1], str.split())))
    
reverse_words("Hola  mundo")

def narcissistic( value ):
    result = 0
    str_value = str(value)
    power = len(str_value)
    for x in str_value:
       result += pow(int(x), power)
    return result == value

print(narcissistic(1547))
