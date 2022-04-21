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
    ax.set(ylabel='Profit', title='Yearly Profit By Category', xlabel='Year')
    return

def yearly_discounts(df): 
    ax = df.groupby(['category', df.index.year])['discount'].sum().unstack(0).plot()
    ax.legend(loc='right', title='Product Category')
    # labels = [pd.to_datetime(t.get_text()).strftime('%Y') for t in ax.get_xticklabels()]
    # ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels([f'{tick:,.0f}%' for tick in ax.get_yticks()])
    ax.set(ylabel='Discount Percentage', title='Yearly Profit By Category', xlabel='Year')
    return
    
def profit_by_region(df):
    # Plot profit by region
    df1 = df.sort_values('profit', ascending=False)
    sns.boxplot(x='region_name', y='profit', data=df1, palette='seismic')
    plt.xlabel('Region')
    plt.ylabel('Profit')
    plt.title('Profit by Region')
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
    plt.title('Profit by State in Central Region')
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
    plt.title('Profit by City in Central Region, Texas')
    plt.show()
    return

