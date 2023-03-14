import json

import nltk
from textblob import TextBlob

nltk.data.path.append(".")


def get_data(review):
    blob = TextBlob(review)
    sentiments = 'POSITIVE' if blob.sentiment.polarity > 0 else 'NEGATIVE'
    tags = blob.tags

    return sentiments, tags

def get_aspect(review):
    blob = TextBlob(review)
    aspects = []
    # Loop over each sentence in the review
    for sentence in blob.sentences:
        # Loop over each word and its part-of-speech tag in the sentence
        for word, pos in sentence.tags:
            # If the word is an adjective or adverb, consider it an aspect
            if pos.startswith('JJ') or pos.startswith('RB'):
                aspect = word.lower()
                # Perform sentiment analysis on the aspect using TextBlob
                sentiment = 'POSITIVE' if TextBlob(aspect).sentiment.polarity > 0 else 'NEGATIVE'
                # Add the aspect and its sentiment score to the list of aspects
                score = TextBlob(aspect).sentiment.polarity
                # Append the aspect and its sentiment score to the list of aspects
                aspects.append({'aspect' : aspect, 'sentiment' : sentiment, 'score' : score})
    
    return aspects

def lambda_handler(event, context):
    if event and 'body' in event:
        reviews = event['body']
        print("data input", reviews)

        if isinstance(reviews, str) and reviews.startswith("{"):
            reviews = json.loads(reviews)["body"]
        
        sentiments = []
        tags = []
        aspects = []
        if not isinstance(reviews, list):
            sentiments, tags = get_data(reviews)
            aspects = get_aspect(reviews)
        else:
            for rev in reviews:
                sentiment, tag = get_data(rev)
                aspect = get_aspect(rev)
                sentiments.append(sentiment)
                tags.append(tag)
                aspects.append(aspect)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'sentiment': sentiments,
                'tags': tags,
                'aspects': aspects
            }),
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'No review provided'
            }),
        }