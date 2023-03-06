import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday","all"]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    print("Would you like to see data for chicago, new york, or washington? \n")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input().lower()
        if city in cities:
            break
        else:
          print("Please enter valid City!")
   
    while True:
        print(months)
        month= input("choose a month:").lower()
        if month in months:
            break
        else :
            print("Please enter valid month!")
    while True :
        print(days)
        day = input("choose the day: ").lower()
        if day in days:
            break
        else:
            print("Please enter valid day!")

   

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
      
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

  
    popular_month= df['month'].mode()[0]

   
    popular_day=df['day_of_week'].mode()[0]

    
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)
    print('Most Popular Month:', popular_month)
    print('Most Popular Day:', popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

  
    
    print('Most Popular Start Station:\n', df['Start Station'].mode()[0])

    print("most commonly used end stationP \n",df['End Station'].mode()[0])
    
    popular_trip=df.groupby(['Start Station', 'End Station']).size().sort_values(ascending = False).head(1)
    print("most popular trip :\n",popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    print(" total travel time",df['Trip Duration'].sum())
    
    print("the average travel time",df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    print("counts of user types :",df['User Type'].value_counts())

    print("counts of gender", df['Gender'].value_counts())
   

    print("earliest year of birth :",df['Birth Year'].min())
    print("most recent  year of birth :",df['Birth Year'].max())
    print("most common year of birth :",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    i=0
    while True:
        
        city, month, day = get_filters()
        response = input('Would you like to view 5 lines of raw data? (Yes/No) ')

        if response.lower() == 'yes':
    
          with open(CITY_DATA[city], 'r') as file:
            lines = file.readlines()
            
            for line in lines[i:i+5]:
                print(line)
            if line == "":
                break

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
