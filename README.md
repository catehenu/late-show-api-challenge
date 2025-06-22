# late-show-api-challenge
# 🎬 Late Show API Challenge

A RESTful API built with Flask, SQLAlchemy, and PostgreSQL for managing episodes of a fictional "Late Show". This project supports basic CRUD operations for episodes, including title, guest, and air date.

---

## 🚀 Features

- List all episodes
- Retrieve a single episode
- Create a new episode
- Update an existing episode
- Delete an episode
- PostgreSQL integration
- Flask-Migrate for database migrations

---

## 📦 Project Structure

late-show-api-challenge/
│
├── server/
│ ├── init.py
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── controllers/
│ │ └── episode_controller.py
│ └── migrations/
│
├── requirements.txt
├── postman_collection.json (optional)
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/late-show-api-challenge.git
cd late-show-api-challenge

📬 API Endpoints
Base URL
bash
Copy
Edit
http://localhost:5000/episodes
Endpoints
Method	Endpoint	Description
GET	/	Get all episodes
GET	/<id>	Get one episode
POST	/	Create a new episode
PUT	/<id>	Update an episode
DELETE	/<id>	Delete an episode

Example Payload
json
Copy
Edit
{
  "title": "Back to the Future Special",
  "guest": "Michael J. Fox",
  "air_date": "2025-06-01"
}
📫 Postman Collection (Optional)
You can import postman_collection.json in Postman for testing the endpoints.

🧪 Testing (Manual)
Use curl, Postman, or HTTPie:

bash
Copy
Edit
curl -X POST http://localhost:5000/episodes/ \
     -H "Content-Type: application/json" \
     -d '{"title":"Season Finale","guest":"Chris Evans","air_date":"2025-07-01"}'
✅ TODO / Improvements
Add authentication

Unit tests with pytest

Dockerize the project

Add pagination to GET endpoint

🧑‍💻 Author
Built by [Your Name] — contributions welcome!






