import time, sys, subprocess, os, contextlib

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
    with open('test.txt', 'w') as file, contextlib.redirect_stdout(file):
        exec(a) 
#------------------------------------------------------------------------
    kek += 1
    t1 = time.process_time()
    with open('test.txt', 'r') as f:
        p = subprocess.Popen([ok, 'f'], stdout=subprocess.PIPE, stdin=f)    
        p_stdout = p.communicate()[0]
        anss = p_stdout.decode()
        p.kill()

    print(time.process_time() - t1, "time", ok)
    worst_time_ok = max(time.process_time() - t1, worst_time_ok);

    t0 = time.process_time() 

    with open('test.txt', 'r') as f:
        p = subprocess.Popen([bad, 'f'], stdout=subprocess.PIPE, stdin=f)    
        p_stdout = p.communicate()[0]
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
print("Worst time of GOOD solution is", worst_time_ok);
print("Worst time of BAD solution is", worst_time_bad);
