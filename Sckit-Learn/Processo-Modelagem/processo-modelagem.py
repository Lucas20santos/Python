# Processo de Modelagem

## Carregamento de Dados

"""
Características - As variáveis dos dados são chamadas de suas características.
Eles tbm  são conhecidos como preditores, entradas ou atributos.
    Matrizes
    Nome de Recursos

Resposta - É a veriável de sáida que depende basicamente das variávies de recurso.
    Vetor de Resposta
    Nomes
"""
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
features_names = iris.feature_names
target_names = iris.target_names
# print("Feature names: ", features_names)
# print("Target names: ", target_names)
# print("\nFirst 10 rows of X:\n", X[:10])

# Dividindo o conjunto de dados
# Vamos dividir os dados em 70% treino e 30% teste

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# print("Shape X_train = ", X_train.shape)
# print("Shape X_test = ", X_test.shape)
# print("Shape y_train = ", y_train.shape)
# print("Shape y_test = ", y_test.shape)

## Treinando o modele usando o algoritmo KNN 

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

classifier_knn = KNeighborsClassifier(n_neighbors=10)
classifier_knn.fit(X_train, y_train)
y_pred = classifier_knn.predict(X_test)

# Verificando a acuracia dos valores de y_test com y_pred
print("Acuracia: ", metrics.accuracy_score(y_test, y_pred))

sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
preds = classifier_knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds] 
print("Predictions:", pred_species)
