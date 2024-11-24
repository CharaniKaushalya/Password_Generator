import random
import string
import streamlit as st


# Password generator function
def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Streamlit UI GUI Interface

st.title("Password Generator")

length = st.slider("Password Length", min_value=6, max_value=32, value=12)
include_uppercase = st.checkbox("Include Uppercase Letters", value=True)
include_numbers = st.checkbox("Include Numbers", value=True)
include_special_chars = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    st.success("Your generated password is:")
    st.code(password)

    #Password_Generator_streamlit.py