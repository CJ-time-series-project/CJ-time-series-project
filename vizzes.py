import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def yearly_cat_profits(df):
    company_cat_profit = (df[['profit','category']].groupby('category')
                  .resample('M').profit.sum().unstack(0))
    ax = (company_cat_profit.resample('Y')
    .sum()
    .plot.bar(width=.8))
    ax.legend(loc='upper right', title='Product Category')
    labels = [pd.to_datetime(t.get_text()).strftime('%Y') for t in ax.get_xticklabels()]
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])
    ax.set(ylabel='Profit', title='Yearly Profit For Each Category', xlabel='Year')
    return

def yearly_discounts(df): 
    ax = df.groupby(['category', df.index.year])['discount'].sum().unstack(0).plot()
    ax.legend(loc='right', title='Product Category')
    # ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels([f'{tick:,.0f}%' for tick in ax.get_yticks()])
    ax.set(ylabel='Discount Percentage', title='Average Discount Percentage Over Time', xlabel='Year')
    return
    
def profit_by_region(df):
    # Plot profit by region
    df1 = df.sort_values('profit', ascending=False)
    sns.boxplot(x='region_name', y='profit', data=df1, palette='seismic')
    plt.xlabel('Region')
    plt.ylabel('Profit')
    plt.title('The Central Region Is The Only Region With Negative Profit')
    plt.ylim(-125, 125)
    plt.axhline(y=0, linestyle='--', color='red')
    plt.show()
    return

def profit_by_state(df):
    central_region = df.loc[df['region_name'] == 'Central']
    central_states = central_region.groupby('state').sum()['profit'].sort_values(ascending=False)
    ax = sns.barplot(central_states, central_states.index, palette='seismic')
    ax.set_xticklabels([f'${x:,.0f}' for x in ax.get_xticks()])
    plt.xticks(rotation=45)
    plt.xlabel('State')
    plt.ylabel('Profit')
    plt.title('Both Illinois and Texas Have Negative Profits but Texas is Double that of Illinois')
    plt.show()
    return

def neg_profit_tx(df):
    central_region = df.loc[df['region_name'] == 'Central']
    texas_cities = central_region.loc[central_region['state'] == 'Texas']
    texas_cities = texas_cities.loc[texas_cities['profit'] < -100]
    texas_profit = texas_cities.groupby('city').sum()['profit'].sort_values(ascending=False)
    texas_profit.sort_values(ascending=False).head()
    ax = sns.barplot(x=texas_profit.index, y=texas_profit, alpha=0.9, palette='seismic')
    ax.set_yticklabels([f'${x:,.0f}' for x in ax.get_yticks()])
    plt.xticks(rotation=45)
    plt.xlabel('City')
    plt.ylabel('Profit')
    plt.title('Houston and San Antonio Offer the Biggest Hit to Profit in Texas')
    plt.show()
    return

