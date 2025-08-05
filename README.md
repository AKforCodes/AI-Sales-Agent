# AI Sales Agent for Distributors

This project is a fully autonomous AI sales agent designed for distributors. It features a modern chat interface where users can make product inquiries in natural language. The agent can check a local inventory database, provide detailed quotes, and even search the web for products that are not in stock.

The backend is built with FastAPI and LangChain, connecting to a PostgreSQL database. The frontend is a modern, responsive chat application built with Next.js and Tailwind CSS.

## Features

- **Conversational AI Chat:** Interact with the sales agent through a modern, user-friendly chat interface.
- **Autonomous Quoting:** The agent can understand a product request, check inventory, and generate a complete quote with pricing, discounts, and delivery ETAs.
- **Local Inventory Search:** Queries a local PostgreSQL database using robust full-text search to find the best product match.
- **External Web Search:** If a product is not found in the local inventory, the agent automatically searches the web using the Google Custom Search API to provide helpful information.
- **Order Logging:** Automatically logs all generated quotes to an `order_history` table in the database for record-keeping.
- **Inventory Management:** Includes a standalone script to check for products that are below their restocking threshold.
- **Full Stack Application:** Complete separation of concerns between the FastAPI backend and the Next.js frontend.

## Tech Stack

| Area        | Technology                                                              |
| :---------- | :---------------------------------------------------------------------- |
| **Backend** | Python, FastAPI, LangChain, PostgreSQL, Uvicorn, Psycopg2               |
| **Frontend**| Next.js, React, TypeScript, Tailwind CSS, react-hot-toast               |
| **AI/LLM**  | OpenAI (GPT-4) with Tool Calling                                        |
| **APIs**    | Google Custom Search JSON API                                           |
| **DevOps**  | Docker, Virtual Environments (venv)                                     |

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Make sure you have the following software installed:
- Python 3.9+
- Node.js and npm
- PostgreSQL
- Git

### Installation & Setup

**1. Clone the Repository**
```bash
git clone [https://github.com/AKforCodes/AI-Sales-Agent-for-Distributors.git](https://github.com/AKforCodes/AI-Sales-Agent-for-Distributors.git)
cd AI-Sales-Agent-for-Distributors


2. Backend Setup

First, set up the database and the Python environment.

Navigate to the backend directory:

Bash

cd backend
Setup PostgreSQL:

Start your PostgreSQL server.

Connect to it using psql or a GUI tool like pgAdmin.

Create a new database for the project:

SQL

CREATE DATABASE sales_db;
Configure Environment Variables:

Create a .env file in the backend directory.

Add your database URL and API keys to it. Replace the placeholders with your actual credentials.

Code snippet

# backend/.env

# PostgreSQL Database URL
DATABASE_URL="postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/sales_db"

# OpenAI API Key
OPENAI_API_KEY="sk-..."

# Google Custom Search API Keys
GOOGLE_CSE_ID="YOUR_SEARCH_ENGINE_ID_HERE"
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
Setup Python Environment and Dependencies:

Create and activate a Python virtual environment:

Bash

python -m venv venv
# On Windows
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate
Install the required Python packages from the requirements.txt file:

Bash

pip install -r requirements.txt
Seed the Database:
Run the seed script to create the necessary tables and populate them with sample data.

Bash

python scripts/seed_db.py
3. Frontend Setup

Next, set up the Next.js chat interface.

Navigate to the frontend directory (from the project root):

Bash

cd frontend
Configure Environment Variables:

Create a file named .env.local in the frontend directory.

Add the URL of your backend API:

Code snippet

# frontend/.env.local
NEXT_PUBLIC_API_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000)
Install Dependencies:
Install the required Node.js packages from the package.json file.

Bash

npm install
Running the Application
To run the full-stack application, you will need two separate terminals.

1. Terminal 1: Start the Backend

Navigate to the backend directory.

Activate your virtual environment (.\venv\Scripts\Activate.ps1 or source venv/bin/activate).

Start the FastAPI server with Uvicorn:

Bash

uvicorn app.main:app --reload
The backend will be running on http://127.0.0.1:8000.

2. Terminal 2: Start the Frontend

Navigate to the frontend directory.

Start the Next.js development server:

Bash

npm run dev
The frontend will be running on http://localhost:3000.

3. Access the Application

Open your web browser and go to http://localhost:3000.

You can now interact with the AI Sales Agent through the chat interface.

Running with Docker (Backend Only)
You can also run the backend server inside a Docker container.

Build the Docker image from the backend directory:

Bash

docker build -t ai-sales-agent .
Run the container. This command maps the container's port 8000 to your machine's port 8000 and passes the environment variables from your local .env file.

Bash

docker run -p 8000:8000 --env-file .env ai-sales-agent
