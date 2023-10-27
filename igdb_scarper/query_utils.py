import pandas as pd
from requests import post
import config as cf
import io, os
from data_utils import *
import time


# def generate_query_video_temp():
#     df_games = pd.read_csv('data/xbox_games_no_sort.csv')
#     list_queries = []
#     with open('query_test.txt', 'w') as res:
#         for g in df_games['id'].values:
#             if build_query_video(g) != "":
#                 list_queries.append(build_query_video(g))
#                 res.write(build_query_video(g) + '\n')


def build_query_video(game_id):
    return "fields video_id,name; where game=" + str(game_id) + ";"


def get_screenshots():
    return


def get_genres():
    response = post(cf.GENRES_URL, **cf.GENRES_HEADERS)
    df_genres = pd.read_json(io.StringIO(read_json_string(response)), orient='records')
    df_genres.to_csv('genres.csv', index=False)


def build_header_games(platform,rating_range):
    ids = get_platform_id(cf.PATH_PLATFORMS, platform)
    q = build_query_games(ids, rating_range[0] , rating_range[1])
    header = {'headers': {'Client-ID': cf.CLIENT_ID,
                          'Authorization': 'Bearer ' + cf.token},
              'data': q}
    return header


def get_video_ids(data, outpath):
    df_games = pd.read_csv(data, sep=',')
    with open(outpath, 'a', encoding='utf8', errors='ignore') as res:
        res.write("id_game,id_video\n")
        for game_id in df_games['id'].values:
            q = build_query_video(game_id)
            header = {'headers': {'Client-ID': cf.CLIENT_ID,
                                  'Authorization': 'Bearer ' + cf.token},
                      'data': q}

            response = post(cf.VIDEOS_URL, **header)

            if len(response.json()) > 0:
                for v in response.json():
                    print("Writing id")
                    res.write(str(v['id'])+','+str(v['video_id'])+'\n')

            else:
                print("No video")
            time.sleep(5)

# old function
# def query_selector(item_type):
#     if item_type == "GAME":
#         ids = get_platform_id('platforms.csv', 'PC')
#         return build_query_games(ids,0,75)
#
#     if item_type == "VIDEO":
#         with open('query_test.txt', 'r') as file:
#             queries = file.readlines()
#             for q in queries:
#                 header = {'headers': {'Client-ID': cf.CLIENT_ID,
#                                       'Authorization': 'Bearer ' + cf.token},
#                           'data': q}
#
#                 response = post(cf.VIDEOS_URL, **header)
#
#                 if len(response.json()) >0:
#                     df_videos = pd.read_json(io.StringIO(read_json_string(response)), orient='records')
#                     df_videos.to_csv('videos.csv', index=False)
#                 else:
#                     print("no video")
#                 time.sleep(8)


def build_query_games(plat_ids,min_rate, max_rate):
    str_query = "fields name,platforms,rating,genres,summary,storyline; where ("
    i = 0
    for key in plat_ids:
        if i < len(plat_ids) - 1:
            str_query += "platforms = " + str(key) + " | "
        else:
            str_query += "platforms = " + str(key)
        i += 1

    str_query += ") & rating > " + str(min_rate)+" & rating < "+str(max_rate)+" ; sort rating desc; limit 500;"
    return str_query


def get_games_by_platform(platform, outdir, rating_range):
    response = post(cf.GAMES_URL, **build_header_games(platform, rating_range))
    df_games = pd.read_json(io.StringIO(read_json_string(response)), orient='records')

    if 'summary' in df_games.columns:
        df_games = preprocess_column(df_games, 'summary')
    if 'storyline' in df_games.columns:
        df_games = preprocess_column(df_games, 'storyline')

    for col in df_games.columns.values:
        if has_nan(df_games,col):
            df_games = replace_nan_with_string(df_games, col, "Missing")
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    df_games.to_csv(build_filename_string(outdir,platform,rating_range), index=False)


def get_platform_ids():
    response = post(cf.PLATFORM_URL, **cf.PLATFORM_HEADERS)
    with open('platforms.csv', 'a', encoding='utf8', errors='ignore') as res:
        json_file = response.json()
        print("response: %s" % str(response.json()))
        # res.write('id,platform\n')
        for platform in json_file:
            res.write(str(platform.get('id')) + ',' + str(platform.get('name')) + '\n')

def get_platform_id(csv, type):
    df_play = pd.read_csv(csv, sep=',')
    list_ids = []
    for key, plat in zip(df_play['id'], df_play['name']):
        if str(plat).find(type) != -1:
            list_ids.append(key)
    return list_ids