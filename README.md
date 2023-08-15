## House Price Prediction

The goal of this model is to predict future house prices based on characteristics such as square footage, bathrooms, bedrooms, views, and others, we are going to build a deep learning model that can predict the future price of houses, which can be consumed through an API.

## The scope of the project:

Create with a baseline
   Create a model solution notebook that presents the different steps to expose the molding predictor through an API.
Factor the above notebook to create a main file that contains the necessary dependencies of the Predict, Models, Preprocess, load, Train, and Data stages.
Expose the model solution through an API, in which information can be captured with bathrooms, bedrooms, bathrooms, etc. and can return the house price prediction.

## Data set

This dataset contains home sales prices for King County, which includes Seattle. Includes homes sold between May 2014 and May 2015.
21 columns.
21597 rows.

## Characteristic

id: Unique identification for each house sold
date: Date of the sale of the house
price: Price of each home sold
bedrooms: Number of bedrooms
bathroom: number of bathrooms, where 0.5 represents a room with a toilet but no shower
sqft_living: square footage of the interior living space of the apartments
sqft_lot: Square feet of lot space
floors: Number of floors
facing the sea: - A dummy variable to know if the apartment has views of the seafront or not.
view: an index from 0 to 4 of how good the view of the property was
condition: - An index from 1 to 5 on the state of the apartment,
grade: An index of 1 to 13, where 1-3 falls short of building construction and design, 7 has a medium level of construction and design, and 11-13 has a high quality construction and design level.
sqft_above – The square footage of the interior space of the home that is above ground level
sqft_basement – The square footage of the interior space of the home that is below ground level
yr_built: the year the house was initially built
yr_renovated: The year the house was last renovated
zipcode: in which zip code area the house is located
lat: latitude
long: Length
sqft_living15: The square feet of interior living space for the 15 nearest neighbors
sqft_lot15: The square footage of the 15 nearest neighbor lots

Currently there is a notebook that shows one of the solutions based on an ANN neural network. This problem can also be solved by different algorithms such as K-NN, Logistic Regression, Multiple Regression among others.

The final result of the project is to be able to make house price predictions based on information such as zip code, number of bathrooms, latitude, longitude, etc.