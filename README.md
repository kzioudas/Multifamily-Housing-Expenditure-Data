# Multifamily Housing Expenditure Data
This task involves analyzing expenditure data from apartment buildings for bill payment. The data is stored in a file called data.csv and includes information such as building ID, expense date, provider, amount, and payment date (if any). Expenses without a payment date are considered as debts.

## Requirements
To run the program and generate the required statistics and graphs, you need to have the following dependencies installed:

pandas
matplotlib
You can install the required libraries using pip:

Copy code
pip install pandas matplotlib

## Usage
Clone the repository and navigate to the project directory.

Ensure that the data.csv file is present in the same directory.

Run the file using a Python interpreter.

Follow the instructions provided by the program to input the desired time period for analysis.

The program will display the calculated statistics and generate the required graphs.

Note: If you encounter any issues related to missing libraries, make sure to install them using the provided instructions.

## Functionality
The program provides the following functionality:

A. Load data for a specific time period
The program loads the expenditure data from the data.csv file for a specified time period.

B. Calculate statistics for the selected dates
The program calculates basic statistics (minimum, maximum, mean, standard deviation, and variance) for the selected dates.

C. Calculate total outstanding bills per apartment building
The program calculates the total outstanding bills for each apartment building.

D. Generate required graphs
The program generates graphs based on the loaded data and the selected time period. The graphs include:

Total debts per apartment building
Debts per month/year
Number of expenses per apartment building
Total debts per apartment building per month
Make sure to have the required dependencies installed to generate the graphs successfully.

## Example
Here's an example of how to use the program:

Clone the repository and navigate to the project directory.

Place the data.csv file in the project directory.

Run the main.py file using a Python interpreter.

Enter the start date and end date of the desired time period in the format dd/mm/yyyy.

The program will display the calculated statistics and generate the required graphs based on the selected time period.

## Conclusion
This program allows you to analyze expenditure data for apartment buildings, calculate statistics, and generate graphs to visualize the data. It provides valuable insights into the financial aspects of multifamily housing.