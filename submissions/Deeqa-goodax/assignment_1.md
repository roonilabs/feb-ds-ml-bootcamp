# Research Assignment: Introduction to Machine Learning

## 1. Defining Machine Learning
Machine Learning (ML) is a branch of Artificial Intelligence where computers learn patterns from data without being explicitly programmed. Unlike traditional programming, which requires manual "if-then" rules, ML systems use examples to figure out the "rules" or "recipes" on their own.

**Real-Life Example: Email Spam Filtering**
Traditional programs might look for specific words like "lottery." However, ML models like the ones used in Gmail study millions of emails labeled "spam" and "not spam." The model learns complex patterns (sender behavior, link structures, and word frequencies) to automatically filter junk mail, adapting as spammers change their tactics.

---

## 2. Supervised vs. Unsupervised Learning
The distinction between these two methods depends on whether the data provided to the computer includes the "correct answers" (labels).

| Feature | Supervised Learning | Unsupervised Learning |
| :--- | :--- | :--- |
| **Data Nature** | Labeled (Teacher-led) | Unlabeled (Self-discovery) |
| **Goal** | Predict numbers or categories | Find hidden patterns or groups |
| **Key Tasks** | Regression & Classification | Clustering |

* **Supervised Example (Regression):** Predicting house prices based on size and location. The model is trained on houses where the final price is already known.
* **Unsupervised Example (Clustering):** Customer segmentation. A company groups customers by similar shopping habits without knowing the groups in advance.



[Image of supervised vs unsupervised learning]


---

## 3. The Machine Learning Workflow
To build a successful model, practitioners follow a standardized workflow:

1.  **Problem Definition:** Determining if the task is classification, regression, or clustering.
2.  **Data Collection:** Gathering data from sensors, databases, or public repositories.
3.  **Preprocessing:** Cleaning "messy" data, handling missing values, and normalizing numbers.
4.  **Splitting:** Separating data into **Training** and **Test** sets.
5.  **Training:** Feeding the training data into an algorithm (e.g., Random Forest) to create a model.
6.  **Evaluation:** Testing the model on unseen data to check its accuracy.
7.  **Deployment & Monitoring:** Integrating the model into an app and retraining it as data changes.



[Image of machine learning workflow diagram]


---

## 4. Overfitting vs. Underfitting
A model must find the "sweet spot" between being too simple and too complex.

* **Underfitting:** The model is too simple to capture the underlying structure (e.g., using a straight line for curved data). Both training and test accuracy are low.
* **Overfitting:** The model is too complex and "memorizes" the training data, including its random noise. While training accuracy is perfect, it fails on new, unseen test data.

**Prevention:** Overfitting can be prevented using **Cross-Validation**, **Regularization**, or simply by providing more diverse training data.



---

## 5. Case Study: ML in Transportation
**Topic:** Predictive Maintenance in Public Transit.
**Summary:** Modern transportation systems use ML algorithms (like Decision Trees and Neural Networks) to monitor vehicle health. By analyzing sensor data—such as engine vibration and heat—the model predicts mechanical failures before they occur. 
**Findings:** Research indicates that this predictive approach reduces vehicle downtime by approximately 25-30% and significantly lowers emergency repair costs for city transit authorities.

---

## References
* Mitchell, T. (1997). *Machine Learning*. McGraw Hill.
* James, G., et al. (2013). *An Introduction to Statistical Learning*. Springer.
* Lesson Notes: *Introduction to Machine Learning*, DS-ML Bootcamp.
