import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    city = str(input("please enter your requested city : ")).lower().strip()

    while(city not in cities):
        city = str(input("please enter 'chicago','new york city' or'washington' : ")).lower().strip()

    # get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march","april","may", "june"]
    month = str(input("please enter desired month or all : ")).lower().strip()

    while(month not in months):
        month = str(input("please enter a month from january to june : ")).strip().lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "monday", "tuesday","wednesday","thursday","friday","saturday" , "sunday"]
    day = str(input("please enter desired day or all : ")).lower().strip()

    while(day not in days):
        day = str(input("please enter any weekday : ")).lower().strip()

    print('-'*40)
    return city, month, day.capitalize()



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
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()


    if month.lower().strip() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['Month']==month]

    # filter by day of week if applicable
    if day.lower().strip() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("the most common month is {}".format(df["Month"].mode()[0]))

    # display the most common day of week
    print("the most common day of week is {}".format(df["day_of_week"].mode()[0]))


    # display the most common start hour
    print("the most common start hour is {}".format(df["Start Time"].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("the most commonly used start station is {}".format(df["Start Station"].mode()[0]))


    # display most commonly used end station
    print("the most commonly used end station is {}".format(df["End Station"].mode()[0]))


    # display most frequent combination of start station and end station trip
    print("the most frequent combination of start station and end station trip ({})".format((df["Start Station"]+" , "+df["End Station"]).mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total trip duration is {} seconds".format(df["Trip Duration"].sum()))

    # display mean travel time
    print("the mean trip duration time is ",(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts())

    # Display counts of gender
    if "Gender" in df:
        print(df["Gender"].value_counts())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("min is {} max is {} common is {}".format(df["Birth Year"].min(),df["Birth Year"].max(),df["Birth Year"].mode()[0]))
    else:
        print(('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rows(df,start):
    print(df.iloc[start:start+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start = 0
        while view_data.lower() == "yes":
            display_rows(df,start)
            view_data = input("Would you like to view the next 5 rows of data? Enter yes or no?")
            start +=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
