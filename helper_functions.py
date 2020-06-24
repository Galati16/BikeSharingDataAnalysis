import pandas as pd
import time
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
weekDays = ('all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday')
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    response = 'N'

    month=''
    
    print('Hello! Let\'s explore some US bikeshare data!\n')

    while response == 'N' or response == 'n':
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input(
        'Which city data do you want to analyse: chicago, new york city, washington?\n').lower().strip()
        while city not in CITY_DATA.keys():
            city = input(
            'Sorry that was not right! Choose chicago, new york city or washington:\n')
        print('Analaysing data for {}!\n'.format(city))

        # get user input for month (all, january, february, ... , june)
        month = input(
        'Which time periode would you like to analyze: (all, january, february, ... , june)?\n').lower().strip()
        while month not in months:
            month = input(
            'Sorry that was not right! Choose all, january, february, ... , june:\n')
        print('Choosen time periode: {}!\n'.format(month))

        # get user input for day of week (all, monday, tuesday, ... sunday)

        day = input(
        'Which day would you like to analyse: (all, monday, tuesday, ... sunday)?\n').lower().strip()
        while day not in weekDays:
            day = input(
            'Sorry that was not right! Choose: all, monday, tuesday, ... sunday\n')
        print('Choosen time periode: {}!'.format(weekDays))
        print('-'*40+'\n')
        
        # make sure input is right:
        print('You choose:\n city: {}\n timeperiod:\n month:{} and days: {}'.format(
        city, month, day))
        response = input('Is that right?(Y/N)\n')
        if response == 'Y' or response == 'y':
            return city, month, day
    


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] =  pd.to_datetime(df['Start Time'])
    df['End Time'] =  pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    

    #Stats of unfiltered data: 
    print('-'*40) 
    print('Bikes in {} were most commonly used in {}, on {}s and at {} o\'clock'.format(
                city.title(), months[df['month'].mode()[0]-1].title(),  df['day_of_week'].mode()[0], df['hour'].mode()[0]))
    print(df['month'].value_counts())
    print(df['day_of_week'].value_counts())
    print(df['hour'].value_counts())
    print('-'*40) 
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
         (pandas DataFrame) df - DataFrame containing city data filtered by month and day
    """
    print('-'*40)
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('-'*40)
    
    start_time = time.time()
    
    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    combination = df['Start Station']+' TO '+ df['End Station']
    print('The most commonly used start station: {}\n'.format(start_station))
    print('The most commonly used end station: {}\n'.format(end_station))
    print('The most frequent combination of start station and end station:\n {}\n'.format(combination.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   
   
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
        Args:
         (pandas DataFrame) df - DataFrame containing city data filtered by month and day
    """
    print('-'*40) 
    print('\nCalculating Trip Duration...\n')
    print('-'*40)
     
    start_time = time.time()

    df['travel time'] = df['End Time'] - df['Start Time']
    df['travel time'].astype('timedelta64[m]')

    # display total travel time
    print('Total travel time: {}  in [m]'.format(df['travel time'].astype('timedelta64[m]').sum()))
    # display mean travel time
    print('Mean travel time: {}  in [m]'.format(df['travel time'].astype('timedelta64[m]').mean(), '.2f'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('-'*40)
    print('\nCalculating User Stats...\n')
    print('-'*40)
    start_time = time.time()

    # Display counts of user types
    count_types = df['User Type'].value_counts()
    print('User Types:\n{}\n'.format(count_types.to_string()))
    
    if city != 'washington':
        # Display counts of gender
        count_gender = df['Gender'].value_counts()

        # Display earliest, most recent, and most common year of birth
        print('Gender stats:\n{}\n'.format(count_gender.to_string()))
        print('Birthyear stats:\nEarliest: {}\nMost Recent: {}\nMost Common Year of Birth: {}\n'.format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

