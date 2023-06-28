# Dapatkan html dengan python

import requests as re

response = re.get ('https://www.nissan.com.kh/news.php?id=15')
html = response.text

print(html) 