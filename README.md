# LangChain Persona App (Streamlit + FastAPI + Docker Compose)

## Run with Docker Compose

### Enter your OpenAPI key

```bash
cp .env.example .env
```
Enter your OpenAPI key

### Build app run docker app
```bash
docker-compose up --build
```


Then open:
- Streamlit app: http://localhost:8501
- FastAPI backend: http://localhost:8000/docs


You can test the AI functionality inside the backend container:

```bash
docker exec -it fastapi-backend /bin/sh
$ python langchain_helper.py
Persona (or exit, quit): 
```

