import streamlit as st
import openai
import os
import json
from dotenv import load_dotenv
from utils.data_loader import load_dataset
from utils.get_base64_of_file import get_base64_of_file
from utils.get_chatgpt_response import get_chatgpt_response
from utils.get_geolocation import get_geolocation

st.set_page_config(page_title="AbleAI")

st.markdown(f"""
    <style>
        .rounded-img {{
            border-radius: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }}
    </style>
    <img src="data:image/png;base64,{get_base64_of_file("./images/logo.jpeg")}" alt="Logo" class="rounded-img" style="width:200px; height:200px;">
""", unsafe_allow_html=True)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
datasets = {
    "locations": load_dataset("./dataset/locations.csv"),
    "parking": load_dataset("./dataset/parking.csv"),
    "restrooms": load_dataset("./dataset/restrooms.csv")
}

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "location" not in st.session_state:
    st.session_state["location"] = None

location_data = None

try:
    location_data = get_geolocation()
    if location_data:
        st.session_state["location"] = f"{location_data['lat']}, {location_data['lon']}"
    else:
        st.session_state["location"] = None
except (json.JSONDecodeError, TypeError, KeyError):
    st.session_state["location"] = None


st.title("AbleAI - Asistentul tău personalizat")

if st.session_state["location"]:
    st.markdown("Vom folosi locația ta curentă pentru a-ți oferi cele mai bune răspunsuri.")
else:
    st.info("Locația nu poate fi accesată. Răspunsurile nu vor fi la fel de precise.")

for chat in st.session_state["chat_history"]:
    st.chat_message(chat["role"]).write(chat["content"])

user_message = st.chat_input("Cu ce te putem ajuta?")

if user_message:
    st.session_state["chat_history"].append({"role": "user", "content": user_message})
    st.chat_message("user").write(user_message)

    print(st.session_state["chat_history"])

    with st.spinner("Se generează răspunsul..."):
        response = get_chatgpt_response(user_message, datasets, location_data, st.session_state["chat_history"])
    st.session_state["chat_history"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
    st.rerun()
