###pip install pytrends

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytrends.request import TrendReq
pytrend = TrendReq(tz=-60, timeout=(10,25)) # BST in summer time - timezone offset by -60

#################### Parameter ####################
KEYWORD_LIST = ['Football', 'Rugby', 'Tennis']
TIMEFRAME = 'today 3-m'
#################### Parameter ####################

pytrend.build_payload(kw_list=KEYWORD_LIST, timeframe=TIMEFRAME)
df = pytrend.interest_over_time()
df = df.rename_axis('date').reset_index()

def display(df):
    plt.figure(figsize=(10, 5))
    for keyword in KEYWORD_LIST:
        plt.plot(df['date'], df[keyword], label=keyword)

    plt.xlabel('Date')
    plt.ylabel('Share of search')
    plt.title('Share of Search Over 3 Months')
    plt.legend()
    plt.show()

display(df)

def display_with_sat(df):
    plt.figure(figsize=(10, 5))
    for keyword in KEYWORD_LIST:
        plt.plot(df['date'], df[keyword], label=keyword)

    df['weekday'] = pd.to_datetime(df['date']).dt.dayofweek
    saturdays = df[df['weekday'] == 5]['date'].to_list()
    saturdays

    # Add vertical lines every Saturday
    for d in saturdays:
        plt.axvline(x=d, color='red', linestyle='--')

    plt.xlabel('Date')
    plt.ylabel('Share of search')
    plt.title('Share of Search Over 3 Months')
    plt.legend()
    plt.show()

display_with_sat(df)