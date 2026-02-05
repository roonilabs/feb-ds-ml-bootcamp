Research Assignment: Introduction to Machine Learning


1. Definition of Machine Learning with a Real‑Life Example

Machine Learning (ML) is a field within artificial intelligence (AI) focused on developing algorithms and statistical models that enable computers to learn patterns from data and make decisions or predictions without being explicitly programmed for each task. ML systems improve performance through experience — meaning they learn from data examples rather than following fixed human‑coded rules.

A real‑life example of machine learning is email spam filtering. Spam detection algorithms learn from thousands of past emails that are labeled as “spam” or “not spam.” The algorithm identifies patterns (e.g., certain keywords, sender behavior) and creates a model that predicts whether future incoming emails are likely spam. Over time, as it processes more labeled examples, it becomes more accurate at filtering new messages.

2. Supervised vs Unsupervised Learning

Both supervised and unsupervised learning are major categories of ML, distinguished by whether labeled data is used.

Supervised Learning

In supervised learning, the algorithm is trained on a dataset where each input has a corresponding correct output (label). The goal is for the system to learn a mapping from input to output so that it can predict correct labels for new data.

Example of Supervised Learning:

A healthcare system trained to diagnose whether a patient has a disease based on medical imaging. The model learns from images labeled “disease present” or “disease absent” and then predicts on unseen images.

Unsupervised Learning

Unsupervised learning works with unlabeled data. Instead of predicting outcomes, the algorithm seeks to find inherent structures, groupings, or patterns in data. This is often exploratory and useful for clustering or simplifying complex datasets.

Example of Unsupervised Learning:

Customer segmentation in business: An unsupervised algorithm groups customers with similar purchasing patterns together, helping marketers tailor strategies without predefined categories.

| Feature         | Supervised Learning       | Unsupervised Learning               |
| --------------- | ------------------------- | ----------------------------------- |
| Labels          | Required                  | Not required                        |
| Goal            | Predict outcomes          | Find patterns/clusters              |
| Example task    | Classification/regression | Clustering/dimensionality reduction |
| Typical example | Disease diagnosis         | Grouping customers by behavior      |


3. What Causes Overfitting and How to Prevent It

Overfitting occurs when a machine learning model learns too much noise and detail from the training data, including random fluctuations that do not generalize to new data. In other words, the model fits the training data extremely well but performs poorly on unseen data. This usually happens when the model is overly complex relative to the data size or when the model memorizes specific examples rather than learning general patterns.

Causes of Overfitting

Model complexity too high for training data (e.g., too many parameters compared to number of data points)

Insufficient training data

Poor data quality or noise in training dataset

Prevention Techniques

Regularization: Techniques such as L1 or L2 penalize overly complex models by adding a penalty for large model weights.

Cross‑validation: Dividing training data into multiple folds to ensure the model performs well across several subsets.

Simplifying the model: Using simpler algorithms to avoid fitting noise.

More data: Collecting more diverse training examples to better represent real data variation.

4. Training and Test Data Split — Process and Importance

In ML, datasets are typically split into training and test sets:

Training data is the portion used by the algorithm to learn patterns and build the predictive model.

Test data is a separate portion used to evaluate the model’s performance on unseen data.

A common split ratio is 80:20 or 70:30, where 70–80% of the data is used for training and 20–30% for testing. This split ensures the model does not just memorize training data but can generalize to new examples. Separate testing is necessary because evaluating the model on unseen data gives a more realistic measure of real‑world performance. Using only training data for evaluation would risk overestimating the model’s effectiveness.

5. Case Study: Machine Learning Applied in Healthcare
Study Chosen:

“A Real‑World Demonstration of Machine Learning Generalizability: Intracranial Hemorrhage Detection on Head CT”

Summary of Findings

This research applied machine learning to detect intracranial hemorrhage (ICH) in head CT scans — a critical condition requiring rapid diagnosis. Researchers trained an ML model using 21,784 CT scans and evaluated it on an external dataset of 5,965 scans from a busy hospital.

Key results included:

Model showed high accuracy on new clinical data, with ~95% sensitivity and 94% specificity.

The study demonstrated that ML models can generalize effectively outside of controlled research settings, achieving robust performance in real hospital conditions.

This case study highlights that machine learning can significantly enhance clinical diagnosis by analyzing medical images at scale and with high reliability, potentially supporting or improving decision‑making by healthcare professionals.

References

1. IBM, What is Machine Learning? — definition and explanation of the ML field.

2. Wikipedia, Machine Learning — overview definitions and core concepts.

3. Wikipedia, Supervised learning.

4. Wikipedia, Unsupervised learning.

5. Wikipedia, Overfitting.

6. Machine learning training/test splitting — Springer definition.

7. Salehinejad et al., Real‑World Demonstration of Machine Learning Generalizability: Intracranial Hemorrhage Detection on Head CT.