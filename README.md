📊 E-Library Data Dashboard

A beginner-friendly Python project that analyzes library transaction data using Pandas and NumPy and creates visualizations using Matplotlib and Seaborn.
The dashboard works with a fixed library_transactions.csv file and provides different options to explore borrowing activity, users, books, genres, and monthly trends.

✨ Features
- 📂 Load library_transactions.csv
- 🧹 Remove missing and duplicate records
- 📅 Convert and process transaction dates
- 📆 Add day and month information
- 📊 View dataset information and statistics
- 👀 Preview the first and last five records
- 📚 Find the most borrowed book
- ⏱️ Calculate average borrowing duration
- 📈 Calculate standard deviation
- 📅 Find the busiest day
- 👥 Find the top 5 active users
- 🔎 Filter transactions by genre
- 📊 Display top 5 books using a bar chart
- 📈 Display monthly borrowing trends
- 🥧 Display borrowing distribution by genre
- 🔥 Display weekly borrowing activity using a heatmap
- 💾 Save the prepared dataset as a CSV file

🛠️ Technologies Used

Technology	Purpose

Python	Main programming language

Pandas	Data loading, cleaning, filtering and analysis

NumPy	Numerical calculations

Matplotlib	Data visualization

Seaborn	Statistical charts and visualizations

OS	Checking whether the dataset exists


📁 Dataset

The project uses:

library_transactions.csv

The CSV file should be kept in the same folder as the Python file.

The dataset contains library transaction information such as:

Column	Description

transaction id	Unique ID of the transaction

date	Date of the transaction

user id	ID of the library user

book title	Title of the borrowed book

genre	Genre of the book

borrowing duration	Number of days the book was borrowed

The program creates three additional columns during data preparation:

day

month

month_no

🧹 Data Preparation

When the dataset is loaded, the program performs the following operations:

1. Checks whether library_transactions.csv exists.
2. Loads the CSV file using Pandas.
3. Removes missing values.
4. Removes duplicate records.
5. Converts the date column into datetime format.
6. Removes invalid dates.
7. Creates the day of the week.
8. Creates the month name.
9. Creates the month number for sorting monthly data.

📋 Dashboard Options

The program provides the following menu:

📊 E-LIBRARY DATA DASHBOARD

1. Load Dataset
2. View Dataset Information
3. View Data Preview
4. Calculate Borrowing Statistics
5. Find Top 5 Active Users
6. Filter by Genre
7. Top Books Bar Chart
8. Monthly Trends Line Chart
9. Genre Distribution Pie Chart
10. Weekly Activity Heatmap
11. Save Prepared Dataset
12. Exit

1️⃣ Load Dataset

Loads and prepares the library_transactions.csv file.

2️⃣ Dataset Information

Displays:
- Number of rows and columns
- Data types
- Missing values
- Statistical information
  
3️⃣ Data Preview

Displays the first five and last five rows of the prepared dataset.

4️⃣ Borrowing Statistics

Calculates:
- Most borrowed book
- Average borrowing duration
- Standard deviation of borrowing duration
- Busiest day of the week
  
5️⃣ Top 5 Active Users

Finds the five users with the highest number of borrowing transactions.

6️⃣ Genre Filter

Allows the user to enter a genre and displays matching transactions.

7️⃣ Top Books Bar Chart

Displays the five most borrowed books using a Seaborn bar chart.

8️⃣ Monthly Trends

Displays the number of borrowing transactions for each month using a line chart.

9️⃣ Genre Distribution

Displays the percentage of borrowed books by genre using a pie chart.

🔟 Weekly Activity Heatmap

Displays borrowing activity from Monday to Sunday using a heatmap.

1️⃣1️⃣ Save Prepared Dataset

Saves the cleaned and prepared data as:

Prepared_library_transactions.csv

📊 Visualizations

The project includes four different visualizations:

Bar Chart

Shows the top 5 most borrowed books.

Line Chart

Shows borrowing trends across different months.

Pie Chart

Shows the distribution of borrowed books by genre.

Heatmap

Shows borrowing activity across the days of the week.

📦 Installation

Make sure Python is installed on your computer.

Install the required libraries:

pip install pandas numpy matplotlib seaborn

If you are using VS Code, you can run this command in the VS Code terminal.

▶️ How to Run

Keep the files in the same folder:

E-Library-Data-Dashboard/

│

├── library_dashboard.py

├── library_transactions.csv

└── README.md

Run the Python program using:

python library_dashboard.py

The dashboard menu will appear in the terminal.

Important: Load the dataset using option 1 before using the other analysis options.

💾 Output File

After selecting the save option, the program creates:

Prepared_library_transactions.csv

This file contains the cleaned dataset along with the additional date-related columns.

🧠 Python Concepts Practiced

This project demonstrates:

- Classes and Objects

- Constructors

- Functions and Methods

- if-elif-else statements

- while loops

- User Input

- File Handling

- CSV Data Handling

- Data Cleaning

- Pandas DataFrames

- NumPy Arrays

- Data Filtering

- GroupBy Operations

- Value Counts

- DateTime Operations

- Data Visualization

📂 Project Structure

E-Library-Data-Dashboard/


│

├── library_dashboard.py

├── library_transactions.csv

├── Prepared_library_transactions.csv

└── README.md

Prepared_library_transactions.csv is generated automatically by the program when the user selects the save option.

🎯 Project Objective

The main purpose of this project is to practice Python programming and basic data analysis by working with a library transaction dataset.

It combines programming concepts with data cleaning, statistical calculations, filtering, and visualization to understand library borrowing patterns.

🚀 Future Improvements

Possible improvements include:

- Adding more analysis options

- Adding more charts

- Creating an interactive graphical interface

- Adding book/user search functionality

- Adding yearly comparisons

- Exporting charts as image files

- Adding more advanced data analysis


