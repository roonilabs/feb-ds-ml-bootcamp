# Research Assignment 1: Introduction to Machine Learning

## 1. Defining Machine Learning
Machine Learning (ML) is a type of artificial intelligence that allows computers to learn from data and improve over time without being specifically programmed for every single task. Instead of following fixed rules, the computer looks for patterns in data to make its own decisions.

**Real-Life Example: Credit Card Fraud Detection**
When you use your credit card, an ML model checks if the purchase fits your usual habits. If you normally buy groceries in your hometown but suddenly spend $2,000 in a different country, the model flags this as an "anomaly" (something unusual) and blocks the card to protect you.


## 2. Supervised vs. Unsupervised Learning
The main difference is whether the computer has a "teacher" (labels) to guide it.

| Feature | Supervised Learning | Unsupervised Learning |
| :--- | :--- | :--- |
| **Concept** | Learning with an answer key. | Learning by finding hidden patterns. |
| **Data Type** | Labeled (Inputs + Correct Answers). | Unlabeled (Inputs only). |
| **Example** | **Spam Filters:** Training a model on emails marked "Spam" or "Inbox." | **Customer Groups:** Grouping online shoppers by their interests automatically. |


## 3. What is Overfitting?
Overfitting happens when a model learns the training data too perfectly—including the random errors and "noise." It's like a student who memorizes a practice test word-for-word but fails the real exam because the questions changed slightly.

* **Causes:** Using a model that is too complex or not having enough training data.
* **Prevention:** We can prevent this by using more data, keeping the model simple, or using "Early Stopping" to finish training before the model starts memorizing noise.


## 4. Training Data vs. Test Data
To make sure a model actually works, we split our data into two parts:
1.  **Training Data (80%):** This is used to teach the model.
2.  **Test Data (20%):** This is the "final exam" used to check how accurate the model is on new data.

**Why split?** If we test the model on the same data it learned from, we won't know if it actually understands the patterns or if it just memorized the answers.


## 5. Case Study: Machine Learning in Business
**Topic:** Amazon’s Recommendation System
**Summary:** Amazon uses "Collaborative Filtering" (a type of ML) to suggest products. By analyzing millions of purchases, the system learns which items are often bought together.
**Findings:** Research shows that these ML recommendations significantly increase sales because they provide a personalized experience for every user, making it easier for customers to find what they need.


## References
* Mitchell, T. (1997). *Machine Learning*. McGraw-Hill.
* Alpaydin, E. (2020). *Introduction to Machine Learning*. MIT Press.
* Esteva, A., et al. (2017). "Dermatologist-level classification of skin cancer." *Nature*.
