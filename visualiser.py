import requests
import streamlit as st

# URL-ul API-ului (modifică dacă nu rulezi local)
API_URL = "http://127.0.0.1:8000"

st.title("Joc Piatră, Hârtie, Foarfecă")

# Secțiunea 1: Creare utilizator
st.header("Creare utilizator")
username = st.text_input("Nume utilizator", key="create_user_username")
password = st.text_input("Parolă", type="password", key="create_user_password")
if st.button("Creează utilizator"):
    response = requests.post(f"{API_URL}/user_create", json={"username": username, "password": password})
    if response.status_code == 200:
        st.success("Utilizator creat cu succes!")
    else:
        st.error(response.json().get("detail", "Eroare la crearea utilizatorului."))

# Secțiunea 2: Start joc
st.header("Start joc")
user_id = st.number_input("Introdu ID-ul utilizatorului", min_value=1, step=1, key="start_game_user_id")
if st.button("Pornește jocul"):
    response = requests.get(f"{API_URL}/start", params={"user_id": user_id})
    if response.status_code == 200:
        game_id = response.json()["game_id"]
        st.session_state["game_id"] = game_id
        st.success(f"Joc creat! ID joc: {game_id}")
    else:
        st.error(response.json().get("detail", "Eroare la crearea jocului."))

# Secțiunea 3: Mutări în joc
if "game_id" in st.session_state:
    st.header(f"Joc activ (ID: {st.session_state['game_id']})")
    player_move = st.radio("Alege mutarea ta", ["piatra", "hartie", "foarfeca"], key="move_selection")
    if st.button("Trimite mutarea"):
        response = requests.post(
            f"{API_URL}/move",
            json={"game_id": st.session_state["game_id"], "player_move": player_move},
        )
        if response.status_code == 200:
            result = response.json()
            if "winner" in result:
                st.success(f"Câștigător: {result['winner']}")
                st.write(f"Scor final: {result['score']}")
                del st.session_state["game_id"]  # Închide jocul
            else:
                st.info(f"Rezultat: {result['result']}")
                st.write(f"Mutarea AI: {result['ai_move']}")
                st.write(f"Scor curent: {result['score']}")
        else:
            st.error(response.json().get("detail", "Eroare la trimiterea mutării."))
