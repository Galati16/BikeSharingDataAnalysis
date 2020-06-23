
from helper_functions import load_data, get_filters, station_stats, trip_duration_stats, user_stats, time_stats

import time
import pandas as pd


#get user choice of city to analyse, and time period:
#city, month, day = get_filters()

#load corresponding data:
#df = load_data(city, month, day)
#station_stats(df)
print(load_data('chicago', 'january', 'monday').info())
#calculate stats for stations:
#    most common start and  end station
#    most common trip from start to end (i.e., most frequent combination of start station and end station)
#station_stats(df)
#trip_duration_stats(df)
#user_stats(df, city)
time_stats(load_data('chicago', 'january', 'monday'))

