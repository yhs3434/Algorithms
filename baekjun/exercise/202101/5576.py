from heapq import heappush, heappop
w = []
k = []
W = 0
K = 0
for _ in range(10):
    heappush(w, (-int(input())))
for _ in range(10):
    heappush(k, (-int(input())))
for i in range(3):
    W += -heappop(w)
    K += -heappop(k)
print(W, K)