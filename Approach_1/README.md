# Building a Chatbot Using Natural Language Processing (NLP) and Deep Neural Networks (DNN)

## Introduction

In this approach, we will explore how to build a chatbot using Natural Language Processing (NLP) and Deep Neural Networks (DNN) in Python. Chatbots are computer programs that can simulate human conversation and provide automated responses to user queries. NLP allows the chatbot to understand and interpret human language, while DNN enables the chatbot to learn and generate appropriate responses.

## Key Concepts

Before diving into the code, let's understand some key concepts related to building a chatbot using NLP and DNN:

- **Natural Language Processing (NLP):** NLP is a subfield of artificial intelligence that focuses on the interaction between computers and human language. It involves tasks such as text tokenization, stemming, and sentiment analysis to understand and process human language.

- **Deep Neural Networks (DNN):** DNN is a type of artificial neural network that consists of multiple layers of interconnected nodes. It is used for complex pattern recognition and learning tasks. In the context of chatbots, DNNs can be trained to understand and generate human-like responses.

- **Tokenization:** Tokenization is the process of breaking down a text into individual words or tokens. It is an essential step in NLP as it allows the chatbot to understand the meaning of each word in a sentence.

- **Stemming:** Stemming is the process of reducing words to their base or root form. It helps in reducing the dimensionality of the vocabulary and improves the efficiency of the chatbot's language processing.

- **Bag of Words:** Bag of Words is a feature engineering technique that represents text data as a numerical vector. It creates a vocabulary of unique words and assigns a binary value (1 or 0) to each word based on its presence or absence in a given sentence.

- **Spelling Correction:** Spelling correction is a crucial aspect of chatbot development. It ensures that the chatbot can handle user queries with spelling errors by suggesting the correct spelling or word.

## Code Structure

The code provided follows a specific structure to build the chatbot. Let's break down the code structure into different sections:

- **Preprocessing Data:** This section involves loading and preprocessing the data required for training the chatbot. The code reads the intents from a JSON file and performs tokenization, stemming, and bag of words feature engineering on the patterns and tags.

- **Model Building:** In this section, the code defines and trains the DNN model using the preprocessed training data. The model architecture consists of input layers, fully connected layers, and a softmax activation function for multi-class classification.

- **Input Preprocessing:** This section includes functions for preprocessing user input. The `bag_of_words` function converts the user input into a numerical vector using the bag of words technique. The `words_to_list` function splits the input sentence into individual words and removes duplicates.

- **Spelling Correction:** The code includes a function `word_checker` that checks the spelling of words in the user input. It compares the words with a vocabulary list and suggests corrections using the `difflib` library.

- **Chat Function:** The `chat` function is the main function that simulates the conversation between the user and the chatbot. It prompts the user for input, preprocesses the input, predicts the intent using the trained model, and generates appropriate responses based on the predicted intent.

## Advantages and Disadvantages

### Advantages:

- **Faster Responses:** Chatbots built using NLP and DNN technology can provide quicker responses to user queries, improving user satisfaction.

- **Ease of Building, Low Memory Consumption:** These chatbots are relatively easy to build and consume less memory compared to more complex AI models.

### Disadvantages:

- **Risk of Providing Incorrect Information:** If the necessary information is not present in the predefined intents, the chatbot may provide inaccurate or irrelevant information to users.

- **Data Requirement:** Building effective NLP and DNN-based chatbots requires access to large amounts of text data, which can be challenging to acquire and prepare.

- **Rule-Based Nature:** These chatbots are somewhat rule-based, which means they rely on predefined patterns and responses, and may not handle entirely novel queries well.

# Code Explaination

## Preprocessing Data

```python
for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        for item in wrds:
            words.extend(wrds)
            docs_patt.append(wrds)
            docs_tag.append(intent['tag'])
            if intent['tag'] not in labels:
                labels.append(intent['tag'])
```
In this code snippet, the patterns from the intents are tokenized using the nltk.word_tokenize function. The words, patterns, and tags are then stored in separate lists for further processing. The unique tags are added to the labels list.

## Model Building

```python
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net)
```
This code snippet defines the architecture of the DNN model using the tflearn library. The input layer is defined with the shape of the training data. Fully connected layers are added with 8 nodes each, and the output layer is defined with the number of unique labels and a softmax activation function. The model is then initialized using the tflearn.DNN class.

## Chat Function

```python
def chat():
    print("BOT: Hi! I am your personal bot. I am here to answer queries on DBATU")
    while True:
        inp = input('User: ')
        if inp.lower() == 'quit' or inp is None:
            break
            
        inp_x = word_checker(inp)
        results = model.predict([bag_of_words(inp_x, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] >= 0.9:
            for tg in data['intents']:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    ms = random.choice(responses)
                    print('BOT: {}'.format(ms))
                    
        else:
            print("BOT: Sorry, I don't know how to answer that yet")
```
This code snippet defines the chat function that simulates the conversation between the user and the chatbot. It starts by printing a welcome message and then enters a loop to continuously prompt the user for input. The user input is preprocessed using the word_checker function to correct any spelling errors. The model predicts the intent based on the preprocessed input, and if the confidence score is above a certain threshold (0.9), a random response from the corresponding intent is generated and displayed. If the confidence score is below the threshold, a default response is displayed.
