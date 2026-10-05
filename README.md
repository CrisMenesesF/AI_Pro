# AI_Pro

## Actividad formativa: GitHub Copilot

### 1. Objetivo

El objetivo de esta actividad es explorar las capacidades de GitHub Copilot como herramienta de inteligencia artificial para apoyar el desarrollo de código.

Para esta actividad se creó un sistema de recomendación de productos utilizando Python y técnicas de aprendizaje supervisado.

---

## 2. Creación del repositorio

Se creó un repositorio privado en GitHub con el nombre:

**AI_Pro**

El repositorio incluye inicialmente los archivos `README.md` y `.gitignore`.

**Captura de pantalla:**  
<img width="1882" height="886" alt="Captura de pantalla 2026-10-05 145429" src="https://github.com/user-attachments/assets/97c25c65-2484-414e-83d5-e8bf7a837136" />



---

## 3. Clonación del repositorio

El repositorio fue clonado localmente utilizando Visual Studio Code y el terminal integrado.

Comando utilizado:

```bash
git clone https://github.com/CrisMenesesF/AI_Pro.git
```
**Captura de pantalla:**  
<img width="1902" height="877" alt="Captura de pantalla 2026-10-05 145513" src="https://github.com/user-attachments/assets/62eb7aed-5eed-48f3-bdb5-c60620df1fd3" />


---

## 4. Creación del archivo Python

Se creó el archivo:

`recommendation_system.py`

Este archivo contiene el código del sistema de recomendación desarrollado con apoyo de GitHub Copilot.

**Captura de pantalla:**  
<img width="1917" height="1021" alt="Captura de pantalla 2026-10-05 164518" src="https://github.com/user-attachments/assets/651302e0-bf5d-424c-afc9-cad1b37f468f" />


---

## 5. Configuración del entorno y dependencias

Para ejecutar el sistema se configuró un entorno virtual de Python en Visual Studio Code.

El entorno virtual fue creado mediante el siguiente comando:

```bash
python -m venv .venv
```

Las dependencias necesarias se instalaron mediante el siguiente comando:

```bash
pip install pandas scikit-learn
```

Las principales librerías utilizadas fueron:

- **Pandas:** utilizada para la creación y manipulación del conjunto de datos.
- **Scikit-learn:** utilizada para implementar el modelo de aprendizaje supervisado mediante `KNeighborsClassifier`, realizar el escalado de los datos y evaluar el modelo.

**Captura de pantalla:**
<img width="1917" height="1022" alt="Captura de pantalla 2026-10-05 165032" src="https://github.com/user-attachments/assets/897da499-026b-4b64-b8d3-a31fb966ea13" />

---

## 6. Ejecución y prueba del sistema

Una vez configurado el entorno e instaladas las dependencias, se ejecutó el programa `recommendation_system.py` desde el terminal integrado de Visual Studio Code.

El programa entrenó el modelo de clasificación utilizando los datos de productos definidos y posteriormente realizó una predicción para un producto nuevo.

Comando utilizado:

```bash
python recommendation_system.py
```

El resultado obtenido fue:

- Precisión del modelo: **66,67 %**
- Categoría recomendada para el producto nuevo: **Tecnología**

**Captura de pantalla:**
<img width="1913" height="1020" alt="Captura de pantalla 2026-10-05 165147" src="https://github.com/user-attachments/assets/cadf9d53-8c3d-4a59-b94c-de7c7033e895" />


## 7. Descripción del funcionamiento del modelo

El sistema desarrollado utiliza un modelo de aprendizaje supervisado para clasificar productos en diferentes categorías.

Para realizar la clasificación se utilizó `KNeighborsClassifier`, algoritmo que determina la categoría de un nuevo producto comparándolo con productos similares presentes en el conjunto de datos.

Antes de aplicar el modelo, los datos numéricos fueron escalados mediante `StandardScaler`, con el objetivo de que las diferentes variables utilizadas en la clasificación puedan ser comparadas de manera adecuada.

El funcionamiento general del sistema es el siguiente:

1. Se define un conjunto de datos con productos y sus características.
2. Los datos se dividen en conjuntos de entrenamiento y prueba.
3. Se realiza el escalado de las variables numéricas.
4. Se entrena el modelo `KNeighborsClassifier`.
5. Se evalúa el rendimiento del modelo utilizando los datos de prueba.
6. Finalmente, se utiliza el modelo para clasificar un producto nuevo y obtener una categoría recomendada.

De esta manera, el sistema permite utilizar los datos existentes para realizar una predicción sobre nuevos productos.

---

## 8. Conclusiones

La actividad permitió explorar el uso de GitHub Copilot como herramienta de apoyo para el desarrollo de código en Python.

A través del proyecto se creó y ejecutó un sistema de recomendación de productos utilizando técnicas de aprendizaje supervisado y el algoritmo `KNeighborsClassifier`.

El proyecto permitió aplicar diferentes etapas del desarrollo, incluyendo la creación y clonación de un repositorio, la configuración de un entorno virtual, la instalación de dependencias, la creación del código y la ejecución y evaluación del modelo.

El sistema obtuvo una precisión de **66,67 %** en la evaluación realizada y clasificó el producto nuevo dentro de la categoría **Tecnología**.

En conclusión, la actividad permitió comprobar cómo una herramienta de inteligencia artificial como GitHub Copilot puede apoyar el proceso de desarrollo, facilitando la creación de código y permitiendo al usuario concentrarse también en la comprensión, ejecución y evaluación de la solución desarrollada.

---



