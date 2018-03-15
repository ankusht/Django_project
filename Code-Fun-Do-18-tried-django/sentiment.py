import json
import requests as req

'''
Consider a list of comments commentList ,
First we need to prepare the body to send requests.
Call the function makeBody with list as argument.

'''

def jsonToLists(some_json) :
	sentiment_arr = []
	count = len(some_json)
	for i in range(count) : 
		sentiment_arr.append(some_json[i]["score"])
	return sentiment_arr

def makeBody(queryList) :
	body = { "documents": [] }
	for i in range(len(queryList)) : 
		body["documents"].append({
			"language": "en",
			"id": i,
			"text" : queryList[i] ,})
	return body 
			
def sentimentValue (body):
	headers = 	{
		'Ocp-Apim-Subscription-Key': '87a8552fd6d2409594544364f43e8825',
		'Content-Type': 'application/json',}
	res = req.post("https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment",headers=headers,data=json.dumps(body))
	# print(res.text)
	sentimentArr = json.loads(res.text)["documents"]
	
	return sentimentArr

def init(commentList) : 
	body = makeBody(commentList)
	sentiment_json = sentimentValue(body)
	sentiment_arr = jsonToLists(sentiment_json)
	sentiment_arr[:] = [x - 0.5 for x in sentiment_arr]
	return sentiment_arr

# commentList = ["i am happy" , "i am disappointed" , "fuck off" , "what the hell is this" , "i love python" , "neutral" , "i am abnormal"]
# sent = init(commentList)
# print(sent)commentList = ["i am happy" , "i am disappointed" , "fuck off" , "what the hell is this" , "i love python" , "neutral" , "i am abnormal"]
# sent = init(commentList)
# print(sent)