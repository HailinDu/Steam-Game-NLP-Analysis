from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
 
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df = pd.read_csv('update.csv')
    df = df.dropna()

    X = df['Review_StopWord']
    y = df['Recommend']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=222)
    tvectorizer = TfidfVectorizer(strip_accents='ascii', token_pattern=r'(?u)\b\w\w+\b', stop_words='english')
    X_train_tvectorizer = tvectorizer.fit_transform(X_train)
    X_test_tvectorizer = tvectorizer.transform(X_test)

    # LogReg model
    lgr = LogisticRegression(max_iter=2000)
    lgr.fit(X_train_tvectorizer, y_train)
    predict = lgr.predict(X_test_tvectorizer)
 
    #Alternative Usage of Saved Model
    # joblib.dump(clf, 'NB_spam_model.pkl')
    # NB_spam_model = open('NB_spam_model.pkl','rb')
    # clf = joblib.load(NB_spam_model)
    
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        testing_vec = tvectorizer.transform(data)
        my_prediction = lgr.predict(testing_vec)
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
    app.run(debug=True)