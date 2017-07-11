"""
Algorithmic Crush

Link to the problem: https://www.hackerrank.com/challenges/sparse-arrays/problem

Comments: This was a very trick one, I spent quite some time trying to do my way,
it was ok for the test cases with almost no data,
but for those with a lot of that my solution sucked.
That was good cause then I learned a new technique call "Prefix Sum".

Solution:
"""

N, M = map(int, input().split())

l = [0] * N

for _ in range(M):
    a, b, k = map(int, input().split())

    l[a - 1] += k

    if b < N:
        l[b] -= k

max = l[0]
x = 0

for i in l:
    x = x + i
    
    if x > max:
        max = x

print(max)
