# Bank Statement Analyser – Installation and Setup Guide

This guide walks you through setting up and running the **Bank Statement Analyser** project on a new system. Follow the steps in order.

---

## 1. Project Overview

**Bank Statement Analyser** is a full-stack web application that:

- Lets users **upload** bank statements (PDF, CSV).
- **Parses** and **processes** transactions with bank identification and structuring.
- **Categorizes** transactions and supports **manual adjustments**.
- Provides a **dashboard** with summaries, category breakdowns, monthly views, and **reporting/exports** (e.g. PDF, CSV).
- Uses **Clerk** for authentication and enforces **privacy** and data retention preferences.

The app has a **Vue 3 + Vite** frontend and a **Django 6** REST API backend, with SQLite as the database.

---

## 2. Detected Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Vue 3, Vue Router, Pinia, Vite 7 |
| **Frontend UI** | Tailwind CSS v4, Lucide Vue icons, Chart.js / vue-chartjs |
| **Frontend Auth** | Clerk (@clerk/vue) |
| **Backend** | Django 6.0, Django REST Framework |
| **Backend Auth** | Clerk (JWT via `ClerkAuthentication`) |
| **Database** | SQLite3 |
| **Backend libs** | pandas, openpyxl, PyPDF2, Pillow, reportlab, numpy, requests, PyJWT |
| **Build / Dev** | Vite (frontend), npm (Node), pip/venv (Python) |
| **Dependency managers** | npm / package.json (frontend), pip / requirements.txt (backend) |

---

## 3. Prerequisites

Install the following **before** cloning or running the project:

| Software | Purpose | Recommended version |
|----------|---------|----------------------|
| **Node.js** | Frontend build and dev server | `^20.19.0` or `>=22.12.0` (see `package.json` engines) |
| **npm** | Frontend dependencies | Comes with Node.js (v10+) |
| **Python** | Backend (Django) | **3.10+** (Django 6 supports 3.10, 3.11, 3.12) |
| **pip** | Backend dependencies | Latest |
| **Git** | Clone repository | Any recent version |

**Check versions:**

```bash
node -v
npm -v
python --version
pip --version
```

---

## 4. Project Setup

### 4.1 Clone the repository

```bash
git clone <repository-url>
cd bank_statement_analyser-1
```

Replace `<repository-url>` with your actual repo URL (e.g. `https://github.com/your-org/bank_statement_analyser-1.git`).

### 4.2 Backend setup

1. **Create and activate a virtual environment** (recommended):

   **Windows (PowerShell):**
   ```powershell
   cd backend
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **Windows (Command Prompt):**
   ```cmd
   cd backend
   python -m venv venv
   venv\Scripts\activate.bat
   ```

   **macOS / Linux:**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` has encoding issues (e.g. UTF-16 BOM), run:

   ```bash
   pip install Django==6.0.1 djangorestframework==3.16.1 django-cors-headers==4.9.0 PyJWT==2.11.0 pandas openpyxl PyPDF2 Pillow reportlab numpy requests
   ```

   Then install the rest from the file or add any missing packages from the list in section 2.

3. **Remain in the `backend` directory** for the next steps (migrations and run server).

### 4.3 Frontend setup

From the **project root** (not inside `backend`):

```bash
npm install
```

No separate frontend directory; the Vue app lives at the repo root.

---

## 5. Environment Configuration

### 5.1 Backend environment variables

The backend reads these from the environment (no `.env` file is committed; set them in your shell or a local `.env` and load them if you use a tool like `python-dotenv`):

| Variable | Required | Description |
|----------|----------|-------------|
| `DJANGO_SECRET_KEY` | No (has dev default) | Secret for Django; set in production. |
| `CLERK_SECRET_KEY` | **Yes** (for auth) | Clerk secret key so the backend can verify JWT tokens. |

Example (PowerShell):

```powershell
$env:DJANGO_SECRET_KEY = "your-secret-key"
$env:CLERK_SECRET_KEY = "sk_test_..."
```

Example (bash):

```bash
export DJANGO_SECRET_KEY="your-secret-key"
export CLERK_SECRET_KEY="sk_test_..."
```

### 5.2 Frontend environment variables

The frontend uses Vite env variables. Create a **`.env`** file in the **project root** (same level as `package.json`). You can copy from the template:

```bash
cp .env.example .env
```

Then edit `.env` and set your keys:

```env
VITE_CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxxxxxxxxx
VITE_API_BASE_URL=http://localhost:8000/api
```

- **`VITE_CLERK_PUBLISHABLE_KEY`** – **Required.** Clerk publishable key; the app throws if this is missing.
- **`VITE_API_BASE_URL`** – Optional; defaults to `http://localhost:8000/api` if not set. Use this to point to your backend API.

Get both keys from the [Clerk Dashboard](https://dashboard.clerk.com) (API Keys section).

---

## 6. Database Setup

The project uses **SQLite**. The database file will be created at `backend/db.sqlite3` when you run migrations.

1. **Ensure you are in the backend directory** and the virtual environment is activated.

2. **Run migrations:**

   ```bash
   cd backend
   python manage.py migrate
   ```

3. **(Optional) Create a superuser** for Django admin:

   ```bash
   python manage.py createsuperuser
   ```

   Then open `http://localhost:8000/admin/` when the server is running.

---

## 7. Running the Application

You need **two processes**: backend and frontend.

### Step 1: Start the backend

From the **backend** directory, with the virtual environment activated:

```bash
cd backend
python manage.py runserver
```

The API will be at **http://localhost:8000**.  
Health check: **http://localhost:8000/api/health/**

### Step 2: Start the frontend

Open a **second terminal**, go to the **project root**, and run:

```bash
npm run dev
```

The app will be at **http://localhost:5173** (or the port Vite shows). The Vite dev server proxies `/uploads`, `/process`, `/results`, `/report`, `/privacy`, `/statements`, and `/categorization` to `http://localhost:8000`.

**Summary of commands:**

| Terminal | Working directory | Command |
|----------|-------------------|---------|
| 1 | `backend` | `python manage.py runserver` |
| 2 | Project root | `npm run dev` |

Then open **http://localhost:5173** in your browser and sign in with Clerk.

---

## 8. Project Folder Structure

```
bank_statement_analyser-1/
├── backend/                    # Django backend
│   ├── manage.py               # Django CLI entry point
│   ├── requirements.txt        # Python dependencies
│   ├── db.sqlite3              # SQLite DB (created after migrate)
│   ├── media/                  # Uploaded files (created at runtime)
│   ├── server/                 # Django project config
│   │   ├── settings.py         # Main settings (DB, CORS, REST, Clerk)
│   │   ├── urls.py             # Root URL config
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── apps/                   # Django apps
│       ├── api/                # Health check and API wiring
│       ├── auth_session/        # Auth/session
│       ├── uploads/            # File upload handling
│       ├── statements/         # Statement models and APIs
│       ├── transactions/       # Transaction models
│       ├── processing/         # Processing jobs and pipeline
│       ├── parsing/            # PDF/Excel/CSV parsers
│       ├── structuring/        # Transaction structuring
│       ├── bank_identification/# Bank detection
│       ├── results/            # Processing results
│       ├── categorization/     # Category rules and AI
│       ├── manual_adjustments/ # User adjustments
│       ├── reporting/          # Reports
│       ├── exports/            # PDF/CSV export
│       ├── computation/        # Totals, monthly, cashflow
│       ├── privacy/            # Privacy and retention
│       └── users/              # User profile and Clerk auth
├── src/                        # Vue frontend source
│   ├── main.js                 # App entry, Pinia, Router, Clerk
│   ├── App.vue
│   ├── router/
│   ├── views/                  # Pages (Login, Upload, Dashboard, etc.)
│   ├── components/
│   ├── layouts/
│   ├── stores/                 # Pinia stores
│   ├── api/                    # API client and endpoint modules
│   └── assets/
├── package.json                # Frontend deps and scripts
├── vite.config.js              # Vite config and API proxy
├── .env                        # Your local env (create from section 5)
└── INSTALLATION.md             # This file
```

---

## 9. Troubleshooting

### Backend

- **`ModuleNotFoundError: No module named 'apps.error_audit'`**  
  The `error_audit` app was removed from `INSTALLED_APPS` in this repo. If you see this, open `backend/server/settings.py` and remove the line `'apps.error_audit',` from the `INSTALLED_APPS` list.

- **`ImproperlyConfigured: CLERK_SECRET_KEY`**  
  Set the `CLERK_SECRET_KEY` environment variable before running `runserver`. Without it, Clerk authentication on the backend may not work.

- **`UnicodeDecodeError` or odd characters when running `pip install -r requirements.txt`**  
  The file may be UTF-16 encoded. Use the `pip install Django==...` command from section 4.2 to install main packages, or re-save `requirements.txt` as UTF-8 and run `pip install -r requirements.txt` again.

- **Port 8000 already in use**  
  Run on another port: `python manage.py runserver 8001`. Then set `VITE_API_BASE_URL=http://localhost:8001/api` in `.env` and ensure CORS in `backend/server/settings.py` allows your frontend origin.

### Frontend

- **"Missing Clerk publishable key"**  
  Add `VITE_CLERK_PUBLISHABLE_KEY=pk_test_...` to a `.env` file in the project root and restart `npm run dev`.

- **API calls return 404 or CORS errors**  
  Ensure the backend is running on port 8000 (or the port in `VITE_API_BASE_URL`) and that `vite.config.js` proxies match your backend. CORS is set for `http://localhost:5173` and `http://127.0.0.1:5173` in `settings.py`.

- **Node version mismatch**  
  Use Node `^20.19.0` or `>=22.12.0` as in `package.json` engines: e.g. `nvm use 20` or install the recommended Node version.

### Database

- **"no such table" or migration errors**  
  Run from `backend`: `python manage.py migrate`. If you changed models, run `python manage.py makemigrations <app_name>` then `python manage.py migrate`.

---

## Quick reference – full setup from scratch

```bash
# 1. Clone and enter project
git clone <repo-url>
cd bank_statement_analyser-1

# 2. Backend
cd backend
python -m venv venv
# Activate venv: .\venv\Scripts\Activate.ps1 (Windows) or source venv/bin/activate (macOS/Linux)
pip install -r requirements.txt
# Set CLERK_SECRET_KEY (and optionally DJANGO_SECRET_KEY)
python manage.py migrate
python manage.py runserver

# 3. Frontend (new terminal, from project root)
# Create .env with VITE_CLERK_PUBLISHABLE_KEY and optionally VITE_API_BASE_URL
npm install
npm run dev
# Open http://localhost:5173
```

This completes the installation and setup guide. For project-specific behaviour (e.g. which file types are supported, how categorization works), refer to the codebase and any other docs in the repository.
