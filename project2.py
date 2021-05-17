from app import app,db
from app.models import Users       

@app.shell_context_processor
def make_shell_content():
  return {"db":db,"Users":Users}