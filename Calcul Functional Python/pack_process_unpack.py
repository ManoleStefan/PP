preturiCarne = [(2000 + x,30 + x * 5) for x in range(11)]

snd = lambda x : x[1]
print(snd(max(map(lambda yc : (yc[1],yc),preturiCarne))))
print(preturiCarne)