import requests
from bs4 import BeautifulSoup

url_file = 'urls.txt'


def fetch_article(url):
  response = requests.get(url)
    # Code 200 means OK, we can consider anything else an error for this project
  if response.status_code != 200:
    print("Failed to retrieve the article")
    # Since we are reading a list of wiki pages return non so we don't get an error later on
    return None
  return response


def clean_webpage(webpage):
  soup = BeautifulSoup(webpage.content, 'html.parser')
# IDS are meant to the unique, so finding by id should give us the right element
  content = soup.find(id="mw-content-text")
  title = soup.find(id="firstHeading").get_text()
  
  
  if content:
    paragraphs = content.find_all('p')
    text = "\n".join([para.get_text().strip() for para in paragraphs])

    return title, text


def read_urls(file):
  with open(file, "r") as file:
    lines = file.readlines()
    file.close()
  return lines


def save_article(article, title, url):
    # encoding ensusres the file is writen in the right format, can be found in head of html
  with open("articles.txt", "a",encoding="utf-8") as file:
    file.write(f"Title:{title} URL:{url}\n")
    file.write(article)
    file.write("\n\n" + "=" * 80 + "\n\n")


def main():
  urls = read_urls(url_file)
  for url in urls:
    print(url)
    wiki_page = fetch_article(url.strip())
    # Since the fetch_article return None we can use an if statment to skip urls that didn't work
    if wiki_page:
        title, text = clean_webpage(wiki_page)
        save_article(text, title, url)


main()


