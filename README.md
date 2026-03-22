🏥 Patient & Appointment Management System
https://patientmanegment-4.onrender.com/
it will get 1 to 3 mints to get start pls wait untill it will start

A web-based Patient and Appointment Management System built using Django and Django REST Framework.

This project allows managing patients, booking appointments, tracking appointment status, and viewing statistics through a dashboard.
📌 Features
👤 Patient Management

Add new patients

View all patients

Search patient by phone number

Delete patient

📅 Appointment Management

Add appointment linked to a patient

View appointments by phone number

Track appointment status:

Done

Pending

Not Done

📊 Dashboard

Total patients

Total appointments

Done appointments

Pending appointments

Not done appointments

Today's appointments

🔗 REST API

Full CRUD API using Django REST Framework:
/api/patients/

/api/appointments/

🛠 Technologies Used

Python

Django

Django REST Framework

SQLite (default database)
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/bhngvinod18b/patientmanagement.git
cd your-repository-name
2️⃣ Create virtual environment
python -m venv venv
Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install dependencies
pip install django djangorestframework

Or if you have requirements.txt:

pip install -r requirements.txt
4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Run the server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
📁 Project Structure
patient/
│── models.py
│── views.py
│── serializers.py
│── urls.py
│── templates/patient/
📊 Dashboard Logic

The dashboard calculates:

Total patients

Total appointments

Appointment status counts

Today's appointments using:

from datetime import date
today = date.today()
appointments.filter(date=today)
🚀 Future Improvements

User authentication

Pagination for API

Better form validation

UI improvements (Bootstrap)

Role-based access

Appointment reminders

📄 License

This project is open-source and free to use.

If you'd like, I can also:

🔥 Make it more professional for your CV

💼 Optimize it for job applications

⭐ Add badges (Python, Django version, etc.)

🧾 Add API examples with request/response

Tell me what level you want 😊

can u make it onece so that i can copy and paste in git

Yes 👍 Below is a clean, ready-to-copy README.md.
Just copy everything inside and paste it into your README.md file on GitHub.

🏥 Patient & Appointment Management System

A web-based Patient and Appointment Management System built using Django and Django REST Framework.

This project allows users to manage patients, schedule appointments, track appointment status, and view overall statistics through a dashboard.

📌 Features
👤 Patient Management

Add new patients

View all patients

Search patients by phone number

Delete patients

📅 Appointment Management

Create appointments linked to patients

View appointments by phone number

Track appointment status:

Done

Pending

Not Done

📊 Dashboard

Total number of patients

Total number of appointments

Count of Done appointments

Count of Pending appointments

Count of Not Done appointments

View today's appointments

🔗 REST API

Full CRUD API built with Django REST Framework:

/api/patients/

/api/appointments/

Supports:

Create

Retrieve

Update

Delete

Search

Lookup by phone number

🛠 Technologies Used

Python

Django

Django REST Framework

SQLite (default database)

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/bhngvinod18b/patientmanegement.git
cd your-repository-name
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies

If you have a requirements file:

pip install -r requirements.txt

Or install manually:

pip install django djangorestframework
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Run the Server
python manage.py runserver

Open your browser and go to:

http://127.0.0.1:8000/
📁 Project Structure
patient/
│── models.py
│── views.py
│── serializers.py
│── urls.py
│── templates/patient/
│     ├── index.html
│     ├── list.html
│     ├── add.html
│     ├── delete.html
│     ├── search.html
│     ├── appointment.html
│     ├── list_appoint.html
│     └── dashboard.html
📊 Dashboard Logic

The dashboard calculates:

Total patients

Total appointments

Appointment status counts

Today's appointments using:

from datetime import date
today = date.today()
appointments.filter(date=today)
🚀 Future Improvements

User authentication system

API pagination

Better validation and error handling

UI improvements using Bootstrap

Role-based access control

Email or SMS appointment reminders

📄 License

This project is open-source and free to use.
