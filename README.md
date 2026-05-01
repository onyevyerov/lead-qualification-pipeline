# Lead Qualification Pipeline

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create `.env` file from `.env.example` and fill in the required values:

```powershell
copy .env.example .env
```

## Run FastAPI

```powershell
uvicorn app.main:app --reload
```

## Expose Local API

Start ngrok in a separate terminal:

```powershell
ngrok http 8000
```

If `ngrok` is not recognized, install it from:

```text
https://ngrok.com/download
```

Then add your authtoken:

```powershell
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

If ngrok was installed manually, run it with the full path:

```powershell
& "C:\Tools\ngrok\ngrok.exe" http 8000
```

Copy the HTTPS forwarding URL and add it to `.env`:

```env
FASTAPI_CALLBACK_URL=https://your-ngrok-url.ngrok-free.app/callback
```

## n8n

Import the workflow:

```text
n8n/workflow.json
```

Update the HTTP Request node URL with your `FASTAPI_CALLBACK_URL`.

Publish the workflow and copy the Production Webhook URL into `.env`:

```env
N8N_WEBHOOK_URL=https://your-n8n-webhook-url
```

## Send Leads

Make sure these are running:

```text
FastAPI
ngrok
published n8n workflow
```

Then run:

```powershell
python scripts/send_leads.py
```

The script sends 5 hardcoded leads to the n8n webhook.