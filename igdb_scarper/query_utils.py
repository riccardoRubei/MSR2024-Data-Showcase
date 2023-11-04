import pandas as pd
from requests import post
import config as cf
import io, os
from data_utils import *
import time
from howlongtobeatpy import HowLongToBeat



# def generate_query_video_temp():
#     df_games = pd.read_csv('data/xbox_games_no_sort.csv')
#     list_queries = []
#     with open('query_test.txt', 'w') as res:
#         for g in df_games['id'].values:
#             if build_query_video(g) != "":
#                 list_queries.append(build_query_video(g))
#                 res.write(build_query_video(g) + '\n')


def build_query_video(game_id):
    return f"fields video_id,name,game; where game= {game_id} ;"


def build_query_screenshots(game_id):
    return f"fields image_id,url,width; where game={game_id};"


def get_screenshots(data,outpath):
    df_games = pd.read_csv(data, sep=',')
    df = pd.DataFrame(columns=['id_game','image_id','url','width'])
    for game in df_games['id'].unique():
        q = build_query_screenshots(game)
        header = {'headers': {'Client-ID': cf.CLIENT_ID,
                                  'Authorization': 'Bearer ' + cf.token},
                      'data': q}
    

        response = post(cf.SCREENSHOTS_URL, **header)

        res = pd.DataFrame(response.json())

        if len(res) > 0:
            res['id_game'] = game

            res['url'] = res['url'].str[2:]

            df = pd.concat([df,res],axis=0)

        time.sleep(1)

    df = df.rename(columns={'image_id':'id_image'})

    df.to_csv(outpath, index=False)
    return

def get_time(game_name):
    ## Returns a df [title_found, main, extra, completionist]. Returns tuple of 0 if not found.
    
    res = HowLongToBeat().search(game_name, similarity_case_sensitive=False)
    times = {'title_found': res[0].game_name, 'main' : res[0].main_story, 'extra': res[0].main_extra, 'completionist': res[0].completionist} if len(res) > 0 else {'title_found': 'Not_Found', 'main':0, 'extra':0, 'completionist':0}
    
    times = pd.DataFrame(times, index=[0])
    return times


def get_genres():
    response = post(cf.GENRES_URL, **cf.GENRES_HEADERS)
    df_genres = pd.read_json(io.StringIO(read_json_string(response)), orient='records')
    df_genres.to_csv('genres.csv', index=False)


def build_header_games(platform,rating_range, is_family):
    if is_family:
        ids = get_platform_list_id(cf.PATH_PLATFORMS, platform)
        q = build_query_games(ids, rating_range[0] , rating_range[1])
        header = {'headers': {'Client-ID': cf.CLIENT_ID,
                              'Authorization': 'Bearer ' + cf.token},
                  'data': q}
    else:
        single_id = get_platform_id_by_name(cf.PATH_PLATFORMS, platform)
        q = build_query_games_single_platform(single_id, rating_range[0], rating_range[1])
        header = {'headers': {'Client-ID': cf.CLIENT_ID,
                              'Authorization': 'Bearer ' + cf.token},
                  'data': q}
    return header


def get_video_ids(data, out_game, out_video):
    df_games = pd.read_csv(data, sep=',')

    with open(out_video, 'w', encoding='utf8',errors='ignore') as video_file:
        with open(out_game, 'w', encoding='utf8', errors='ignore') as game_file:
            game_file.write("id_game,id_video\n")
            video_file.write("id_video,name\n")
            for game_id in df_games['id'].values:
                list_video_id = []
                q = build_query_video(game_id)
                header = {'headers': {'Client-ID': cf.CLIENT_ID,
                                      'Authorization': 'Bearer ' + cf.token},
                          'data': q}

                response = post(cf.VIDEOS_URL, **header)

                if len(response.json()) > 0:

                    for v in response.json():
                        print("Writing id")
                        url_video = f"{cf.YOU_TUBE_URL}{v['video_id']}"
                        list_video_id.append(url_video)
                        video_file.write(f"{url_video},{v['name']}\n")
                    video_ids = '#'.join(list_video_id)
                    game_file.write(f"{v['game']},{video_ids} \n")
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


def build_query_games_single_platform(plat_id,min_rate, max_rate):
    str_query = "fields name,platforms,rating,genres,summary,storyline; where platforms =" + str(plat_id)
    str_query += "& rating > " + str(min_rate)+" & rating < "+str(max_rate)+" ; sort rating desc; limit 500;"
    return str_query


def get_platform_id_by_name(platform_data,platform_name):
    df_platform = pd.read_csv(platform_data)
    df_platform.set_index('name', inplace=True)
    platform_id = 0
    for idx, row in df_platform.iterrows():
        if idx == platform_name:
            platform_id = row['id']

    return platform_id


def get_games_by_platform(platform, out_dir, rating_range, is_family):
    response = post(cf.GAMES_URL, **build_header_games(platform, rating_range, is_family))
    df_games = pd.read_json(io.StringIO(read_json_string(response)), orient='records')

    if 'summary' in df_games.columns:
        df_games = preprocess_column(df_games, 'summary')
    if 'storyline' in df_games.columns:
        df_games = preprocess_column(df_games, 'storyline')

    for col in df_games.columns.values:
        if has_nan(df_games,col):
            df_games = replace_nan_with_string(df_games, col, "Missing")
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    df_games.to_csv(build_filename_string(out_dir,platform,rating_range), index=False)


def get_platform_ids():
    response = post(cf.PLATFORM_URL, **cf.PLATFORM_HEADERS)
    with open('platforms.csv', 'a', encoding='utf8', errors='ignore') as res:
        json_file = response.json()
        print("response: %s" % str(response.json()))
        # res.write('id,platform\n')
        for platform in json_file:
            res.write(str(platform.get('id')) + ',' + str(platform.get('name')) + '\n')

def get_platform_list_id(csv, type):
    df_play = pd.read_csv(csv, sep=',')
    list_ids = []
    for key, plat in zip(df_play['id'], df_play['name']):
        if str(plat).find(type) != -1:
            list_ids.append(key)
    return list_ids