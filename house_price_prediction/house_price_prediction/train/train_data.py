from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
# creating a model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from sklearn.compose import ColumnTransformer
import pandas as pd

COLUMNS_TO_DROP = ['id', 'zipcode', 'date']

class HousingDataPipeline:
    """
    A class representing the Titanic data processing and modeling pipeline.

    Attributes:
        NUMERICAL_VARS (list): A list of numerical variables in the dataset.
        CATEGORICAL_VARS_WITH_NA (list): A list of categorical variables with missing values.
        NUMERICAL_VARS_WITH_NA (list): A list of numerical variables with missing values.
        CATEGORICAL_VARS (list): A list of categorical variables in the dataset.
        SEED_MODEL (int): A seed value for reproducibility.

    Methods:
        create_pipeline(): Create and return the Titanic data processing pipeline.
    """
    
    def __init__(self,seed_model):
        self.SEED_MODEL = seed_model
       
        
    def create_pipeline(self):
        """
        Create and return the Titanic data processing pipeline.

        Returns:
            Pipeline: A scikit-learn pipeline for data processing and modeling.
        """
        self.PIPELINE = Pipeline([
                            ('Agregar_Variables',CustomTransformer()),
                            ('DropColumns',DropColumnsTransformer()),                   ]
                                 )
        return self.PIPELINE
    
    def fit_logistic_regression(self, X_train, y_train):
        """
        Fit a Logistic Regression model using the predefined data preprocessing pipeline.

        Parameters:
        - X_train (pandas.DataFrame or numpy.ndarray): The training input data.
        - y_train (pandas.Series or numpy.ndarray): The target values for training.

        Returns:
        - logistic_regression_model (LogisticRegression): The fitted Logistic Regression model.
        """
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
        
        #logistic_regression = LogisticRegression(C=0.0005, class_weight='balanced', random_state=self.SEED_MODEL)
        #pipeline = self.create_pipeline()
        #pipeline.fit(X_train, y_train)
        #model.fit(pipeline.transform(X_train), y_train)
        return model
    
    def transform_test_data(self, X_test):
        """
        Apply the data preprocessing pipeline on the test data.

        Parameters:
        - X_test (pandas.DataFrame or numpy.ndarray): The test input data.

        Returns:
        - transformed_data (pandas.DataFrame or numpy.ndarray): The preprocessed test data.
        """
        pipeline = self.create_pipeline()
        return pipeline.transform(X_test)


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
    
class DropColumnsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.COLUMNS_TO_DROP = COLUMNS_TO_DROP
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_copy = X.drop(self.COLUMNS_TO_DROP, axis=1)
        return 
    
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