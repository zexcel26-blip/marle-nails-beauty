import streamlit as st
from datetime import date

st.set_page_config(page_title="Marle Nails & Beauty", page_icon="👑", layout="wide")

# --- DISEÑO HERMOSO MARLE ---
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
    .stButton > button { background: linear-gradient(135deg, #EC407A, #FFD700); color: white; border-radius: 20px; font-weight: bold; border: none; padding: 10px 25px; }
</style>
""", unsafe_allow_html=True)

if 'servicios' not in st.session_state:
    st.session_state.servicios = []
if 'galeria' not in st.session_state:
    st.session_state.galeria = []
if 'es_admin' not in st.session_state:
    st.session_state.es_admin = False

CLAVE_ADMIN = "marle123"

# --- PORTADA ---
st.markdown("<h1>👑 MARLE NAILS & BEAUTY 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>✨ Belleza que inspira | Barranquilla ✨</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="promo-box">
    <h2 style="color:white;">💖 ¿SUEÑAS CON UN CABELLO LISO, BRILLANTE Y SIN FRIZZ? 💖</h2>
    <p style="font-size:20px;">¡Yo lo hago realidad con mis manos! ✨ Mira mis trabajos reales abajo 👇</p>
    <p style="font-size:18px;">📣 <b>PROMO ESTA SEMANA:</b> Agenda tu Keratina y luce ESPECTACULAR</p>
</div>
""", unsafe_allow_html=True)

# 3 TARJETAS BONITAS
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>💇‍♀️ KERATINA</h3><p>Cabello liso, suave y brillante como espejo ✨</p><p class="gold-text">⭐ LA MÁS PEDIDA ⭐</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>💅 UÑAS</h3><p>Uñas hermosas, elegantes y duraderas 💖</p><p>Diseños que enamoran</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>👁️ PESTAÑAS</h3><p>Mirada que impacta, pestañas perfectas 😍</p><p>Quedarás divina</p></div>', unsafe_allow_html=True)

st.markdown("---")

# --- MENÚ ---
st.sidebar.title("💅 Menú Marle")
st.sidebar.markdown("### 👑 Bienvenida hermosa 💖")
menu = st.sidebar.selectbox("¿Qué quieres ver?", ["Ver Mi Trabajo 💖", "🔒 Soy Marle - Entrar como Admin"])

# --- ADMIN SOLO TU ---
if menu == "🔒 Soy Marle - Entrar como Admin":
    if not st.session_state.es_admin:
        st.markdown("### 🔒 Zona Privada Solo Para Marle")
        clave = st.text_input("Escribe tu contraseña", type="password")
        if st.button("Entrar 👑"):
            if clave == CLAVE_ADMIN:
                st.session_state.es_admin = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")
    else:
        st.success("¡Hola Marle! Modo Admin 👑")
        if st.button("Cerrar sesión"):
            st.session_state.es_admin = False
            st.rerun()
        menu_admin = st.selectbox("Panel Privado - SOLO TU", ["Agregar Servicio Privado", "📸 Subir Trabajo Realizado", "Borrar", "Mi Ganancia Total - SOLO YO"])

        if menu_admin == "Agregar Servicio Privado":
            st.subheader("➕ Agregar Servicio - PRIVADO")
            with st.form("form"):
                clienta = st.text_input("Nombre de la Clienta")
                servicio = st.selectbox("Servicio", ["Aplicación de KERATINA", "Uñas", "Pestañas", "Otro"])
                inversion = st.number_input("Inversión - SOLO TU LO VES", min_value=0, value=40500)
                cobrado = st.number_input("Cobrado - SOLO TU LO VES", min_value=0, value=120000)
                fecha = st.date_input("Fecha", value=date.today())
                guardar = st.form_submit_button("💖 Guardar Servicio")
                if guardar and clienta:
                    ganancia = cobrado - inversion
                    margen = (ganancia / cobrado * 100) if cobrado > 0 else 0
                    st.session_state.servicios.append({"clienta": clienta, "servicio": servicio, "inversion": inversion, "cobrado": cobrado, "ganancia": ganancia, "margen": margen, "fecha": str(fecha)})
                    st.success(f"¡Guardado! Ganaste ${ganancia:,.0f} con margen {margen:.1f}% 💖")
                    st.balloons()

        if menu_admin == "📸 Subir Trabajo Realizado":
            st.subheader("📸 Subir Trabajo - Esto SI lo verá el público")
            with st.form("form_fotos"):
                clienta_foto = st.text_input("Nombre de la clienta")
                servicio_foto = st.selectbox("Qué le hiciste", ["KERATINA", "Uñas", "Pestañas", "Otro"])
                col1, col2 = st.columns(2)
                with col1:
                    antes = st.file_uploader("📷 Foto ANTES", type=["jpg","jpeg","png"])
                with col2:
                    despues = st.file_uploader("✨ Foto DESPUÉS", type=["jpg","jpeg","png"])
                subir = st.form_submit_button("💖 Publicar Trabajo")
                if subir:
                    if antes and despues and clienta_foto:
                        st.session_state.galeria.append({"clienta": clienta_foto, "servicio": servicio_foto, "antes": antes, "despues": despues})
                        st.success(f"¡Trabajo de {clienta_foto} publicado! 💖")
                    else:
                        st.warning("Porfa sube las 2 fotos y el nombre 🙏")

        if menu_admin == "Borrar":
            st.subheader("🗑️ Borrar - SOLO TU")
            if st.session_state.servicios:
                for i, s in enumerate(st.session_state.servicios):
                    st.write(f"{i} - {s.get('clienta')} | {s.get('servicio')} | Ganancia: ${s.get('ganancia'):,.0f} | Margen: {s.get('margen',0):.1f}%")
                indice = st.number_input("Número a borrar", min_value=0, max_value=len(st.session_state.servicios)-1, value=0)
                if st.button("🔴 BORRAR SERVICIO"):
                    st.session_state.servicios.pop(indice)
                    st.rerun()

        if menu_admin == "Mi Ganancia Total - SOLO YO":
            total_g = sum([s.get("ganancia",0) for s in st.session_state.servicios])
            total_i = sum([s.get("inversion",0) for s in st.session_state.servicios])
            total_c = sum([s.get("cobrado",0) for s in st.session_state.servicios])
            col1, col2, col3 = st.columns(3)
            col1.metric("💰 Ganancia Total", f"${total_g:,.0f}")
            col2.metric("💸 Invertido", f"${total_i:,.0f}")
            col3.metric("💖 Cobrado", f"${total_c:,.0f}")
            if total_c > 0:
                st.metric("📊 Tu Margen Total", f"{(total_g/total_c*100):.1f}%")

# --- VISTA PÚBLICA HERMOSA ---
if menu == "Ver Mi Trabajo 💖":
    st.markdown("## ✨ TRABAJOS YA REALIZADOS - 100% REALES ✨")
    st.markdown("<p style='text-align:center; font-size:18px;'>Trabajos hechos con amor por mis manos en Barranquilla 💖</p>", unsafe_allow_html=True)
    if not st.session_state.galeria:
        st.info("Pronto verás aquí mis transformaciones ✨ ¡Aparta tu cupo ya!")
    else:
        for item in reversed(st.session_state.galeria):
            st.markdown(f"### 👑 {item['clienta']} - {item['servicio']} ✨")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**ANTES 😱**")
                st.image(item['antes'], use_container_width=True)
            with c2:
                st.markdown("**DESPUÉS 😍✨**")
                st.image(item['despues'], use_container_width=True)
            st.markdown("<p style='text-align:center;'>💖 ¿Quieres quedar así de hermosa? Escríbeme ya! 💖</p>", unsafe_allow_html=True)
            st.divider()

    st.markdown("""
    <div class="card">
        <h3>💖 ¿Por qué elegir a Marle? 💖</h3>
        <p>✅ Keratina que deja el cabello suave y brillante</p>
        <p>✅ Uñas hermosas y duraderas</p>
        <p>✅ Pestañas que enamoran</p>
        <p>✅ Atención con amor en Barranquilla</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="promo-box">
        <h2 style="color:white;">📲 AGENDA YA POR WHATSAPP</h2>
        <p style="font-size:22px;"><b>+57 304 381 0896</b></p>
        <p>¡Cupos limitados! No te quedes sin tu cita 💖</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align:center;'>💖 Marle Nails & Beauty | Barranquilla | Sígueme y agenda tu cita 💖</p>", unsafe_allow_html=True)
