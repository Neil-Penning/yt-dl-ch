import sys, requests, json


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Need API then url")
    # other
    url = "https://youtube.googleapis.com/youtube/v3/playlists"
    data = {
        "part" : "snippet,contentDetails",
        "channelId" : sys.argv[1],
        "key" : sys.argv[2],
        "maxResults" : 25
        #"mine" : False
    }
    #print(data)
    response = requests.get(url, params=data)
    response_dict = json.loads(response.text)
    #print(response)
    #print(response.content)
    for r in response_dict["items"]:
        #print(r)
        print("yt-dl-pl " + r["id"] + "\t#" + r["snippet"]["title"])
        #print(r["etag"])

