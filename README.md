# Submissions Portal

A modern Django web application for collecting contact submissions, viewing analytics, and integrating with Supabase (PostgreSQL) and Metabase dashboards.

---

## 🚀 Features

- **Django 4.x** web framework
- **Supabase PostgreSQL** database integration
- **Metabase** analytics dashboard embedding
- Responsive, beautiful UI
- Easy deployment and configuration

---

## 🛠 Requirements

- Python 3.8+
- Django 4.x
- PostgreSQL (Supabase recommended)
- pip (Python package manager)
- Optional: Metabase for analytics

---

## ⚡️ Quickstart

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the `demoapp` directory with the following keys:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DATABASE_URL=your-postgres-connection-url

ALLOWED_HOSTS=127.0.0.1,localhost,*

METABASE_SITE_URL=your-metabase-site-url
METABASE_SECRET_KEY=your-metabase-secret-key
METABASE_DASHBOARD_ID=your-metabase-dashboard-id
```

> **Note:** Replace each value with your own credentials.  
> Never commit `.env` files to version control.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the app.

---

## 📊 Metabase Integration

- Configure your `.env` with Metabase credentials.
- The app will embed your Metabase dashboard for real-time analytics.

---

## 🚢 Deployment

- Set `DEBUG=False` in production.
- Update `ALLOWED_HOSTS` for your domain.
- Use secure database URLs and manage secrets safely.

---

## 📝 License

MIT (or your chosen license)

---

## 💡 Support & Contributing

- For issues, open a GitHub issue.
- Pull requests welcome!