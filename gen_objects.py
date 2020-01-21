import random

def arr(n, minn, maxn):
    a = [random.randint(minn, maxn) for i in range(n)];
    return ' '.join(map(str, a));
    
def seg(l, r):
    tr = random.randint(l + 1, r);
    tl = random.randint(l, tr);
    return ' '.join(map(str, [tl, tr]));
        
def string(n, maxn):
    maxn -= 'a'
    a = [chr(random.randint(0, maxn) + ord('a')) for i in range(n)]
    return ''.join(a);

def permutation(n):
    a = [i + 1 for i in range(n)]
    random.shuffle(a);
    return ' '.join(map(str, a));    

#NOTWORKING------------------------
def requests(n, pool, fr, to, addchar):   
    a = [str(random.choice(pool)) + ' ' + seg(fr, to) for i in range(n)]
    return '\n'.join(map(str, a));    

#generate tree with size = n, deep = [0, 1000]
def tree(n, deep):
    s = ''
    bal = 0
    n -= 1
    for i in range(n * 2):
        if (bal == 0):
            s += '['
            bal += 1
            continue;
        if (n * 2 - i == bal):
            s += ']'
            bal -= 1
            continue;
        if (random.randint(0, 1000) <= deep):
            bal += 1
            s += '['
        else:
            bal -= 1
            s += ']'
    n += 1
    s = '[' + s + ']'
    indexes = [0] * 2 * n
    stack = [] 
    cur_index = 0;
    for i in range(n * 2):
        if (s[i] == '['):
            stack.append(cur_index)
            indexes[i] = cur_index
            cur_index += 1
        else:
            indexes[i] = stack.pop()
    res = []
    for i in range(n):
        cur = 0
        while (indexes[cur] != i):
            cur += 1
        cur += 1
        while (indexes[cur] != i):
            res.append([i + 1, indexes[cur] + 1])
            tmp = indexes[cur]
            cur += 1
            while (indexes[cur] != tmp):
                cur += 1
            cur += 1
    return res

        
#-----------------------------------