# Día 19: Evaluación de Modelos de Clasificación

En aprendizaje automático, una vez entrenado un modelo, es **crucial evaluar su rendimiento** usando métricas adecuadas. Estas métricas permiten entender **qué tan bien está funcionando** el modelo con datos nuevos.

## 🔹 1. Precisión (Accuracy)

**Definición:**  
Proporción de predicciones correctas sobre el total de predicciones.

**Fórmula:**  
`Precisión = (TP + TN) / (TP + TN + FP + FN)`

**Interpretación:**  
- Una precisión de 0.95 significa que el 95% de las predicciones fueron correctas.
- Es útil cuando hay clases balanceadas, pero puede ser engañosa con clases desbalanceadas.

## 🔹 2. Recall (Sensibilidad)

**Definición:**  
Mide la capacidad del modelo para detectar correctamente los positivos reales.

**Fórmula:**  
`Recall = TP / (TP + FN)`

**Interpretación:**  
- Alto recall significa que se detectan la mayoría de los verdaderos positivos.
- Crítico en contextos médicos, detección de fraudes, etc.

## 🔹 3. Precisión (Precision)

**Definición:**  
Proporción de verdaderos positivos sobre todos los positivos predichos.

**Fórmula:**  
`Precision = TP / (TP + FP)`

**Interpretación:**  
- Alto precision indica que los positivos predichos son generalmente correctos.
- Útil cuando los falsos positivos son costosos.

## 🔹 4. F1-Score

**Definición:**  
Promedio armónico entre precision y recall.

**Fórmula:**  
`F1 = 2 * (Precision * Recall) / (Precision + Recall)`

**Interpretación:**  
- Equilibra precisión y recall.
- Útil en datasets con desequilibrio de clases.

## 🔹 5. Curva ROC (Receiver Operating Characteristic)

**Definición:**  
Representación gráfica de la capacidad del modelo para distinguir entre clases.

- Eje X: Tasa de Falsos Positivos (FPR)
- Eje Y: Tasa de Verdaderos Positivos (TPR o Recall)

**Área bajo la curva (AUC - ROC):**  
- De 0 a 1 (más cercano a 1 es mejor).
- AUC de 0.5 indica modelo aleatorio.

## 📌 Consideraciones Clave

| Escenario                        | Métrica Prioritaria   |
|----------------------------------|------------------------|
| Diagnóstico médico               | Recall                 |
| Filtro de spam                   | Precision              |
| Clasificación general equilibrada| Accuracy / F1-score    |
| Modelos probabilísticos          | ROC y AUC              |
