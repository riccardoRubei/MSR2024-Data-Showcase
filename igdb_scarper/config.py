# endpoints
GAMES_URL = "https://api.igdb.com/v4/games"
PLATFORM_URL = "https://api.igdb.com/v4/platforms"
GENRES_URL = "https://api.igdb.com/v4/genres"
VIDEOS_URL = "https://api.igdb.com/v4/game_videos"
SCREENSHOTS_URL = "https://api.igdb.com/v4/screenshots"
SEARCH_URL = "https://api.igdb.com/v4/search"


# query keywords
QUERY_HEAD = "fields "
GAME_FIELDS = "name,tags,platforms,rating;"


#platform all

XB = "Xbox_all"
PL = "PlayStation_all"
NT = "Nintendo_all"
PC = "PC_all"


# local dirs

PATH_PL = "data/" + PL + '/'
PATH_NT = "data/" + NT + '/'
PATH_XB = "data/" + XB + '/'
PATH_PC = "data/" + PC + '/'

PATH_PLATFORMS = "platforms.csv"

# auth config
token = "bty0p3wvcq7bmvayacu7d5r20r3az7"
CLIENT_ID = "m0jr7fmh5098pvc0szzs7zjxcq0cxe"
AUTH = {'Authorization': "Bearer {}".format(token)}
GENRES_HEADERS= {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name; limit 500;'}
PLATFORM_HEADERS =  {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name; search "PC"; limit 20;'}
SEARCH_HEADERS =  {'headers': {'Client-ID': CLIENT_ID, 'Authorization': 'Bearer ' + token},'data': 'fields name,platform; search "Playstation"; limit 50;'}