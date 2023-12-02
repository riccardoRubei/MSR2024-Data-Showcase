import pandas as pd
import os
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
            du.create_path_if_not(path)
            qu.get_games_by_platform(platform=plat, out_dir=path, rating_range=r)
            time.sleep(10)


def get_video_metadata(platform_list, platform_paths):

    for plat, path in zip(platform_list, platform_paths):
        qu.get_video_ids(path,plat)

if __name__ == '__main__':

    dataset_path = os.path.join("screenshots", "genres")
    images, labels = du.load_images_and_labels(dataset_path,15)
    print(images.shape, labels.shape)
    images2, labels2 = du.load_images_and_labels(dataset_path,"Turn-based strategy (TBS)")
    print(images2.shape, labels2.shape)

    #platforms = [cf.XB, cf.PL, cf.PC, cf.NT]
    #paths = [cf.PATH_XB, cf.PATH_PL, cf.PATH_PC, cf.PATH_NT]
    #get_games_metadata(platforms, paths)
    #du.compute_stats(platforms, paths)
    #get_video_metadata(platforms, paths)
    #qu.get_video_ids(cf.PATH_PL_TEMP+'PlayStation_games_rating_between_1698811200_1701320400.csv', 'video_ps_76_100.csv', 'video_cat.csv')
    #df_video = pd.read_csv('video_ps_76_100.csv', sep=',')









