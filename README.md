# 🔁 SkillSwap API — FastAPI Backend

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge\&logo=render\&logoColor=white)](https://render.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()

A **high-performance REST API built with FastAPI** that powers the **SkillSwap platform**.

SkillSwap allows users to **exchange skills instead of money**, matching people who can teach a skill with those who want to learn it.

The backend provides **user skill management, matching algorithms, and analytics endpoints**.

---

# 🌐 Live API

### Base URL

https://fastapi-project-5-skillswap-platform.onrender.com

### Interactive API Documentation

Swagger UI
https://fastapi-project-5-skillswap-platform.onrender.com/docs

ReDoc
https://fastapi-project-5-skillswap-platform.onrender.com/redoc

---

# 🚀 Features

* ⚡ FastAPI asynchronous performance
* 📚 Auto-generated API documentation
* 🔄 Full CRUD operations for skill profiles
* 🔎 Skill search system
* 🤝 Skill exchange matching algorithm
* 📊 Skill popularity analytics
* 🌐 CORS enabled for frontend communication
* 🧩 Lightweight in-memory storage

> Note: Data resets when the server restarts in the current version.

---

# 🏗 Architecture

```
Streamlit Frontend
        │
        ▼
   FastAPI Backend
        │
        ▼
   In-Memory Skill Store
```

Future improvements could include:

* PostgreSQL database
* Redis caching
* Authentication (JWT)
* AI skill recommendations

---

# 📡 API Endpoints

| Method | Endpoint                    | Description                 |
| ------ | --------------------------- | --------------------------- |
| GET    | `/skills`                   | Retrieve all users          |
| GET    | `/skills/{username}`        | Retrieve a specific user    |
| POST   | `/skills/add`               | Add a new skill profile     |
| PUT    | `/skills/update`            | Update user skills          |
| DELETE | `/skills/delete/{username}` | Delete a user               |
| GET    | `/skills/search`            | Search users by skill       |
| GET    | `/skills/match`             | Find skill exchange matches |
| GET    | `/skills/analytics`         | Skill popularity analytics  |

---

# 📥 Example Request

### Add Skill Profile

POST /skills/add

Request body

```json
{
  "username": "alex",
  "can_teach": "python",
  "wants_to_learn": "spanish"
}
```

Response

```json
{
  "message": "Skill added successfully"
}
```

---

# 📂 Project Structure

```
skillswap-backend
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Development

Clone the repository

```
git clone https://github.com/iqroguerex-cpu/skillswap-backend
```

Navigate into project

```
cd skillswap-backend
```

Install dependencies

```
pip install -r requirements.txt
```

Run the API

```
uvicorn main:app --reload
```

Open API docs

```
http://127.0.0.1:8000/docs
```

---

# ☁️ Deployment

The backend is deployed using **Render**.

Render automatically:

* pulls the repository from GitHub
* installs dependencies
* runs the FastAPI server

Start command used:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# 🖥 Frontend

The **SkillSwap dashboard** is built with **Streamlit**.

Frontend App
https://skillswapfrontendbychinmay.streamlit.app/

---

# 👨‍💻 Author

**Chinmay V Chatradamath**

GitHub
https://github.com/iqroguerex-cpu

---

⭐ If you found this project useful, consider **starring the repository**.
