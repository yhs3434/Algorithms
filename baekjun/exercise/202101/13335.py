n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
trucks.reverse()

time = 0
bridge = []
bridgeWeight = 0
while trucks or bridge:
    time += 1
    if bridge:
        for i in range(len(bridge) - 1, -1, -1):
            bridge[i] = (bridge[i][0]+1, bridge[i][1])
            if bridge[i][0] >= w:
                bridgeWeight -= bridge[i][1]
                bridge.pop(0)

    if len(bridge) < w:
        if trucks:
            truck = trucks[-1]
            if truck + bridgeWeight <= l:
                bridgeWeight += truck
                bridge.append((0, truck))
                trucks.pop()
print(time)