This will be an AI agent that builds code from prompts.

## FastAPI Meal Tracker Example

### How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI server:
   ```bash
   uvicorn autodev-agent.main:app --reload
   ```

### Example Requests

- **Submit a meal:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/meals" -H "Content-Type: application/json" -d '{"name": "Salad", "calories": 350, "timestamp": "2024-05-23T12:00:00"}'
  ```

- **List all meals:**
  ```bash
  curl "http://127.0.0.1:8000/meals"
  ```
