from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generamos un dataset sintético
X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)

# Dividimos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo con overfitting: árbol muy profundo
modelo_overfit = DecisionTreeClassifier(max_depth=None)
modelo_overfit.fit(X_train, y_train)

# Modelo regularizado: profundidad limitada
modelo_regularizado = DecisionTreeClassifier(max_depth=3)
modelo_regularizado.fit(X_train, y_train)

# Evaluamos
print("Overfitting:")
print("Entrenamiento:", accuracy_score(y_train, modelo_overfit.predict(X_train)))
print("Prueba:", accuracy_score(y_test, modelo_overfit.predict(X_test)))

print("\nRegularizado:")
print("Entrenamiento:", accuracy_score(y_train, modelo_regularizado.predict(X_train)))
print("Prueba:", accuracy_score(y_test, modelo_regularizado.predict(X_test)))
