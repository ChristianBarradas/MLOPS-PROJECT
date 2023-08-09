import numpy as np
import pandas as pd
from sklearn.metrics import (explained_variance_score, mean_absolute_error,
                             mean_squared_error)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


class HousePricePredictor:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def explore_data(self):
        print(self.df)
        print(self.df.columns.values)
        print(self.df.head())
        print(self.df.tail())
        print(self.df.isnull().sum())
        print(self.df.info())
        print(self.df.describe().transpose())

    def preprocess_data(self):
        self.df = self.df.drop(['id', 'zipcode'], axis=1)
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['month'] = self.df['date'].apply(lambda date: date.month)
        self.df['year'] = self.df['date'].apply(lambda date: date.year)
        self.df = self.df.drop('date', axis=1)

    def split_data(self):
        X = self.df.drop('price', axis=1)
        y = self.df['price']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    def scale_data(self):
        scaler = MinMaxScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)
        print('Max: ', self.X_train.max())
        print('Min: ', self.X_train.min())

    def build_model(self):
        self.model = Sequential()
        self.model.add(Dense(19, activation='relu'))
        self.model.add(Dense(19, activation='relu'))
        self.model.add(Dense(19, activation='relu'))
        self.model.add(Dense(19, activation='relu'))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')

    def train_model(self):
        self.model.fit(x=self.X_train, y=self.y_train.values,
                       validation_data=(self.X_test, self.y_test.values),
                       batch_size=128, epochs=400)

    def evaluate_model(self):
        predictions = self.model.predict(self.X_test)
        print('MAE: ', mean_absolute_error(self.y_test, predictions))
        print('MSE: ', mean_squared_error(self.y_test, predictions))
        print('RMSE: ', np.sqrt(mean_squared_error(self.y_test, predictions)))
        print('Variance Regression Score: ', explained_variance_score(self.y_test, predictions))

    def predict_single_house(self, house_data):
        scaler = MinMaxScaler()
        house_data = scaler.fit_transform(house_data.values.reshape(-1, 19))
        predicted_price = self.model.predict(house_data)[0, 0]
        return predicted_price


if __name__ == "__main__":
    predictor = HousePricePredictor('/Users/SISTEMAS/MLOPs_Project/DataSet/kc_house_data.csv')
    predictor.explore_data()
    predictor.preprocess_data()
    predictor.split_data()
    predictor.scale_data()
    predictor.build_model()
    predictor.train_model()
    predictor.evaluate_model()

    single_house_data = predictor.df.drop('price', axis=1).iloc[0]
    predicted_price = predictor.predict_single_house(single_house_data)
    print('\n\nDescriptive Statistics:\n', predictor.df['price'].describe())
    print(f'Features of new house:\n{single_house_data}')
    print(f'Predicted Price: {predicted_price:.2f}')
