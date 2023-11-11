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

PATH_PL = "raw_data_IGDB/" + PL + '/'
PATH_NT = "raw_data_IGDB/" + NT + '/'
PATH_XB = "raw_data_IGDB/" + XB + '/'
PATH_PC = "raw_data_IGDB/" + PC + '/'

PATH_PL_TEMP = "IGDB_metadata/" + PL + '/'
PATH_NT_TEMP = "IGDB_metadata/" + NT + '/'
PATH_XB_TEMP = "IGDB_metadata/" + XB + '/'
PATH_PC_TEMP = "IGDB_metadata/" + PC + '/'



PATH_SCREENSHOTS = "screenshots"
PATH_GENRES = "raw_data_IGDB/genres.csv"



PATH_PLATFORMS = "platforms.csv"
PATH_RATINGS= "/igdb_scarper/raw_data_IGDB\\PlayStation_all\\PlayStation_games_rating_between_0_25.csv"

# auth config
token = "bty0p3wvcq7bmvayacu7d5r20r3az7"
CLIENT_ID = "m0jr7fmh5098pvc0szzs7zjxcq0cxe"
AUTH = {'Authorization': "Bearer {}".format(token)}
GENRES_HEADERS= {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name; limit 500;'}
#PLATFORM_HEADERS =  {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name; search "PC"; limit 20;'}
#SEARCH_HEADERS =  {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name,platform; search "Playstation"; limit 50;'}