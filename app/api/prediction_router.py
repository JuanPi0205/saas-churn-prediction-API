import joblib
import pandas as pd
import os

from fastapi import HTTPException
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Literal




router = APIRouter(prefix="/model", tags=["Model"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RUTA_MODELO = os.path.join(BASE_DIR, '..', 'models', 'modelo_retencion_clientes.pkl')

try:
    modelo = joblib.load(RUTA_MODELO)
    print("✅ Modelo cargado correctamente.")
except FileNotFoundError:
    raise RuntimeError(f"❌ No se encontró el modelo en: {RUTA_MODELO}")


class DatosCliente(BaseModel):
    SeniorCitizen: bool = Field(description="¿Es una persona de la tercera edad?")
    tenure: int = Field(description="Meses de antigüedad con la empresa")
    MonthlyCharges: float = Field(description="Cobro mensual en dólares")
    TotalCharges: float = Field(description="Cobro total acumulado")


    InternetService: Literal["DSL", "Fiber optic", "No"]
    Contract: Literal["Month-to-month", "One year", "Two year"]
    PaymentMethod: Literal["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]


@router.post("/api/v1/predecir-churn")
def predecir_abandono(cliente: DatosCliente):
    try:

        columnas_esperadas = modelo.feature_names_in_
        df_input = pd.DataFrame(0.0, index=[0], columns=columnas_esperadas)


        df_input.at[0, "SeniorCitizen"] = 1.0 if cliente.SeniorCitizen else 0.0
        df_input.at[0, "tenure"] = float(cliente.tenure)
        df_input.at[0, "MonthlyCharges"] = float(cliente.MonthlyCharges)
        df_input.at[0, "TotalCharges"] = float(cliente.TotalCharges)


        if cliente.InternetService == "Fiber optic":
            df_input.at[0, "InternetService_Fiber optic"] = 1.0

        if cliente.Contract == "One year":
            df_input.at[0, "Contract_One year"] = 1.0
        elif cliente.Contract == "Two year":
            df_input.at[0, "Contract_Two year"] = 1.0

        if cliente.PaymentMethod == "Electronic check":
            df_input.at[0, "PaymentMethod_Electronic check"] = 1.0


        prediccion = modelo.predict(df_input)
        resultado_binario = int(prediccion[0])

        return {
            "alerta_churn": bool(resultado_binario == 1),
            "mensaje": "Alto riesgo de abandono. ¡Ofrecer soporte!" if resultado_binario == 1 else "Cliente estable.",
            "codigo_prediccion": resultado_binario
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando la predicción: {str(e)}")
f
