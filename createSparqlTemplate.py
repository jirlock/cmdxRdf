import mylib

# reference page below
# https://graphdb.ontotext.com/documentation/10.0/devhub/rest-api/curl-commands.html#rest-api-curl-commands-sparql-template-management

def createTemplate(base_url, repo_id, templateId, query_str):
    url = base_url + '/rest/repositories/' + repo_id + 'sparql-templates'
    header = 'Content-Type: application/json'
    data = {
        "query": query_str,
        "templateID": templateId
    }
    mylib.POST(url, data, header)




