import random, time, sys, subprocess, os, contextlib
from random import randint

def arr(n, minn, maxn):
    a = [random.randint(minn, maxn) for i in range(n)];
    return ' '.join(map(str, a));
    
def seg(l, r):
    tr = random.randint(l + 1, r);
    tl = random.randint(l, tr);
    return ' '.join(map(str, [tl, tr]));
        
def string(n, maxn):
    a = [chr(random.randint(0, maxn % 26) + ord('a')) for i in range(n)]
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
        if (randint(0, 1000) <= deep):
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

ansf = 0
anss = 0
kek = 0

INF = 10 ** 9;
worst_time_ok = -INF;
worst_time_bad = -INF;
fin = open("pattern.txt", 'r')
pattern = []
for i in fin.readlines():
    pattern.append(i)
print("pattern:", pattern)

print("Enter count of iterations(-1 = INF)")
it = int(input())
print("Enter time limit(x2)")
TL = float(input())
TL *= 2

print("Enter name of first solution(without .exe)")
ok = input()

print("Enter name of second solution(without .exe)")
bad = input()
os.system('g++ -std=c++17 -O2 -o' + ok + '.exe ' + ok + '.cpp')
os.system('g++ -std=c++17 -O2 -o' + bad + '.exe ' + bad + '.cpp')
test = ""

ok = './' + ok + '.exe'
bad = './' + bad + '.exe'


while (ansf == anss and kek != it):
    if (kek != 0):
        print("OK", kek)
#------------------------------------------------------------------------
    a = ''.join(pattern)
    print('a:', a)
    with open('test.txt', 'w') as file, contextlib.redirect_stdout(file):
        exec(a) 
    exit(0)
#------------------------------------------------------------------------
    kek += 1
    t1 = time.process_time()
    p = subprocess.Popen([ok, 'f'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)    
    p_stdout = p.communicate(input=b'test.txt')[0]
    anss = p_stdout.decode()
    p.kill()

    print(time.process_time() - t1, "time", ok)
    worst_time_ok = max(time.process_time() - t1, worst_time_ok);

    t0 = time.process_time() 

    p = subprocess.Popen([bad, 'f'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)    
    p_stdout = p.communicate(input=b'test.txt')[0]
    ansf = p_stdout.decode()
    p.kill()

    print(time.process_time() - t0, "time", bad)
    worst_time_bad = max(time.process_time() - t0, worst_time_bad);
    if (worst_time_ok > TL):
        print("TL", kek)
        exit(0);
    
if (ansf == anss):
    print("OK", kek, "You can find test example in test.txt");
else:
    print("WA", kek, "You can find test in test.txt")
    print("ok answer:", anss);
    print("wrong answer:", ansf);
fout = open("test.txt", "w");
print(test, file = fout)
fout.close()
print("Worst time of GOOD solution is", worst_time_ok);
print("Worst time of BAD solution is", worst_time_bad);
