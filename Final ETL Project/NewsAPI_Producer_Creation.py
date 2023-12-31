# -*- coding: utf-8 -*-
"""NewsAPI_Producer.Creation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffU2vdapKws1BnooyM-NWesssbVT-8n1

# News API
This API can get news articles from different sources and different topics.

---


Documentation for Python API can be found at:
https://github.com/mattlisiv/newsapi-python
"""

'''
You do need to install following packages using pip package manager
pip install newsapi
pip install newsapi-python
pip install kafka-python
'''
from newsapi import NewsApiClient
import json
from kafka import KafkaProducer
from datetime import datetime

# Get your free API key from https://newsapi.org/, just need to sign up for an account
key = "020c47b8af024288aa64775a57f94ce8"

# Initialize api endpoint
newsapi = NewsApiClient(api_key=key)

# Define the list of media sources
sources = 'bbc-news,cnn,fox-news,nbc-news,the-guardian-uk,the-new-york-times,the-washington-post,usa-today,independent,daily-mail'

# /v2/everything
all_articles = newsapi.get_everything(q='france',
                                      sources=sources,
                                      language='en')

# Function to clean article data
def clean_article(article):
    # Add data cleaning logic here
    # Remove special characters or unwanted elements
    cleaned_title = article['title'].encode('ascii', 'ignore').decode('utf-8')  # Remove non-ASCII characters

    # Handle null or missing values
    cleaned_author = article.get('author', 'Unknown')  # Replace missing author with 'Unknown'

    # Example: Convert timestamp to a more readable format
    published_at = article.get('publishedAt')
    cleaned_published_at = None
    if published_at:
        cleaned_published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
        
    # Add data cleaning logic here
    # Remove special characters or unwanted elements
    cleaned_description = article['description'].encode('ascii', 'ignore').decode('utf-8')  # Remove non-ASCII characters

    # Create a new dictionary with cleaned data
    cleaned_article = {
        'title': cleaned_title,
        'author': cleaned_author,
        'publishedAt': cleaned_published_at,
        'description': cleaned_description
    }

    return cleaned_article

# Print the titles of the articles
for article in all_articles['articles']:
    cleaned_article = clean_article(article)
    print(cleaned_article['title'])
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('vidhya-my-news', json.dumps(cleaned_article).encode('utf-8'))