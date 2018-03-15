import myapp.lib.sentiment as sentiment
import myapp.lib.fb_comments as comments

def get_no_of_parts(total_duration,length_of_part):
	if(total_duration%length_of_part==0):
		return total_duration/length_of_part
	else:
		return total_duration/length_of_part + 1

def get_part(time,length_of_part):
	if(time%length_of_part==0 and time>0):
		return time/length_of_part
	else:
		return time/length_of_part +1

def get_length_of_part(total_duration):
	length_of_part = 0
	if(total_duration<=1800):
		length_of_part = 120
	elif (total_duration>1800 and total_duration<=2700):
		length_of_part = 180
	elif (total_duration>2700 and total_duration<=3600):
		length_of_part = 300
	elif (total_duration>3600 and total_duration<=5400):	
		length_of_part = 450
	elif (total_duration>5400 and total_duration<=7200):
		length_of_part = 480
	else:
		length_of_part = 600		
	return length_of_part

		


def get_score(sentiment_arr,times,total_duration):
	length_of_part = get_length_of_part(total_duration)
	print("length_of_part = %d"%(length_of_part))
	no_of_parts = int(get_no_of_parts(total_duration,length_of_part))
	print("no_of_parts = %d"%(no_of_parts))
	scores = [0.0]*(no_of_parts)
	for s in sentiment_arr:
		index = sentiment_arr.index(s)
		time = times[index]
		part = int(get_part(time,length_of_part))
		scores[part-1]+= s
	return scores, length_of_part

def main(video_url):
	time_break_list = []
	response = comments.init(video_url)
	sentiment_arr = sentiment.init(response["message_list"])
	times = response["timeStamp_list"]
	total_duration = response["video_duration"]
	print(sentiment_arr)
	print(times)
	print(total_duration)
	scores, length_of_part = get_score(sentiment_arr,times,total_duration)
	for i in range(len(scores)):
		print("part = %d , sentiment = %f"%(i+1,scores[i]))	
	for i in range(len(scores)):
		print("duration", length_of_part * i)
		time_break_list.append(length_of_part * i)
	# print("length : ", total_duration)
	time_break_list.append(total_duration)
	output = {
		"time_break_list" : time_break_list,
		"scores" : scores
	}
	return output

if __name__ == '__main__':
	video_url = input()	
	main(video_url)	
	


