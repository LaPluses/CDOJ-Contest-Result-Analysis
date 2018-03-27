import json
import csv

f = json.loads( open( "Ranklist.json" , encoding = 'utf-8' ).read() )['rankList']['rankList']
csvfile = open('rank.csv', "w", encoding='gb18030')
spamwriter = csv.writer(csvfile, dialect=("excel") )
for _ in f:
    itemList = _['itemList']
    name = _['name']
    penalty = _['penalty']
    rank = _['rank']
    Li = []
    Li.append( rank )
    Li.append( name )
    for index, __ in enumerate(itemList):
        if __['solved']:
            Li.append('√(' + str(__['tried']) + ')')
        else:
            if __['tried']:
                Li.append('×(' + str(__['tried']) + ')')
            else:
                Li.append( '' )
    spamwriter.writerow(list(map(str, Li)))

if __name__ == '__main__':
    pass
