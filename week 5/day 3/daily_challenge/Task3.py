import pandas as pd
import matplotlib.pyplot as plt

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')


item_quantity = chipo.groupby('item_name')['quantity'].sum()


top_items = item_quantity.nlargest(5)

plt.bar(top_items.index, top_items.values)


plt.title('Total Quantity of Top 5 Items')
plt.xlabel('Item Name')
plt.ylabel('Total Quantity')


plt.savefig('top_5_items_quantity_bar.png')

