import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class CSVReader:
    @staticmethod
    def read_csv():
        print("reading csb from path")
        return pd.read_csv("/Users/sraavanchevireddy/Desktop/Machine Learning Datasets/covid19_tweets.csv")


data_reader = CSVReader.read_csv()
data_reader.describe()
print(data_reader.isnull().count())

# Validate and remove the null values
data_reader = data_reader.dropna()
unique_months = list(pd.DatetimeIndex(data_reader['date']).month.unique())  # Gives the unique months in the dataset.

if not unique_months:
    print("list is empty")
else:
    top_july = data_reader["user_location"][pd.DatetimeIndex(data_reader['date']).month == 7].value_counts()
    top_august = data_reader["user_location"][pd.DatetimeIndex(data_reader['date']).month == 8].value_counts()
    top_all_time = (top_july + top_august).sort_values(ascending=False)
    print(top_all_time)

    fig, ax = plt.subplots(figsize=(13, 10))
    plt.xlabel("Location", fontsize=12)
    plt.ylabel("NO. Tweets", fontsize=12)
    top_july[0:15].plot(kind='bar', title="Top 15 Countries posted about Covid-19 in July", )
    plt.show()


