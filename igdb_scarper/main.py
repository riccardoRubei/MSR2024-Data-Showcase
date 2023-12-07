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



if __name__ == '__main__':

<<<<<<< HEAD
    metadata_src = [cf.PATH_PC]
    video_dst = [cf.PATH_PC_VIDEOS]

    #qu.get_genres()
=======
    dataset_path = os.path.join("screenshots", "genres")
    images, labels = du.load_images_and_labels(dataset_path,15)
    print(images.shape, labels.shape)
    images2, labels2 = du.load_images_and_labels(dataset_path,"Turn-based strategy (TBS)")
    print(images2.shape, labels2.shape)

    #platforms = [cf.XB, cf.PL, cf.PC, cf.NT]
    #paths = [cf.PATH_XB, cf.PATH_PL, cf.PATH_PC, cf.PATH_NT]
    #get_games_metadata(platforms, paths)
>>>>>>> b86a6385a620903a545581604840367457ab8d70
    #du.compute_stats(platforms, paths)
    #get_video_metadata(platforms, paths)

    # for src, dest in zip(metadata_src,video_dst):
    #     qu.get_video_ids(src, dest)
    #df_video = pd.read_csv('video_ps_76_100.csv', sep=',')
    root = 'videos/'
    list_files =[root+'video_cat_nt.csv',root+'video_cat_pc.csv', root+'video_cat_pl.csv', root+'video_cat_xb.csv']
    du.merge_csv(list_files,'all_videos.csv')









