# regression_project
Codeup regression project utilizing Zillow data

# Project Description

Value of real property can be a difficult thing to assess. Numerous variables come into play when assessing relative values of properties. It is important to find the most predictive variables in pursuit of finding value in order simplify the process in the future. 
 
The following project is intended to unearth the factors contributing to property value. In pursuit of this end, I utilized the Codeup Zillow dataset from 2017 for properties in Orange, Los Angeles, and Ventura Counties in California. This dataset provides information on properties including tax value, previous taxes paid, year built, square footage, and room information. I will be exploring these variables to determine which ones may provide insight into what drives property value. 

# Project Goal

* Discover variables contributing to property value for Zillow
* Utilize these drivers to develop a regression machine learning model to predict property value
* The information derived from this model can subsequently be used on data from new property transactions to predict value


# Initial Thoughts

My initial hypothesis states that primary drivers of property value will be previous taxes paid and square footage.

# Planning Process

* Acquire dataset from Codeup database

* Prepare data:
  * Clean columns to account for null values
  * Create dummy variables for categorical strings

* Explore data for variables driving value
  * Answer the following initial questions:
      * Why drives differences in value between nearby properties?
      * Why do properties with similar attributes differ in value between locations?
      * How does number of bathrooms or bedrooms affect property value?
      * How directly are square footage and value related?

* Develop a model to predict property value
  * Use variables identified as drivers to build predictive models
  * Evaluate models on train and validate data
  * Select the best model based on Mean of Squared Errors (MSE)
  * Evaluate the best model on test data

# Data Dictionary 

The following dictionary only defines columns used in analysis for this dataset.

| Feature | Definition |
|:--------|:-----------|
|Tax Value| Dollar value of property sold in 2017|
|Tax Amount| Taxes, in dollars, previously paid on property|
|Year Built| Year property was built|
|Square Feet| Total square footage of property|
|Bedrooms| Number of bedrooms|
|Bathrooms| Number of bathrooms. Partial means no washing facility, only toilet|

# Reproduction Instructions


 1. Clone this repo.
 2. Acquire the data from codeup
 3. Put the data in the file containing the cloned repo.
 4. Run notebook.


# Takeaways and Conclusions

* Higher monthly charges seem to be a driver of churn
* Customers with automatic billing seem to churn at a lower rate than those who pay manually
* The longer the contract, the less likely a customer will churn
* Having dependents does seem to affect churn, indicating that nor only financial factors can be good predictors


# Recommendations

* Focus on incentivising long term contracts with customers
* Push family plans to draw in those with dependents
