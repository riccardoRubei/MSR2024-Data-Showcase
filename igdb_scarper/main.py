import pandas as pd

import query_utils as qu
import data_utils as du
import config as cf
import time


def get_games_metadata():
    ranges = du.generate_range_ratings(0, 100, 10)

    for r in ranges:
        qu.get_games_by_platform(platform=cf.NT, out_dir=cf.PATH_NT, rating_range=r)
        time.sleep(5)


if __name__ == '__main__':
    get_games_metadata()

    #qu.get_video_ids('raw_data_IGDB/PlayStation_all/PlayStation_games_rating_between_76_100.csv', 'video_ps_76_100.csv', 'video_cat.csv')
    #df_video = pd.read_csv('video_ps_76_100.csv', sep=',')
    #print(df_video.shape)
    #print(qu.get_platform_id_by_name('PlayStation 2', 'platforms.csv'))
    #get_games_metadata()







