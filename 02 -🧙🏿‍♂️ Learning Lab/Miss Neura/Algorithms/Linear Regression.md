---
created: 2023-10-29T06:46:00
updated: 2023-10-22T12:00
tags:
  - mathematicalalgorithms
  - missneura
  - linearregression
external-links: 
type: Blog
---
![[Pasted image 20231029071400.png]]


Hey friends! 👋 It's me, Miss Neura, here today to break down linear regression. 

Now I know "regression" sounds kinda intimidating. 😅 But it's really not so bad! 

Linear regression is a useful way to model relationships between variables and make predictions. It works by fitting a line to data points. Simple enough, right? 📏

I'll explain step-by-step how linear regression crunches numbers to find the line of best fit. Stick with me! 🤓 

By the end, you'll understand the math behind these models and how to build your own. Regression won't seem so scary anymore. 😎

The key is finding the line that minimizes the distance between predictions and actual data points. We want to squash those residuals! 

Let's start with some history to see where linear regression originated before we dig into the details. ⏳

Then we can walk through an example to really solidify how it works. Alright, let's get our learn on! 🚀

# History

Linear regression models have been around for a long time! 

The basics were first described way back in the 1800s. 😮 A mathematician named Francis Galton observed that the heights of parents and their children tended to regress toward the average height in the general population. 

In the early 1900s, more work was done to describe linear regression as we know it today. A famous statistician named Ronald Fisher formalized the model and methods for fitting a line to data.

The first use of automated computation for linear regression came in the 1940s. A cytologist named Gertrude Cox pioneered the use of punch card machines to calculate regression. Talk about old school tech! 👵

Since then, linear regression has been used across many fields from economics to genetics as computing power exploded over the decades.  

Today, it's one of the fundamental machine learning and statistics techniques for modeling linear relationships between variables. Phew, linear regression has come a long way! ⏳

Now that we've seen some history, let's move on to understanding how these models actually work their magic. 🧙‍♀️ Onward!

# How Linear Regression Works

Alright, time to dig into the meat of how linear regression works! 🥩

The goal is to model the relationship between two continuous variables - we'll call them X and Y. 

X is the independent variable and Y is the dependent variable. Independent variables are the inputs, dependent variables are the outputs.

For example, X could be amount spent on ads and Y could be sales generated. Or X could be size of a house and Y could be its price. 

Linear regression finds the best straight line (aka linear model) that fits the data points for X and Y. 

This line can be used to predict future values for Y based on a given value of X. Pretty nifty! 

The line is characterized by its slope (m) and intercept point (b). Together, they determine where the line is placed.

The optimal m and b values are found using the least squares method. What does this mean?

It minimizes the distance between data points and the line, also called the residuals. Squashing residuals = happy line. 😊

This is referred to as the **cost function**, which is a mathematical formula that calculates the total error or "cost" of the current linear regression model. It sums up the residuals (differences between predicted and actual values) for all data points.

So in a nutshell, linear regression uses historical data to find the best fit line for continuous variables. This line can then make predictions! ✨

# The Algorithm

Let's say we want to model the relationship between the number of hours studied (x) and test score (y).

We have the following hours studied and test scores:

Hours Studied (x): 2, 4
Test Scores (y): 80, 90 

Our model is still:

**y = mx + b**

We need to find m and b. 

Let's guess m = 5 and b = 75 

Plugging this into our model and cost function:

For x = 2 hours studied, predicted test score would be y = 5x2 + 75 = 85 
Actual y = 80
Residual = 85 - 80 = 5

Now let's test x = 4 hours studied, predicted y = 5x4 + 75 = 95
Actual y = 90  
Residual = 95 - 90 = 5 

Cost function: 
The formula to calculate the cost function (or the error between the predicted vs the actual across data points) is **J(m,b) = Σ(y - (mx + b))^2**

So in our example:
J(m,b) = 5^2 + 5^2 = 50

To minimize J, we can tweak m and b. Let's try:
m = 10, b = 60

Now:
For x = 2 hours studied, predicted y = 10x2 + 60 = 80  
Residual = 0

For x = 4, predicted y = 10x4 + 60 = 100
Residual = 10

Cost function: 
J(m,b) = 0^2 + 10^2 = 100

So we can see tweaking m and b changes the residuals and cost J. We want to find the combo with lowest J.

In this tiny example, m=10, b=60 minimizes J. 

So our final line is:
**y = 10x + 60**

The equation y = 10x + 60 represents the best fit straight line relationship between hours studied (x) and test scores (y).

Specifically:

- The slope is 10. This means for every 1 additional hour studied, the model predicts the test score will increase by 10 points.
- The intercept is 60. This means when 0 hours are studied, the model predicts a test score of 60 points.

So in plain terms:

- Studying more hours corresponds to getting higher test scores
- There is a linear relationship where studying 10 additional hours predicts scoring 10 more points
- Even with 0 hours studied, the model predicts a baseline score of 60 points

This simple linear model captures the positive correlation between study time and test results. The line models how test scores are expected to improve by a certain amount per hour studied.

# Advantages

Alright, linear regression has some really great advantages worth highlighting! 😃

First up, it's super simple to implement and interpret. ♟️ The math isn't too wild, and the output is an easy-to-understand line equation.

It can also handle multiple independent variables at once! 🤯 Just plug them into the equation and away you go. Multi-variable modeling ftw!

Additionally, linear regression works well when there truly is a linear relationship in the data. 📈 It shines when x and y are correlated in a straight-ish line.

From a computational side, linear regression has pretty minimal requirements. 💻 It can run efficiently without massive processing power.

Lastly, this technique is used across so many fields and has stood the test of time. 🏆 A true flexible MVP algorithm!

Of course, every hero has their kryptonite. Let's flip to some disadvantages next...😼

# Disadvantages

Alright, linear regression does have some weaknesses we gotta talk about. ⚠️

First, it relies on the assumption that the relationship between variables is actually linear. 📏 Messy non-linear data will throw things off. 

It's also prone to overfitting with lots of input features, which can lead to poor generalization on new data. Too much complexity can skew the model. 🤪

Linear regression is sensitive to outliers too. A few weird data points can drastically change that best fit line. 👀

And if there's correlation but not causation between variables, the model might make inaccurate predictions. 🤥 

Finally, linear regression can't capture non-linear relationships that are inherently more complex. 🤷‍♀️ Curves, loops, jumps - nope!

But don't fret! Many of these disadvantages have workarounds or alternative algorithms. 💪

Alright, we're nearing the finish line! Let's talk about some real-world applications next. 🏁

# Applications

One of the most popular uses of linear regression is predicting housing prices! 🏡 

Features like square footage, location, age, etc. are used to model price. This helps estimate the value of new properties.

It's also commonly used in finance to forecast things like revenue, demand, inventory needs and other trends. 💰 Helpful for budgeting!

Economics is another field that leverages linear regression. It can estimate impacts of policy changes on metrics like GDP, unemployment, inflation, and growth. 📈 

Insurance companies use these models to assess risk factors and set appropriate premiums. Predicting claims helps pricing. 🚗

Even fields like healthcare apply linear regression. It helps model the effect of medications, treatments, diets on patient outcomes. 🩺 

Beyond these examples, linear regression powers many fundamental machine learning algorithms under the hood too!

It provides a simple baseline for modeling all kinds of relationships between variables. 🔍

# TL;DR

- Linear regression is used to model the relationship between two continuous variables. It fits a straight line through data points by minimizing the residuals (differences between predicted and actual y values).
- The line equation is defined as y=mx+b, where m is the slope and b is the intercept. The slope tells us how much y changes for each unit increase in x. The intercept is where the line crosses the y-axis.
- The optimal m and b values are found via gradient descent - iteratively tweaking to reduce error. This results in the line of best fit that most closely models the linear relationship.
- Key strengths of linear regression include simplicity, interpretability, and modeling linear correlations well. Weaknesses include sensitivity to outliers and inability to capture non-linear trends.

Overall, linear regression is a fundamental machine learning technique for predicting a numerical target based on linear relationships between variables. It continues to serve as a building block for more advanced algorithms too!
# Vocab List

- Regression - Modeling the relationship between variables
- Dependent variable - The output variable we're predicting (y)
- Independent variable - The input variable (x)
- Slope (m) - How much y changes per change in x
- Intercept (b) - Where the line crosses the y-axis
- Residuals - The differences between predicted and actual y
- Cost function (J) - Quantifies total error of the line
- Gradient descent - Iteratively updates to minimize J
- Overfitting - Model matches training data too closely