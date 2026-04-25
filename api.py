from fastapi import FastAPI
import docker
import random
from sqlalchemy import create_engine, text

control_engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@control-db:5432/DB"
)

app = FastAPI()

client = docker.from_env()

@app.post("/create")
def create_db():
    port = random.randint(5500, 6000)
    name = f"pg_{port}"

    try:
        container = client.containers.run(
            "postgres:14.5",
            name=name,
            environment={
                "POSTGRES_USER": "user",
                "POSTGRES_PASSWORD": "pass",
                "POSTGRES_DB": "db"
            },
            ports={'5432/tcp': port},
            detach=True
        )

        with control_engine.connect() as conn:
            conn.execute(text("""
                INSERT INTO instances (container_name, port, db_user, db_password, db_name)
                VALUES (:name, :port, :user, :password, :db)
            """), {
                "name": name,
                "port": port,
                "user": "user",
                "password": "pass",
                "db": "db"
            })

            conn.execute(text("""
                INSERT INTO logs (action, container_name, port)
                VALUES (:action, :name, :port)
            """), {
                "action": "create",
                "name": name,
                "port": port
            })

            conn.commit()

        return {
            "container_name": name,
            "port": port
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/list")
def list_dbs():
    with control_engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM instances"))
        return [dict(row._mapping) for row in result]

@app.get("/logs")
def get_logs():
    with control_engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM logs ORDER BY created_at DESC"))
        return [dict(row._mapping) for row in result]