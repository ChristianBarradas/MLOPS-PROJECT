# data analysis and wrangling
import pandas as pd
import numpy as np

# creating a model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# scaling and train test split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# evaluation on test data
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score


df = pd.read_csv('/Users/SISTEMAS/MLOPs_Project/DataSet/kc_house_data.csv')


print(df)
print(df.columns.values)
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.info())
print(df.describe().transpose())

df1 = df.drop(['date'], axis=1)

sns.set(style="whitegrid", font_scale=1)
plt.figure(figsize=(13, 13))
plt.title('Pearson Correlation Matrix', fontsize=25)
sns.heatmap(df1.corr(), linewidths=0.25, vmax=0.7, square=True, cmap="GnBu", linecolor='w', annot=True, annot_kws={"size": 7}, cbar_kws={"shrink": .7})

price_corr = df1.corr()['price'].sort_values(ascending=False)
print(price_corr)


df = df.drop('id', axis=1)
df = df.drop('zipcode', axis=1)

df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].apply(lambda date: date.month)
df['year'] = df['date'].apply(lambda date: date.year)

df = df.drop('date', axis=1)

# Check the new columns
print(df.columns.values)

# Features
X = df.drop('price', axis=1)

# Label
y = df['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler = MinMaxScaler()

# fit and transfrom
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# everything has been scaled between 1 and 0
print('Max: ', X_train.max())
print('Min: ', X_train.min())


model = Sequential()

# input layer
model.add(Dense(19, activation='relu'))

# hidden layers
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))

# output layer
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

model.fit(x=X_train, y=y_train.values,
          validation_data=(X_test, y_test.values),
          batch_size=128, epochs=400)


# predictions on the test set
predictions = model.predict(X_test)

print('MAE: ', mean_absolute_error(y_test, predictions))
print('MSE: ', mean_squared_error(y_test, predictions))
print('RMSE: ', np.sqrt(mean_squared_error(y_test, predictions)))
print('Variance Regression Score: ', explained_variance_score(y_test, predictions))

print('\n\nDescriptive Statistics:\n', df['price'].describe())


# fueatures of new house
single_house = df.drop('price', axis=1).iloc[0]
print(f'Features of new house:\n{single_house}')

# reshape the numpy array and scale the features
single_house = scaler.transform(single_house.values.reshape(-1, 19))

# run the model and get the price prediction
print('\nPrediction Price:', model.predict(single_house)[0, 0])

# original price
print('\nOriginal Price:', df.iloc[0]['price'])
