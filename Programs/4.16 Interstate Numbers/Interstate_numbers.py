# Odds = N/S
# Evens = E/W

highway = int(input())

dir = highway % 2
if dir == 1:
    direction = 'north/south'
else:
    direction = 'east/west'

aux = highway // 100
serve = highway - (aux*100)

if highway <=0 or highway >=1000:
    print(highway, ' is not a valid interstate highway number.', sep='')
elif aux != 0:
    print('The ', highway, ' is auxiliary, serving the ', serve, ', going ', direction,'.', sep='')
else:
   print('The ', highway, ' is primary, going ', direction,'.', sep='')