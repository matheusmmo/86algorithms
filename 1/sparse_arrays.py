"""
Sparse Array

Link to the problem: https://www.hackerrank.com/challenges/sparse-arrays/problem

Solution:
"""
l = {}

for _ in range(int(input())):
    s = input()
    
    l[s] = l.get(s, 0) + 1

for _ in range(int(input())):
    print(l.get(input(), 0))
