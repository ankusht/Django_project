import requests as req
import json
perm_token = "EAAd0ep1GT0wBAEbm1UTKaZAZBaxZAc6Iyg9gnlJWYxuHY0Wd2BklpJSvS6XpfsKIvsD6RdYrqZC0hUMyIKwsqZAAPZB40SxiQt7GmMSAko1Ln0GzPXG68eBQNcmmtifahM8v4ZAtemmnryaOMn20QoAke7ORZBPShv8bAwZBm9woNP1EkNvi0axSK"
timeStamp_list = [] 
message_list = []
def jsonToLists(some_json) :
    count = len(some_json)
    for i in range(count) : 
        print(some_json[i])
        print("----------")
        try :
            tmp = some_json[i]["live_broadcast_timestamp"]
        except : 
            tmp = -111
        timeStamp_list.append(tmp)
        message_list.append(some_json[i]["message"])
    return 

def getVideoId(video_url) : 
    video_id = video_url.split("/")[5]
    return video_id

def makeRequest(video_id) :
    host_url = "https://graph.facebook.com/v2.12/" + video_id + "?fields=created_time,live_status,updated_time,backdated_time,backdated_time_granularity,comments{live_broadcast_timestamp,message},length&access_token=" + perm_token 
    response = req.get(host_url)
    response_json = json.loads(response.text)
    response_code = response.status_code
    return response_json,response_code

def init(url) :
    video_id = getVideoId(url)
    response_json , response_code = makeRequest(video_id)
    print(response_json)
    print(response_json["comments"]["data"])
    jsonToLists(response_json["comments"]["data"])
    live_status = response_json["live_status"]
    video_duration = response_json["length"]
    output = {
        "live_status" : live_status ,
        "video_duration" : video_duration , 
        "timeStamp_list" : timeStamp_list , 
        "message_list" : message_list , 
        "video_id" : video_id,
    }
    return output

# if __name__ == "_main_" :
#     video_url = raw_input()
#     init(video_url)
# url = "https://www.facebook.com/election.commission.iitk/videos/810829939120636"
# video_id = getVideoId(url)
# response_json , response_code = makeRequest(video_id)
# print(video_id , response_json , response_code)