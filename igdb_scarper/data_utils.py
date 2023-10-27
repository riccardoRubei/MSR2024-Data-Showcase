import json
from pytube import YouTube
import pandas as pd



def download_video(id_video):
    yt = YouTube('http://youtube.com/watch?v='+str(id_video))
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


def read_json_string(json_string):
    return json.dumps(json_string.json(), sort_keys=True, indent=4)


def build_filename_string(outdir, platform, rating_range):
    return outdir+platform+'_games_rating_between_'+str(rating_range[0])+'_'+str(rating_range[1])+'.csv'


# 1. Function to preprocess a column
def preprocess_column(df, column_name):
    # Using regex to replace newline characters and other non-alphanumeric characters except spaces
    df[column_name] = df[column_name].replace(to_replace=[r'\n', r'[^\w\s]'], value=[' ', ''], regex=True)
    return df

# 2. Function to replace NaN values with a specific string
def replace_nan_with_string(df, column_name, replace_with="Missing"):
    df[column_name].fillna(replace_with, inplace=True)
    return df

def has_nan(df, column_name):
    """Check if a column in a dataframe has NaN values."""
    return df[column_name].isnull().any()