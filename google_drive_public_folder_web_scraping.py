import requests
import pandas as pd
from io import StringIO


url = "https://drive.google.com/uc?export=download&id=1PZWSBl3rb9afQwKu3KHf2rpHVJ5Ou-Jd"
response = requests.get(url)
lines = response.text.splitlines()

# for i, line in enumerate(lines[:5]):
#     print(f"Line {i+1}: {line[:200]}")  # print first 200 chars of each line
df = pd.read_csv(StringIO(response.text))
print(df.head())

# During scraping, it was observed that Google Drive dynamically renders file listings using JavaScript, 
# which prevents extraction via requests and BeautifulSoup. As a result, the dataset was accessed 
# through its publicly available CSV export endpoint to ensure reliable and ethical data collection.