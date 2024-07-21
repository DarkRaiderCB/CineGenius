## CineGenius - Your own movie genre classifier

### Dataset link: <a href='https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb'> Click here </a>

#### Use the app <a href='https://cinegenius.streamlit.app/'>here</a>.

### Hosted with Streamlit

CineGenius is a movie genre classification app that allows users to input a plot description and receive a predicted genre. The application leverages a trained Support Vector Classifier (SVC) model to perform the classification.

## Features

- **User Input:** Enter a plot description of a movie.
- **Classification:** The app classifies the plot description into one of 27 movie genres.
- **Interactive UI:** Built using Streamlit for an easy-to-use interface.

## Requirements

Ensure you have the following dependencies installed:

- joblib
- streamlit
- pandas
- nltk
- scikit-learn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DarkRaiderCB/CineGenius.git
    ```
2. Navigate to the project directory:
    ```sh
    cd cinegenius
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Download NLTK data:
    ```sh
    python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501` to use the application.

### Thanks for visiting!
