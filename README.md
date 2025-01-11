# RAG-LLM-for-Jira-Ticket-Analysis
RAG LLM for Jira Ticket Analysis Experiment

Overview

I wanted to experiment with LLMs (Large Language Models) and RAG (Retrieval-Augmented Generation) to see if it was possible to deploy all the required components using containers. When I discovered the Ollama Docker container, I decided to test a few use cases.

One of those use cases was enabling users to interact with Jira incident tickets in a more intuitive way. This project provides a containerized solution that ingests a CSV export of Jira tickets, converts them into a structured format, and allows users to query the data using natural language.

How It Works

This project is built using three main components, all running inside Docker containers:
	1.	Ollama (LLM Container) – Provides the core language model processing.
	2.	Python Backend (FastAPI) – Handles data retrieval and converts Jira CSV data into a structured format for querying.
	3.	React Frontend – A web UI where users can ask questions and receive insights about Jira tickets.

This setup ensures that all data processing remains within the local environment without relying on external APIs or cloud services.

Project Structure

This section describes the key files and directories in this project.

Backend (FastAPI)
	•	backend/Dockerfile – Defines the Python backend container, installing dependencies and setting up FastAPI.
	•	backend/src/main.py – The main FastAPI application that handles API requests.
	•	backend/src/rag_retriever.py – Implements the RAG retrieval logic, processing Jira ticket data and returning relevant information.
	•	backend/requirements.txt – Lists Python dependencies, including uvicorn, pandas, and fastapi.

Frontend (React)
	•	web/Dockerfile – Defines the frontend container, setting up React for the UI.
	•	web/public/index.html – The main HTML template for rendering the web application.
	•	web/src/App.js – The core React component, handling user input and displaying responses.
	•	web/src/index.js – Entry point for the React app.

Data & Processing
	•	docs/sample-docs/my-sample.txt – A sample text file used for testing retrieval.
	•	backend/data/jira_tickets.csv – The raw Jira data (exported as CSV) that gets processed.
	•	backend/src/csv_parser.py – A script that chunks CSV data into structured text for LLM retrieval.

Deployment & Configuration
	•	docker-compose.yaml – Orchestrates all containers (Ollama, Backend, and Frontend) in a single command.

Use Cases & Queries

Once the system is running, users can ask questions like:

Which tickets are currently in ‘In Progress’ status?
How many tickets were closed in the last 7 days?
What is the most frequently affected system?

These queries allow teams to analyze Jira data quickly without manually searching through reports.

How to Run
	1.	Clone the repository:
    2.	Start all services: docker compose up --build
	3.	Access the UI: http://localhost:3000 

Future Enhancements
	•	Better parsing of Jira ticket descriptions and comments.
	•	Enhanced analytics such as trend detection.
	•	Integration with live Jira APIs instead of CSV files.
    •	Transition to Vector DB.
	•	Enhance respnses to determine frequent fix actions.
	•	Integration with Confluence Documentation to find instructions on how to resolve an issue.
