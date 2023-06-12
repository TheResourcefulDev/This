#!usr/bin/python
import this
import codecs
from VADER_SENTIMENT import *
print('')
print('>>> Your Python Journey start\'s here.. ...')
import __hello__
# imports and prints """Hello World!"""

SAVE_FILE_PATH = './this.txt'

def get_rot13_decode(rot13_text, ALPHA, ASCII_letters):
    """
    Decode a string using the ROT13 cipher.
    A simple letter substitution cipher that replaces
    the letters with the 13th letter after repeating alphabetically.
    Args:
        rot13_text (str): The string to be decoded.
    Returns:
        str: The decoded string.
    """
    decoding = {}
    for c in (65, ASCII_letters):
        for i in range(ALPHA+1):
            decoding[chr(i+c)] = chr((i+13) % (ALPHA+1) + c)
    decode_1 = "".join([decoding.get(c, c) for c in rot13_text])
    print('MANUAL rot-13 Decode Complete!')
    return decode_1

def get_codecs_decode(rot13_text, DECODER='rot-13'):
    """
    This function uses the `codecs.decode` function from the
    `codecs` module to perform decoding
    on the given string using the ROT13 cipher.
    Args:
        rot13_text (str): The string to be decoded.
    Returns:
        str: The decoded string.
    """
    decoding_2 = codecs.decode(rot13_text, DECODER)
    print('CODECS MODULE Decode Complete!')
    return decoding_2

def main():
    global ASCII_letters
    rot13_text = this.s
    ASCII_letters = this.c
    ALPHA = this.i
    findme = this.d

    # Input sets DECODER - defult = rot-13
    DECODER = input("Choose Decoder {Leave blank for defult = rot-13}")
    if DECODER == '':
        DECODER = 'rot-13'
    elif DECODER == 'd':
        print(findme)
    print(f"Decoder loading : {DECODER}")

    # decodes text using Manual Python, returns decoded text
    decoding_1 = get_rot13_decode(rot13_text, ALPHA, ASCII_letters)

    # decodes text using built in Python codecs module, returns decoded text
    decoding_2 = get_codecs_decode(rot13_text,DECODER)

    # compares decodes and returns
    try:
        assert decoding_1 == decoding_2
        print('Comapring Manual decode.. ...')
        print(f"Match : {decoding_1 == decoding_2}")
        
        with open(SAVE_FILE_PATH, 'w+') as pythonic:
            pythonic.write(decoding_1)

        print(f"Your file has been saved : {SAVE_FILE_PATH}")
    except:
        print('Failed.....')
        print('No file saved.')

    # runs sentiment analysis on by loading the saved text, returns line by line results
    analysis_result = analyze_text_file(SAVE_FILE_PATH)

    # assigns and prints analysis results label
    sentiment_label = get_overall_sentiment_label(analysis_result['sentiment_scores'])

    print("\nIndividual Sentence Scores:")
    for i, sentence in enumerate(analysis_result['sentences'], start=1):
        print(f"Sentence {i}: {sentence['text']}")
        print("Sentiment scores:", sentence['scores'])
        print()
    print("Overall Sentiment Scores:", analysis_result['sentiment_scores'])
    print("Sentiment Scale : \n Very Negative \n Negative \n  Neutral \n    Positive \nVery Positive")
    print(f"The Statement Sentiment is : {sentiment_label}")

if __name__ == '__main__':
    main()
