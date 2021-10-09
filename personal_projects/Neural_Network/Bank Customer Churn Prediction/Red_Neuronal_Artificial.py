# Red Neuronal Artificial

# Importando las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando los datasets
dataset = pd.read_csv('C:/Users/luigi/Documents/Programacion/Aprendizaje_Programacion/01_Empezando_con_Python/01-06_Machine_Learning/Apuntes_Udm/Redes_Neuronales_Artificiales/modelo_bajas_banco.csv')
X = dataset.iloc[:, 3:-1].values  # (CreditScore)-(EstimatedSalary): 4 - 12
y = dataset.iloc[:, 13].values  # Columna 13


# Datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Convierte los female y male en 0 y 1
labelencoder_X_2 = LabelEncoder()
X[:,2] = labelencoder_X_2.fit_transform(X[:,2])

# Convierte y acomoda los paises en columnas de 0 y 1
columntransformer = ColumnTransformer([("Geography", OneHotEncoder(),[1])], remainder='passthrough')
X = np.array(columntransformer.fit_transform(X), dtype=np.int64)
X = X[:, 1:] # Para eliminar la variable ficticia

# Separando sets de datos en Entrenamiento y Prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Escalado de Caracteristicas
from sklearn.preprocessing import StandardScaler
escaladoestandar = StandardScaler()
X_train = escaladoestandar.fit_transform(X_train)
X_test = escaladoestandar.transform(X_test)

# Importando librerias de Keras
import keras
from keras.models import Sequential
from keras.layers import Dense

# Iniciando Red Neuronal (Sequential significa que la red neuronal sera creada en secuencias, capa por capa, manualmente)
clasificador = Sequential()

# Agregando capa Input y primera capa oculta

#                    No. Nodos=6                                                    No. de Variables = 11
clasificador.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
#                 No hay valor espefico


# Agregando segunda capa oculta
clasificador.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))


# Agregando la capa output
clasificador.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))


# Compilando la Red Neuronal
clasificador.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Encajando Red Neuronal con set de Entrenamiento

#
clasificador.fit(X_train, y_train, batch_size = 10, epochs = 100)
#                               No hay un num especifico               

# Haciendo predicciones y evaluando el modelo

# Prediciendo el Set de Pruebas
y_pred = clasificador.predict(X_test)
y_pred = (y_pred>0.5)

# Matriz de Confusion
from sklearn.metrics import confusion_matrix
matrizconfusion = confusion_matrix(y_test, y_pred)


# Agregando nuevo cliente

nuevo_cliente = clasificador.predict(escaladoestandar.transform(np.array([[0,0,600,1,40,3,60000,2,1,1,50000]])))
nuevo_cliente = (nuevo_cliente > 0.5)
