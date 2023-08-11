from api import create_app
from api.models.models import Base
from api.database import engine
import uvicorn

app = create_app()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)
