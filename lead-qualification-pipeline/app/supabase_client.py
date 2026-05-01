import httpx

from app.config import get_settings
from app.schemas import EnrichedLead


def build_headers(api_key: str) -> dict:
    headers = {
        "apikey": api_key,
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }

    if api_key.startswith("eyJ"):
        headers["Authorization"] = f"Bearer {api_key}"

    return headers


def save_lead(lead: EnrichedLead) -> dict:
    settings = get_settings()

    url = (
        f"{settings.supabase_url.rstrip('/')}"
        f"/rest/v1/{settings.supabase_table_name}"
    )

    response = httpx.post(
        url,
        headers=build_headers(settings.supabase_service_role_key),
        json=lead.model_dump(),
        timeout=10,
    )

    if response.is_error:
        raise RuntimeError(
            f"Supabase error {response.status_code}: {response.text}"
        )

    data = response.json()

    if not data:
        raise RuntimeError("Supabase insert returned no data.")

    return data[0]
