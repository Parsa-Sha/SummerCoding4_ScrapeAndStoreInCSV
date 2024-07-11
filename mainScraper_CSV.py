from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

web = 'https://www.audible.ca/search'
path = 'C:/Files/Code_Actually/ScrapeAndStore/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)

products = driver.find_elements(by='xpath', value='//li[contains(@class, "productListItem")]')


book_title = []
book_author = []
book_length = []


for product in products:
    book_title.append(product.find_element(by='xpath', value='.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(by='xpath', value='.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(by='xpath', value='.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)
