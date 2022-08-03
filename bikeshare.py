import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
        city= input("Enter city name: ").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        Month_list=['january','february','march','april','may','june','all']
        month=input("Enter Month(ex: january,february, ... ,june) or all: ").lower()
        if month in Month_list:
            break
        else:
            print("Please enter valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_list=['monday','sunday','tuesday','thursday','friday','all','wednesday','saturday']
        day=input("Enter day name or all: ").lower()
        if day in day_list:
            break
        else:
            print("Please enter valid day")


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month != 'all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day != 'all':
        df=df[df['day_of_week']==day.title()]
    


    return df
def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    print('Most common month: ',popular_month)


    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday_name
    popular_day=df['day_of_week'].mode()[0]
    print('Most common day: ',popular_day)


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most common start hour: ',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print('The most commonly used start station is: ',common_start)


    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print('The most commonly used end station is: ',common_end)


    # TO DO: display most frequent combination of start station and end station trip
    combination=(df['Start Station']+" : "+df['End Station']).mode()[0]
    print('The most frequent combination of start and end stations is: ',combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('The total tarvel time is: ',total_time)



    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('The mean tarvel time is: ',mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types=df['User Type'].value_counts()
    print("Counts of user types: ",user_types)


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        genders=df['Gender'].value_counts()
        print('Counts of Gender: ',genders)


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year=df['Birth Year'].min().astype(int)
        print('The earliest Year of birth is: ',earliest_year)
        recent_year=df['Birth Year'].max().astype(int)
        print('The earliest Year of Birth is: ',recent_year)
        common_year=df['Birth Year'].mode()[0].astype(int)
        print('The most common year of birth is: ',common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
