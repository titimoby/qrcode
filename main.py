import streamlit as st
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
import io

st.title("QR code generation")

text_input = st.text_input("What text do you want to encode?")
action_button = st.button("Generate QR code")
image_element = st.image("./Calm.jpg")

if action_button or text_input:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(text_input)
    image_pil = qr.make_image(
        image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer()
    )
    buffer = io.BytesIO()
    image_pil.save(buffer, format="PNG")
    image_element.image(buffer.getvalue())
