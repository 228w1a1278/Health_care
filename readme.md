# 🏥 Hospital Management System (HMS) - EHR Edition

Welcome to the **Hospital Management System (HMS)**, a highly functional, robust backend web application built with **Python** and **Django**. This project demonstrates complete end-to-end full-stack development, featuring Role-Based Access Control (RBAC), intelligent state management, real-time backend validation, and a built-in Electronic Health Record (EHR) system. Whether you’re a fellow developer or a hiring manager, this project reflects my capabilities in building scalable database architectures, complex routing, and practical clinical workflows.

## 💼 About the Project

The Hospital Management System is a comprehensive tool designed to digitize the patient journey from the front desk to the doctor's office. It replaces chaotic paper systems with a seamless, role-divided web portal. Receptionists can manage queues and handle rejected appointments through a dynamic alert system, while doctors have access to a clinical dashboard. The core of the application features an automated Electronic Health Record (EHR) engine that tracks patient vitals and lab reports across multiple visits, entirely powered by Django's ORM and SQLite.

## 🔑 Core Features

- **Role-Based Access Control (RBAC)**: Secure, customized dashboards routing users seamlessly to either the Receptionist Command Center or the Doctor Triage Dashboard based on their Django Auth Group.
- **Smart Appointment Booking & Clash Validation**: Backend logic automatically queries the database to prevent double-booking a doctor for the exact same date and time.
- **Dynamic Alert & Rescheduling System**: If a doctor rejects a patient, the receptionist receives an immediate dashboard alert. The reschedule protocol auto-fills patient data and uses JavaScript to dynamically hide the rejecting doctor from future selection.
- **Electronic Health Records (EHR)**: A smart, scrollable history module that automatically fetches and displays a patient's past completed visits, symptoms, and lab test reports during a live consultation.
- **"PDF-Ready" Prescriptions**: Completed appointments dynamically generate a clean, official hospital letterhead view optimized for native browser printing (`Ctrl+P`).
- **One-Click Mock Data Injection**: Includes a custom Python script (`setup_mock_data.py`) to instantly populate the database with groups, test credentials, and rich medical histories for immediate testing without manual entry.

## 🔧 Tech Stack

- **Backend Framework**: Python, Django
- **Database**: SQLite (Django Default ORM)
- **Frontend / UI**: HTML5, Bootstrap 5 (CDN)
- **Interactivity**: Vanilla JavaScript
- **Version Control**: Git & GitHub

## 📽️ Working of the App

- 🧑‍💻 **Receptionist Mode**: Full CRUD capabilities for the daily queue. Add new patients, monitor the status of appointments (Pending, Accepted, Rejected, Completed), and quickly reassign rejected patients using smart-filtered dropdowns.
- 🩺 **Doctor Mode**: Read and Write access to clinical data. Doctors can accept or reject pending appointments, mark no-shows, and write detailed prescriptions while cross-referencing past EHR data.
- 🔄 **State Machine Logic**: Appointments dynamically flow through strict lifecycle states (`Pending` -> `Accepted`/`Rejected` -> `Completed`/`Cancelled`), immediately updating UI elements across different user dashboards.
- 💾 **Database Persistence**: All patient histories, user roles, and appointment updates are securely committed to the SQLite database via Django Models.

## 🔮 Future Enhancements

- Integrate a live backend database like PostgreSQL for large-scale production deployment.
- Implement WebSocket integration (Django Channels) for instant, page-refresh-free notification pop-ups.
- Add advanced user authentication features like JWT, Two-Factor Authentication (2FA), and password reset flows.
- Integrate automated email or SMS reminders for patients using Celery and Redis.

## Contact

I’m open to opportunities and collaborations!  
📧 Reach out to me at [saicharanchilla7777@gmail.com](mailto:saicharanchilla7777@gmail.com)  
🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/saicharan-chilla-2b2201271/)  
💻 Check out more of my work on [GitHub](https://github.com/228w1a1278)
