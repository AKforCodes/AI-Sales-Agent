# AI Sales Agent - Backend

This directory contains the FastAPI backend for the AI Sales Agent.

## Setup and Installation

### 1. Prerequisities
- Python 3.9+
- PostgreSQL server running locally or accessible via a URL.
- An OpenAI API Key.

### 2. Setup PostgreSQL
1.  Connect to your PostgreSQL instance.
2.  Create a new database. For example: `CREATE DATABASE sales_db;`
3.  Create a user and grant privileges if necessary.

### 3. Configure Environment
1.  Navigate to the `backend` directory.
2.  Create a file named `.env` by copying the `.env.example` file (if you have one) or creating it from scratch.
3.  Fill in your `DATABASE_URL` and `OPENAI_API_KEY`.
    ```env
    DATABASE_URL="postgresql://user:password@host:port/sales_db"
    OPENAI_API_KEY="sk-..."
    ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
