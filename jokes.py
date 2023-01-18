import requests
from bs4 import BeautifulSoup
import tweepy
import random
import schedule
import time

# List of websites to scrape jokes from
joke_sites = [
    "https://www.jokes4us.com/cleanjokes.html",
    "https://www.laughfactory.com/jokes/clean-jokes",
    "https://www.rd.com/joke/clean-jokes/",
    "https://www.funnycleanjokes.net/",
    "https://www.jokesoftheday.net/clean-jokes",
    "https://www.short-funny.com/clean-jokes.php"
]


def scrape_jokes():
    jokes = []
    for site in joke_sites:
        page = requests.get(site)
        soup = BeautifulSoup(page.content, "html.parser")
        # find all the jokes on the website
        site_jokes = soup.find_all("div", class_="content")
        jokes.extend(site_jokes)
    return jokes


def post_joke(joke):
    # Insert your Twitter API keys here
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Post the joke to Twitter
    api.update_status(joke)


def job():
    jokes = scrape_jokes()
    post_joke(random.choice(jokes))


schedule.every().day.at("12:00").do(job)
schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
