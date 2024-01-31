import urllib.request
import json

def GET(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = json.loads(response.read())
            headers = response.getheaders()
            status = response.getcode()

            print(headers)
            print(status)
            print(body)
    
    except urllib.error.URLError as e:
        print(e.reason)


def POST(url, req_data, req_headers):
    req = urllib.request.Request(url, data=req_data.encode(), method='POST', headers=req_headers)
    try:
        with urllib.request.urlopen(req) as response:
            body = json.loads(response.read())
            headers = response.getheaders()
            status = response.getcode()

            print(headers)
            print(status)
            print(body)

    except urllib.error.URLError as e:
        print(e.reason)

def concatRdf(triples):
    rdf = ''
    for triple in triples:
        rdf += triple + '\n'
    return rdf

def createLabelTriple(uri, label):
    return uri + ' rdfs:label ' + '"' + label + '"' + '.'

def createBuildingUri(baseUri, id):
    return '<' + baseUri + '/building/' + id + '>' 

def createLevelUri(baseUri, id):
    return '<' + baseUri + '/level/' + id + '>'

def createRoomUri(baseUri, id):
    return '<' + baseUri + '/room/' + id + '>'

#return String
def createBuildingRdf(uri, label):
    classTriple = uri + ' a rec:Building.'
    labelTriple = createLabelTriple(uri, label)
    return concatRdf([classTriple, labelTriple])

def createLevelRdf(uri, label, buildingId):
    classTriple = uri + ' a rec:Level.'
    labelTriple = createLabelTriple(uri, label)
    buildingTriple = uri + ' rec:isPartOf ' + buildingId + '.'
    levelTriple = buildingId + ' rec:hasPart ' + uri + '.'
    return concatRdf([classTriple, labelTriple, buildingTriple, levelTriple])

def createRoomRdf(uri, label, levelId):
    classTriple = uri + ' a rec:Room.'
    labelTriple = createLabelTriple(uri, label)
    levelTriple = uri + ' rec:isPartOf ' + levelId + '.'
    roomTriple = levelId + ' rec:hasPart ' + uri + '.'
    return concatRdf([classTriple, labelTriple, levelTriple, roomTriple])

def executeSparqlTemplate():
    return 0

