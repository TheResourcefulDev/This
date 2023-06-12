import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def analyze_sentiment(text):
    """
    Perform sentiment analysis on the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing sentiment scores.

    Example:
        >>> analyze_sentiment("VADER is smart, handsome, and funny.")
        {'neg': 0.0, 'neu': 0.217, 'pos': 0.783, 'compound': 0.8316}
    """
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    return ss


def analyze_text_file(file_path):
    """
    Perform sentiment analysis on a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        dict: A dictionary containing sentiment scores for the entire text.

    Example:
        >>> analyze_text_file("example.txt")
        {
            'sentiment_scores': {'neg': 0.286, 'neu': 0.571, 'pos': 0.143, 'compound': -0.6486},
            'sentences': [
                {'text': 'VADER is smart, handsome, and funny.', 'scores': {'neg': 0.0, 'neu': 0.217, 'pos': 0.783, 'compound': 0.8316}},
                {'text': 'Today sux', 'scores': {'neg': 0.714, 'neu': 0.286, 'pos': 0.0, 'compound': -0.3612}},
                ...
            ]
        }
    """

    with open(file_path, 'r') as file:
        text = file.read()

    sentences = tokenize.sent_tokenize(text)
    sid = SentimentIntensityAnalyzer()

    sentiment_scores = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    sentence_scores = []

    for sentence in sentences:
        scores = sid.polarity_scores(sentence)
        sentence_scores.append({'text': sentence, 'scores': scores})

        sentiment_scores['neg'] += scores['neg']
        sentiment_scores['neu'] += scores['neu']
        sentiment_scores['pos'] += scores['pos']
        sentiment_scores['compound'] += scores['compound']

    total_sentences = len(sentences)
    sentiment_scores['neg'] /= total_sentences
    sentiment_scores['neu'] /= total_sentences
    sentiment_scores['pos'] /= total_sentences
    sentiment_scores['compound'] /= total_sentences

    result = {
        'sentiment_scores': sentiment_scores,
        'sentences': sentence_scores
    }

    return result

def get_overall_sentiment_label(sentiment_scores):
    """
    Get the overall sentiment label based on sentiment scores.

    Args:
        sentiment_scores (dict): A dictionary containing sentiment scores.

    Returns:
        str: The overall sentiment label.

    Example:
        >>> scores = {'neg': 0.0, 'neu': 0.217, 'pos': 0.783, 'compound': 0.8316}
        >>> get_overall_sentiment_label(scores)
        'Very Positive'
    """
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.5:
        return "Very Positive"
    elif compound_score >= 0.05:
        return "Positive"
    elif compound_score > -0.05:
        return "Neutral"
    elif compound_score > -0.5:
        return "Negative"
    else:
        return "Very Negative"



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path as a command-line argument.")
    else:
        file_path = sys.argv[1]
        analysis_result = analyze_text_file(file_path)

        sentiment_label = get_overall_sentiment_label(analysis_result['sentiment_scores'])


        print(f"Sentiment analysis for {file_path}:\n")
        print("Overall Sentiment Scores:", analysis_result['sentiment_scores'])
        print(" - Very Negative < Negative = Neutral = Positive > Very Positive - ")
        print(f"The Sentiment is : {sentiment_label}")
        print("\nIndividual Sentence Scores:")
        for i, sentence in enumerate(analysis_result['sentences'], start=1):
            print(f"Sentence {i}: {sentence['text']}")
            print("Sentiment scores:", sentence['scores'])
            print()

        print(f"Sentiment analysis for {file_path}:\n")
        print("Overall Sentiment Scores:", analysis_result['sentiment_scores'])
        print(" - Very Negative < Negative = Neutral = Positive > Very Positive - ")
        print(f"The Sentiment is : {sentiment_label}")