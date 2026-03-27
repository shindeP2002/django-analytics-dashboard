# 📊 Django Analytics Dashboard

## 🚀 Live Demo
👉 [https://your-render-link.onrender.com](https://django-analytics-dashboard-3.onrender.com)

---

## 📌 Overview
A full-stack analytics tracking system built using Django and Django REST Framework.

It tracks user events (login, button clicks) and provides aggregated insights via REST APIs and an interactive dashboard.

---

## 🎯 Features
- Track user activity (login, button clicks)
- REST APIs with authentication
- Aggregated analytics using Django ORM (`Count`, `annotate`)
- Interactive dashboard with Chart.js
- India GeoJSON map visualization using Leaflet

---

## 🔄 How It Works
1. User events are logged via API
2. Data stored in EventLog model
3. Aggregated using Django ORM
4. APIs return processed data
5. Frontend displays analytics via charts & maps

---

## 🛠 Tech Stack
- Backend: Django, Django REST Framework
- Frontend: HTML, JavaScript
- Visualization: Chart.js
- Map: Leaflet.js

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/api/events/` | Log user events |
| GET | `/api/analytics/summary/` | Summary analytics |
| GET | `/api/analytics/buttons/` | Button-wise clicks |

---

## 📷 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Chart
![Chart](screenshots/chart.png)

### API Response
![API](screenshots/api.png)

---

## ⚙️ Setup

```bash
git clone <repo-url>
cd analytics_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
