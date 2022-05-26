Project Plan:
The plan is to use our access to the Codeup database to acquire data which we'll use to figure out why customers at the Telco Co are churning.
Once we've written the proper python code in a module to acquire the data that we want we'll run it and save it as a cache to our local computer.
From there we'll use another module which we'll use to prepare our data by splitting it up into three separate groups making sure that the variable we want, which is churn is evenly distributed.
The three groups will be train, our largest group, validate, and test.
Depending on the question we're asking we'll run various statistical tests and produce visualizations to help us better understand the data.
Once we're ready to model our data we will encode it into numbers that our machine learning algorithms can accept.
We'll select appropriate models that can be run based on the kind of data that we're dealing with.
We'll run it through multiple machine models till we come up with our best ones.
We'll use run the model using our validate set to further narrow these down to our single best model.
We'll then use our untouched test set with the best model to make our best predictions.

Data Dictionary:

# using function from acquire module to access database and make a dataframe
telco_df = acquire.get_telco_data()

# splitting data into train, validate, and test dfs
train, validate, test = prep.prep_telco(telco_df)

# setting α at 0.05 for a 95% confidence interval
α = 0.05

# creating a crosstabulation between Tech Support and Churn
tech_sup_xtab = pd.crosstab(train.tech_support, train.churn)

# creates a barplot from crosstab which compares churn rates and Tech Support
barplot = tech_sup_xtab.plot.bar(rot=0)

# creates a crosstab from train df with churn and contract type
k_type_xtab = pd.crosstab(train.contract_type, train.churn)

# puts customers who've been with telco for 2 or more years in a new df
two_yrs_plus = train[train.tenure >= 24]

# selects customers who also had the two yr contract
k_type_3x2yrs_plus = two_yrs_plus[two_yrs_plus.contract_type_id == 3]

# crosstabs and returns churn with 2 yr contract customers with 24+ months
k_type_3x2yrs_plus_xtab = pd.crosstab(k_type_3x2yrs_plus.contract_type, k_type_3x2yrs_plus.churn)

# puts customers who've been with telco for 2 or more years in a new df
lessthan_2yrs = train[train.tenure < 24]

# selects customers who also had the two yr contract
k_type_3xlessthan_2yrs = lessthan_2yrs[lessthan_2yrs.contract_type_id == 3]

# crosstabs and returns churn with 2 yr contract customers with <24 months
k_type_3xlessthan_2yrs_xtab = pd.crosstab(k_type_3xlessthan_2yrs.contract_type, k_type_3xlessthan_2yrs.churn)

# puts customers who've been with telco for 1 or more years in a new df
one_yr_plus = train[train.tenure >= 12]

# crosstabs and returns churn with 2 yr contract customers with 12+ months
k_type_2x1yr_plus_xtab = pd.crosstab(k_type_2x1yr_plus.contract_type, k_type_2x1yr_plus.churn)

# puts customers who've been with telco for less than 1 yr in a new df
lessthan_1yr = train[train.tenure < 12]

# selects customers who also had the 1 yr contract
k_type_2xlessthan_1yr = lessthan_1yr[lessthan_1yr.contract_type_id == 2]

# crosstabs and returns churn with 2 yr contract customers with <12 months
k_type_2xlessthan_1yr_xtab = pd.crosstab(k_type_2xlessthan_1yr.contract_type, k_type_2xlessthan_1yr.churn)

# puts customers who've been with telco for 1 or more months in a new df
one_mo_plus = train[train.tenure >= 1]

# puts customers who've been with telco for less than 1 month in a new df
lessthan_1mo = train[train.tenure < 1]

# selects customers who had the month-to-month contract
k_type_1xlessthan_1mo = lessthan_1mo[lessthan_1mo.contract_type_id == 1]

# merges and return the previous crosstabs together into a new df
merged_df = pd.concat([k_type_3x2yrs_plus_xtab, k_type_3xlessthan_2yrs_xtab, k_type_2x1yr_plus_xtab, k_type_2xlessthan_1yr_xtab, k_type_1x1_mo_plus_xtab])

# gets the top 5% on customers with highest monthly charges
top_5_pct = train.nlargest(math.floor(.05*(len(train))),'monthly_charges'

# crosstabulation of customers with the top 5% in monthly charges with churn
top_5_pct_xtab = pd.crosstab(top_5_pct.shape[0], top_5_pct.churn)

# Gets top 5% from those who don't churn
top_5_pct_no_churn = top_5_pct[top_5_pct.churn == 'No']

# pre-processes only the categorical variables of top 5% df
clean_top_5_pct = prep.clean_telco_cat(top_5_pct)

# pre-processes our explored data sets for machine learning
retrain = prep.clean_telco_cat(train)
revalidate = prep.clean_telco_cat(validate)
retest = prep.clean_telco_cat(test)

# splits our training set into x and y values to run in our algorithms
X_train = retrain.drop(columns=['churn_Yes'])
y_train = retrain['churn_Yes']

# splits our validate set into x and y values to run in our algorithms
X_validate = revalidate.drop(columns=['churn_Yes'])
y_validate = revalidate['churn_Yes']

# splits our test set into x and y values to run in our algorithms
X_test = retest.drop(columns=['churn_Yes'])
y_test = retest['churn_Yes']

# returns the most common answer for churn_Yes, which is 0 meaning our baseline
# is that they won't churn
baseline = y_train.mode()

# calculates our expected baseline accuracy
matches_baseline_prediction = y_train == 0
baseline_accuracy = matches_baseline_prediction.mean()

# makes a Random Forest model six steps deep
reforest = RandomForestClassifier(max_depth=6, random_state=321)

# makes a prediction for each value based on our training data
y_pred = reforest.predict(X_train)

# gives the probabilities the model gave for each value it used to make a prediction
y_pred_proba = reforest.predict_proba(X_train)

# sets up the  K-Nearest Neighbors model; weights = ['uniform', 'density']
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')

# a variable is set to the a numpy array of the prediction made for each value
# in the test set
y_pred = knn.predict(X_test)

# a variable for the probabilities it gave each value in making its predictions
y_pred_proba = knn.predict_proba(X_test)

# returns a df for each customer with their prediction and its given probability
probability_of_churn = pd.DataFrame(y_pred_proba, columns = ['probability', 'of churn'])
prediction_of_churn = pd.DataFrame(y_pred, columns = ['prediction of churn'])
customer_id = pd.DataFrame(test['customer_id'])

# prints a confusion matrix for the predictive outcomes of our test values
print(confusion_matrix(y_test, y_pred))

# sets a variable for the decision tree classification down six levels
clf = DecisionTreeClassifier(max_depth=6, random_state=321)

# fits the decision tree model to our training data set
clf = clf.fit(X_train, y_train)

# makes a decision tree prediction on the training set obeservations
y_pred = clf.predict(X_train)

# provides the probabilities it use to make predictions on the training set
y_pred_proba = clf.predict_proba(X_train)

# uses the validate set to make predictions for the decision tree classification model
y_pred = clf.predict(X_validate)

# variable for customers who churned in training data set
churn_train = train[train.churn == 'Yes']

# variable for customers who did not churn in training data set
no_churn_train = train[train.churn == 'No']

# sets x & y values equal to churned tenure and monthly charges for correlation test
x = churn_train.tenure
y = churn_train.monthly_charges

# sets x & y values equal to not churned tenure and monthly charges for correlation test
x = no_churn_train.tenure
y = no_churn_train.monthly_charges

# Classification Project Objectives

- [x] Document code
- [x] Explain process
    - [x] Data acquistion
    - [x] Preparation
    - [x] Exploratory data analysis and statistical testing
    - [x] Modeling
    - [x] Model evaluation
- [x] Findings
- [x] Key takeaways
- [x] Jupyter Notebok "Final Report"

## Deliverables
1. [x] Readme.md file (plan)
2. [x] Final Report.ipynb (report)
3. [x] Acquire.py & Prepare.py Modules
4. [x] Predictions.csv (predict)
5. [x] 1+ non-final .ipynb Notebooks for exploration (explore), modeling (model), and other work (wrangle)

## 1. Readme.md
- [x] Include a project plan which helps guide both the user and yourself through the different stages of the pipeline and steps you took to get to your conclusion
- [x] Include a data dictionary, which is important to provide in order to define and disambiguate each of the variables you are analyzing
- [x] Include useful and adequate instructions for reproducing your analysis and final report
- [x]  include a clear project goal that reflect on what you are trying to achieve for the business/organization (in the scenario layed out and should be specific enough to know when you have reached it and concise enough to keep in 1-2 sentences)
- [x] Include a project description that provides context for your project, including explaining why you are tackling this project, why it is important and how it could be of use to someone else beyond just the interest or new knowledge. It dives in a bit deeper than the goals and not a copy of the class project spec
- [x] Include initial questions and focus you are going into the analysis with, what were your initial ideas and thoughts, and did those play out to be true

## 2. .ipynb
- [x] In .ipynb include, in a markdown cell, a verbal explanation of the steps taken to prepare the data and why you made those decisions
- [x] Data split into three samples (Train, Validate, and Test) prior to exploration
    - [x] imputers, scalers, feature elimination, and selection algorithms should all be run after the split, so they are fit on train and transform validate and test
- [x] Key questions asked and answered of the data using natural language in markdown cells
- [x] Headers prior to the visualizations or statistical tests (does not take the place of stating your hypothesis/alternative hypothesis when doing a statistical test)
- [x] All statistical tests supported with a visualization of the interaction of the tested variables
- [x] Charts in the final report should have titles and labels that are descriptive and useful
- [x] The correct statistical tests are run, given the data type and distribution, and the correct conclusions are drawn
- [x] Markdown cells contain a clear answer in layman's terms
- [x] Your code contains code comments that are helpful to the reader in understanding what each blocks/lines of code are doing.
- [x] Markdown that documents your thought process, decision making, and navigation through the pipeline throughout the notebook consistently, wtih not just headers
    - Planning
    - Acquistion
    - Preparation
    - Exploration
    - Pre-processing
    - Modeling
    - Delivery
- [x] Conclusion summary that addresses the questions you raised in the opening of the project, which should tie together your analysis, the drivers of the outcome, and how you would expect your ML model to perform in the future on unseen data, in layman's terms
- [x] Conclusion that contains actionable recommendations based on your insights and analysis to your simulated audience, not about what to do differently with the data
- [x] Include next steps from a data science perspective that will assist in improving your research

## 3. Create modules making sure they have docstrings in your own words 
- ✅ acquire.py
- ✅ prepare.py
- ✅ env.py
- [x] In .py or .ipynb explain decisions made and reasons are communicated and documented for handling missing values.
- [x] explaining what it does, its input(s) and output(s)
- [x] split data into 50%, 30%, and 20%, (or 50%, 26%, 24%) (starting point)
- [x] reproducible i.e. random state

## 4. Predictions made from the top model developed
- [x] 3 columns
    1. [x] customer_id
    2. [x] probability of churn
    3. [x] prediction of churn (1=churn, 0=not_churn)
        - [x] from your best performing model ran on X_test

## 5. Other notebooks for explore, model, and wrangle
- [x] Decisions made and reasons are communicated and documented for handling missing values

## Questions to answer in exploration with 📊 and statistics

1. ✅ Question 1 -  Do customers who use Tech Support churn at a significantly different rate and if so is it more or less?

2. ✅ Question 2 - What are the rates of churn of 1 and 2 year contracts both before and after fullfilling their obligations as compared to month-to-month contracts?

3. ✅ Question 3 - What groups of customers pay the most in monthly charges but aren't churning?
    
4. ✅ Question 4 - ~~What services offered show the lowest rates of overall churn?~~
     ~~What's the likelihood that a customer will churn in the next month or year?~~
     Is there a significant difference in correlation between monthly charges and tenure for customers churn vs those who do not?
     
     ## Create at least 4 different visualizations that have the following:
a. 1️⃣ 2️⃣ 3️⃣ 4️⃣ A question in **markdown** that you want to answer

b. 1️⃣ 2️⃣ A visualization

c. 1️⃣ A statistical test (in at least 2 of your 4)

d. 1️⃣ 2️⃣ A clear answer or takeaway in **markdown** and natural language to the question based on your exploration

## Tests to run
## Fit 3 models using the following:

1. train
2. predict
3. evaluate with train

## Select the best model by evaluating with validate

## Evaluate best model on test

## Make a Predictions.csv file with the following:
- 3 columns: `customer_id`, `probability of churn`, and `prediction of churn`. (1=churn, 0=not_churn).
- These predictions should be from your best performing model ran on `X_test`.
- Note that the order of the `y_pred` and `y_proba` are numpy arrays coming from running the model on `X_test`. The order of those values will match the order of the rows in `X_test`, so you can obtain the customer_id from `X_test` and concatenate these values together into a dataframe to write to CSV.

## Make copy of notebook

## One will be your report name `Final_Report.ipynb` with markdown with the following sections:
- Intro
- Project overview
- Goals
    - Find driver for customer churn at Telco. Why are customers churning?
    - Make a report that non-data scientists can understand
    - Target audience is your manager and their manager
    - Make predictions here??
- Exploration
    - Summary
        - [x] Summarize your exploration section analysis (in a markdown cell using natural language): what you found and how you will use it moving forward. This includes key takeaways from all the questions answered in explore, a list of which features will be used in modeling and why, and which features will not move forward and why
- Modeling - enhance markdown here
    - Which eval metric did you use and why?
    - Which performed the best and why?
    - Add viz of best model showing its performance
- Conclusion
    - Goals achieved
    - Key takeaways
    - Next steps
    - Prediction performance expectations
    - Recommendations to reduce churn
- Etc.
Walk through and explain what you did to prepare the data and answer each viz/test individually

## Clean Up
- Comment out code including .py files
- Make Readme (.md) file

## Practice 5 minute presentation
- Be ready to answer questions about the following:
     - Code
     - Process
     - Findings
     - Key takeaways
     - Model
     
- [ ] Speaker kicks off the presentation by introducing themselves and their project through a one-liner of what it's about.
- [ ] Way you communicate should be appropriate for the audience: volume, speed of talk, flow, professionalism. (Codeup Data Science Instructor Team, virtually delivered via jupyter notebook)
- [ ] Notebook talked through step-by-step, in an understandable and meaningful way. Extraneous content in the notebook is not present.
    - [ ]  All visualizations in the final report are mentioned or discussed
- [ ] Presentation is concluded with a summary of what was found, recommendations, and next steps.
- [ ] Time limit is adhered to
    - [ ] Appropriate time spent on each section
    - [ ] Not by talking quickly but by reducing the amount or depth of information conveyed
    - [ ] Speech should be natural, and take the time needed for the audience to consume the information
    - [ ] Time not spent scrolling through 10's of visualizations or hundreds of lines of code
    
- Use needs to have their own env.py file with 'password', 'host', and 'user' for username to access Codeup database.