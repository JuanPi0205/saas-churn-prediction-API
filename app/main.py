# app/main.py



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.prediction_router import router as prediction_router


app = FastAPI(
    title="API de Retencion de clinetes (SaaS Churn)",
    description="Predice si un cliente va a cancelar su suscripción basándose en un algoritmo de ML"
)



# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router)

