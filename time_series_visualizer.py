import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#testing

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates= ['date'])
# print(df.head())
# print(df.describe())

# Clean data
df = df[
  (df['value'] < df['value'].quantile(0.975)) &
  (df['value'] > df['value'].quantile(0.025))
]

def draw_line_plot():
  # Draw line plot
  fig = plt.figure()
  plt.plot(df.index, df['value'])
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  # plt.show()
  # plt.savefig('line_plot.png')

  ####
  ####
  # FOR SOME REASON plt.show() doesn't allow fig.savefig below.
  # Maybe it doesn't let the code run at all?
  ####
  ####

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  # I'm thinking group by year and month
  # print(df.head())
  
  df_bar = df.copy()
  #print('-------------- \n', df_bar)
  # print(df_bar.info())
  # print(df_bar.describe())
  df_bar = df_bar.groupby([df_bar['date'].dt.year, df_bar['date'].dt.month])['value'].mean()
  #print('-------------- \n', df_bar)

  df_bar = df_bar.unstack()
  #print('-------------- \n', df_bar)
  #print(df_bar.describe())

  fig = df_bar.plot(kind='bar', legend=True).figure
  # plt.show()

  # Draw bar plot
  plt.legend(title='Months')
  plt.legend(labels=['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December'])
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  df_box['month_number'] = df_box.date.dt.month
  df_box.sort_values(by= ['month_number'], inplace= True)
  # Draw box plots (using Seaborn)
  fig, (ax1, ax2) = plt.subplots(1, 2)

  ax1 = sns.boxplot(x=df['date'].dt.year, y=df['value'], ax=ax1)
  ax1.set_xlabel('Year')
  ax1.set_ylabel('Page Views')
  ax1.set_title('Year-wise Box Plot (Trend)')

  ax2 = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax2)
  ax2.set_xlabel('Month')
  ax2.set_ylabel('Page Views')
  ax2.set_title('Month-wise Box Plot (Seasonality)')




  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
