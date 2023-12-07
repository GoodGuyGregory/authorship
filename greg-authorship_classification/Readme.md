## Authorship

For this project I used some common sense strategies for determining the authorship. I leaned heavily on the **feature selection** tools within scikit learn
from a **TfidVectorizer** which is basically a *Bag of Words* approach but with more fine tuning to determine frequency of more insightful words. I basically fed the texts of each author
into a simple open and read slicer. 

The process reads the files contents and splits each line into a paragraph using a regex character `\n\n` and inserts that paragraph
seperated text into a list of paragraphs from that author. I made a decision to train the model with each of these text paragraphs.
I dictated the model to train against my preferred author of the two Mary Shelly. To do this I used a binary classification for each paragraph from both authors.
I dictated the paragraphs into a dictionary **textData** which features an appended text with it's expected label of `'0'` for a Jane Austen text paragraph and a `'1'` for 
a Mary Shelly paragraph. 

Once the `textData` dictionary was classified and labeled it is ready to be converted into a dataframe of the contents to then be split with the sklearn method
`train-test_split` this was composed of a test and training split of 30% testing and 70% training data to prevent over fitting.

after it has been trained against the data from both authors. I was able to produce the vectorizer which represents the `TfidVectorizer` I took the liberty of spicing it up by adding a few parameters to give it more 
insight into word selection and feature creation. I set the feature limit within the data to be around  features 150 and a max_df of 0.90 meaning it will look at words that are rarer in each text paragraph roughly a 10% for a more
unique feature selection. I played with this parameter and was able to see accuracy of 70 for Shelly around 10% or `0.10` increasing seemed to have allowed a higher precision against Jane Austen.

I was able to then fit the training data from the `X_train` and `x_test` data to the vectorizer and then fit the DecisionTreeClassifier to 
the predict test data fom the X_test_vectorization

I used the classification_report and accuracy_score methods against the test data to produce a decent looking precision and accuracy rating for the learner.

**Running The Program**

all files included in the .zip must be in the same working directory for the project.

Install the appropriate packages with **pip** this might vary on your machine as there might be a different 
call to pip if you're using `python3` you might have to run **pip3** within the working directory of the project.


```shell
pip install sklearn
pip install pandas
pip install re
``` 

running the application. change directories into the folder containing the python code and the sanitized text files.
it is highly possible that you might have to use `python3 authorship.py` instead of simply `python authorship.py`

Let me know if you have any questions, trouble

Greg



**Resources**

[Text Files in SciKitLearn ](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

[TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)

[Comparisons in SciKitLearn Performance with Text Vectors](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
