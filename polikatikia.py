import pandas as pd
import matplotlib.pyplot as plt
import datetime
# A. Load data for a specific time period
def load_data(start_date, end_date):
    # Read the CSV file
    df = pd.read_csv('data.csv')
    
    # Convert date_created column to datetime format
    df['date_created'] = pd.to_datetime(df['date_created'], utc=True)
    
    # Filter the data for the specified time period
    mask = (df['date_created'].dt.date >= start_date) & (df['date_created'].dt.date <= end_date)
    filtered_df = df[mask]
    
    return filtered_df


# B. Calculate statistics for the selected dates
def calculate_statistics(df):
    # Calculate minimum, maximum, mean, standard deviation, and variance
    min_poso = df['poso'].min()
    max_poso = df['poso'].max()
    mean_poso = df['poso'].mean()
    std_poso = df['poso'].std()
    var_poso = std_poso ** 2
    
    return min_poso, max_poso, mean_poso, std_poso, var_poso


# C. Calculate total outstanding bills per apartment building
def calculate_debts_per_building(df):
    # Group the data by buildingID and sum the outstanding amounts
    debts_per_building = df.groupby('buildingID')['poso'].sum()
    
    return debts_per_building


# D. Generate required graphs
def generate_graphs(data):
    # Total debts per apartment building
    debts_per_building = data.groupby('buildingID')['poso'].sum()
    plt.figure(figsize=(10, 5))
    plt.bar(debts_per_building.index, debts_per_building.values)
    plt.xlabel('buildingID')
    plt.ylabel('Total Debts')
    plt.title('Total Debts per Apartment Building')
    plt.show()

    # Debts per month/year
    data['date_created'] = pd.to_datetime(data['date_created'])
    debts_per_month_year = data.groupby(data['date_created'].dt.to_period('M'))['poso'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(debts_per_month_year.index.astype(str), debts_per_month_year.values)
    plt.xlabel('Month/Year')
    plt.ylabel('Total Debts')
    plt.title('Debts per Month/Year')
    plt.xticks(rotation=45)
    plt.show()

    # Number of expenses per apartment building
    expenses_per_building = data.groupby('buildingID').size()
    plt.figure(figsize=(10, 5))
    plt.bar(expenses_per_building.index, expenses_per_building.values)
    plt.xlabel('buildingID')
    plt.ylabel('Number of Expenses')
    plt.title('Number of Expenses per Apartment Building')
    plt.show()

    # Total debts per apartment building per month
    debts_per_building_month = data.groupby(['buildingID', data['date_created'].dt.to_period('M')])['poso'].sum()
    debts_per_building_month.unstack(level=0).plot(kind='bar', figsize=(10, 5))
    plt.xlabel('Month')
    plt.ylabel('Total Debts')
    plt.title('Total Debts per Apartment Building per Month')
    plt.legend(title='buildingID')
    plt.show()

def get_time_period():
    while True:
        try:
            start_date_str = input("Enter the start date (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()

            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()

            if start_date > end_date:
                print("Start date cannot be greater than end date. Please try again.")
                continue

            return start_date, end_date

        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

def print_stats(data):
    min_poso, max_poso, mean_poso, std_poso, var_poso = calculate_statistics(data)
    print('Statistics for the selected dates:')
    print('Minimum Poso:', min_poso)
    print('Maximum Poso:', max_poso)
    print('Mean Poso:', mean_poso)
    print('Standard Deviation:', std_poso)
    print('Variance:', var_poso)
# Usage example:
start_date, end_date = get_time_period()


data = load_data(start_date, end_date)
print_stats(data)
# Generate the required graphs
generate_graphs(data)
