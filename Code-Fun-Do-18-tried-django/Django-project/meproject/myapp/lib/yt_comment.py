from myapp.lib import yt_comment_api as yt_api
# # # # #
ITERATION_CALL = 10
# # # # #

def get_videoId(url) :
    tmp = url.split("?")[1]
    video_id = tmp.split("=")[1]
    return video_id


def process(video_id) :
    response_raw = yt_api.init(video_id)
    return response_raw
    

def init(url) :
    video_id = get_videoId(url)
    response_list = process(video_id)
    return response_list