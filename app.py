"""
The provided Python code defines functions for preprocessing text data using nltk and performing sentiment
analysis using TextBlob, with an example interaction loop for a sentiment analysis chatbot.

:param text: The `text` parameter in the code refers to the input text that the user provides during
the interaction with the Sentiment Analysis Chatbot. This text is processed and analyzed for
sentiment using the TextBlob library and various natural language processing techniques like
tokenization, lemmatization, correction and sentiment analysis
:return: The `analyze_sentiment` function returns two values:
1. `polarity`: A numerical value representing the sentiment polarity of the input text.
3. `response`: A string response generated based on the sentiment polarity of the input text.
"""



from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random

# Preprocessing user input
def preprocess_text(text):
    tokens = word_tokenize(text.lower()) # Tokenizing and converting the input text to lower case 
    
    lemmatizer = WordNetLemmatizer() # Initializing lemmatizer
    
    lemmatized_tokens = [
        lemmatizer.lemmatize(word) for word in tokens if word.isalnum() # lemmatizing tokens (pens->pen) keeping contextual meaning, not changing tags
    ]
    
    preprocessed_sentence = " ".join(lemmatized_tokens) # Reconstructing the sentence from lemmatized tokens for contextual understanding
    # print(preprocessed_sentence)
    
    return preprocessed_sentence

# Sentiment Analysis
def analyze_sentiment(text):
    preprocessed_text = preprocess_text(text)  # Preprocessing the input text
    blob = TextBlob(preprocessed_text)  # Creating a TextBlob object
    blob=blob.correct() # Corrects spelling errors
    # print(blob)
    polarity = blob.sentiment.polarity  # Calculate polarity (Represents the sentiment's overall positivity or negativity.)

    positive_responses = [
        "That sounds great! 😊",
        "I'm happy to hear that! Keep it up! 😄",
        "Awesome! You're in a good mood today! 🌟"
    ]

    negative_responses = [
        "I'm sorry to hear that. 😔",
        "That doesn't sound good. Want to talk about it? 😢",
        "Oh no! Things will get better soon. 🙏"
    ]

    neutral_responses = [
        "Got it. Let's see what else we can talk about. 🤔",
        "Okay, Tell me more. 😊",
        "Hmm, Got it. Thanks for sharing. 😊"
    ]

    # Generate response based on polarity
    if polarity > 0:
        response = random.choice(positive_responses) 
    elif polarity < 0:
        response = random.choice(negative_responses) 
    else:
        response = random.choice(neutral_responses) 
    
    return polarity, response

# Interaction
if __name__ == "__main__":
    print("")
    print("-----------------------------------------------------------------------")
    print("Welcome to the Sentiment Analysis Chatbot! Type 'exit' to end the chat.")
    print("-----------------------------------------------------------------------")

    while True:
        print("")
        user_input = input("[You]: ")
        print("__________________________________________________")
        print("")

        if user_input.lower() == "exit":
            print("[Chatbot]: Goodbye!")
            print("__________________________________________________")
            break
        
        polarity, response = analyze_sentiment(user_input)
        # print(f"Polarity: {polarity}")
        print(f"[Chatbot]: {response}")
        print("__________________________________________________")
