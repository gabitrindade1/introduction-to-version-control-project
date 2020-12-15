import pandas as pd
import time as t
import calendar as c


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-=' * 55)

    # get user input for a city (chicago, new york city, washington)
    city = input('* Choose one of these cities Chicago, New York City, Washington. Enter your answer: ').strip().lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('\033[1:35mInvalid option!\033[m Please, choose a valid city:  ').strip().lower()
    print('--> The city option \033[31m{}\033[m has been successfully registered...'.format(city))
    t.sleep(1)

    # get user input for month (january, february, ... , june or all)
    month = input('* Choose a month from January to June or "all" for no filter. Enter your answer: ').strip().lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('\033[1:35mInvalid option!\033[m Please, choose a valid month:  ').strip().lower()
    print('--> The month option \033[31m{}\033[m has been successfully registered...'.format(month))
    t.sleep(1)

    # get user input for a day of the week (monday, tuesday, ... , sunday or all)
    day = input('* Choose a day of the week from Monday to Sunday or "all" for no filter. Enter your answer: ').strip().lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('\033[1:35mInvalid option!\033[m Please, choose a valid day:  ').strip().lower()
    print('--> The day option \033[31m{}\033[m has been successfully registered...'.format(day))

    print('-=' * 55)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\033[36mCalculating the most frequent times of travel...\033[m\n')
    start_time = t.time()

    # display the most common month
    popular_month = df['Month'].mode()[0]
    # convert the number of the month to its name
    popular_month = c.month_name[popular_month]
    print('Most popular month: ', popular_month)

    # display the most common day of week
    popular_day = df['Day_of_week'].mode()[0]
    print('Most popular day of week: ', popular_day)

    # extract hour from the Start Time column to create an hour column
    df['Hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['Hour'].mode()[0]
    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds.\n" % (t.time() - start_time))
    print('-=' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\033[36mCalculating the most popular stations and trip...\033[m\n')
    start_time = t.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'] + ' to ' + df['End Station']
    frequent_combination = df['Start_End'].mode()[0]
    print('Most frequent combination of start station and end station trip:\n', frequent_combination)

    print("\nThis took %s seconds.\n" % (t.time() - start_time))
    print('-='*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n\033[36mCalculating trip duration...\033[m\n')
    start_time = t.time()

    # display total travel time in hours and minutes
    total_travel_time_sec = df['Trip Duration'].sum()
    total_travel_time_min = total_travel_time_sec / 60
    total_travel_time_h = total_travel_time_sec / (60 * 60)
    print('Total travel time for the period: {:.2f} hours or {:.2f} min' .format(total_travel_time_h, total_travel_time_min))

    # display mean travel time in hours and minutes
    avg_travel_time_sec = df['Trip Duration'].mean()
    avg_travel_time_min = avg_travel_time_sec / 60
    avg_travel_time_h = avg_travel_time_sec / (60 * 60)
    print('Mean travel time for the period: {:.2f} hours or {:.2f} min' .format(avg_travel_time_h, avg_travel_time_min))

    print("\nThis took %s seconds.\n" % (t.time() - start_time))
    print('-='*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\n\033[36mCalculating user stats...\033[m\n')
    start_time = t.time()

    # display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('User types:\n', count_user_types)

  # display counts of gender for the cities that have this kind of data
    if city == 'new york city' or city == 'chicago':
        count_gender = df['Gender'].value_counts()
        print('\nUser\'s gender:\n', count_gender)
        # display earliest, most recent, and most common year of birth for the cities that have this kind of data
        earliest_year_birth = df['Birth Year'].min()
        recent_year_birth = df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]
        print('\nEarliest year of birth:\n', earliest_year_birth)
        print('\nMost recent year of birth:\n', recent_year_birth)
        print('\nMost common year of birth:\n', common_year_birth)

    print("\nThis took %s seconds.\n" % (t.time() - start_time))
    print('-='*40)


def raw_data(df):
    """Displays 5 rows at a time from the current dataset based on users request"""
    start_index = 0
    end_index = 5
    # get user input for displaying raw data
    display_data = input('\nWould you like to display some raw data from the current dataset? Enter "yes" or "no": ').strip().lower()
    # displays the full width
    pd.set_option('display.width', 400)
    # display all columns
    pd.set_option('display.max_columns', 15)
    while True:
        # display 5 rows at a time from the dataset
        print('\n', df[start_index:end_index])
        # get user input for displaying more raw data
        display_data = input('\nWould you like to see the next 5 rows? Enter "yes" or "no": ').strip().lower()
        # add 5 more rows
        end_index += 5
        if display_data == 'no':
            print('-=' * 40)
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter "yes" or "no": ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
