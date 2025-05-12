
import streamlit as st
import requests
import os

st.title("AI-Powered Photo Search")

menu = st.sidebar.selectbox("Choose action", ["Upload Photo", "Search"])

API_URL = os.getenv("API_URL", "http://localhost:8000")

if menu == "Upload Photo":
    uploaded_file = st.file_uploader("Choose a photo")
    if uploaded_file:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{API_URL}/upload", files=files)
        st.write(response.json())

elif menu == "Search":
    name = st.text_input("Person Name")
    alone = st.checkbox("Alone")
    age_range = st.slider("Age Range", 0, 100, (0, 100))
    reference_image = st.text_input("Reference Image Filename (already uploaded)")

    if st.button("Search"):
        query = {
            "person_name": name,
            "alone": alone,
            "min_age": age_range[0],
            "max_age": age_range[1],
            "reference_image": reference_image
        }
        response = requests.post(f"{API_URL}/search", json=query)
        st.json(response.json())
