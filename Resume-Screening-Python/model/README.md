Model artifacts for Resume-Screener

Files:
- `clf.pkl` — trained classifier (pickle format)
- `tfidf.pkl` — TF-IDF vectorizer (pickle format)

Usage example (Python):
```python
import joblib
clf = joblib.load('clf.pkl')
tfidf = joblib.load('tfidf.pkl')
``` 

Note: This folder intentionally excludes the training dataset. Ensure you have the appropriate license/consent to publish the model files.