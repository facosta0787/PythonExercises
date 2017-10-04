VALUE_CARDS = {0:'A',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'10',10:'J',11:'Q',12:'K'}
cards = []
suits = ['♠','♥','♦','♣']
drawed_cards = []

for key,value in VALUE_CARDS.items():
  cards.append(value)

def create_card(card,family):
  top = ' _______'
  row = '|       |'.format(card)
  middle = '|   {0}   |'.format(family)
  if len(card) > 1:
    rowCard = '|{0}     |'.format(card)
    bottom = '|_____{0}|'.format(card)
  else:
    rowCard = '|{0}      |'.format(card)
    bottom = '|______{0}|'.format(card)
  card_str = '{0}\n{1}\n{2}\n{3}\n{2}\n{5}'.format(top,rowCard,row,middle,row,bottom)
  return card_str

for suit in suits:
  for value in cards:
    card_created = create_card(value,suit)
    drawed_cards.append(card_created)

print(len(drawed_cards))

for i in range(len(drawed_cards)):
  print(drawed_cards[i])
