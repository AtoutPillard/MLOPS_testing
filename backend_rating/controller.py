import numpy as np
import model as md
import joblib
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import sklearn, xgboost # Do not remove

# Download if necessary nltk ressources
for res_name, res_path in md.nltk_ressources.items():
    try:
        nltk.data.find(res_path)
    except LookupError:
        nltk.download(res_name)

def __loader(path):
    """
    Load files

    Params:
    -------
        path: str, path to the file to load
    
    Return:
    -------
    the loaded file
    """
    return joblib.load(path)

var = {
    k: __loader(path) for k, path in md.paths.items()
}
var["stopwords"] = set(stopwords.words('english'))


def __process_text(text):
    """
    Transform a given text into a list of token without stop word

    Params:
    -------
        text: str, text to convert

    Return:
    -------
    list[string], list of token in the text without stop words
    """
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if not token in var["stopwords"]]
    return tokens

def __preprocessing(request):
    """
    Apply preprocessing given anime informations

    Params:
        - request: flask.request
    
    Return:
        sparse matrix of type '<class 'numpy.float64'>'
    """
    # LOAD
    data = request.form
    if len(request.form)==0:
        data = request.json

    df = pd.DataFrame({
        k: [data[k]]
        for k in data.keys()
    })

    # TRANSFORM

    ## Missing values

    ## Handle missing values, discard stop words
    for col in list(set(md.single_value_cols).intersection(df.columns)):
        df[col] = df[col].fillna("").apply(__process_text)

    for col in list(set(md.list_value_cols).intersection(df.columns)):
        df[col] = df[col].fillna("['']").astype(str).apply(lambda x: eval(x))
    
    # Concatenate all columns
    df["txt"] = df[df.columns[0]]
    for col in df.columns[1:]:
        df["txt"] += df[col]

    # Transform the content from list[string] --> string
    df["txt"] = df["txt"].apply(lambda x: " ".join(x).lower())

    # Transform string to vec and return
    return var["vectorizer"].transform(df["txt"])

def predict_rating(request):
    """
    Return a rating prediction based on the anime details
    
    Params:
    -------
        request : flask.request
    
    Return:
        float
    """
    ## Apply preprocessing
    X = __preprocessing(request)
    
    ## Make prediction
    res = var["model"].predict(X)

    ## Format and return
    return round(res[0].item(),1)
