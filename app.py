import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Laboratorio de Óptica", layout="wide")
st.title("🔬 Laboratorio de Óptica Interactivo")
st.sidebar.title("📚 Temas")
tema = st.sidebar.radio("Selecciona:", ["Espectro", "Ley de Snell", "Prisma", "Arco Iris"])

if tema == "Espectro":
    st.header("🌈 Espectro Electromagnético")
    lon = st.slider("Longitud de onda (nm)", 10, 1000000, 550)
    freq = 3e8 / (lon * 1e-9)
    st.write(f"Longitud: {lon} nm | Frecuencia: {freq:.2e} Hz")
    
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axhspan(0, 1, color='red', alpha=0.3)
    ax.text(500, 0.5, f'Posición: {lon} nm', ha='center', fontsize=12)
    ax.set_xlim(10, 1000000)
    ax.set_xscale('log')
    st.pyplot(fig)

elif tema == "Ley de Snell":
    st.header("📐 Ley de Snell")
    n1 = st.slider("n1 (medio 1)", 1.0, 2.5, 1.0, 0.01)
    n2 = st.slider("n2 (medio 2)", 1.0, 2.5, 1.5, 0.01)
    ang1 = st.slider("Ángulo incidencia (°)", 0, 89, 45)
    
    import math
    sin_ang2 = (n1/n2) * math.sin(math.radians(ang1))
    if sin_ang2 <= 1:
        ang2 = math.degrees(math.asin(sin_ang2))
        st.success(f"Ángulo refracción: {ang2:.2f}°")
    else:
        st.error("¡Reflexión total interna!")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axhline(0, color='black', linewidth=2)
    ax.plot([0,0], [-1,1], 'k--')
    ax.annotate('', xy=(0,0), xytext=(-0.7, 0.7), arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.annotate('', xy=(0.7, 0.7), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='orange', lw=2))
    if sin_ang2 <= 1:
        ax.annotate('', xy=(0.5, -0.7), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    st.pyplot(fig)

elif tema == "Prisma":
    st.header("🔺 Dispersión en Prisma")
    ang_prisma = st.slider("Ángulo del prisma (°)", 30, 75, 60)
    st.write("La luz blanca se separa en colores al pasar por el prisma")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    triangulo = plt.Polygon([(0, 1), (-1, -0.5), (1, -0.5)], 
                            fill=True, facecolor='lightblue', alpha=0.5, edgecolor='black', linewidth=2)
    ax.add_patch(triangulo)
    
    colores = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    for i, color in enumerate(colores):
        y_offset = (i - 2.5) * 0.1
        ax.annotate('', xy=(1.5, y_offset - 0.3), xytext=(1, y_offset),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    st.pyplot(fig)

elif tema == "Arco Iris":
    st.header(" Arco Iris")
    ang_sol = st.slider("Altura del sol (°)", 0, 42, 20)
    
    if ang_sol > 42:
        st.warning("El arco iris no es visible con el sol tan alto")
    else:
        st.success(f"Arco iris visible a {42 - ang_sol}° sobre el horizonte")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colores = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    for i, color in enumerate(colores):
        radio = 2.5 - i * 0.1
        angulos = np.linspace(0, np.pi, 100)
        x = radio * np.cos(angulos)
        y = radio * np.sin(angulos)
        ax.plot(x, y, color=color, linewidth=8, alpha=0.6)
    
    ax.plot(0, 0, 'ko', markersize=10)
    ax.text(0, -0.3, 'Observador', ha='center')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    st.pyplot(fig)
