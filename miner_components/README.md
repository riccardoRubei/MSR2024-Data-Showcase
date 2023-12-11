# IGDB miner

- `config.py`: Contains configuration settings and constants for the project, including IGDB endpoints, token configuration and local paths
  
- `data_utils.py`: It contains utility functions to download gameplay videos from YouTube and handling JSON object 
  
- `genres.csv`: It stores values related to game genres and their corresponding IDs.
  
- `main.py`: The primary script that initiates and controls the flow of the project.
  
- `platforms.csv`: It represents all the platforms available in IGDB and their corresponding IDs
  
- `query_utils.py`: Provides utility functions specifically designed for querying and data retrieval purposes.

---


# Setting the IGDB API

To replicate the data collected in this study, you need a Twitch Account. To this end, you can follow the instructions available [here](https://api-docs.igdb.com/#getting-started)


# Download IGDB game Metadata

The `get_games_by_platform` function is used to download and preprocess game metadata based on the specified platform and rating range. The processed data is then saved as a CSV file in the designated output directory. It is contained in `data_utils.py` module.


```python
get_games_igdb(platforms, paths)
```
where platforms and paths are lists of platform families and the folder respectively.  

### Example usage

To collect all the platform metadata, run the following script
```     
platforms = [cf.XB, cf.PL, cf.PC, cf.NT]
paths = [cf.PATH_XB, cf.PATH_PL, cf.PATH_PC, cf.PATH_NT]
get_games_igdb(platforms, paths)
```
where the values are stored in the `config.py` file.

# Download videos

The `download_video` function download the actual .MP4 from the all_videos.csv files

### Function Signature

```
download_video(cf.VIDEO_DATA)
```



# HLTB Miner

## Setup:

To set up the HLTB Miner, download the zip from the url: https://github.com/dangeloandrea14/hl2b_python_API
and install it via pip, e.g.,

``` pip install ../hl2b_python_API/howlongtobeapty ```

depending on its location on your machine.


# Download Game completion metadata

The `get_time` function is used to POST a request for a single game, given a title, returning a Pandas DataFrame with all the attributes.


```python
def get_time(game_name)
```

Similarly, the `get_all_times` function iterates over `get_time` to obtain info for all the games in a list, given the path to a Pandas DF containing a column named 'name' where the game titles are stored.

```python
def get_all_times(df_path)
```