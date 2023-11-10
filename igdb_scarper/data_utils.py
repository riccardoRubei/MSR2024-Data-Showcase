import json
from pytube import YouTube
import pandas as pd
import requests



def download_video(id_video):
    yt = YouTube('http://youtube.com/watch?v='+str(id_video))
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


def download_image(image_url, out, size = 'thumb'):
    #thumb for thumbnails
    #original for original size

    if 'https' not in image_url:
        image_url = 'https://' + image_url

    img_data = requests.get(image_url).content
    with open(out, 'wb') as handler:
        handler.write(img_data)


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


def generate_range_ratings(start, end, delta):
    tuple_list = []
    current = start
    while current <= end - delta:
        tuple_list.append((current, current + delta))
        current += delta
    return tuple_list

# Use the function to generate tuples from 0 to 100 with a delta of 10

