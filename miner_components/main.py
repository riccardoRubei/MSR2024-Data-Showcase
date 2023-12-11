import os
import igdb_miner as im
import hltb_miner as hm
import data_utils as du
import config as cf
import time
import argparse

def get_games_igdb(platform_list, platform_paths):
    ranges = du.generate_date_intervals()
    for r in ranges:
        for plat, path in zip(platform_list, platform_paths):
            print("downloading ", plat)
            du.create_path_if_not(path)
            im.get_games_by_platform(platform=plat, out_dir=path, rating_range=r)
            time.sleep(10)


def download_screenshots(screen_folder, genres_folder,genre):
    dataset_path = os.path.join(screen_folder, genres_folder)
    images, labels = du.load_images_and_labels(dataset_path,15)
    print(images.shape, labels.shape)
    images2, labels2 = du.load_images_and_labels(dataset_path,genre)
    print(images2.shape, labels2.shape)







# if __name__ == '__main__':
#
#     platforms = [cf.XB, cf.PL, cf.PC, cf.NT]
#     paths = [cf.PATH_XB, cf.PATH_PL, cf.PATH_PC, cf.PATH_NT]
#     get_games_igdb(platforms, paths)
#     download_screenshots(cf.PATH_SCREENSHOTS, cf.GENRE_FOLDER, cf.GENRE_TEST)
#     du.download_video(cf.VIDEO_DATA)
#     hm.get_all_times(cf.HLTB_DATA)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run various game data functions")
    parser.add_argument('--function', choices=['get_games', 'download_screenshots', 'download_video', 'get_all_times'], required=True, help='Select the function to run')

    args = parser.parse_args()

    if args.function == 'get_games':
        platforms = [cf.XB, cf.PL, cf.PC, cf.NT]
        paths = [cf.PATH_XB, cf.PATH_PL, cf.PATH_PC, cf.PATH_NT]
        get_games_igdb(platforms, paths)
    elif args.function == 'download_screenshots':
        download_screenshots(cf.PATH_SCREENSHOTS, cf.GENRE_FOLDER, cf.GENRE_TEST)
    elif args.function == 'download_video':
        du.download_video(cf.VIDEO_DATA)
    elif args.function == 'get_all_times':
        hm.get_all_times(cf.HLTB_DATA)




