import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to provide a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input("Please input the name of the city to analyze (chicago, new york city, or washington) : ").lower()
        if city in cities:
            break
        else:
            print("oops i am sorry, please enter ""chicago"", ""new york city"", or ""washington"" exactly as shown")
            continue

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    while True:
        month = input("name of the month to filter by, or ""all"" to apply no month filter: ").lower()
        if month in months:
            break
        else:
            print("oops i am sorry, please enter ""january"", ""february"", ""march"", ""april"", ""may"", ""june"", or ""all"" exactly as shown")
            continue
    # get user input for month (all, january, february, ... , june)

    days = ('monday', 'tuesday', 'wednesday', 'thursday' 'friday', 'saturday', 'sunday', 'all')
    while True:
        day = input("name of the day to filter by, or ""all"" to apply no day filter: ").lower()
        if day in days:
            break
        else:
            print("oops i am sorry, please enter ""monday"", ""tuesday"", ""wednesday"", ""thursday"", ""friday"", ""saturday"", ""sunday""or ""all"" exactly as shown")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the provided city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    # load data file into a dataframe

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # convert the Start Time column to datetime

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # extract month and day of week from Start Time to create new columns

    if month != 'all':
    # filter by month if applicable
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # use the index of the months list to get the corresponding int

        df = df[df['month'] == month]
        # filter by month to create the new dataframe

    if day != 'all':
    # filter by day of week if applicable
        df = df[df['day'] == day.title()]
        # filter by day of week to create the new dataframe

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df.loc[:,"month"].mode()[0]
    print('most common month is: ', popular_month)
    # display the most common month

    popular_day = df.loc[:,"day"].mode()[0]
    print('most common day of week is: ', popular_day)
    # TO DO: display the most common day of week

    popular_hour = df.loc[:,"hour"].mode()[0]
    print('most common start hour is: ', popular_hour)
    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    pop_start_stat = df.loc[:,"Start Station"].mode()[0]
    print('most common used start station is: ', pop_start_stat)
    # display most commonly used start station

    pop_end_stat = df.loc[:,"End Station"].mode()[0]
    print('most common used end station is: ', pop_end_stat)
    # display most commonly used end station

    pop_trip = (df.loc[:,"Start Station"] + " --- " + df.loc[:,"End Station"]).mode()[0]
    print('most frequent combination of start station and end station trip: ', pop_trip)
    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    sum_travel_time = df.loc[:,"Trip Duration"].sum()
    print('total travel time is ', sum_travel_time)
    # display total travel time

    mean_travel_time = df.loc[:,"Trip Duration"].mean()
    print('mean travel time is ', mean_travel_time)
    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count_type = df.loc[:,"User Type"].value_counts()
    print('counts of user types is:\n', count_type)
    # Display counts of user types

    try:
        counts_gender = df.loc[:,"Gender"].value_counts()
        print('counts of genders is:\n', counts_gender)
    except KeyError:
        print("No Gender column exist!")

    # Display counts of gender

    try:
        earliest_year = df.loc[:,"Birth Year"].min()
        print('earliest year is ', earliest_year)
        recent_year = df.loc[:,"Birth Year"].max()
        print('most resent year is ', recent_year)
        common_year = df.loc[:,"Birth Year"].mode()[0]
        print('most common year is ', common_year)
        # Display earliest, most recent, and most common year of birth
    except KeyError:
        print("No Birth exist!")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays lines of raw input."""

    print('\nDisplaying five lines of raw input...\n')
    start_time = time.time()

    start = 0
    stop = 5

    while True:
        show_records = input('\nWould you like to see five lines of raw input? Enter yes or no.\n')
        if show_records.lower() != 'yes':
            break
        else:
            lines_rows = df.iloc[start:stop,]
            print("five lines of rows: \n", lines_rows)
            start += 5
            stop += 5
        # Displays lines of raw input in increments of five


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)




        restart = input('\nWould you like to restart? Please enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
