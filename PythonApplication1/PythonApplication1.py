def exc1():
    l = []
    c=input('Start>')
    while c != '#':
        l.append(c)
        c=input('Continue?>')
    n_l = []
    for e in l:
        up = 0
        low = 0
        for e1 in e:
            if e1.isupper():
                up = up + 1
            elif e1.islower():
                low = low + 1
            else:
                continue;
        if up > low:
            e = e.upper()
            n_l.append(e)
        else: 
            e = e.lower()
            n_l.append(e)

    for e in n_l:
        print(e)
def exc2():
    c = input('Start?>')
    while c != '#':
        a = input('Number 1>')
        b = input('Number 2>')
        if a.isdigit() and b.isdigit():
            print(a, '+', b, '=', int(a)+int(b))
        c = input('Continue?>')
def exc3():
    students = []
    c = input('Start?>')
    while c != '#':
        (name, group) = input('Pair>').split(',')
        s = (name, group)
        students.append(s)
        c = input('Continue?>')
    print(students)
    students.sort(key = lambda x: x[1])
    print(students)
def exc4():
    l = []
    c = int(input('>'))
    while c != 0:
        l.append(c)
        c = int(input('>'))
    l.sort()
    print(l)
def exc5():
    l = []
    c = int(input('>'))
    while c != 0:
        l.append(c)
        c = int(input('>'))
    l.sort(reverse=True)
    print(l)
import random
def exc6():
    while True:
        ticket = []
        while len(ticket) != 6:
            r = random.randint(1,49)
            if ticket.count(r) > 0:
                continue
            else:
                ticket.append(r)
        rand = []
        while len(rand) != 6:
            r = random.randint(1,49)
            if rand.count(r) > 0:
                continue
            else:
                rand.append(r)
        print("Your ticket: ", ticket)
        print("Winner: ", rand)

        if rand == ticket:
            print("Congratulations!!!YOU ARE WINNER")
        else:
            print("You have lost!((")
        c = input("Try again?(y/n) : ")
        if c == 'n':
            break
def exc7(l):
    def asc(l):
        a = l[0]
        for c in l:
            if c >= a:
                a = c
            else:
                return False
        return True
    def desc(l):
        b = l[0]
        for c in l:
            if c <= b:
                b = c
            else:
                return False
        return True

    return asc(l) or desc(l)
def exc8():
    db = {}
    #queries = []
    s = input('>')
    while s != '#':
        (cus, prod, num) = s.split(' ')
        #queries.append((cus, prod, num))
        if cus not in db.keys():
            db[cus] = {}
        if prod not in db[cus].keys():
            db[cus][prod] = int(num)
        else:
            db[cus][prod] += int(num)
        s = input('>')

    for k in db.keys():
        print(f"{k}:")
        for k2 in db[k].keys():
            print(k2, " ", db[k][k2])
def exc9():
    N = int(input('N>'))
    p = {}
    for i in range(0, N):
        s = input('>').split(' ')
        p[s[0]] = s[1:]
    M = int(input('M>'))
    o = []
    for i in range(0, M):
        (s1,s2) = input('>').split(' ')
        if s1 =='read':
            if 'R' in p[s2]:
                o.append('OK')
            else:
                o.append('Access denied')
        elif s1 == 'write':
            if 'W' in p[s2]:
                o.append('OK')
            else:
                o.append('Access denied')
        else:
            if 'X' in p[s2]:
                o.append('OK')
            else:
                o.append('Access denied')
    for e in o:
        print(e)
def exc10():
    candidates = {}
    q = '0'
    while True:
        q = input(">")
        if q == '':
            break
        (cand, vot) = q.split(" ")
        if cand not in candidates.keys():
            candidates[cand] = int(vot)
        else:
            candidates[cand] += int(vot)
    print(candidates)
def exc11():
    N = int(input('N>'))
    states1 = {}
    for i in range(0, N):
        (s1, s2) = input('>').split(' ')
        states1[s1] = int(s2)
    d = {}
    cand = {}
    states2 = {}
    while True:
        s = input('>')
        if s=='':
            break
        (a, b) = s.split(' ')
        if b not in cand.keys():
            cand[b] = 0
        if a not in states2.keys():
            states2[a] = ""
        if a not in d.keys():
            d[a] = {}
        if b not in d[a].keys():
            d[a][b] = 1
        else:
            d[a][b] += 1

    for st in d.keys():
        states2[st] = max(d[st], key = lambda key: d[st][key])
        print(states2[st], " ", states1[st])


        



#exc1()
#exc2()
#exc3()
#exc4()
#exc5()
#exc6()


"""
l1 = random.sample(range(1, 100), 3)
print(l1)
print(exc7(l1))
l2 = [1,2,3,5,6,9]
l3 = [9,6,4,2,2,2]
print(exc7(l2))
print(exc7(l3))
"""

#exc8()
#exc9()
#exc10()
exc11()


