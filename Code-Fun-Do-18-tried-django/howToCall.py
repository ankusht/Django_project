'''
First of all import sentiment and comments modules
if you have a video url then first of all call comments.init(video_url)
response will be dictionary containing 
    response = {
        "live_status" : live_status ,
        "video_duration" : video_duration , 
        "timeStamp_list" : timeStamp_list , 
        "message_list" : message_list , 
        "video_id" : video_id, 
        }
    
Though live_status and video_id are of not much use,
Now call sentiment analysis for comments by calling 
    sentiment_arr = sentiment.init(response["message_list"])
this will return an array of sentiments for each comment.
So now you have two arrays to proceed further
sentiment_arr and response["timeStamp_list]
first array contains sentiment for each comment whereas second one contains timestamp.
Total duration can be found using response["video_duration"]

'''