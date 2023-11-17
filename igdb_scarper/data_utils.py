import json
from pytube import YouTube
import pandas as pd
import requests, os
from pandas.errors import EmptyDataError
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def download_video(id_video):
    yt = YouTube('http://youtube.com/watch?v='+str(id_video))
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


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



import datetime
import time

def generate_date_intervals_unix(years=20, interval_months=1):
    """
    Generate a list of date tuples covering intervals over a number of years, in Unix timestamp strings.

    Args:
    - years (int, optional): Number of years to cover. Defaults to 5.
    - interval_months (int, optional): Number of months per interval. Defaults to 1.

    Returns:
    - list: List of date tuples in the format (start_date, end_date) where each date is a Unix timestamp string.
    """

    # Get the current date and calculate the start year
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

# Test the function with default parameters

