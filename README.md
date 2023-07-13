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
      * What is the variable most strongly correlated with property value?
      * How closely are the variables potentially affecting value related to each other?
      * How does number of bathrooms or bedrooms affect property value?
      * What drives differences in value between counties?

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
|FIPS| Federal Information Processing Standards, categorical variable of county codes for above counties|

# Reproduction Instructions


 1. Clone this repo.
 2. Acquire the data from codeup
 3. Put the data in the file containing the cloned repo.
 4. Run notebook.


# Takeaways and Conclusions

* Tax Amount is the variable most closely correlated with Value
* A number of variables are interrelated, particularly bathrooms, bedrooms, and square footage
* Differences in average value between counties require examination of multiple variables
* Polynomial is best performing model


# Recommendations

* Focus any future models around tax value
* Focus on selling on Orange County
