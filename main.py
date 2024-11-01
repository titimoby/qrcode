import streamlit as st
import qrcode as qr
import io

st.title("QR code generation")

text_input = st.text_input("What text do you want to encode?")
action_button = st.button("Generate QR code")
image_element = st.image("./Calm.jpg")

if action_button:
    image_pil = qr.make(text_input)
    buffer = io.BytesIO()
    image_pil.save(buffer, format="PNG")
    image_element.image(buffer.getvalue())
