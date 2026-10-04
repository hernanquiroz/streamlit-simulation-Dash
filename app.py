
import streamlit as st

st.title("¡Hola! Mi primera app de física")
st.write("Laboratorio de Óptica Interactivo")

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"¡Bienvenido {nombre} al laboratorio de óptica!")

st.markdown("---")
st.header("🌈 Espectro Electromagnético")
st.write("Mueve el slider para ver diferentes longitudes de onda")

longitud = st.slider("Longitud de onda (nm)", 10, 1000, 550)
st.write(f"Longitud seleccionada: **{longitud} nm**")

if longitud < 400:
    st.info("🟣 Ultravioleta")
elif longitud < 700:
    st.success("🟢 Luz Visible")
else:
    st.warning("🔴 Infrarrojo")
