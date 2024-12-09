# Sentiment_Analysis_Chatbot_using_NLTK_TextBlob

This project demonstrates a simple sentiment analysis chatbot that analyzes the user's mood based on their input and provides contextual responses. It uses natural language processing (NLP) techniques such as tokenization, lemmatization, and sentiment analysis to interpret the sentiment of user text.

---

## Features

- **Text Preprocessing**:
  - Tokenization: Splits user input into individual words.
  - Lemmatization: Converts words to their base forms while preserving their contextual meaning.
  - Spell Correction: Automatically corrects spelling errors in user input.

- **Sentiment Analysis**:
  - Determines the sentiment polarity of the user input (positive, neutral, or negative).
  - Polarity is used to gauge the mood of the user.

- **Dynamic Responses**:
  - Provides appropriate responses for positive, neutral, and negative sentiments.

---

## Requirements

Make sure you have the following Python libraries installed:

- `textblob`
- `nltk`

Install all required libraries with:
```pip install -r requirements.txt```

---

## Example Interaction

-----------------------------------------------------------------------
Welcome to the Sentiment Analysis Chatbot! Type 'exit' to end the chat.
-----------------------------------------------------------------------

You: I'm feeling great today!
__________________________________________________

Chatbot: Awesome! You're in a good mood today! 🌟
__________________________________________________

You: I am a bit sad right now.
__________________________________________________

Chatbot: I'm sorry to hear that. 😔
__________________________________________________

You: exit
__________________________________________________

Chatbot: Goodbye!
__________________________________________________
---

 
