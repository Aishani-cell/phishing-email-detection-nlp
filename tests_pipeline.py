import joblib
from phishing_nlp_detection import clean_text

def test_clean_text_basic():
    s = "Hello, this is a test: click http://bad.link"
    cleaned = clean_text(s)
    assert "http" not in cleaned
    assert "click" in cleaned

def test_model_saved_and_loadable():
    model = joblib.load('phishing_detector.joblib')
    assert 'vectorizer' in model and 'model' in model
