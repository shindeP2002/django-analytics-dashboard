📊 Django Analytics Dashboard

A full-stack analytics tracking system built using Django, Django REST Framework, Chart.js, and Leaflet.js.
This project tracks user events and displays aggregated analytics with interactive visualizations.

🚀 Live Demo:-
👉 https://django-analytics-dashboard-3.onrender.com/

📌 Features :-

Uses Django ORM aggregation instead of manual loops
Track user events (login, button clicks)
Store event data with timestamps
REST APIs for analytics
Aggregated insights using Django ORM (Count, annotate)
Interactive dashboard with charts
India map visualization using Leaflet (GeoJSON)
Admin panel for managing data
Deployed on cloud
🛠️ Tech Stack
Backend: Django, Django REST Framework
Frontend: HTML, CSS, JavaScript
Charts: Chart.js
Maps: Leaflet.js
Database: SQLite
Deployment: Render

📂 Project Structure
django-analytics-dashboard/
│
├── analytics_app/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│ └── admin.py
│
├── analytics_pro/
│ ├── settings.py
│ ├── urls.py
│
├── templates/
│ └── index.html
│
├── static/
├── manage.py
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository

git clone https://github.com/shindeP2002/django-analytics-dashboard.git
cd django-analytics-dashboard

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py migrate

5️⃣ Create Superuser

python manage.py createsuperuser

6️⃣ Run Server

python manage.py runserver

7️⃣ Open in Browser

http://127.0.0.1:8000/

🔐 Admin Panel

http://127.0.0.1:8000/admin/

Use your credentials to:

Add Event Logs
Manage user activity
🔌 API Endpoints
🔹 POST /api/events/

Log a user event

Request:
{
"event_type": "button_click",
"button_name": "login"
}

🔹 GET /api/analytics/summary/

Returns summary analytics

Response:
{
"total_events": 5,
"total_button_clicks": 4,
"total_logins": 1
}

🔹 GET /api/analytics/buttons/

Returns button click analytics

Response:
[
{
"button_name": "login",
"total_clicks": 1
},
{
"button_name": "signup",
"total_clicks": 3
}
]

📊 Dashboard Features
📍 India map visualization
📈 Bar chart for button clicks
📦 Summary section:
Total Events
Total Clicks
Total Logins
🚀 Deployment (Render)

Steps followed:

Push project to GitHub
Connect repository to Render
Add Build Command:
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
Start Command:
gunicorn analytics_pro.wsgi
⚠️ Issues Faced & Solutions
404 Error → Fixed by adding index route
403 Forbidden → Fixed authentication handling
Chart not visible → Added Chart.js CDN
Admin data not visible → Fixed migrations in deployment
Deployment errors → Fixed build command

## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Chart
![Chart](screenshots/chart.png)

### Admin Panel
![Admin](screenshots/admin.png)

### API Response
![API](screenshots/api.png)
![API](screenshots/summaryApi.png)


🧠 Learnings
Django ORM aggregation (Count, annotate)
REST API development using DRF
Frontend-backend integration using Fetch API
Deployment and debugging on cloud
Handling real-world errors

💼 Author
Poonam Shinde
Aspiring Software Developer
