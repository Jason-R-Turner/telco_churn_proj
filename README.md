# Classification Project Objectives

- [ ] Document code
- [ ] Explain process
    - [ ] Data acquistion
    - [ ] Preparation
    - [ ] Exploratory data analysis and statistical testing
    - [ ] Modeling
    - [ ] Model evaluation
- [ ] Findings
- [ ] Key takeaways
- [ ] Jupyter Notebok "Final Report"

## Deliverables
1. [ ] Readme.md file (plan)
2. [ ] Final Report.ipynb (report)
3. [x] Acquire.py & Prepare.py Modules
4. [ ] Predictions.csv (predict)
5. [ ] 1+ non-final .ipynb Notebooks for exploration (explore), modeling (model), and other work (wrangle)

## 1. Readme.md
- [ ] Include a project plan which helps guide both the user and yourself through the different stages of the pipeline and steps you took to get to your conclusion
- [ ] Include a data dictionary, which is important to provide in order to define and disambiguate each of the variables you are analyzing
- [ ] Include useful and adequate instructions for reproducing your analysis and final report
- [ ]  include a clear project goal that reflect on what you are trying to achieve for the business/organization (in the scenario layed out and should be specific enough to know when you have reached it and concise enough to keep in 1-2 sentences)
- [ ] Include a project description that provides context for your project, including explaining why you are tackling this project, why it is important and how it could be of use to someone else beyond just the interest or new knowledge. It dives in a bit deeper than the goals and not a copy of the class project spec
- [ ] Include initial questions and focus you are going into the analysis with, what were your initial ideas and thoughts, and did those play out to be true

## 2. .ipynb
- [ ] In .ipynb include, in a markdown cell, a verbal explanation of the steps taken to prepare the data and why you made those decisions
- [ ] Data split into three samples (Train, Validate, and Test) prior to exploration
    - [ ] imputers, scalers, feature elimination, and selection algorithms should all be run after the split, so they are fit on train and transform validate and test
- [ ] Key questions asked and answered of the data using natural language in markdown cells
- [ ] Headers prior to the visualizations or statistical tests (does not take the place of stating your hypothesis/alternative hypothesis when doing a statistical test)
- [ ] All statistical tests supported with a visualization of the interaction of the tested variables
- [ ] Charts in the final report should have titles and labels that are descriptive and useful
- [ ] The correct statistical tests are run, given the data type and distribution, and the correct conclusions are drawn
- [ ] 
- [ ] Markdown cells contain a clear answer in layman's terms
- [ ] Your code contains code comments that are helpful to the reader in understanding what each blocks/lines of code are doing.
- [ ] Markdown that documents your thought process, decision making, and navigation through the pipeline throughout the notebook consistently, wtih not just headers
    - Planning
    - Acquistion
    - Preparation
    - Exploration
    - Pre-processing
    - Modeling
    - Delivery
- [ ] Conclusion summary that addresses the questions you raised in the opening of the project, which should tie together your analysis, the drivers of the outcome, and how you would expect your ML model to perform in the future on unseen data, in layman's terms
- [ ] Conclusion that contains actionable recommendations based on your insights and analysis to your simulated audience, not about what to do differently with the data
- [ ] Include next steps from a data science perspective that will assist in improving your research

## 3. Create modules making sure they have docstrings in your own words 
- ✅ acquire.py
- ✅ prepare.py
- ✅ env.py
- [ ] In .py or .ipynb explain decisions made and reasons are communicated and documented for handling missing values.
- [ ] explaining what it does, its input(s) and output(s)
- [ ] split data into 50%, 30%, and 20%, (or 50%, 26%, 24%) (starting point)
- [ ] reproducible i.e. random state

## 4. Predictions made from the top model developed
- [ ] 3 columns
    1. [ ] customer_id
    2. [ ] probability of churn
    3. [ ] prediction of churn (1=churn, 0=not_churn)
        - [ ] from your best performing model ran on X_test
The order of y_pred and y_proba numpy arrays come from running the model on X_test, which match the order of the rows in X_test. You can obtain the customer_id from X_test and concatenate these values together into a dataframe to write to CSV.

## 5. Other notebooks for explore, model, and wrangle
- [ ] Decisions made and reasons are communicated and documented for handling missing values

## Questions to answer in exploration with 📊 and statistics
similar to the following:
- Are customers with DSL more or less likely to churn?
- What month are customers most likely to churn and does that depend on their contract type?
- Is there a service that is associated with more churn than expected?
- Do customers who churn have a higher average monthly spend than those who don't?

1. ✅ Question 1 -  Do customers who use Tech Support churn at a significantly different rate and if so is it more or less?

2. ✅ Question 2 - What are the rates of churn of 1 and 2 year contracts both before and after fullfilling their obligations as compared to month-to-month contracts?

3. ✅ Question 3 - What groups of customers pay the most in monthly charges but aren't churning?
    - Try to visualize
    
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
        - [ ] Summarize your exploration section analysis (in a markdown cell using natural language): what you found and how you will use it moving forward. This includes key takeaways from all the questions answered in explore, a list of which features will be used in modeling and why, and which features will not move forward and why
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