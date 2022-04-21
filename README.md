
# TIME SERIES PROJECT - SUPERSTORE -
Reported by Craig Calzado and Jerry Nolf
Codeup - Innis Cohort - April 22, 2022

---
  
## Project Overview

---
 
#### 1. Goals:
- Determine the best way to launch a new marketing campaign in the near future.
- Determine the target of the campaign.
- Back reccomendations of target with statistics and visualizations.

--- 
 
#### 2. Description:
Working as a data scientist at Superstore, the Vp of Marketing has come to our team and asked for insight in terms of growth opportunites for the next marketing campaign. He is in need of a better understanding of who we should target in our upcoming marketing campaing and what segments, categories, etc. we should focus on pushing.

--- 
 
#### 3. Initial Questions:
- Where, in our sales area, is the biggest opportunity to increase profit?
- What segments can offer the greatest positive impact on profit?
- What region has more growth potential?
- Which region has the biggest customer base?
- What items offer highest/lowest profits?
- What category offer the highest/lowest profits? 
---
  
#### 4. Defined Deliverables:
- README file - provides a better understanding of the project
- Explore Workbooks - Draftings of explored areas and conclusions drawn for the original data
- wrangle.py - provides reproducible code to automate acquiring and preparing the data
- Final Report - provides final presentation-ready wrangle and findings
- Slide Deck - 2 visualizations and an executive summary with recommendations and rationale
- 5-minute presentation to VP of Marketing 

---

#### 5. Data Dictionary:
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
|  Variables             |    Definition                              |    DataType             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
|order_date (index)    |  Date order was placed                          |  datetime64[ns]    |
|order_id              |  Order identifier assigned to each product name for each order | object |
|ship_date             |  Date order was shipped                         | datetime64[ns]      |
|segment               |  Customer type: Consumer, Cooperate, Home Office  |  object     |
|city                  |  City to which shipment was delivered  |  object    |
|state                 |  State to which shipment was delivered  |  object    |
|postal_code           |  Postal code to which shipment was delivered   |  float64   |
|sales                 |  Sale total for product id * quantity in given order ($USD)  | float64     |
|quantity              |  Total number of specified product ordered  | float64     |
|discount              |  Percentage of discount applied to order in decimal form  | float64     |
|profit                |  Sales - Product Cost  | float64     |
|category              |  Category the product belongs to  | object    |
|sub-category          |  Subcategory the product belongs to  |  object    |
|customer_name         |  Name of customer   | object     |
|product_name          |  Name of product  |  object    |
|region_name           |  General area of US where order was placed: 'Central', 'South', 'East', 'West'  |  object    |
|avg_items_sales       |  Average sale amount for each item in an order  |  int64    |
|original_sales        |  Sale amount before any discounts are applied  |  int64    |

---

## PROJECT PLAN - USING THE DATA SCIENCE PIPELINE:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Evaluate ➜ Deliver
 
#### 1. PLAN
- [x] Define the project goal
- [x] Determine proper format for the audience
- [x] Asked questions that would lead to final goal
- [x] Define an MVP

 
#### 2. ACQUIRE
- [x] Create a function to pull appropriate information from the zillow database
- [x] Create and save a wrangle.py file in order to use the function to acquire
 
#### 3. PREPARE

- [x] Import functions from wrangle.py module
- [x] Drop duplicate columns that are deemed unneccessary
- [x] Assign order_date as datetime
- [x] Set index as order_date for time series analysis
- [x] Create any new columns that are considered usable for a deeper dive into the data
 
#### 4. EXPLORE
Using Jupyter Notebook:
- [x] Answer key questions about hypotheses and find the best customer segment in regards to
- [x] Run at least two statistical tests
- [x] Document findings
- [x] Create visualizations with the intent to discover variable relationships
- [x] Identify variables related to customer segments and _________
- [x] Identify any potential data integrity issues
- [x] Summarize conclusions, provide clear answers, and summarize takeaways
- [x] Explain plan of action as deduced from work to this point
 
#### 5. EVALUATE
- [x] Identify believed areas of growth 
- [x] Establish appropriate statistcial tests to reinforce findings
- [x] Interpret and document findings
 
#### 6. DELIVERY
- [x] Prepare a five-minute presentation using Google Slides
- [x] Include an introduction of the project and goals
- [x] Provide an executive summary of findings, key takeaways, recommendations, and rationale
- [x] Create a walkthrough of the analysis 
- [x] Include 2 presentation-worthy visualizations that support the problem and recommendation
- [x] Provide final takeaways, recommend a course of action, and next steps
- [x] Be prepared to answer questions following the presentation
- [x] Prepare final notebook in Jupyter Notebook
- [x] Create clear walk-though of the Data Science Pipeline using headings and dividers
- [x] Explicitly define questions asked during the initial analysis
- [x] Visualize relationships
- [x] Document takeaways

---
  
## Reproducibility:
### Steps to Reproduce
1. Have your env file with proper credentials saved to the working directory
2. Ensure that a .gitignore is properly made in order to keep privileged information private
3. Clone repo from github to ensure availability of the acquire and prepare imports
4. Ensure pandas, numpy, matplotlib, scipy, sklearn, and seaborn are available
5. Follow steps outline in this README.md to run Final_Zillow_Report.ipynb

---

## KEY TAKEAWAYS:

### Conclusion: 
Marketing can offer the greatest impact for the Central region. In particular, the state of Texas has the greatest loss of profit with the company's largest profit-hemorraging cities in Houston and San Antonio. We believe that the best foot forward is to stop offering discounts in order to help individal categories but rather offer discounting based on quantity of product sold per order.


#### The goals of this project were to 
- Determine the best way to launch a new marketing campaign in the near future
- Determine the target of the campaign
- Back reccomendations of target with statistics and visualizations

### Recommendation(s):
Going forward, marketing campaigns must focus on discounting larger quantities sold for orders as opposed to current strategies that offer discounts for categories seen as failing based on previous reporting.

### Next Steps:
With more time, I would like to:

- Dive into Illinois' issues and the impact of proper marketing
- Look into how to improve the impact of profit by individual products

--- 



