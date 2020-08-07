import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthly_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

daily_data = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore the first 6 months of US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in city_data:
        city_name = input("\nEnter Chicago, New York City, or Washington to view their bikeshare data. \n")
        if city_name.lower() in city_data:
            city = city_data[city_name.lower()]
            #City data successfully selected.
        else:
            print("City name invalid, please enter Chicago, New York City, or Washington.\n")
            #City data not successfully selected, loop to start.

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in monthly_data:
        month_name = input("\nWhich month would you like to view? (Enter 'All' to view all 6 months)\n")
        if month_name.lower() in monthly_data:
            month = month_name.lower()
            #Month data successfully selected.
        else:
            print("Month entered is invalid, please enter a month between January and June, or All.\n")
            #Month data not successfully selected, loop to start.

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in daily_data:
        day_name = input("\nWhich day of the week would you like to view? (Enter 'All' to view a full week)\n")
        if day_name.lower() in daily_data:
            day = day_name.lower()
            #Day data successfully selected.
        else:
            print("Day entered is invalid, please enter a day of the week or 'All' to view the full week.")
            #Day data not successfully selected, loop to start.

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = monthly_data.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel within the given filters...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The month with the most rentals:\n " + monthly_data[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The day of the week with the most rentals:\n " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The beginning time of the most rentals:\n " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip within the given filters...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most popular starting station:\n " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station:\n " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "->" + df['End Station']).mode()[0]
    print("The most commonly used start and end station combination:\n " + str(frequent_combination.split("->")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration within the given filters...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time of all rentals:\n " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time of all rentals:\n " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats within the given filters...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The number of user types: \n" + str(user_types))

    if city != 'washington.csv':
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth year:\n {}'.format(earliest_birth))
        print('Most recent birth year:\n {}'.format(most_recent_birth))
        print('Most common birth year:\n {}'.format(most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to the first five rows of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
