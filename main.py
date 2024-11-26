from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User, Game
from database import SessionLocal
import random

app = FastAPI()


# Helper pentru baza de date
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint: Creare utilizator
@app.post("/user_create")
def user_create(username: str, password: str, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}


# Endpoint: Start joc
@app.get("/start")
def start(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_game = Game(user_id=user_id)
    db.add(new_game)
    db.commit()
    return {"game_id": new_game.id}


# Endpoint: Mutare
@app.post("/move")
def move(game_id: int, player_move: str, db: Session = Depends(get_db)):
    if player_move not in ["piatra", "hartie", "foarfeca"]:
        raise HTTPException(status_code=400, detail="Invalid move")

    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    # Alegere aleatorie pentru calculator
    ai_move = random.choice(["piatra", "hartie", "foarfeca"])

    # Logică joc
    result = None
    if player_move == ai_move:
        result = "draw"
    elif (player_move == "piatra" and ai_move == "foarfeca") or \
            (player_move == "hartie" and ai_move == "piatra") or \
            (player_move == "foarfeca" and ai_move == "hartie"):
        game.score_player += 1
        result = "player"
    else:
        game.score_ai += 1
        result = "ai"

    db.commit()

    # Verificare câștigător
    if game.score_player == 2:
        return {"winner": "player", "score": {"player": game.score_player, "ai": game.score_ai}}
    elif game.score_ai == 2:
        return {"winner": "ai", "score": {"player": game.score_player, "ai": game.score_ai}}

    return {"result": result, "ai_move": ai_move, "score": {"player": game.score_player, "ai": game.score_ai}}
