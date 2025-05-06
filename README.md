# 🌍 Language Collector

A Django web application for language enthusiasts to collect and organize vocabulary words across multiple languages.

![Dashboard Screenshot](static/images/screenshot.png)

## ✨ Features

### Core Features
- **User Authentication**: Secure signup/login with profile management
- **Language Tracking**: Add/Edit/Delete languages with country associations
- **Vocabulary Builder**: Store and organize words with translations
- **Country Mapping**: Associate languages with countries where they're spoken

### Stretch Features
- 🃏 Interactive flashcards for vocabulary practice
- 📊 Learning progress dashboard with troll motivation
- 🎤 Audio pronunciation recording (Web Audio API)
- 🏆 Gamification with badges and achievements
- 🔍 Advanced search and filtering

## 🛠️ Tech Stack

**Backend:**
- Python 3.9+
- Django 4.0+
- PostgreSQL/MySQL

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5
- Chart.js (for visualizations)

**DevOps:**
- Docker
- GitHub Actions (CI/CD)
- Heroku/AWS (Deployment)

## 📦 Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- Virtualenv

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/language-collector.git
cd language-collector

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your credentials

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver