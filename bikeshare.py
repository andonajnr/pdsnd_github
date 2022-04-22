import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def display_data():
    while True:
        try:
           raw_data = str((input('Which city would you like to see the first five lines of raw data? Chicago, New York city or Washington\n')).lower())
           if raw_data == 'chicago' or raw_data == 'new york city' or raw_data == 'washington':
                break 
           else:
               raise ValueError('Invalid Input')
        except:
            print('\n That\'s an invalid city \n')
        print('\n Attempted Input \n')
        
    if raw_data == 'chicago':
        with open("chicago.csv", "r") as f:
            lines = f.readlines()
            start = 0
            end = start + 5
            five_lines = lines[start:end]
            for line in five_lines:
                print(line)
    elif raw_data == 'new york city':
        with open("new_york_city.csv", "r") as f:
            lines = f.readlines()
            start = 0
            end = start + 5
            five_lines = lines[start:end]
            for line in five_lines:
                print(line)
    elif raw_data == 'washington':
        with open("washington.csv", "r") as f:
            lines = f.readlines()
            start = 0
            end = start + 5
            five_lines = lines[start:end]
            for line in five_lines:
                print(line)
                    
    while True:
        more_data = input('\nWould you like to see five more lines? Enter yes or no.\n')
        if more_data.lower() == 'yes':
            start +=5
            end = start + 5
            next_lines = lines[start:end]
            for line in next_lines:
                print(line)
        else:
            break
            
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
           city = str((input('Which city would you like to explore? Chicago, New York city or Washington\n')).lower())
           if city == 'chicago' or city == 'new york city' or city == 'washington':
               break 
           else:
               raise ValueError('Invalid')
        except:
            print('\n That\'s an invalid city \n')
        print('\n Attempted Input \n')
     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         try:
           month = str((input('Which month are you interested in exploring? Please type all or january, ...june\n')).lower())
           if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                break 
           else:
               raise ValueError('Invalid')
         except:
               print('\n That\'s an invalid month \n')
         print('\n Attempted Input \n')     
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
           day = str((input('Which of the weekdays? Please type all or monday, tuesday, ... sunday\n')).lower())
           if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
               break 
           else:
               raise ValueError('Invalid')
        except:
            print('\n That\'s an invalid month \n')
        print('\n Attempted Input \n')
        
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

   # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:\n', common_month)


    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common Day:\n', common_day)


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:\n', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:\n', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:\n', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df['Start Station'] + df['End Station']
    common_start_end_station = start_end_station.mode()[0]
    print('Most Common Start & End Station:\n', common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].count()
    print('Count of user type is: ', user_count)

    # TO DO: Display counts of gender
    if 'Gender'  == True:
        gender_count = df['Gender'].count()
        print('Count of gender is: \n', gender_count)
    else:
        print('Gender data is not available for this city\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year'  == True:
         earliest_birth_year = np.min(df['Birth Year'])
         print('Earliest Birth Year is: ', earliest_birth_year)
         recent_birth_year = np.max(df['Birth Year'])
         print('Most Recent Birth Year is: ', recent_birth_year)
         common_birth_year = df['Birth Year'].mode()[0]
         print('Most Common Birth Year is: ', common_birth_year)
    else:
        print('Birth Year data is not available for this city\n')
    
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        display_data()
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
                    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



            
if __name__ == "__main__":
	main()
            