# Social Media Backend Clone using FastAPI

This project is a backend clone of a social media app built using FastAPI for learning purposes. It features routes for posts, users, authentication, and voting. The project is fully deployed on Render and utilizes CI/CD with GitHub Actions, OAuth2 JWT tokens for authorization, and Alembic for database migrations, SQLAlchemy for object relational mapping and much more.

## API Routes

### 1. Post Route

This route handles the creation, deletion, updating, and retrieval of posts.

### 2. Users Route

This route is responsible for creating users and searching for users by their ID.

### 3. Auth Route

This route manages the login system.

### 4. Vote Route

This route manages the voting system, allowing for upvotes and removing votes. Note that there is no logic for downvotes.

## Deployment

The full stack project is deployed on Render and can be accessed at [https://social-media-backend-rbkm.onrender.com](https://social-media-backend-rbkm.onrender.com).


## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YazanGhunaim/social-media-backend.git
   cd social-media-backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Running Migrations

To run Alembic migrations:

```bash
alembic upgrade head
```

## Running Tests

To run the tests:

```bash
pytest
```
