from fastapi import FastAPI, HTTPException, status

from app.schemas import EnrichedLead
from app.supabase_client import save_lead

app = FastAPI(title="Lead Qualification Callback API")


@app.post("/callback", status_code=status.HTTP_201_CREATED)
def receive_callback(lead: EnrichedLead) -> dict:
    try:
        saved_lead = save_lead(lead)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        ) from error

    return {
        "status": "saved",
        "lead": saved_lead,
    }
