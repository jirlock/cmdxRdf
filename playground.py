import mylib

'''
baseurl = 'http://localhost:7200'
repoid = 'cmdxRepo0'
repoid2 = 'recBrickShaclValidationRepo'
url = baseurl + '/rest/repositories/' + repoid + '/import/server'

mylib.GET(url)
'''

baseUri = 'http://utcmdx.ac.jp/resource'

buildingUri = mylib.createBuildingUri(baseUri, 'en01')
print(mylib.createBuildingRdf(buildingUri, "1号館"))

levelUri = mylib.createLevelUri(baseUri, 'en01/1')
print(mylib.createLevelRdf(levelUri, '1階', buildingUri))

roomUri = mylib.createRoomUri(baseUri, 'en01/1/1')
print(mylib.createRoomRdf(roomUri, 'エントランス', levelUri))

