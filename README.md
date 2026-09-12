# AutoEngineer

AutoEngineer is a Flask marketplace that connects customers with automobile engineers in Nigeria.

## Run locally

From this directory, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, fill in the values you need, and start the app:

```powershell
flask --app app run --debug --port 5001
```

Open `http://127.0.0.1:5001` in your browser. Local development uses `autoengineer.db`; it is ignored by Git.

## Deploy on Render

1. Push this folder to a GitHub repository.
2. In Render, choose **New > Blueprint** and connect the repository.
3. Select `render.yaml` and deploy the blueprint.
4. In the Render service settings, set `ADMIN_EMAIL` and `PAYSTACK_SECRET_KEY` as secret environment variables.
5. In Paystack, set the service-payment callback URL to `https://YOUR-RENDER-DOMAIN.onrender.com/payments/callback`, the subscription callback URL to `https://YOUR-RENDER-DOMAIN.onrender.com/subscriptions/callback`, and the webhook URL to `https://YOUR-RENDER-DOMAIN.onrender.com/payments/webhook`.
6. For recurring Premium billing, create Paystack plans priced at NGN 3,000 weekly, NGN 9,000 monthly, and NGN 45,000 annually. Add their plan codes as `PAYSTACK_PREMIUM_WEEKLY_PLAN`, `PAYSTACK_PREMIUM_MONTHLY_PLAN`, and `PAYSTACK_PREMIUM_ANNUAL_PLAN`. Without plan codes, the app still verifies a one-time checkout for each selected period.

The blueprint creates the web service and a PostgreSQL database. Render supplies `DATABASE_URL` and generates `FLASK_SECRET_KEY` automatically.

## GitHub commands

Replace the URL with the new repository URL from GitHub:

```powershell
git add .
git commit -m "Prepare AutoEngineer for Render"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```