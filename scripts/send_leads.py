import sys
from pathlib import Path

import httpx

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.config import get_settings  # noqa: E402


LEADS = [
    {
        "name": "John Smith",
        "company": "Acme Inc",
        "message": "We are looking for AI automation for our sales team.",
    },
    {
        "name": "Sarah Johnson",
        "company": "Bright Retail",
        "message": "Our ecommerce team wants to automate customer support with AI.",
    },
    {
        "name": "Michael Brown",
        "company": "OldTown Bakery",
        "message": "I need a simple website for my local bakery.",
    },
    {
        "name": "Emily Davis",
        "company": "DataFlow Analytics",
        "message": "We want to integrate OpenAI into our internal reporting system.",
    },
    {
        "name": "Robert Wilson",
        "company": "QuickFix Plumbing",
        "message": "Can you help us create flyers for our plumbing business?",
    },
]


def send_lead(webhook_url: str, lead: dict) -> None:
    response = httpx.post(
        webhook_url,
        json=lead,
        timeout=15,
    )
    response.raise_for_status()

    print(f"Sent lead: {lead['name']} | Status: {response.status_code}")


def main() -> None:
    settings = get_settings()

    if not settings.n8n_webhook_url:
        raise RuntimeError("N8N_WEBHOOK_URL is not set in .env")

    for lead in LEADS:
        send_lead(settings.n8n_webhook_url, lead)


if __name__ == "__main__":
    main()