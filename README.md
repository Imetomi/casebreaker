# CaseBreaker

CaseBreaker is an AI-guided case study learning platform that helps users master various disciplines through interactive case studies. The platform currently supports case studies in Law, Healthcare, Economics, Finance, and History.

## Features

- Interactive case study exploration across multiple disciplines
- AI-powered chat interface for guided learning
- Rich content organization with fields, subtopics, and cases
- Modern, responsive user interface
- RESTful API backend with SQLite database

## Tech Stack

### Frontend
- **Framework**: Next.js 14 (React)
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI
- **State Management**: React Hooks
- **API Client**: Native fetch
- **Language**: TypeScript

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Migration Tool**: Alembic
- **Package Manager**: Poetry
- **Language**: Python 3.11+

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Node.js 18 or higher
- Poetry (Python package manager)
- npm or yarn

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd casebreaker-backend
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Initialize the database and run migrations:
   ```bash
   poetry run alembic upgrade head
   ```

4. Seed the database with initial data:
   ```bash
   poetry run python seed_data.py
   ```

5. Start the development server:
   ```bash
   poetry run uvicorn casebreaker_backend.main:app --reload
   ```
   The API will be available at http://localhost:8000

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd casebreaker-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   The application will be available at http://localhost:3000

## Project Structure

### Frontend
```
casebreaker-frontend/
├── src/
│   ├── app/              # Next.js app router pages
│   ├── components/       # Reusable React components
│   │   ├── Cases/       # Case study related components
│   │   ├── Chat/        # Chat interface components
│   │   ├── fields/      # Field and subtopic components
│   │   └── ui/          # Common UI components
│   └── lib/             # Utility functions and API client
└── public/              # Static assets
```

### Backend
```
casebreaker-backend/
├── src/
│   └── casebreaker_backend/
│       ├── routers/     # API route handlers
│       ├── models/      # SQLAlchemy models
│       ├── schemas/     # Pydantic schemas
│       └── services/    # Business logic and external services
├── alembic/             # Database migrations
└── tests/              # Test suite
```

## API Documentation

Once the backend server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

The project uses a monorepo structure with two main directories:
- `casebreaker-frontend/`: Next.js frontend application
- `casebreaker-backend/`: FastAPI backend application

Each directory has its own dependencies and can be developed independently.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
