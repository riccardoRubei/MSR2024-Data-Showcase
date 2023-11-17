import pandas as pd

import query_utils as qu
import data_utils as du
import config as cf
import time


def get_games_metadata(platform_list, platform_paths):
    #ranges = du.generate_range_ratings(65, 70, 1)
    ranges = du.generate_date_intervals_unix()
    for r in ranges:
        for plat, path in zip(platform_list, platform_paths):
            print("downloading ", plat)
            qu.get_games_by_platform(platform=plat, out_dir=path, rating_range=r)
            time.sleep(10)


def get_video_metadata(platform_list, platform_paths):

    for plat, path in zip(platform_list, platform_paths):
        qu.get_video_ids(path,plat)

if __name__ == '__main__':

    platforms = [cf.PATH_PC_VIDEOS]
    paths = [cf.PATH_PC_TEMP]
    #get_games_metadata(platforms, paths)
    #du.compute_stats(platforms, paths)
    get_video_metadata(platforms, paths)
    #qu.get_video_ids(cf.PATH_PL_TEMP+'PlayStation_games_rating_between_1698811200_1701320400.csv', 'video_ps_76_100.csv', 'video_cat.csv')
    #df_video = pd.read_csv('video_ps_76_100.csv', sep=',')









