import json
from pytube import YouTube
import pandas as pd
import requests, os
from pandas.errors import EmptyDataError
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from datetime import datetime
import datetime
import time
import numpy as np
import csv
import cv2
import matplotlib.pyplot as plt


def download_video(input_video):
    df_video=pd.read_csv(input_video)
    list_videos = df_video['id_video'].values.astype(str)
    for vid in list_videos:
        yt = YouTube(vid)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


def load_images_and_labels(path, genre):
    images = []
    labels = []
    genres = pd.read_csv(os.path.join("..","final_dataset","genres.csv"))
    if isinstance(genre, str):
        genre_no = genres[genres["genre"] == genre]["genre_id"].values[0]
    else:
        genre_no = genre
        genre = genres[genres["genre_id"] == genre_no]["genre"].values[0]


    class_path = os.path.join(path, str(genre))

    for filename in os.listdir(class_path):
        if filename[0] == '.':
            continue
        img_path = os.path.join(class_path, filename)
                
        img = cv2.imread(img_path)
        if img is None:
            continue
        
        img = img / 255.0
        
        images.append(img)
        labels.append(genre_no)
    
    images = np.array(images)
    labels = np.array(labels)
    
    return images, labels



def download_image(image_url, outs, size = 'thumb'):
    #thumb for thumbnails
    #original for original size

    if 'https' not in image_url:
        image_url = 'https://' + image_url

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    img_data = requests.get(image_url).content
    
    for out in outs:
        with open(out, 'wb') as handler:
            handler.write(img_data)
            handler.close()


def read_json_string(json_string):
    return json.dumps(json_string.json(), sort_keys=True, indent=4)


def build_filename_string(outdir, platform, rating_range):
    return outdir+platform+'_games_rating_between_'+str(rating_range[0])+'_'+str(rating_range[1])+'.csv'



def preprocess_column(df, column_name):
    # Using regex to replace newline characters and other non-alphanumeric characters except spaces
    df[column_name] = df[column_name].replace(to_replace=[r'\n', r'[^\w\s]'], value=[' ', ''], regex=True)
    return df


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




def count_games(directory, platform, out_dir):
    # List to hold row count data
    row_count_list = []
    # Initialize total row counter
    total_row_count = 0

    # List all files in the provided directory
    for file in os.listdir(directory):
        # Check if the file is a CSV
        if file.endswith('.csv'):
            file_path = os.path.join(directory, file)  # Full path to the file
            try:
                # Try to read the file with pandas
                df = pd.read_csv(file_path)
                # Count the rows, assuming the first row is a header
                row_count = len(df)
            except EmptyDataError:
                # If an EmptyDataError occurs, mark the row count as 0
                row_count = 0

            # Append to list as a tuple
            row_count_list.append((file, row_count))
            # Add to total row count
            total_row_count += row_count

    # Convert list to DataFrame
    row_count_df = pd.DataFrame(row_count_list, columns=['filename', 'number of rows'])
    # Define the output CSV file path
    output_csv_path = os.path.join(out_dir, platform + '_row_counts.csv')
    # Save to CSV
    row_count_df.to_csv(output_csv_path, index=False)

    # Print total row count
    print(f'Total number of rows: for {platform} {total_row_count}')

    # Return the path to the output CSV file
    return total_row_count

def compute_stats(platform_list, platform_paths):
    tot_platform = 0
    for plat, path in zip(platform_list, platform_paths):
        if not os.path.exists(path):
            os.mkdir(path)
        count = count_games(path, plat, 'stats/')
        tot_platform += count

    print('All', tot_platform)



def unix_time_to_datetime(unix_time_str):
    try:
        # Convert the Unix timestamp string to a floating-point number
        unix_time = float(unix_time_str)

        # Convert the Unix timestamp to a datetime object
        datetime_obj = datetime.utcfromtimestamp(unix_time)

        return datetime_obj
    except ValueError:
        # Handle the case where the input string is not a valid Unix timestamp
        return None

# Example usage:

def create_path_if_not(path):
    if not os.path.exists(path):
        os.makedirs(path)


def generate_date_intervals(years=10, interval_months=1):
    end_date = datetime.date.today()
    start_year = end_date.year - years

    # Initialize the start date at the beginning of the start year
    current_start_date = datetime.date(start_year, 1, 1)
    intervals = []

    # Generate intervals until the current date is reached or passed
    while current_start_date <= end_date:
        try:
            # Try to create the end date by adding the interval in months
            current_end_date = current_start_date.replace(
                month=current_start_date.month + interval_months) - datetime.timedelta(days=1)
        except ValueError:
            # Handle end of year rollover
            year_adjustment = (current_start_date.month + interval_months - 1) // 12
            month_adjustment = (current_start_date.month + interval_months - 1) % 12 + 1
            current_end_date = current_start_date.replace(
                year=current_start_date.year + year_adjustment,
                month=month_adjustment) - datetime.timedelta(days=1)

        # Convert dates to Unix timestamp strings
        start_timestamp_str = str(int(time.mktime(current_start_date.timetuple())))
        end_timestamp_str = str(int(time.mktime(current_end_date.timetuple())))

        # Append the interval in Unix timestamp string format
        intervals.append((start_timestamp_str, end_timestamp_str))

        # Set the next interval's start date
        try:
            current_start_date = current_end_date.replace(day=1, month=current_end_date.month + 1)
        except ValueError:
            # Handle the case for December to January transition
            current_start_date = current_end_date.replace(day=1, year=current_end_date.year + 1, month=1)

    return intervals



def merge_csv_2(file1, file2, output_file):

    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file1, sep= ',')
    df2 = pd.read_csv(file2, sep= ',')

    # Concatenate the DataFrames along the rows
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

def merge_csv(files, output_file):
    all_rows = set()
    header_saved = False

    with open(output_file, 'w', newline='', encoding='utf-8') as fout:
        writer = csv.writer(fout)

        for file in files:
            with open(file, 'r', newline='', encoding='utf-8') as fin:
                reader = csv.reader(fin)
                header = next(reader)

                if not header_saved:
                    writer.writerow(header)  # Write the header only once.
                    header_saved = True

                for row in reader:
                    row_tuple = tuple(row)  # Convert the list to a tuple for set operations
                    if row_tuple not in all_rows:
                        all_rows.add(row_tuple)
                        writer.writerow(row)




def plot():
    # Data
    data = {
        'Platform': ['Xbox'] * 5 + ['Playstation'] * 5 + ['Nintendo'] * 5 + ['PC'] * 5,
        'Genres': ['Shooter', 'RPG', 'Platform', 'Simulator', 'Fighting',
                   'Shooter', 'RPG', 'Platform', 'Puzzle', 'Simulator',
                   'Platform', 'Puzzle', 'Shooter', 'RPG', 'Simulator',
                   'Adventure', 'Simulator', 'RPG', 'Shooter', 'Indie'],
        'N. Games': [2999, 1620, 1479, 1163, 1012,
                     3828, 2985, 1969, 1794, 1789,
                     3410, 3280, 2458, 2297, 1817,
                     10041, 9014, 8873, 8782, 8212]
    }
    df = pd.DataFrame(data)

    # Colors for each platform
    colors = {
        'Xbox': 'green',
        'Playstation': 'darkblue',
        'Nintendo': 'red',
        'PC': 'black'
    }

    for platform in df['Platform'].unique():
        # Filter the data for the specific platform
        subset = df[df['Platform'] == platform]

        # Bar plot
        plt.figure(figsize=(8, 6))
        plt.bar(subset['Genres'], subset['N. Games'], color=colors[platform])
        #plt.title(platform)
        plt.ylabel('Number of Games',fontsize= 22)
        plt.xticks(subset['Genres'], rotation=45, fontsize=22)
        plt.tight_layout()

        # Save the plot as a PNG file
        plt.savefig(f'{platform}_games_plot.png')

        # Show the plot
        plt.show()


