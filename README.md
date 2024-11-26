Descriere Proiect
Acest proiect este un API REST pentru jocul "Piatră, Hârtie, Foarfecă" implementat cu FastAPI. Jocul include autentificare, suport pentru mai mulți utilizatori și funcționalități pentru a inițializa un joc nou, a face mutări și a verifica rezultatul.

Caracteristici
Crearea utilizatorilor cu nume de utilizator și parolă.
Autentificare bazată pe utilizator pentru inițializarea și continuarea jocurilor.
Alegere aleatorie a mutării calculatorului.
Logica jocului "cel mai bun din trei" (primul care ajunge la două puncte câștigă).
Păstrarea scorului și a stării jocului în baza de date.
Teste unitare pentru validarea funcționalităților API-ului.
Tehnologii Folosite
FastAPI: Framework pentru dezvoltarea API-ului REST.
SQLAlchemy: ORM pentru gestionarea bazei de date.
SQLite: Baza de date utilizată (pentru simplitate).
pytest: Pentru testarea unităților.
Instalare și Configurare

1. Clonare proiect



git clone https://github.com/numele-tau/joc-piatra-hartie-foarfeca.git
cd joc-piatra-hartie-foarfeca

2. Configurare mediu virtual



python3 -m venv venv
source venv/bin/activate  # Pentru Linux/Mac
venv\Scripts\activate     # Pentru Windows

3. Instalare dependințe



pip install -r requirements.txt
4. Configurare baza de date
Baza de date va fi generată automat. Dacă folosești SQLite, fișierul bazei de date (app.db) va fi creat în directorul proiectului.

Utilizare
Pornire Server
Pentru a porni serverul local:



uvicorn main:app --reload
API-ul va fi disponibil la: http://127.0.0.1:8000

Testare API
Poți folosi Swagger UI pentru a testa endpoint-urile, disponibil la: http://127.0.0.1:8000/docs

Endpoint-uri Disponibile
POST /user_create

Creează un utilizator nou.
Input JSON:
json

{
  "username": "nume_utilizator",
  "password": "parola"
}
Răspuns:
json

{
  "message": "User created successfully"
}
GET /start

Creează un joc nou pentru utilizatorul autentificat.
Parametru: user_id (ID-ul utilizatorului).
Răspuns:
json

{
  "game_id": 1
}
POST /move

Trimite o mutare în joc.
Input JSON:
json

{
  "game_id": 1,
  "player_move": "piatra"
}
Răspuns (scor intermediar):
json

{
  "result": "player",
  "ai_move": "hartie",
  "score": {
    "player": 1,
    "ai": 0
  }
}
Răspuns (final):
json

{
  "winner": "player",
  "score": {
    "player": 2,
    "ai": 1
  }
}
Cum este Implementat
Modele (Models):

User: Reprezintă utilizatorii din sistem.
Game: Reprezintă un joc cu scorul aferent.
Baza de date (SQLite):

Configurată cu ajutorul SQLAlchemy.
Conține două tabele:
users: pentru utilizatori.
game: pentru scoruri și starea fiecărui joc.
Logica jocului:

Mutările valide sunt: piatra, hartie, foarfeca.
Alegerea calculatorului este generată aleatoriu.
Scorurile sunt actualizate în baza de date după fiecare mutare.
Jocul se termină când un jucător ajunge la 2 puncte.
Testare:

S-au scris teste pentru endpoint-uri folosind pytest.
Exemple:
Creare utilizator.
Start joc.
Mutări și verificarea câștigătorului.
Cum rulez testele?
Pentru a rula toate testele:


pytest
Îmbunătățiri posibile
Adăugarea autentificării cu token-uri JWT.
Extinderea API-ului pentru istoric jocuri.
Suport pentru mai multe tipuri de jocuri.
