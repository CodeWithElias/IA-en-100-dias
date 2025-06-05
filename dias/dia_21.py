from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# cargar datos
X, y = load_iris(return_X_y=True)
y_cat = to_categorical(y)

# dividir datos
X_train, X_test, y_train, y_test = train_test_split(X,y_cat, test_size=0.2, random_state=42)

# crear modelo
modelo = Sequential()
modelo.add(Dense(10, input_shape=(4,), activation='relu'))
# capa oculta
modelo.add(Dense(3, activation='softmax'))

# compilar
modelo.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

# entrenar 
modelo.fit(X_train, y_train, epochs=50, verbose=0)

# evaluar
loss, acc = modelo.evaluate(X_test, y_test)
print(f"Precision en test: {acc:.2f}")