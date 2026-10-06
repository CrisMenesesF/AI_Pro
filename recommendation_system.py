"""Ejemplo académico de clasificación de productos con K vecinos más cercanos."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# Cada fila representa un producto de ejemplo y su categoría conocida.
datos_productos = pd.DataFrame(
    [
        # Productos de tecnología
        {"producto": "Audífonos inalámbricos", "precio": 850, "calificacion": 4.6, "ventas_mensuales": 210, "garantia_meses": 12, "categoria": "Tecnología"},
        {"producto": "Teclado mecánico", "precio": 1200, "calificacion": 4.7, "ventas_mensuales": 160, "garantia_meses": 24, "categoria": "Tecnología"},
        {"producto": "Cargador portátil", "precio": 650, "calificacion": 4.3, "ventas_mensuales": 240, "garantia_meses": 12, "categoria": "Tecnología"},
        {"producto": "Reloj inteligente", "precio": 1500, "calificacion": 4.5, "ventas_mensuales": 180, "garantia_meses": 24, "categoria": "Tecnología"},
        {"producto": "Bocina Bluetooth", "precio": 900, "calificacion": 4.4, "ventas_mensuales": 200, "garantia_meses": 12, "categoria": "Tecnología"},
        {"producto": "Webcam HD", "precio": 1100, "calificacion": 4.6, "ventas_mensuales": 140, "garantia_meses": 24, "categoria": "Tecnología"},
        # Productos para el hogar
        {"producto": "Taza térmica", "precio": 180, "calificacion": 4.5, "ventas_mensuales": 300, "garantia_meses": 3, "categoria": "Hogar"},
        {"producto": "Lámpara de escritorio", "precio": 350, "calificacion": 4.2, "ventas_mensuales": 190, "garantia_meses": 6, "categoria": "Hogar"},
        {"producto": "Organizador de cocina", "precio": 120, "calificacion": 4.4, "ventas_mensuales": 280, "garantia_meses": 0, "categoria": "Hogar"},
        {"producto": "Juego de sábanas", "precio": 500, "calificacion": 4.7, "ventas_mensuales": 150, "garantia_meses": 6, "categoria": "Hogar"},
        {"producto": "Botella reutilizable", "precio": 220, "calificacion": 4.3, "ventas_mensuales": 320, "garantia_meses": 3, "categoria": "Hogar"},
        {"producto": "Cojín decorativo", "precio": 160, "calificacion": 4.1, "ventas_mensuales": 170, "garantia_meses": 0, "categoria": "Hogar"},
        # Productos deportivos
        {"producto": "Tapete de yoga", "precio": 400, "calificacion": 4.6, "ventas_mensuales": 180, "garantia_meses": 6, "categoria": "Deporte"},
        {"producto": "Mancuernas", "precio": 700, "calificacion": 4.5, "ventas_mensuales": 130, "garantia_meses": 12, "categoria": "Deporte"},
        {"producto": "Cuerda para saltar", "precio": 150, "calificacion": 4.2, "ventas_mensuales": 290, "garantia_meses": 3, "categoria": "Deporte"},
        {"producto": "Balón de fútbol", "precio": 550, "calificacion": 4.7, "ventas_mensuales": 220, "garantia_meses": 6, "categoria": "Deporte"},
        {"producto": "Guantes de gimnasio", "precio": 280, "calificacion": 4.3, "ventas_mensuales": 160, "garantia_meses": 3, "categoria": "Deporte"},
        {"producto": "Banda elástica", "precio": 200, "calificacion": 4.4, "ventas_mensuales": 250, "garantia_meses": 0, "categoria": "Deporte"},
    ]
)

# Las características numéricas que utilizará el modelo.
caracteristicas = [
    "precio",
    "calificacion",
    "ventas_mensuales",
    "garantia_meses",
]
X = datos_productos[caracteristicas]
y = datos_productos["categoria"]

# Se separan los datos para medir el desempeño con productos no usados al entrenar.
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=1 / 3, random_state=42, stratify=y
)

# El escalado es importante porque KNN calcula distancias entre las características.
modelo = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=3),
)
modelo.fit(X_entrenamiento, y_entrenamiento)


def recomendar_categoria(
    modelo_entrenado,
    precio,
    calificacion,
    ventas_mensuales,
    garantia_meses,
):
    """Predice la categoría de un producto nuevo a partir de sus características."""
    producto_nuevo = pd.DataFrame(
        [
            {
                "precio": precio,
                "calificacion": calificacion,
                "ventas_mensuales": ventas_mensuales,
                "garantia_meses": garantia_meses,
            }
        ],
        columns=caracteristicas,
    )
    return modelo_entrenado.predict(producto_nuevo)[0]


def main():
    # El modelo predice las categorías del conjunto de prueba.
    predicciones = modelo.predict(X_prueba)

    # La precisión indica la proporción de predicciones correctas.
    precision = accuracy_score(y_prueba, predicciones)
    print(f"Precisión del modelo: {precision:.2%}")

    # Ejemplo: recomendar una categoría para un producto nuevo.
    categoria = recomendar_categoria(
        modelo,
        precio=750,
        calificacion=4.5,
        ventas_mensuales=200,
        garantia_meses=12,
    )
    print(f"Categoría recomendada para el producto nuevo: {categoria}")


if __name__ == "__main__":
    main()