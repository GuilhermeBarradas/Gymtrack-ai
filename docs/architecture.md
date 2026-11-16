
# GymTrack AI Architecture

## 1. Project Overview

GymTrack AI is a gym workout tracking and progress analysis application.

The application allows users to record their workouts, track exercise performance over time, and receive AI-powered insights based on their training history.

## 2. System Components

- **Java Spring Boot:** Main backend API. Handles users, authentication, workout records, exercise data, and deterministic performance metrics.
- **Python FastAPI:** AI service. Handles AI-powered workout analysis and communication with the language model.
- **PostgreSQL:** Relational database. Stores users, exercises, workouts, sets, and analysis records.
- **Gemini:** Large Language Model used to generate informative workout analyses.
- **pgvector:** PostgreSQL extension used for vector storage and similarity search in the RAG system.

## 3. High-Level Architecture

The Java backend is the main entry point for application requests.

It communicates with PostgreSQL to store and retrieve application data.

When a user requests an AI analysis, the Java backend sends the relevant workout metrics to the Python AI service.

The Python service retrieves relevant training documentation using RAG and pgvector, then uses Gemini to generate an informative response.

The AI service returns its analysis to the Java backend.

## 4. Design Principles

- Keep business logic and workout calculations in Java.
- Keep AI integration and RAG logic in Python.
- Use deterministic calculations for workout statistics.
- Do not allow the AI model to modify workout records.
- Keep API keys and secrets outside the source code.
- Use clear separation of responsibilities between services.

## 5. Project Scope

The initial version focuses on workout tracking, historical performance analysis, and informative AI-generated insights.

The application is not intended to provide medical diagnoses, rehabilitation advice, or guaranteed training prescriptions.
