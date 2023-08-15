"""Main module."""
from load.load_data import DataRetriever
from train.train_data import HousingDataPipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
# scaling and train test split
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
import pandas as pd
import joblib
from train.train_data import HousingDataPipeline
from sklearn.metrics import mean_squared_error,mean_absolute_error,explained_variance_score
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np

DATASETS_DIR = '/Users/SISTEMAS/MLOPs_Project/DataSet/kc_house_data.csv'
COLUMNS_TO_DROP = ['id', 'zipcode', 'date']
SEED_MODEL = 404
TRAINED_MODEL_DIR = '/Users/SISTEMAS/MLOPS-PROJECT/house_price_prediction/house_price_prediction/models/'
# Guardar la red neuronal en un archivo .pkl
FILE_NAME = 'neural_network_model.pkl'

class CustomTransformer(BaseEstimator, TransformerMixin):
    #the constructor
    '''setting the add_bedrooms_per_room to True helps us check if the hyperparameter is useful'''
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    #estimator method
    def fit(self, X, y = None):
        return self
    #transfprmation
    def transform(self, X, y = None):
        #agregar 2 columnas
        X_copy = X.copy()
        X_copy['date'] = pd.to_datetime(X_copy['date'])
        X_copy['month'] = X_copy['date'].apply(lambda date: date.month)
        X_copy['year'] = X_copy['date'].apply(lambda date: date.year)
        #X_copy = X_copy.drop('date', axis=1)
        return X_copy

    
#Agregar_Caracteristicas = CustomTransformer()
#DataSet = Agregar_Caracteristicas.transform(df)  

class DropColumnsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.COLUMNS_TO_DROP = COLUMNS_TO_DROP
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_copy = X.drop(self.COLUMNS_TO_DROP, axis=1)
        return X_copy

# Instanciar el custom transformer
#drop_columns_transformer = DropColumnsTransformer(COLUMNS_TO_DROP)
class CustomMinMaxScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.scaler = MinMaxScaler()
        
    def fit(self, X, y=None):
        # Ajusta el escalador en los datos de entrenamiento
        self.scaler.fit(X)
        return self
    
    def transform(self, X):
        # Transforma los datos usando el escalador ajustado
        X_scaled = self.scaler.transform(X)
        return X_scaled

if __name__== "__main__":
# Retrive data
#Instantiate the Pipeline class
    
    #Read Data
    df = pd.read_csv(DATASETS_DIR)

    House_Price_Pipeline = Pipeline([
        ('Agregar_Variables',CustomTransformer()),
        ('DropColumns',DropColumnsTransformer()),
        ]) 
                                                   
    df = House_Price_Pipeline.fit_transform(df)  
    
    X_train, X_test, y_train, y_test = train_test_split(df.drop('price',axis=1),
                                                    df['price'],test_size=0.3,random_state=101
                                                    )

    scaler = MinMaxScaler()
    # fit and transfrom
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
  
    #Crear el modelo
    model = Sequential()

    # input layer
    model.add(Dense(19,activation='relu'))

    # hidden layers
    model.add(Dense(19,activation='relu'))
    model.add(Dense(19,activation='relu'))
    model.add(Dense(19,activation='relu'))
    # output layer
    model.add(Dense(1))
    model.compile(optimizer='adam',loss='mse')
    
    model.fit(x=X_train,y=y_train.values,
          validation_data=(X_test,y_test.values),
          batch_size=128,epochs=400)
    
    # predictions on the test set
    predictions = model.predict(X_test)

    print('MAE: ',mean_absolute_error(y_test,predictions))
    print('MSE: ',mean_squared_error(y_test,predictions))
    print('RMSE: ',np.sqrt(mean_squared_error(y_test,predictions)))
    print('Variance Regression Score: ',explained_variance_score(y_test,predictions))

    joblib.dump(model, TRAINED_MODEL_DIR+FILE_NAME)
    print(f"Modelo guardado en {TRAINED_MODEL_DIR+FILE_NAME}")


