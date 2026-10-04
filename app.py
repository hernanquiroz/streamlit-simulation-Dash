
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Laboratorio de Óptica Interactivo", layout="wide")

# Título principal
st.title("🔬 Laboratorio de Óptica Interactivo")
st.markdown("---")

# Sidebar para navegación
st.sidebar.title("📚 Temas de Óptica")
tema = st.sidebar.radio(
    "Selecciona un tema:",
    ["Espectro Electromagnético", "Reflexión y Refracción (Ley de Snell)", 
     "Dispersión de la Luz", "El Arco Iris"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Para estudiantes de Licenciatura en Ciencias Naturales**")

# ============================================
# TEMA 1: ESPECTRO ELECTROMAGNÉTICO
# ============================================
if tema == "Espectro Electromagnético":
    st.header("🌈 Espectro Electromagnético Interactivo")
    
    st.markdown("""
    El espectro electromagnético abarca todas las formas de radiación electromagnética, 
    desde las ondas de radio hasta los rayos gamma. La única diferencia entre ellas es 
    su **longitud de onda** y **frecuencia**.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎛️ Controles")
        longitud_onda = st.slider(
            "Longitud de onda (nm)", 
            10, 1000000, 550, 
            help="Mueve el slider para explorar diferentes regiones del espectro"
        )
        
        frecuencia = 3e8 / (longitud_onda * 1e-9)  # c = λν
        
        st.markdown(f"""
        **Propiedades calculadas:**
        - Longitud de onda: **{longitud_onda} nm** ({longitud_onda*1e-9:.2e} m)
        - Frecuencia: **{frecuencia:.2e} Hz**
        - Energía del fotón: **{frecuencia * 6.626e-34:.2e} J**
        """)
        
        if longitud_onda < 10:
            region = "Rayos Gamma"
            color = "#FF0000"
        elif longitud_onda < 400:
            region = "Ultravioleta"
            color = "#8B00FF"
        elif longitud_onda < 700:
            region = "Luz Visible"
            color = "#00FF00"
        elif longitud_onda < 1000:
            region = "Infrarrojo Cercano"
            color = "#FF4500"
        elif longitud_onda < 100000:
            region = "Infrarrojo"
            color = "#FF0000"
        elif longitud_onda < 1000000:
            region = "Microondas"
            color = "#FFD700"
        else:
            region = "Ondas de Radio"
            color = "#0000FF"
        
        st.success(f"✅ **Región del espectro:** {region}")
    
    with col2:
        st.subheader("📊 Visualización")
        
        fig, ax = plt.subplots(figsize=(10, 4))
        espectro_x = np.linspace(10, 1000000, 1000)
        espectro_y = np.ones_like(espectro_x)
        
        colores = []
        for lam in espectro_x:
            if lam < 10:
                colores.append('#FF0000')
            elif lam < 400:
                colores.append('#8B00FF')
            elif lam < 700:
                t = (lam - 400) / 300
                if t < 0.33:
                    colores.append('#FF0000')
                elif t < 0.67:
                    colores.append('#00FF00')
                else:
                    colores.append('#0000FF')
            elif lam < 1000:
                colores.append('#FF4500')
            elif lam < 100000:
                colores.append('#FF0000')
            elif lam < 1000000:
                colores.append('#FFD700')
            else:
                colores.append('#0000FF')
        
        for i in range(len(espectro_x)-1):
            ax.axvspan(espectro_x[i], espectro_x[i+1], color=colores[i], alpha=0.7)
        
        ax.axvline(x=longitud_onda, color='black', linewidth=3, linestyle='--')
        ax.text(longitud_onda, 1.1, f'{longitud_onda} nm', ha='center', fontsize=10, fontweight='bold')
        
        ax.set_xscale('log')
        ax.set_ylim(0, 1.3)
        ax.set_xlabel('Longitud de onda (nm) - Escala logarítmica', fontsize=12)
        ax.set_ylabel('Intensidad relativa', fontsize=12)
        ax.set_title('Espectro Electromagnético Completo', fontsize=14, fontweight='bold')
        ax.set_yticks([])
        
        regiones_pos = {
            'Rayos\nGamma': 5, 'UV': 100, 'Visible': 550, 
            'IR': 10000, 'Micro': 100000, 'Radio': 500000
        }
        
        for nombre, pos in regiones_pos.items():
            ax.text(pos, 0.5, nombre, ha='center', fontsize=8, fontweight='bold', color='white',
                   bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("---")
    st.subheader("📖 Conceptos Clave")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **🔴 Rayos Gamma y X**
        - Longitud de onda: < 10 nm
        - Alta energía
        - Usos: Medicina, astronomía
        """)
    with col2:
        st.markdown("""
        **🟢 Luz Visible**
        - Longitud de onda: 400-700 nm
        - Energía intermedia
        - Única región visible al ojo humano
        """)
    with col3:
        st.markdown("""
        **🔵 Ondas de Radio**
        - Longitud de onda: > 1 mm
        - Baja energía
        - Usos: Comunicaciones, radar
        """)

# ============================================
# TEMA 2: REFLEXIÓN Y REFRACCIÓN
# ============================================
elif tema == "Reflexión y Refracción (Ley de Snell)":
    st.header("🔍 Reflexión y Refracción - Ley de Snell")
    
    st.markdown("""
    Cuando la luz pasa de un medio a otro, cambia de dirección. Este fenómeno se describe 
    mediante la **Ley de Snell**:
    $$n_1 \\sin(\\theta_1) = n_2 \\sin(\\theta_2)$$     """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎛️ Parámetros")
        n1 = st.selectbox("Medio 1 (incidente):", ["Vacío (n=1.00)", "Aire (n=1.0003)", "Agua (n=1.33)", "Vidrio (n=1.50)", "Diamante (n=2.42)"], index=2)
        n2 = st.selectbox("Medio 2 (refractado):", ["Vacío (n=1.00)", "Aire (n=1.0003)", "Agua (n=1.33)", "Vidrio (n=1.50)", "Diamante (n=2.42)"], index=3)
        
        n1_val = float(n1.split('=')[1].split(')')[0])
        n2_val = float(n2.split('=')[1].split(')')[0])
        
        angulo_inc = st.slider("Ángulo de incidencia (°)", 0, 89, 45, help="Ángulo entre el rayo incidente y la normal")
    
    with col2:
        st.subheader("📊 Cálculos")
        angulo_inc_rad = np.radians(angulo_inc)
        sin_angulo_ref = (n1_val / n2_val) * np.sin(angulo_inc_rad)
        
        if sin_angulo_ref <= 1:
            angulo_ref_rad = np.arcsin(sin_angulo_ref)
            angulo_ref = np.degrees(angulo_ref_rad)
            st.markdown(f"""
            **Resultados:**
            - Ángulo de incidencia: **{angulo_inc}°**
            - Ángulo de reflexión: **{angulo_inc}°**
            - Ángulo de refracción: **{angulo_ref:.2f}°**
            """)
            if n1_val > n2_val:
                angulo_critico = np.degrees(np.arcsin(n2_val / n1_val))
                st.warning(f"⚠️ **Ángulo crítico:** {angulo_critico:.2f}°")
                if angulo_inc >= angulo_critico:
                    st.error("🚨 **¡REFLEXIÓN TOTAL INTERNA!**")
        else:
            st.error("🚨 **REFLEXIÓN TOTAL INTERNA** - No hay refracción")
            angulo_ref = None
        
        st.markdown(f"""
        **Aplicando Ley de Snell:**
        $$\\theta_2 = \\arcsin\\left(\\frac{{{n1_val} \\times \\sin({angulo_inc}°)}}{{{n2_val}}}\\right)$$         """)
    
    st.subheader("🎨 Simulación Visual")
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axhline(y=0, color='black', linewidth=2)
    ax.text(0.5, 0.1, f'Medio 1: {n1}', ha='center', fontsize=12, fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(0.5, -0.1, f'Medio 2: {n2}', ha='center', fontsize=12, fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    ax.plot([0, 0], [-1, 1], 'k--', linewidth=1, label='Normal')
    
    longitud_rayo = 0.8
    x_inc = -longitud_rayo * np.sin(angulo_inc_rad)
    y_inc = longitud_rayo * np.cos(angulo_inc_rad)
    ax.annotate('', xy=(0, 0), xytext=(x_inc, y_inc), arrowprops=dict(arrowstyle='->', color='red', lw=3))
    
    x_ref = longitud_rayo * np.sin(angulo_inc_rad)
    y_ref = longitud_rayo * np.cos(angulo_inc_rad)
    ax.annotate('', xy=(x_ref, y_ref), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='orange', lw=3))
    
    if angulo_ref is not None:
        angulo_ref_rad_calc = np.radians(angulo_ref)
        x_refr = longitud_rayo * np.sin(angulo_ref_rad_calc)
        y_refr = -longitud_rayo * np.cos(angulo_ref_rad_calc)
        ax.annotate('', xy=(x_refr, y_refr), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=3))
    
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Reflexión y Refracción de la Luz', fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)

# ============================================
# TEMA 3: DISPERSIÓN DE LA LUZ
# ============================================
elif tema == "Dispersión de la Luz":
    st.header("🌈 Dispersión de la Luz - El Prisma")
    
    st.markdown("""
    La **dispersión** es el fenómeno por el cual la luz blanca se separa en sus colores componentes.
    **Ley de Cauchy:** $n(\\lambda) = A + \\frac{B}{\\lambda^2}$     """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎛️ Parámetros del Prisma")
        angulo_prisma = st.slider("Ángulo del prisma (°)", 30, 75, 60)
        angulo_inc_prisma = st.slider("Ángulo de incidencia (°)", 0, 80, 45)
        material = st.selectbox("Material del prisma:", ["Vidrio crown (n≈1.52)", "Vidrio flint (n≈1.62)", "Diamante (n≈2.42)", "Agua (n≈1.33)"], index=0)
    
    with col2:
        st.subheader("📊 Dispersión Cromática")
        longitudes_onda = {'Violeta': (380, 1.532), 'Azul': (450, 1.528), 'Verde': (520, 1.525), 'Amarillo': (580, 1.523), 'Naranja': (620, 1.521), 'Rojo': (700, 1.518)}
        st.markdown("**Índices de refracción por color:**")
        for color, (lam, n) in longitudes_onda.items():
            st.markdown(f"- **{color}** (λ={lam}nm): n={n:.3f}")
    
    st.subheader("🎨 Simulación del Prisma")
    fig, ax = plt.subplots(figsize=(14, 8))
    angulo_prisma_rad = np.radians(angulo_prisma)
    altura_prisma = 0.6
    base_prisma = 2 * altura_prisma * np.tan(angulo_prisma_rad / 2)
    
    vertice_sup = (0, altura_prisma)
    vertice_izq = (-base_prisma/2, -altura_prisma/2)
    vertice_der = (base_prisma/2, -altura_prisma/2)
    prisma = plt.Polygon([vertice_sup, vertice_izq, vertice_der], fill=True, facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.3)
    ax.add_patch(prisma)
    
    colores_rgb = {'Violeta': '#8B00FF', 'Azul': '#0000FF', 'Verde': '#00FF00', 'Amarillo': '#FFFF00', 'Naranja': '#FFA500', 'Rojo': '#FF0000'}
    angulo_inc_rad = np.radians(angulo_inc_prisma)
    
    for color, (lam, n_color) in longitudes_onda.items():
        x_entrada = -base_prisma/4
        y_entrada = 0
        ax.annotate('', xy=(x_entrada, y_entrada), xytext=(-1.5, 0.3), arrowprops=dict(arrowstyle='->', color=colores_rgb[color], lw=2))
        
        angulo_ref_interno = np.arcsin(np.sin(angulo_inc_rad) / n_color)
        x_salida = base_prisma/4
        y_salida = -0.1
        ax.plot([x_entrada, x_salida], [y_entrada, y_salida], color=colores_rgb[color], linewidth=2, alpha=0.7)
        
        angulo_salida = angulo_ref_interno * 1.5
        x_final = x_salida + 0.8 * np.sin(angulo_salida)
        y_final = y_salida - 0.8 * np.cos(angulo_salida)
        ax.annotate('', xy=(x_final, y_final), xytext=(x_salida, y_salida), arrowprops=dict(arrowstyle='->', color=colores_rgb[color], lw=2))
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)

# ============================================
# TEMA 4: EL ARCO IRIS
# ============================================
elif tema == "El Arco Iris":
    st.header("🌈 El Arco Iris - Formación y Física")
    
    st.markdown("""
    El arco iris es causado por la **reflexión, refracción y dispersión** de la luz solar en las gotas de agua.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎛️ Parámetros")
        angulo_sol = st.slider("Altura del sol sobre el horizonte (°)", 0, 42, 20)
        tamano_gota = st.slider("Tamaño de gota (mm)", 0.5, 5.0, 2.0, 0.1)
        intensidad = st.slider("Intensidad de la luz", 0.3, 1.0, 0.8, 0.1)
    
    with col2:
        st.subheader("📐 Ángulos Característicos")
        st.markdown("""
        **Arco Iris Primario:** 42° desde la antisolar.
        **Arco Iris Secundario:** 51° desde la antisolar.
        """)
        if angulo_sol > 42:
            st.warning("⚠️ El arco iris no es visible con el sol a más de 42°")
        else:
            st.success(f"✅ Condiciones favorables: Sol a {angulo_sol}°")
    
    st.subheader("🎨 Simulación del Arco Iris")
    fig, ax = plt.subplots(figsize=(14, 8))
    
    for i in range(100):
        color_sky = (0.5 + 0.5*i/100, 0.7 + 0.3*i/100, 1.0)
        ax.axhspan(i/100 * 4 - 2, (i+1)/100 * 4 - 2, color=color_sky, alpha=0.3)
    
    ax.axhspan(-2, -1, color='green', alpha=0.3)
    
    angulo_sol_rad = np.radians(angulo_sol)
    sol = plt.Circle((-3, 3 * np.sin(angulo_sol_rad)), 0.3, color='yellow', zorder=5)
    ax.add_patch(sol)
    
    if angulo_sol <= 42:
        angulos_colores = {'Rojo': 42, 'Naranja': 41, 'Amarillo': 40, 'Verde': 39, 'Azul': 38, 'Violeta': 37}
        colores_rgb = {'Rojo': '#FF0000', 'Naranja': '#FFA500', 'Amarillo': '#FFFF00', 'Verde': '#00FF00', 'Azul': '#0000FF', 'Violeta': '#8B00FF'}
        for color, angulo in angulos_colores.items():
            angulos_arc = np.linspace(0, np.pi, 100)
            x_arc = 2.5 * np.cos(angulos_arc)
            y_arc = 2.5 * np.sin(angulos_arc)
            ax.plot(x_arc, y_arc, color=colores_rgb[color], linewidth=8 * intensidad, alpha=0.6 * intensidad)
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2, 4)
    ax.set_aspect('equal')
    plt.tight_layout()
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🎓 Laboratorio de Óptica Interactivo | Licenciatura en Ciencias Naturales</p>
    <p>Desarrollado con Streamlit + Python + Matplotlib</p>
</div>
""", unsafe_allow_html=True)
