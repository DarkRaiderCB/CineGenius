import joblib
import streamlit as st
import pandas as pd
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
nltk.download('punkt')

model = joblib.load('svc_model2.joblib')
vectorizer = joblib.load('vectorizer.joblib')


def cleaned(text):
    """
    function for cleaning text and tokenizing
    parameters: text (str)
    return: cleaned text (str)
    """
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower().strip()
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    stemmer = SnowballStemmer('english')
    filtered_words = [stemmer.stem(word) for word in filtered_words]
    return ' '.join(filtered_words)


def prediction(model, test):
    if model.predict(test) == 1:
        return "spam"
    else:
        return "ham"


encoded_labels = {
    0: "action",
    1: "adult",
    2: "adventure",
    3: "animation",
    4: "biography",
    5: "comedy",
    6: "crime",
    7: "documentary",
    8: "drama",
    9: "family",
    10: "fantasy",
    11: "game-show",
    12: "history",
    13: "horror",
    14: "music",
    15: "musical",
    16: "mystery",
    17: "news",
    18: "reality-tv",
    19: "romance",
    20: "sci-fi",
    21: "short",
    22: "sport",
    23: "talk-show",
    24: "thriller",
    25: "war",
    26: "western"
}


def get_genre(encoded_value):
    return encoded_labels.get(encoded_value, "Genre")


def prediction(model, test):
    res = model.predict(test)
    genre = get_genre(res[0])
    return genre


# Streamlit app
st.title("CineGenius - Your Movie Genre Classifier")

user_input = st.text_area("Enter plot description:")

if st.button("Classify"):
    if user_input:
        ctest = cleaned(user_input)
        ctest = pd.Series([ctest])
        ctest = vectorizer.transform(ctest)

        result = prediction(model, ctest)

        st.write(f"The movie is classified as: **{result}**")
    else:
        st.warning("Please enter a description text to classify.")
