from add_game import add_game_by_id
from boardgamegeek import BoardGameGeek

bgg = BoardGameGeek()

troy = bgg.collection('WhoDislikesKittens')
al = bgg.collection('mad4hatter')
pif = bgg.collection('play_it_forward')

username = 'play_it_forward'
password = 'YourPasswordHere'

to = []
ao = []
po = []
        
to = [items.id for items in troy if items.owned]
po = [items.id for items in pif if items.owned]
ao = [items.id for items in al if items.owned]        
        
tdif = [i for i in to if not i in po]
adif = [i for i in ao if not i in po]

dif = tdif + adif
dif = list(set(dif))

print dif

if len(dif) > 0:
    for i in range(len(dif)):
        add_game_by_id(dif[i],username,password)
