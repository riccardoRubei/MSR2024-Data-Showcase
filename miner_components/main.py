import os
import igdb_miner as qu
import data_utils as du
import config as cf
import time


def get_games_igdb(platform_list, platform_paths):
    ranges = du.generate_date_intervals()
    for r in ranges:
        for plat, path in zip(platform_list, platform_paths):
            print("downloading ", plat)
            du.create_path_if_not(path)
            qu.get_games_by_platform(platform=plat, out_dir=path, rating_range=r)
            time.sleep(10)


def download_screenshots():
    dataset_path = os.path.join("screenshots", "genres")
    images, labels = du.load_images_and_labels(dataset_path,15)
    print(images.shape, labels.shape)
    images2, labels2 = du.load_images_and_labels(dataset_path,"Turn-based strategy (TBS)")
    print(images2.shape, labels2.shape)


def get_games_hltb():
     #TODO Andrea
    return


if __name__ == '__main__':
    platforms = [cf.XB, cf.PL, cf.PC, cf.NT]
    paths = [cf.PATH_XB, cf.PATH_PL, cf.PATH_PC, cf.PATH_NT]
    get_games_igdb(platforms, paths)
