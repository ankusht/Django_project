from myapp.lib import yt_comment
from myapp.lib import sentiment

def get_output(sentiments_arr):
	positive_score = 0
	negative_score = 0
	positive_responses = 0
	negative_responses = 0
	print("Sentiment array : ", sentiments_arr)
	for sentiment in sentiments_arr:
		if(sentiment>=0):
			positive_score+= sentiment
			positive_responses+=1
		else:
			negative_score+= sentiment
			negative_responses+=1
	total_responses = positive_responses + negative_responses
	precentage_pos = (positive_responses/total_responses)*100
	precentage_neg = (negative_responses/total_responses)*100
	output = {'positive_score':positive_score,'negative_score':negative_score,
			 'positive_responses':positive_responses,'negative_responses':negative_responses,
			 'precentage_pos':precentage_pos,'precentage_neg':precentage_neg}

	return output		 


def main(video_url):
	
	comments = yt_comment.init(video_url)
	sentiments_arr = sentiment.init(comments)
	print("---------")
	print(sentiments_arr)
	output = get_output(sentiments_arr)
	# output = 1
	print(output)
	return output


if __name__ == '__main__':
	video_url = input()
	main(video_url)