import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


def main():
    textData = {'text': [], 'label':[]}

    # read in the files from Austen, divide paragraphs into an array of individual values.
    northanger = open('austen-northanger-abbey.txt', encoding="utf8").read().split('\n\n')
    for line in range(len(northanger)):
        northanger[line] = re.sub('\n', ' ', northanger[line])
        textData['text'].append(northanger[line])
        textData['label'].append(0)


    pridePredjudice = open('austen-pride-and-prejudice.txt', encoding="utf8").read().split('\n\n')
    for line in range(len(pridePredjudice)):
            pridePredjudice[line] = re.sub('\n', ' ', pridePredjudice[line])
            textData['text'].append(pridePredjudice[line])
            textData['label'].append(0)

    frankenstein = open('shelley-frankenstein.txt', encoding="utf8").read().split('\n\n')
    for line in range(len(frankenstein)):
        frankenstein[line] = re.sub('\n',' ',frankenstein[line])
        textData['text'].append(frankenstein[line])
        textData['label'].append(1)

    theLastman = open('shelley-the-last-man.txt', encoding="utf8").read().split('\n\n')
    for line in range(len(theLastman)):
        theLastman[line] = re.sub('\n', ' ', theLastman[line])
        textData['text'].append(theLastman[line])
        textData['label'].append(1)

    # build a dataFrame to store all vector data from both authors with unique features
    df = pd.DataFrame(textData)

    #  train with 70% of overall data and 30% testing
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.3)

    vectorizer = TfidfVectorizer(max_df=0.50, max_features=150)
    X_train_vectorizer = vectorizer.fit_transform(X_train)
    X_test_vectorizer = vectorizer.transform(X_test)

    decisionTree = DecisionTreeClassifier()
    decisionTree.fit(X_train_vectorizer,y_train)

    # run a prediction
    y_pred = decisionTree.predict(X_test_vectorizer)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy}*100")
    print(f"Classification Report:\n{report}")




main()