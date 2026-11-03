# 🛡️ Cyber Threat Detection Dashboard

A Django-based Cyber Threat Detection Dashboard that identifies suspicious IP activity using failed login attempt counts. It provides threat classification, severity analysis, security statistics, and visual charts.

## 🚀 Features

- **IP Monitoring:** Enter and monitor IP addresses.
- **Threat Detection:** Identify suspicious activity based on failed login attempts.
- **Severity Classification:** Classify detected activity as High or Low severity.
- **Dashboard Statistics:** Display total scans, threats, safe activities, and high-severity detections.
- **Threat Analysis Charts:** Visualize threat distribution and security statistics.
- **Detection History:** Store detection records in an SQLite database.

## 🛠️ Technologies Used

- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Data Visualization:** Chart.js
- **Version Control:** Git and GitHub

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/siri138/Cyber-Threat-Detection.git
```

### 2. Navigate to the Django project

```bash
cd Cyber-Threat-Detection/backend/config
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install django djangorestframework
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the dashboard

Visit: http://127.0.0.1:8000/

## 🔍 How It Works

1. Enter an IP address and the number of failed login attempts.
2. Submit the information for analysis.
3. The backend evaluates the failed attempt count.
4. Activity with five or more failed attempts is classified as a high-severity threat.
5. Results are stored in SQLite and reflected in dashboard statistics and charts.

## ⚠️ Note

This is a demonstration project using rule-based detection and manually entered data. It does not currently monitor live network traffic or automatically block malicious IP addresses.

## 👩‍💻 Author

**Vinnakota Rani Sirisha**

GitHub: [siri138](https://github.com/siri138)
