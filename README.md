### ⚡ FuelFlow Pro
The High-Performance Nutrition Engine for Athletic Organizations
FuelFlow Pro is a robust, server-side rendered (SSR) management platform built with Django. Designed for sports complexes, training centers, and athletic teams, it streamlines the complex task of nutrition scheduling. By bridging the gap between professional dietetics and daily athletic training, FuelFlow Pro ensures that every athlete is fueled for peak performance through a seamless, intuitive web interface.

### 🚀 Key Features
Performance Scheduling: A dynamic interface for creating and managing periodized nutrition blocks.

Integrity Logic: Built-in validation engine to prevent scheduling conflicts and ensure dietary consistency.

Professional Reporting: Automated high-fidelity PDF generation for offline team distribution.

SaaS-Ready Payments: Integrated Razorpay gateway for secure membership renewals and team-wide subscriptions.

Administrative Oversight: Comprehensive dashboard for organization leads to monitor and manage team-wide fueling strategies.

### 🛠 Tech Stack & Architecture

##### Backend: Python 3.x / Django 5.x (Monolithic SSR Architecture)

##### Frontend: Django Template Language (DTL) / Tailwind CSS / Modern ES6+ JavaScript

##### Database: PostgreSQL (Production) / SQLite (Development)

##### Deployment: Vercel / AWS S3 (Static Asset Management)

### 🔐 Demo Access
```
Username: testuser
Password: test_12345
```
### 💻 Engineering Setup
1. Clone & Environment
```
git clone https://github.com/jomerventolero/fuelflow-pro
cd fuelflow-pro
python -m venv venv
```

### 1. Activation
```
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
### 2. Dependency Management
```
pip install -r requirements.txt
```
### 3. Environment Configuration
Create a .env file in the root directory to manage secure credentials:

```
# SMTP Configuration for Team Notifications
EMAIL_HOST_USER = 'your-email@provider.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```
### 4. Database & Static Assets
``` bash
python manage.py migrate
python manage.py collectstatic
```
### 5. Launch Development Server
``` bash
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/ to access the local instance.