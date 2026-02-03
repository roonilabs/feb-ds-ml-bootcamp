**1.What is Machine Learning?**

Machine learning is a subfield of artificial intelligence that uses algorithms trained on data sets to create models capable of performing tasks that would otherwise only be possible for humans, such as categorizing images, analyzing data, or predicting price fluctuations. Today, machine learning is one of the most common forms of artificial intelligence and often powers many of the digital goods and services we use every day

**Real world examples**

**Online shopping**

This is probably one of the least obvious ways people interact with AI in their daily lives. Many online shopping and ecommerce platforms use AI to streamline their customer experience in a variety of ways. 

As a customer, you may experience AI through:

Personalized product recommendations based on previous shopping activity or customer profile.
Pricing optimization based on supply, demand, or previous shopping activity.
Chatbots to provide instant responses to customer service or technical issues.
Shipping and delay estimates.
As a business owner, you may consider implementing AI in the following additional ways:

Sales and demand forecasting to help you manage your inventory in the face of increased or decreased demand.
Creating customer profiles and segmentation to boost sales.
Smart analytics to show in real-time how your business is performing

**2. Supervised Learning vs Unsupervised Learning**

In supervised learning, the algorithm “learns” from the training data set by iteratively making predictions on the data and adjusting for the correct answer. While supervised learning models tend to be more accurate than unsupervised learning models, they require upfront human intervention to label the data appropriately. For example, a supervised learning model can predict how long your commute will be based on the time of day, weather conditions and so on. But first, you must train it to know that rainy weather extends the driving time

Unsupervised learning models, in contrast, work on their own to discover the inherent structure of unlabeled data. Note that they still require some human intervention for validating output variables. For example, an unsupervised learning model can identify that online shoppers often purchase groups of products at the same time. However, a data analyst would need to validate that it makes sense for a recommendation engine to group baby clothes with an order of diapers, applesauce, and sippy cups

**Examples**

**Supervised**

Imagine we have a basket full of different fruits that we want the machine to identify. The machine first looks at the image of a fruit and extracts features like its shape, color and texture. Then it compares these features to the fruits it has already learned during training. If the new fruit’s features closely match those of an apple, the machine will predict that the fruit is an apple.

For example, suppose we train the machine by showing it fruits one by one:

If the fruit is round, has a small depression at the top and is red, it is labeled as an Apple.
If the fruit is long, curved and greenish-yellow, it is labeled as a Banana.
Now after this training, if we give the machine a new fruit (say a banana) from the basket and ask it to identify it, the machine will use what it has learned during training. It will analyze the shape and color of the new fruit and classify it as a Banana placing it in the correct category. In this way, the machine learns from the training data (the basket with labeled fruits) and applies that knowledge to recognize new, unseen fruits

**Unsupervised**

Imagine we have a machine learning model trained on many unlabeled images of dogs and cats. The model has never seen any labeled example that says “dog” or “cat” before so it doesn’t know how these animals look like.

Now, if we give the model a new image that contains both dogs and cats it won’t be able to directly label them as “dog” or “cat.” It will group parts of the image based on similarities and differences in features like shape or texture. It might separate the image into two groups one with dog-like features and other with cat-like features.

This happens because unsupervised learning doesn’t rely on prior knowledge or training with labeled data. It finds patterns and organizes data on its own helps in discovering information that wasn’t given before

**3.Overfitting**

**What is Overfitting?**
Overfitting occurs when the model cannot generalize and fits too closely to the training dataset instead

**Overfitting examples**

Consider a use case where a machine learning model has to analyze photos and identify the ones that contain dogs in them. If the machine learning model was trained on a data set that contained majority photos showing dogs outside in parks , it may may learn to use grass as a feature for classification, and may not recognize a dog inside a room.
Another overfitting example is a machine learning algorithm that predicts a university student's academic performance and graduation outcome by analyzing several factors like family income, past academic performance, and academic qualifications of parents. However, the test data only includes candidates from a specific gender or ethnic group. In this case, overfitting causes the algorithm's prediction accuracy to drop for candidates with gender or ethnicity outside of the test dataset

**How can you prevent overfitting?**

You can prevent overfitting by diversifying and scaling your training data set or using some other data science strategies, like those given below.

**Early stopping**

Early stopping pauses the training phase before the machine learning model learns the noise in the data. However, getting the timing right is important; else the model will still not give accurate results.
Pruning
You might identify several features or parameters that impact the final prediction when you build a model. Feature selection—or pruning—identifies the most important features within the training set and eliminates irrelevant ones. For example, to predict if an image is an animal or human, you can look at various input parameters like face shape, ear position, body structure, etc. You may prioritize face shape and ignore the shape of the eyes.

**Regularization**

Regularization is a collection of training/optimization techniques that seek to reduce overfitting. These methods try to eliminate those factors that do not impact the prediction outcomes by grading features based on importance. For example, mathematical calculations apply a penalty value to features with minimal impact. Consider a statistical model attempting to predict the housing prices of a city in 20 years. Regularization would give a lower penalty value to features like population growth and average annual income but a higher penalty value to the average annual temperature of the city.

**Ensembling**
Ensembling combines predictions from several separate machine learning algorithms. Some models are called weak learners because their results are often inaccurate. Ensemble methods combine all the weak learners to get more accurate results. They use multiple models to analyze sample data and pick the most accurate outcomes. The two main ensemble methods are bagging and boosting. Boosting trains different machine learning models one after another to get the final result, while bagging trains them in parallel.

**Data augmentation**

Data augmentation is a machine learning technique that changes the sample data slightly every time the model processes it. You can do this by changing the input data in small ways. When done in moderation, data augmentation makes the training sets appear unique to the model and prevents the model from learning their characteristics. For example, applying transformations such as translation, flipping, and rotation to input images

**4.Training data vs Testing data**

When we build any machine learning model, the data we use is divided into two important parts: training data and testing data. Training data teaches a model how to make predictions, and testing data checks how well the model has learned. In this article, we’ll understand what each one means, why both are necessary, and how they work together to create accurate ML models.

**Training Data**
Training data is the dataset used to teach a machine learning model. It usually contains labeled examples (where the correct output is already known). The model studies these examples, finds patterns, and slowly learns to make predictions on its own.

**During training, the model**

looks at input and output pairs
identifies relationships
adjusts its internal rules
improves its accuracy over time
Models with large and good-quality training data usually perform better.

**Testing Data**
Once the model has learned from training data, we need new, unseen data to check if it has learned correctly. This new dataset is called testing data. Testing data helps to:

**measure accuracy**
check if the model is overfitting
verify if the model can handle new information
If a model performs well on testing data, it means it has truly understood the patterns instead of just memorizing.

Why Do We Need Both Training and Testing Data?
Training and testing data serve two different goals:

Training data teaches the model.
Testing data checks the model’s understanding.
Using the same data for both would be unfair, separate datasets make sure the model:

learns meaningful patterns
generalizes well to real-world data
doesn't just memorize answers
This separation is essential to avoid overfitting, where a model becomes extremely good at training data but performs poorly on new data

**5.Case Study : How machine learning helps security**

the enter must need scurity so the mechine learning ver help full like Find threats on a network and Keep people safe when browsing also have more learning about how Provide endpoint malware protection and Detect malware in encrypted traffic

**References**

1:coursera.org/articles

2:IBM

3:Cisco

4:AWS

5: geeksforgeeks.org
