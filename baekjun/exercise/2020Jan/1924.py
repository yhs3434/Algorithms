# 2007년
# https://www.acmicpc.net/problem/1924

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['MON', 'TUE', "WED", 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int,input().split(' '))

daySum = sum(months[1: x])
daySum += y-1
print(days[daySum%7])