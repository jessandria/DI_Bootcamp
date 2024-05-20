import pandas as pd
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')


chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))


plt.scatter(chipo['item_price'], chipo['quantity'])


plt.title('Relationship between Price of Items and Quantity Ordered')
plt.xlabel('Item Price ($)')
plt.ylabel('Quantity Ordered')


plt.savefig('price_vs_quantity_scatter.png')


plt.show()
