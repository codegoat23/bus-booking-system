


from backend.db.database import create_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import Bus, Trip
from backend.routers.buses import router as buses_router   
from backend.routers.trips import router as trips_router
from backend.routers.seats import router as seats_router

create_tables()

app = FastAPI(
    title="bus booking API",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000 ,reload=True)
    
    
app.include_router(buses_router)
app.include_router(trips_router)
app.include_router(seats_router)


@app.get("/")
def home():
    return {"message": "Bus Booking API is running 🚌"}