import mylib
import pandas as pd

def parseBuilding(row):
    type = row[0]
    label = row[1]
    return type, label

def parseLevel(row):
    type = row[0]
    label = row[1]
    level = int(row[2])
    return type, label, level

def parseRoom(row):
    type = row[0]
    label = row[1]
    level = int(row[2])
    id = int(row[3])
    try:
        rel = list(map(int, row[4].split(',')))
    except:
        rel = []
    return type, label, level, id, rel

csvpath = 'en01space.csv'

df = pd.read_csv(csvpath, delimiter=',', encoding='utf-8')
dfnp = df.to_numpy()

rdf_list = []

baseUri = 'http://utcmdx.ac.jp/resource'
campus = 'hongo'
faculty = 'en'
bldg = '01'

for i in range(len(dfnp)):
    if dfnp[i][0] == 'b':
        type, label = parseBuilding(dfnp[i])
        #print(type, label)
        tmpTriple = mylib.createBuildingRdf(baseUri, campus, faculty, bldg, label)
        rdf_list.append(tmpTriple)
    
    if dfnp[i][0] == 'l':
        type, label, level = parseLevel(dfnp[i])
        #print(type, label, level)
        tmpTriple = mylib.createLevelRdf(baseUri, campus, faculty, bldg, str(level), label)
        rdf_list.append(tmpTriple)

    if dfnp[i][0] == 'r':
        type, label, level, room, rel = parseRoom(dfnp[i])
        #print(type, label, level, id, rel)
        tmpTriple = mylib.createRoomRdf(baseUri, campus, faculty, bldg, str(level), str(room), label)
        rdf_list.append(tmpTriple)

        #relations
        roomUri = mylib.createRoomUri(baseUri, campus, faculty, bldg, str(level), str(room))
        for r in rel:
            tmpRoomUri = mylib.createRoomUri(baseUri, campus, faculty, bldg, str(level), str(r))
            relRdf = mylib.createRoomRelationRdf(roomUri, tmpRoomUri)
            rdf_list.append(relRdf)


rdf_body = mylib.concatRdf(rdf_list)

rdf_header = \
'@prefix rec: <http://www.w3id.org/rec#> .\n\
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n'

rdf = mylib.concatRdf([rdf_header, rdf_body])

print(rdf)

with open('en01.ttl', 'w', encoding='utf-8') as f:
    f.write(rdf)


