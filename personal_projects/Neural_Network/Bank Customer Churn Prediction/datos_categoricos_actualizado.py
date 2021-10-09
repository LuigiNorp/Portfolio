# Data Preprocessing

# Importando Librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing sets de datos
dataset = pd.read_csv('C:/Users/luigi/Documents/Programacion/Aprendizaje_Programacion/01_Empezando_con_Python/01-06_Machine_Learning/Apuntes_Udm/Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Arreglando Datos Faltantes
# Actualizar Imputer
from sklearn.impute import SimpleImputer
missingvalues = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)
missingvalues = missingvalues.fit(X[:, 1:3])
X[:, 1:3]=missingvalues.transform(X[:, 1:3])


# Codificando Datos Categoricos
# Codificando Variable Independiente
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X = LabelEncoder()
#X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
#onehotencoder = OneHotEncoder(categorical_features = [0])
#X = onehotencoder.fit_transform(X).toarray()
# Encoding the Dependent Variable
#labelencoder_y = LabelEncoder()
#y = labelencoder_y.fit_transform(y)

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)
# Codificando Y
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)
# Separando en Set de Entrenamiento y Prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# Escalado de Categorias
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))