# My Preprocessing Reflection

In this assignment, I learned how to turn messy data into clean data that a computer can understand. Here is what I did and why:

### 1. Filling Blank Spots (Missing Values)
Some cars didn't have their mileage (Odometer) or location listed. 
- For the **Odometer**, I used the **median** (the middle number) because it's not affected by one or two crazy high numbers.
- For things like **Location** and **Doors**, I used the **mode** (the most common entry) because it's the safest guess.

### 2. Fixing Typos
The data had "Subrb" instead of "Suburb" and used "??" for unknown places. I fixed these first so that my counts would be correct. Cleaning typos is like proofreading before you start doing math.

### 3. Handling "Crazy" Numbers (Outliers)
Some prices or mileages were way too high or too low. I used a method called **IQR** to find the boundaries and "clipped" the numbers. This means if a number was too high, I brought it down to a fair maximum. This helps the model not get confused by extreme values.

### 4. Making New Info (Feature Engineering)
I created three new things from the data:
- **CarAge**: How old the car is.
- **IsNew**: A simple Yes/No (1/0) if the car is less than 5 years old.
- **HighUsage**: A Yes/No if the car has been driven more than average.
- I also made **LogPrice**, which helps the math work better for prices.

### 5. Scaling
Finally, I simplified the numbers so they are all on the same scale (mostly between -3 and 3). This is called **Standardization**. It's like making sure you're comparing apples to apples.

---
*Abdilaahi190*
