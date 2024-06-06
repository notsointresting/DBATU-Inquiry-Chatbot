import requests
from bs4 import BeautifulSoup
from fpdf import FPDF  # Import FPDF
import os

def get_latest_news(url):
    """
    Fetches the latest news from the given URL and returns a list of dictionaries containing:
        - title: The news title
        - link: The URL of the news article
        - date: The date the news was uploaded
    """

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if there's an HTTP error

    soup = BeautifulSoup(response.content, 'html.parser')

    news_articles = soup.find_all('article', class_='exad-post-grid-three exad-col')
    

    news_list = []
    for article in news_articles[:5]:  # Get only the first 5 articles
        title = article.find('h3').find('a').text.strip()
        link = article.find('h3').find('a')['href']
        date = article.find('li', class_='exad-post-date').find('a').text.strip()

        news_item = {
            'title': title,
            'link': link,
            'date': date
        }
        news_list.append(news_item)

    return news_list

def create_pdf(news_list_1, news_list_2, filename):
    """
    Creates a PDF file with the latest news information from both URLs.
    """

    pdf = FPDF()  # Force UTF-8 encoding (if using a newer fpdf version)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # Add news from the first URL
    pdf.cell(0, 10, 'Latest News from https://dbatu.ac.in/students-notice-board/', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    for news in news_list_1:
        pdf.cell(0, 5, f"Title: {news['title']}", 0, 1)
        pdf.cell(0, 5, f"Link: {news['link']}", 0, 1)
        pdf.cell(0, 5, f"Date: {news['date']}", 0, 1)
        pdf.cell(0, 10, '', 0, 1)

    # Add news from the second URL
    pdf.cell(0, 10, 'Latest News from https://dbatu.ac.in/exam-section1/', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    for news in news_list_2:
        pdf.cell(0, 5, f"Title: {news['title']}", 0, 1)
        pdf.cell(0, 5, f"Link: {news['link']}", 0, 1)
        pdf.cell(0, 5, f"Date: {news['date']}", 0, 1)
        pdf.cell(0, 10, '', 0, 1)

    filepath = os.path.join('data', filename)

    pdf.output(filepath, 'F')


def main():
    pdf_name = 'test1.pdf'
    os.remove(pdf_name) if os.path.exists(pdf_name) else None  # Remove the file if it already exists (so i can get the latest news and avoid duplicates)
    url_1 = "https://dbatu.ac.in/students-notice-board/"
    url_2 = "https://dbatu.ac.in/exam-section1/"
    latest_news_1 = get_latest_news(url_1)
    latest_news_2 = get_latest_news(url_2)

    create_pdf(latest_news_1, latest_news_2, 'latest_news.pdf') 

    