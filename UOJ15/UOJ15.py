from collections import deque

# fmt:off
win = {
    (0, 2), (0, 3),
    (1, 3), (2, 4),
    (3, 4), (1, 0), (2, 1), (3, 2), (4, 0), (4, 1)}
# fmt:on
n, na, nb = map(int, input().split())
sa, sb = 0, 0
A = deque(map(int, input().split()), maxlen=na)
B = deque(map(int, input().split()), maxlen=nb)
for i in range(n):
    sa += int((A[0], B[0]) in win)
    sb += int((B[0], A[0]) in win)
    A.rotate(-1)
    B.rotate(-1)
print(sa, sb)
