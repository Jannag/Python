"""
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
"""
number = int(input())
d = []
k = {}
for i in range(number):
    d += [input().split(';')]
for i in range(len(d)):
    for j in d[i][::2]:
        k[j] = {'total_games': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'total_points': 0}
for i in range(len(d)):
    k[d[i][0]]['total_games'] += 1
    k[d[i][2]]['total_games'] += 1
    if int(d[i][1]) < int(d[i][3]):
        k[d[i][0]]['losses'] += 1
        k[d[i][2]]['wins'] += 1
        k[d[i][2]]['total_points'] += 3
    elif int(d[i][1]) > int(d[i][3]):
        k[d[i][2]]['losses'] += 1
        k[d[i][0]]['wins'] += 1
        k[d[i][0]]['total_points'] += 3
    elif int(d[i][1]) == int(d[i][3]):
        k[d[i][0]]['draws'] += 1
        k[d[i][0]]['total_points'] += 1
        k[d[i][2]]['draws'] += 1
        k[d[i][2]]['total_points'] += 1
for i in k:
    print(i+':', end='')
    for j in k[i].values():
        print(j, end=' ')
    print()
