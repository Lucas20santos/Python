# Pré-Processamento de dados

## Binarização

import numpy as np
from sklearn import preprocessing
input_data = np.array(
    [
        [2.1, -1.9, 5.5],
        [-1.5, 2.4, 3.5],
        [0.5, -7.9, 5.6],
        [5.9, 2.3, -5.8]
    ]
)

# print(input_data)

data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
# print("Binarized data:\n", data_binarized)

## Romação média

# print("Media = ", input_data.mean(axis=0))
# print("Desvio Padrão = ", input_data.std(axis=0))

# data_scaled = preprocessing.scale(input_data)
# print("Média removida: ", data_scaled.mean(axis=0))
# print("Desvio padraõ removido = ", data_scaled.std(axis=0))


# Escala

# data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
# data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
# print ("\nMin max scaled data:\n", data_scaled_minmax)

# Normalização

## Normalização L1

# data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
# print("\nL1 normalized data:\n", data_normalized_l1)

## Normalização L2

data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 normalized data:\n", data_normalized_l2)

