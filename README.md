# Python stressing 
###### *only for unux(alfa version)* 
### Easy streps to use this repository
1. Make sure that python3.6 installed
2. Open terminal and print **git clone https://github.com/khaser/PythonStressing**
3. Move you ok and wrong solutions cpp files to dir PythonStressing
4. Write tests generator code to pattern.txt on python3.6 
You can use my functions to easy generate trees, permutations, strings e.t.c.
    4.1. **arr(size, min_value, max_value)** - return array of integers
    4.2. **string(size, max_char)** - return string consisting of chars from 'a' to max_char in in alphabetical order
    4.3. **tree(size, branching)** - return list of pairs connected vertexes, which is a tree. branching[0, 1000]- argument responsible for max_deep in tree. if branching == 0 tree is broom, end if branching == 1000 tree is bamboo.(now working slow (**O(size ^ 2)**)
    4.4. **permutation(size)** - return permutation of integers
    4.5. **seg(tl, tr)** - return list of 2 integers **[a, b] : tl <= a <= b <= tr**
    4.6. ***IN PROGRESS***
5. run python3 stress.py
6. follow script instructions
7. get your test in test.txt
