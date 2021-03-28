import subprocess
import json
def search_query(search):
    secret_key = "code-rag:bea21d20248106b55d4734c074217df5428db4c5"
    base_url = "https://api.github.com/search/repositories"
    query = "q="
    q = search.split()
    for i in range(len(q)):
        if i!=len(q)-1:
            query += (q[i]+"+")
        else:
            query += (q[i]+"&")
    query += "per_page=10"
    query += "&sort=stars&order=desc"
    output = subprocess.Popen(["curl",secret_key, base_url + "?" + query],shell=True, stdout=subprocess.PIPE)
    jsonS,_ = output.communicate()
    data = json.loads(jsonS)
    response = []
    for i in range(min(len(data["items"]),10)):
        response.append(data["items"][i]["html_url"])
    return response