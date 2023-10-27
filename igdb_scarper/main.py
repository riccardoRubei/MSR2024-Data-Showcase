from query_utils import get_games_by_platform, get_video_ids
from data_utils import download_video
import config as cf

import  time


def get_games_metadata(list_platform, list_ranges):

    get_games_by_platform(platform=cf.XB, outdir=cf.PATH_XB, rating_range=(0, 25))
    time.sleep(5)
    get_games_by_platform(platform=cf.XB, outdir=cf.PATH_XB, rating_range=(26, 50))
    time.sleep(5)
    get_games_by_platform(platform=cf.XB, outdir=cf.PATH_XB, rating_range=(51, 76))
    time.sleep(5)
    get_games_by_platform(platform=cf.XB, outdir=cf.PATH_XB, rating_range=(76, 100))


if __name__ == '__main__':
    get_video_ids('data/Playstation_all/PlayStation_games_rating_between_76_100.csv', 'video_ps_76_100.csv')







