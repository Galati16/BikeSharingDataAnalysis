
import pandas as pd

from helper_functions import load_data, get_filters, station_stats, trip_duration_stats, user_stats

while True:
    #get user choice of city to analyse, and time period:
    city, month, day = get_filters()

    #load corresponding data:
    df = load_data(city, month, day)

    #calculate stats for stations:
    #    most common start and  end station
    #    most common trip from start to end (i.e., most frequent combination of start station and end station)
    station_stats(df)

    #calculate stats for trip duration:
    trip_duration_stats(df)

    #calculate user stats, if available:
    user_stats(df, city)
    
    # handle raw data input interactivley depending on user input
    user_input = input('Would you like to see the raw data? (Y/N).y\n If you would like to restart, write: restart.\n')
    if user_input.lower() == 'n' or user_input.lower() == 'no' :
        break
    else:
        i=0
        while user_input == 'y' or user_input.lower() == 'yes':
            i += 5
            print(df.head(i))
            user_input = input('\nWould you like to see the next five values? (Y/N)\n')
                


