from pytrends.request import TrendReq
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser' #Setting the browser as the default app to display the graphs

pytrends = TrendReq(hl='en-US', tz=-300)  #Authentication with Google Trends
keyword="trump" #This is the keyword(s) we will use to search for
kw_list=[keyword]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') #Make the search
data = pytrends.interest_over_time()  #Get the interest over time data
data = data.reset_index() 
#Printing of the data on the browser
fig = px.line(data, x="date", y=keyword, title='Keyword Web Search Interest Over Time')
fig.show() 
data.to_csv("data.csv") #Convert our data to CSV and store it