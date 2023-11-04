import pandas as pd

import query_utils as qu
import data_utils as du
import config as cf
import time


def get_games_metadata():
    qu.get_games_by_platform(platform=cf.XB, out_dir=cf.PATH_XB, rating_range=(75, 100), is_family=False)
    time.sleep(5)
    # qu.get_games_by_platform(platform=cf.XB, out_dir=cf.PATH_XB, rating_range=(0, 25))
    # time.sleep(5)
    # qu.get_games_by_platform(platform=cf.XB, out_dir=cf.PATH_XB, rating_range=(0, 25))
    # time.sleep(5)
    # qu.get_games_by_platform(platform=cf.XB, out_dir=cf.PATH_XB, rating_range=(0, 25))


if __name__ == '__main__':
    qu.get_video_ids('raw_data_IGDB/PlayStation_all/PlayStation_games_rating_between_76_100.csv', 'video_ps_76_100.csv', 'video_cat.csv')
    df_video = pd.read_csv('video_ps_76_100.csv', sep=',')
    #print(df_video.shape)
    #print(qu.get_platform_id_by_name('PlayStation 2', 'platforms.csv'))
    #get_games_metadata()







