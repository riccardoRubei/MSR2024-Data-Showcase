
# IGDB crawler

- `config.py`: Contains configuration settings and constants for the project, including IGDB endpoints, token configuration and local paths
  
- `data_utils.py`: It contains utility functions to download gameplay videos from YouTube and handling JSON object 
  
- `genres.csv`: It stores values related to game genres and their corresponding IDs.
  
- `main.py`: The primary script that initiates and controls the flow of the project.
  
- `platforms.csv`: It represents the all the platform available in IGDB and their corresponding IDs
  
- `query_utils.py`: Provides utility functions specifically designed for querying and data retrieval purposes.

---


# Setting the IGDB API

To replicate the data collected in this study, you need a Twitch Account. To this end, you can follow the instructions available [here](https://api-docs.igdb.com/#getting-started)


# Download Game Metadata

The `get_games_by_platform` function is used to download and preprocess game metadata based on the specified platform and rating range. The processed data is then saved as a CSV file in the designated output directory. It is contained in `data_utils.py` module.


```python
def get_games_by_platform(platform, outdir, rating_range)
```

### Parameters:

- **platform** (String): 
  - Description: The gaming platform for which metadata needs to be fetched.
  - Example values: "PC", "PlayStation", "Xbox", etc.

- **outdir** (String): 
  - Description: The directory path where the resulting CSV file will be saved. If the directory does not exist, it will be created.

- **rating_range** (Integer tuple): 
  - Description: It defines the min and max ratings of the games that need to be fetched. 


### Example usage

To get games belonging to all Xbox platforms with a rating between 0 and 25, you can run the following command:
```python
get_games_by_platform(platform="Xbox", outdir="your_local_path", rating_range=(0, 25))
```

Please note that you can use all the constant available in the `config.py` file.

# Download videos

The `get_video_ids` function retrieve video IDs associated with game IDs from a given dataset and writes them to a specified output file.

### Function Signature

```python
def get_video_ids(data, outpath)
```

### Parameters:

- **data** (String): 
  - Description: The path to the CSV file containing game metadata.
  
- **outpath** (String): 
  - Description: The path where the resulting CSV file will be saved. This file will list the game IDs and their associated video IDs.


To collect the available video for PlayStation games, you can run:

```python
get_video_ids('csv_file_with_game_IDs', 'out.csv')
```

To download the actual video, please use the function `download_video(id_video)` in the data_utils.py file