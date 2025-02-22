from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .routers import fields_router, subtopics_router, case_studies_router, sessions_router

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(fields_router, prefix=settings.API_V1_STR)
app.include_router(subtopics_router, prefix=settings.API_V1_STR)
app.include_router(case_studies_router, prefix=settings.API_V1_STR)
app.include_router(sessions_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to CaseBreaker API"}
