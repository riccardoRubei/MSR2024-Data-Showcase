# endpoints
GAMES_URL = "https://api.igdb.com/v4/games"
PLATFORM_URL = "https://api.igdb.com/v4/platforms"
GENRES_URL = "https://api.igdb.com/v4/genres"
VIDEOS_URL = "https://api.igdb.com/v4/game_videos"
SCREENSHOTS_URL = "https://api.igdb.com/v4/screenshots"
SEARCH_URL = "https://api.igdb.com/v4/search"
YOU_TUBE_URL = "http://youtube.com/watch?v="

# query keywords
QUERY_HEAD = "fields "
GAME_FIELDS = "name,tags,platforms,rating;"


#platform all

XB = "Xbox"
PL = "PlayStation"
NT = "Nintendo"
PC = "PC"


# local dirs

PATH_PL = "IGDB_old/" + PL + '/'
PATH_NT = "IGDB_old/" + NT + '/'
PATH_XB = "IGDB_old/" + XB + '/'
PATH_PC = "IGDB_old/" + PC + '/'

PATH_PL_VIDEOS = "videos/" + PL + '/'
PATH_NT_VIDEOS = "videos/" + NT + '/'
PATH_XB_VIDEOS = "videos/" + XB + '/'
PATH_PC_VIDEOS = "videos/" + PC + '/'



PATH_SCREENSHOTS = "screenshots"
PATH_GENRES = "genres.csv"



PATH_PLATFORMS = "platforms.csv"
PATH_RATINGS= "/igdb_scarper/raw_data_IGDB\\PlayStation_all\\PlayStation_games_rating_between_0_25.csv"


#error handling

MAX_RETRIES = 3  # Maximum number of retries
RETRY_INTERVAL = 5  # Seconds to wait between retries


# auth config
token = "bty0p3wvcq7bmvayacu7d5r20r3az7"
CLIENT_ID = "m0jr7fmh5098pvc0szzs7zjxcq0cxe"
AUTH = {'Authorization': "Bearer {}".format(token)}
GENRES_HEADERS= {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name; limit 500;'}
PLATFORM_HEADERS =  {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields id,name ;  limit 500;'}
#SEARCH_HEADERS =  {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name,platform; search "Playstation"; limit 50;'}