# 달달함이 넘쳐흘러
# https://www.acmicpc.net/problem/17256
# https://github.com/yhs3434

a = {}
b = {}
c = {}

x,y,z = map(int, input().split(' '))
a['x'] = x
a['y'] = y
a['z'] = z

x,y,z = map(int, input().split(' '))
c['x'] = x
c['y'] = y
c['z'] = z

b['x'] = c['x'] - a['z']
b['y'] = c['y'] // a['y']
b['z'] = c['z'] - a['x']

print(b['x'], b['y'], b['z'])