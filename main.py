from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

class SignupUser(User):
    confirm_password: str

class Prompt(BaseModel):
    prompt: str

@app.post('/login')
def login(user: User):
    # Implement your login logic here
    return {"message": "Logged in successfully", "username": user.username}

@app.post('/signup')
def signup(user: SignupUser):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match!")
    # Implement your sign-up logic here
    return {"message": "Signed up successfully", "username": user.username}

@app.post('/generate_content')
def generate_content(prompt: Prompt):
    if not prompt.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    # Implement your content generation logic here using GeminiAI
    generated_text = f"Generated content for prompt: {prompt.prompt}"
    return {"text": generated_text}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
