import pandas as pd
import numpy as np
import requests
import BeautifulSoup
import matplotlib.pyplot as plt

def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))

	#getting data from the website for stock price history records
	url = 'http://www.nasdaq.com/symbol/'+stock+'/historical'
	response = requests.get(url)
	html_content = response.content
	soup = BeautifulSoup.BeautifulSoup(html_content)

	#getting table rows from the html content
	stock_data =[]
	rows = soup.findAll('tbody')[-1].findAll('tr')[1:]

	#seperating table data and appending into a list
	for row in rows:
		cols = row.findAll('td')
		cols = [element.text.strip() for element in cols]
		stock_data.append([element for element in cols if element])

	#building Dataframe
	df = pd.DataFrame(stock_data,columns=['date','openp','highp','lowp','closep','volume'])
        import ipdb;ipdb.set_trace()
	#plotting the closing stock price w.r.t date
	x = df['date']
	y = df['closep']

	ax1.plot_date(x,y,'-', label='Price')
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.grid(True)

	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09,bottom=0.20,right=0.94,top=0.90,wspace=0.2, hspace=0)
	plt.show()

graph_data('infy')
