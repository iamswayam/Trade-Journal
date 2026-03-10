# 📒 Trade Journal

A Django-based trade journaling application to log, track, and analyze daily trades with P&L calculation and performance insights.

---

## Features

- 📈 Daily trade entry and management
- 💰 Automatic P&L calculation
- 📊 Performance tracking over time
- 🐳 Docker support for easy local setup and deployment
- 🔐 User authentication and per-user trade data

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | HTML, CSS, JavaScript |
| DevOps | Docker, Docker Compose |

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (optional)

### 1. Clone the Repository

git clone https://github.com/iamswayam/Trade-Journal.git
cd Trade-Journal

### 2. Configure Environment Variables

cp .env.example .env

Open .env and fill in your values.

### 3. Run with Docker

docker-compose up --build

Visit http://localhost:8000

### 4. Run without Docker

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## Project Structure

Trade-Journal/
├── tradebook/        # Django project settings
├── myapp/            # Core application
├── static-coll/      # Static files
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker configuration
└── docker-compose.yml

---

## Author

Swayam Siddha Panda — github.com/iamswayam

---

## License

MIT License — free to use, modify and distribute.
