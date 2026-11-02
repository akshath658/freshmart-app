# 🥬 FreshMart

A full-stack grocery store inventory management system.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React (Create React App) |
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |

## Features

- CRUD operations for products (Add, View, Update, Delete)
- Search & filter products by name, description, or ID
- Sort by ID, name, price, or quantity
- Real-time stock quantity tracking
- Responsive UI with grocery-themed design
- RESTful API with auto-generated docs (Swagger)

## Project Structure

freshmart-app/
├── main.py              # FastAPI app & routes
├── models.py            # Pydantic schemas
├── database_models.py   # SQLAlchemy models
├── database.py          # DB connection & session
├── requirements.txt     # Python dependencies
└── frontend/
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js       # Main React component
        ├── App.css      # Styles
        └── TaglineSection.js

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 14+

### Backend Setup

    # Create virtual environment
    python -m venv myenv
    myenv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Set up PostgreSQL database
    # Create a database named "fastapi_demo"

    # Run the server
    uvicorn main:app --reload

Backend runs at: http://localhost:8000
API Docs: http://localhost:8000/docs

### Frontend Setup

    cd frontend
    npm install
    npm start

Frontend runs at: http://localhost:3000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /products | Get all products |
| GET | /products/{id} | Get single product |
| POST | /products | Add new product |
| PUT | /products/{id} | Update product |
| DELETE | /products/{id} | Delete product |

## Product Schema

    {
      "id": 1,
      "name": "Bananas (1 dozen)",
      "description": "Fresh Alphonso bananas, naturally ripened",
      "price": 60.00,
      "quantity": 200
    }

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection string | postgresql+psycopg2://postgres:1234@localhost:5432/fastapi_demo |

## Example Store Details

📍 Shop No. 12, Green Valley Market, Main Road, Sector 15, Gurugram, Haryana – 122001
🕐 Mon–Sat: 7 AM – 10 PM | Sun: 8 AM – 9 PM
📞 +91 98765 43210

## License

MIT

---

Built by akshath658   