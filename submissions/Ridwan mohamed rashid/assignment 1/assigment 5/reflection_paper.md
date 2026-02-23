## **1. What I Implemented**

In this project, I developed a spam detection system using three machine learning models: **Logistic Regression**, **Random Forest**, and **Naive Bayes**. The dataset contained two main columns: the email **Message** and its **Category** (spam or ham). I began by cleaning the data, converting missing messages to empty strings, and mapping the labels into numeric form—`0` for spam and `1` for ham.
After preparing the data, I applied **TF-IDF vectorization** to transform the text messages into numerical features suitable for machine learning models. I then trained the three models and evaluated their performance using accuracy, precision, recall, and F1-score.



## **2. Comparison of the Models**

The three models performed differently during testing.
**Logistic Regression** was stable and gave a good balance between accuracy and recall.
**Random Forest** performed well but sometimes misclassified short messages because tree-based models can struggle with very sparse text features.
**Naive Bayes** was the fastest and surprisingly strong, especially for detecting spam, because it works well with word-frequency-based features.

When I tested the system with single messages (sanity check), each model responded slightly differently. For example, promotional messages like *“Congratulations! You won a prize”* were correctly flagged as spam by all models. Normal conversation messages were consistently labeled as ham.
Overall, Naive Bayes gave the most realistic results for short messages, but Logistic Regression had the most balanced performance.


## **3. Understanding Random Forest**

Random Forest is an **ensemble learning method** that builds many decision trees during training. Instead of relying on one tree, the model combines the predictions of all trees and uses the majority vote (classification) or average (regression) to make a final prediction.
This reduces the risk of overfitting, since the randomness in selecting data samples and features helps the model generalize better. In text classification, however, the high dimensionality of TF-IDF sometimes limits the effectiveness of tree-based methods.


## **4. Metrics Discussion**

After comparing the evaluation metrics:

* **Logistic Regression** generally achieved high accuracy and good precision.
* **Naive Bayes** had excellent recall for spam messages, meaning it rarely missed true spam.
* **Random Forest** had decent accuracy but was not the best at handling sparse text features.

These results show that Logistic Regression is strong at handling TF-IDF features, while Naive Bayes excels when dealing with word probabilities. Random Forest, although powerful on numerical datasets, is less efficient for high-dimensional text data.


## **5. Personal Findings**

In conclusion, I found Logistic Regression to be the best overall model for this spam detection task. It offered a strong balance across all metrics and produced stable predictions. Naive Bayes, even though simple, performed surprisingly well and would be ideal for fast, lightweight applications.
This project helped me understand how different machine learning algorithms behave with text data, and how preprocessing steps like TF-IDF can significantly influence model performance. It also reinforced the importance of comparing multiple models before choosing the best one.