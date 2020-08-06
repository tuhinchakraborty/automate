import os
from dotenv import load_dotenv
from twilio.rest import Client
import schedule
import requests
from bs4 import BeautifulSoup

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
from_whatsapp_number = os.environ['TWILIO_NUMBER']
to_whatsapp_number = os.environ['WHATSAPP_RECEIVER_NUMBER']
WIKIPEDIA_BASE_URL = os.environ['WIKIPEDIA_BASE_URL']
WIKIPEDIA_MAIN_PAGE = os.environ['WIKIPEDIA_MAIN_PAGE']


def get_featured_article():
    req = requests.get(WIKIPEDIA_BASE_URL + WIKIPEDIA_MAIN_PAGE)
    soup = BeautifulSoup(req.content, "html.parser")
    span = soup.find(id="From_today's_featured_article")
    feature_article_header = span.parent
    feature_article_body = feature_article_header.findNext('div')
    return feature_article_body.findNext('p').findNext('a')['href']


def send_message():
    message = """From today's featured article\n""" + WIKIPEDIA_BASE_URL + get_featured_article()
    print(message)
    client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)


send_message()
