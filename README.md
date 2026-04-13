# 📊 SaaS Churn Prediction API 

Un motor predictivo de Machine Learning desplegado como una API RESTful rápida y robusta, diseñado para identificar proactivamente a los clientes con alto riesgo de cancelar su suscripción (Churn).

Este proyecto cierra la brecha entre la Ciencia de Datos y la Ingeniería de Software, tomando un modelo predictivo desde su fase de Análisis Exploratorio (EDA) hasta su puesta en producción.

## 🎯 El Problema de Negocio
Adquirir un nuevo cliente es mucho más caro que retener a uno existente. Esta API permite a los sistemas de CRM o dashboards empresariales consultar en tiempo real el nivel de riesgo de un usuario basándose en su perfil de facturación, antigüedad y tipo de contrato, permitiendo a los equipos de retención actuar *antes* de que el cliente se vaya.

## ⚙️ Características Técnicas Principales
* **Desarrollo de API con FastAPI:** Endpoints de alto rendimiento con documentación automática (Swagger UI).
* **Validación Estricta de Datos:** Uso de `Pydantic` para garantizar la integridad de los *payloads* JSON entrantes, transformando variables legibles (ej. `"Fiber optic"`) en matrices procesables por la máquina (One-Hot Encoding) en tiempo real.
* **Modelo de Machine Learning:** Entrenamiento de un algoritmo `RandomForestClassifier` optimizado para la detección de patrones de abandono.
* **Manejo de Clases Desbalanceadas:** Implementación de **SMOTE** (Synthetic Minority Over-sampling Technique) para evitar el sesgo hacia la clase mayoritaria y aumentar drásticamente la capacidad (Recall) de detectar clientes en riesgo real.
* **Arquitectura Limpia:** Separación clara entre los artefactos de Machine Learning (archivos `.pkl`) y la lógica de la aplicación web.

## 🛠️ Tech Stack
* **Backend:** Python 3, FastAPI, Uvicorn, Pydantic.
* **Data Science:** Pandas, scikit-learn, imbalanced-learn, Seaborn, Matplotlib.
* **Serialización:** Joblib.
