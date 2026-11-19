import streamlit as st
from datetime import date
import os, json, base64
from PIL import Image

st.set_page_config(page_title="Marle Nails & Beauty", page_icon="👑", layout="wide")

# --- GUARDADO PERMANENTE ---
os.makedirs("data", exist_ok=True)
FILE_SERV = "data/servicios.json"
FILE_GAL = "data/galeria.json"

def cargar(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r") as f:
            try: return json.load(f)
            except: return []
    return []

def guardar(ruta, datos):
    with open(ruta, "w") as f:
        json.dump(datos, f)

if 'servicios' not in st.session_state:
    st.session_state.servicios = cargar(FILE_SERV)
if 'galeria' not in st.session_state:
    st.session_state.galeria = cargar(FILE_GAL)
if 'es_admin' not in st.session_state:
    st.session_state.es_admin = False

def img_a_base64(file):
    return base64.b64encode(file.getvalue()).decode()

def base64_a_img(b64):
    return base64.b64decode(b64)

CLAVE_ADMIN = "marle123"

# --- DISEÑO HERMOSO ---
st.markdown("""
<style>
    .main { background-color: #FFF5F8; }
    h1 { color: #C2185B; text-align: center; font-family: 'Georgia'; text-shadow: 2px 2px #FFD700; }
    h2, h3 { color: #AD1457; text-align: center; }
    .promo-box {
        background: linear-gradient(135deg, #FF80AB, #FF4081, #FFD700);
        padding: 25px; border-radius: 20px; text-align: center; color: white;
        box-shadow: 0 8px 20px rgba(255,64,129,0.4); margin: 15px 0;
    }
    .card {
        background: white; padding: 20px; border-radius: 20px;
        border: 2px solid #F8BBD0; box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        text-align: center; margin: 10px;
    }
    .gold-text { color: #B8860B; font-weight: bold; }
    .stButton > button { background: linear-gradient(135deg, #EC407A, #FFD700); color: white; border-radius: 20px; font-weight: bold; border: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>👑 MARLE NAILS & BEAUTY 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>✨ Belleza que inspira | Barranquilla ✨</h3>", unsafe_allow_html=True)
st.markdown("""
<div class="promo-box">
    <h2 style="color:white;">💖 ¿SUEÑAS CON UN CABELLO LISO, BRILLANTE Y SIN FRIZZ? 💖</h2>
    <p style="font-size:20px;">¡Yo lo hago realidad! ✨ Mira mis trabajos reales abajo 👇</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="card"><h3>💇‍♀️ KERATINA</h3><p>Cabello liso como espejo ✨</p><p class="gold-text">⭐ LA MÁS PEDIDA ⭐</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><h3>💅 UÑAS</h3><p>Diseños que enamoran 💖</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><h3>👁️ PESTAÑAS</h3><p>Mirada que impacta 😍</p></div>', unsafe_allow_html=True)

st.sidebar.title("💅 Menú Marle")
menu = st.sidebar.selectbox("¿Qué quieres ver?", ["Ver Mi Trabajo 💖", "🔒 Soy Marle - Entrar como Admin"])

if menu == "🔒 Soy Marle - Entrar como Admin":
    if not st.session_state.es_admin:
        st.markdown("### 🔒 Zona Privada Solo Para Marle - Baja un poquito 👇")
        clave = st.text_input("Escribe tu contraseña", type="password")
        if st.button("Entrar 👑"):
            if clave == CLAVE_ADMIN:
                st.session_state.es_admin = True
                st.rerun()
            else: st.error("Contraseña incorrecta")
    else:
        st.success("¡Hola Marle! Modo Admin 👑")
        if st.button("Cerrar sesión"):
            st.session_state.es_admin = False
            st.rerun()
        menu_admin = st.selectbox("Panel Privado - SOLO TU", ["Agregar Servicio Privado", "📸 Subir Trabajo Realizado", "Mi Ganancia Total - SOLO YO"])

        if menu_admin == "Agregar Servicio Privado":
            st.subheader("➕ Agregar Servicio - PRIVADO, NO SE BORRA")
            with st.form("form"):
                clienta = st.text_input("Nombre Clienta")
                servicio = st.selectbox("Servicio", ["Aplicación de KERATINA", "Uñas", "Pestañas", "Otro"])
                inversion = st.number_input("Inversión - SOLO TU", min_value=0, value=40500)
                cobrado = st.number_input("Cobrado - SOLO TU", min_value=0, value=120000)
                fecha = st.date_input("Fecha", value=date.today())
                if st.form_submit_button("💖 Guardar Para Siempre"):
                    ganancia = cobrado - inversion
                    margen = (ganancia / cobrado * 100) if cobrado > 0 else 0
                    st.session_state.servicios.append({"clienta": clienta, "servicio": servicio, "inversion": inversion, "cobrado": cobrado, "ganancia": ganancia, "margen": margen, "fecha": str(fecha)})
                    guardar(FILE_SERV, st.session_state.servicios)
                    st.success(f"¡Guardado PARA SIEMPRE! Ganaste ${ganancia:,.0f} 💖")
                    st.balloons()

        if menu_admin == "📸 Subir Trabajo Realizado":
            st.subheader("📸 Subir Trabajo - Este SI lo ve el público y NO se borra")
            with st.form("form_fotos"):
                clienta_foto = st.text_input("Nombre clienta")
                servicio_foto = st.selectbox("Qué le hiciste", ["KERATINA", "Uñas", "Pestañas", "Otro"])
                col1, col2 = st.columns(2)
                with col1: antes = st.file_uploader("📷 Foto ANTES", type=["jpg","jpeg","png"])
                with col2: despues = st.file_uploader("✨ Foto DESPUÉS", type=["jpg","jpeg","png"])
                if st.form_submit_button("💖 Publicar Para Siempre"):
                    if antes and despues and clienta_foto:
                        item = {"clienta": clienta_foto, "servicio": servicio_foto, "antes_b64": img_a_base64(antes), "despues_b64": img_a_base64(despues)}
                        st.session_state.galeria.append(item)
                        guardar(FILE_GAL, st.session_state.galeria)
                        st.success(f"¡Trabajo de {clienta_foto} guardado PARA SIEMPRE! 💖")
                    else: st.warning("Sube las 2 fotos y el nombre 🙏")

        if menu_admin == "Mi Ganancia Total - SOLO YO":
            total_g = sum([s.get("ganancia",0) for s in st.session_state.servicios])
            total_i = sum([s.get("inversion",0) for s in st.session_state.servicios])
            total_c = sum([s.get("cobrado",0) for s in st.session_state.servicios])
            col1, col2, col3 = st.columns(3)
            col1.metric("💰 Ganancia Total", f"${total_g:,.0f}")
            col2.metric("💸 Invertido", f"${total_i:,.0f}")
            col3.metric("💖 Cobrado", f"${total_c:,.0f}")

if menu == "Ver Mi Trabajo 💖":
    st.markdown("## ✨ TRABAJOS YA REALIZADOS - 100% REALES ✨")
    if not st.session_state.galeria:
        st.info("Pronto verás aquí mis transformaciones ✨")
    else:
        for item in reversed(st.session_state.galeria):
            st.markdown(f"### 👑 {item['clienta']} - {item['servicio']} ✨")
            c1, c2 = st.columns(2)
            try:
                with c1:
                    st.markdown("**ANTES 😱**")
                    st.image(base64_a_img(item['antes_b64']), use_container_width=True)
                with c2:
                    st.markdown("**DESPUÉS 😍✨**")
                    st.image(base64_a_img(item['despues_b64']), use_container_width=True)
            except: st.write("Foto guardada")
            st.divider()
    st.markdown('<div class="promo-box"><h2 style="color:white;">📲 AGENDA YA +57 304 381 0896</h2></div>', unsafe_allow_html=True)
