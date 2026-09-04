import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

FILE_NAME = "library_transactions.csv"


class LibraryDashboard:

    def __init__(self):
        self.df = None

    def load_data(self):
        if not os.path.exists(FILE_NAME):
            print("\nFile not found!")
            print("Keep library_transactions.csv in the same folder.")
            return

        self.df = pd.read_csv(FILE_NAME)
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)

        self.df["date"] = pd.to_datetime(
            self.df["date"], errors="coerce"
        )
        self.df.dropna(subset=["date"], inplace=True)

        self.df["day"] = self.df["date"].dt.day_name()
        self.df["month"] = self.df["date"].dt.month_name()
        self.df["month_no"] = self.df["date"].dt.month

        print("\nDataset loaded successfully!")

    def check_data(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        print("\n========== DATASET INFORMATION ==========")
        print("Shape:", self.df.shape)
        print("\nData Types:")
        print(self.df.dtypes)
        print("\nMissing Values:")
        print(self.df.isnull().sum())
        print("\nStatistics:")
        print(self.df.describe())

    def view_data(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        print("\n========== DATA PREVIEW ==========")
        print("\nFirst 5 rows:")
        print(self.df.head())

        print("\nLast 5 rows:")
        print(self.df.tail())

    def statistics(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        book = self.df["book title"].mode()[0]
        duration = np.array(self.df["borrowing duration"])

        print("\n========== BORROWING STATISTICS ==========")
        print("Most Borrowed Book:", book)
        print("Average Duration:", round(np.mean(duration), 2), "days")
        print("Standard Deviation:", round(np.std(duration), 2), "days")
        print("Busiest Day:", self.df["day"].mode()[0])

    def top_users(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        print("\n========== TOP 5 ACTIVE USERS ==========")
        print(self.df["user id"].value_counts().head(5))

    def genre_filter(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        genre = input("\nEnter genre: ").strip()

        result = self.df[
            self.df["genre"].str.lower() == genre.lower()
        ]

        if result.empty:
            print("No transactions found.")
        else:
            print("\nRecords found:", len(result))
            print(result[
                ["transaction id", "date", "book title", "user id"]
            ].head(10))

    def top_books_chart(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        books = self.df["book title"].value_counts().head(5)

        plt.figure(figsize=(9, 5))
        sns.barplot(x=books.values, y=books.index)

        plt.title("Top 5 Most Borrowed Books")
        plt.xlabel("Borrowings")
        plt.ylabel("Book Title")
        plt.tight_layout()
        plt.show()

    def monthly_chart(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        data = (
            self.df.groupby(["month_no", "month"])
            ["transaction id"].count()
            .reset_index()
            .sort_values("month_no")
        )

        plt.figure(figsize=(10, 5))
        sns.lineplot(
            data=data,
            x="month",
            y="transaction id",
            marker="o"
        )

        plt.title("Monthly Borrowing Trends")
        plt.xlabel("Month")
        plt.ylabel("Transactions")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def genre_chart(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        data = self.df["genre"].value_counts()

        plt.figure(figsize=(7, 7))
        plt.pie(
            data.values,
            labels=data.index,
            autopct="%1.1f%%"
        )

        plt.title("Borrowing Distribution by Genre")
        plt.show()

    def activity_heatmap(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        days = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]

        data = (
            self.df["day"]
            .value_counts()
            .reindex(days)
            .fillna(0)
        )

        heatmap = pd.DataFrame([data.values], columns=days)

        plt.figure(figsize=(10, 3))
        sns.heatmap(
            heatmap,
            annot=True,
            fmt="g",
            cbar=False
        )

        plt.title("Weekly Borrowing Activity")
        plt.yticks([])
        plt.show()

    def save_data(self):
        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        self.df.to_csv(
            "Prepared_library_transactions.csv",
            index=False
        )

        print("\nPrepared dataset saved successfully!")


def menu():
    print("""
==================================================
          📊 E-LIBRARY DATA DASHBOARD
==================================================

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
0. Exit

==================================================
""")


def main():
    dashboard = LibraryDashboard()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            dashboard.load_data()
        elif choice == "2":
            dashboard.check_data()
        elif choice == "3":
            dashboard.view_data()
        elif choice == "4":
            dashboard.statistics()
        elif choice == "5":
            dashboard.top_users()
        elif choice == "6":
            dashboard.genre_filter()
        elif choice == "7":
            dashboard.top_books_chart()
        elif choice == "8":
            dashboard.monthly_chart()
        elif choice == "9":
            dashboard.genre_chart()
        elif choice == "10":
            dashboard.activity_heatmap()
        elif choice == "11":
            dashboard.save_data()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()