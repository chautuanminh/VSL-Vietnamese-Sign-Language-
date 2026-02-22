from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys

# Add your module paths
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
# Also add subdirectories if needed, though usually adding the base dir is enough for absolute imports
# However, the current code imports like 'from modules import ...' which implies 'backend' is in sys.path
# or 'backend/modules' is in sys.path.
# Looking at the original code, it was adding auth, modules, yolo, monitor separately.
for sub in ["auth", "modules", "yolo", "monitor"]:
    sub_path = os.path.join(BASE_DIR, sub)
    if sub_path not in sys.path:
        sys.path.append(sub_path)


#Import database and models
from modules.database import Base, engine
from auth import routes as auth_routes
from modules import yolo_db 
from yolo.routes import router as yolo_router
from monitor import routes as monitor_routes
import modules.monitor_models  # register monitoring models with SQLAlchemy metadata



#Check database connection
try:
    conn = engine.connect()
    print("Database connected successfully!")
    conn.close()
except Exception as e:
    print("Database connection failed:", e)


# Create tables for any imported models (development convenience)
try:
    Base.metadata.create_all(engine)
    print(" Database tables ensured (create_all).")
except Exception as e:
    print(" Failed to create tables automatically:", e)

app = FastAPI(title="Sign Language Backend API")




#CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




#Include authentication routes
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(yolo_router)
app.include_router(monitor_routes.router)




# Root route
@app.get("/")
def root():
    return {"message": "✅ Sign Language Backend is running!"}

#Health check
@app.get("/health")
def health():
    return {"status": "ok"}
