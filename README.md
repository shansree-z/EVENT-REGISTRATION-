#  ShanEventz Registration Website 

[![Python](https://img.shields.io/badge/PYTHON-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

> **A high-performance, serverless event registration portal with a premium Glassmorphism UI.**

---

## Project Overview
ShanEventz is a custom-branded web application designed for seamless attendee registration. By integrating a **Streamlit** frontend with a **Google Forms** backend, the system achieves a secure, low-latency data pipeline without the need for expensive database hosting.

---

##  Key Features
* **Modern Aesthetic:** Bold Red & Black gradient background with Glassmorphism UI effects.
* **White-Label Experience:** Custom CSS overrides to hide default Streamlit headers and GitHub branding.
* **Smart Data Pipeline:** Real-time data synchronization with Google Sheets via HTTP POST requests.
* **Categorized Selection:** Multiselect interface for Technical and Non-Technical event tracks.

## Technical Architecture
This project follows a **Serverless Architecture**:
* **Frontend:** [Streamlit](https://streamlit.io/) (Python) for UI rendering and state management.
* **Transport:** Python `requests` library for secure data transmission.
* **Backend Storage:** Google Forms API (formResponse) & Google Sheets for data persistence.


## 🗂️Repository Contents
* `app.py`: The core application script featuring custom CSS and submission logic.
* `requirements.txt`: Necessary dependencies (`streamlit`, `requests`).
* `README.md`: Technical documentation and architecture overview.

## ⚙️ Setup & Installation
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/shansree-z/event-registration.git](https://github.com/shansree-z/event-registration.git)
   
