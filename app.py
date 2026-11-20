import streamlit as st
import os, json, uuid

st.set_page_config(page_title="MARLE NAILS BEAUTY", page_icon="🌸", layout="centered")

# --- GUARDADO PARA QUE NO SE BORRE NUNCA ---
os.makedirs("imagenes", exist_ok=True)
ARCHIVO = "imagenes/datos.json"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {"trabajos": [], "inversiones": []}

def guardar(trabajos, inversiones):
    with open(ARCHIVO, "w") as f:
        json.dump({"trabajos": trabajos, "inversiones": inversiones}, f)

datos = cargar()
if 'trabajos' not in st.session_state:
    st.session_state.trabajos = datos["trabajos"]
if 'inversiones' not in st.session_state:
    st.session_state.inversiones = datos["inversiones"]

# --- TUS COLORES LINDOS DE LA FOTO ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Poppins:wght@300;400&display=swap');
.stApp {background-color: #fdf6f8; background-image: radial-gradient(#f9d5e5 1px, transparent 1px); background-size: 28px 28px;}
h1,h2,h3 {font-family: 'Cormorant Garamond', serif !important; color: #8e4a63 !important; letter-spacing: 1px;}
p, label, div {font-family: 'Poppins', sans-serif !important; font-weight: 300 !important; color: #6d4c5b !important;}
.card-delicada {background: rgba(255,255,255,0.9); border-radius: 22px; padding: 22px; border: 1px solid #f9d5e5; box-shadow: 0 10px 30px rgba(142,74,99,0.06); margin-bottom: 18px;}
.stButton>button {background: #8e4a63; color: white !important; border-radius: 30px; letter-spacing: 1.5px; text-transform: uppercase; font-size: 12px !important; padding: 12px 20px; border: 1px solid #8e4a63;}
.stButton>button:hover {background: transparent; color: #8e4a63 !important;}
.contact-card {background: white; border-radius: 20px; padding: 18px; border: 1px solid #f9d5e5; text-align: center; box-shadow: 0 8px 20px rgba(142,74,99,0.05);}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;font-size:42px;margin-bottom:0'>MARLE NAILS BEAUTY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;letter-spacing:4px;font-size:11px;text-transform:uppercase;margin-top:5px;color:#b07a8f !important'>Delicate • Beauty • Studio</p>", unsafe_allow_html=True)

# --- TU CONTACTO REAL ---
st.markdown(f"""
<div class='contact-card'>
<p style='margin:0;letter-spacing:2px;text-transform:uppercase;font-size:11px'>Contáctame mi reina 🌸</p>
<p style='margin:10px 0;font-size:14px'>📱 <b>+57 3043810896</b><br>📍 Barranquilla - A domicilio y en estudio</p>
<a href='https://wa.me/573043810896' target='_blank' style='text-decoration:none;background:#8e4a63;color:white !important;padding:10px 22px;border-radius:25px;font-size:12px;letter-spacing:1px'>💬 ESCRÍBEME POR WHATSAPP</a>
</div>
""", unsafe_allow_html=True)
st.write("")

# --- BOTON ADMIN ---
c1, c2 = st.columns([3,1])
with c2:
    if not st.session_state.get('admin', False):
        if st.button("🔐 Admin"): st.session_state.show_login = True
    else:
        if st.button("Cerrar"): 
            st.session_state.admin = False
            st.rerun()

if not st.session_state.get('admin', False) and st.session_state.get('show_login', False):
    with st.container():
        st.markdown("<div class='card-delicada'><b>Acceso privado solo para Marle 🌸</b></div>", unsafe_allow_html=True)
        clave = st.text_input("Contraseña", type="password")
        if st.button("Entrar a mi privado"):
            if clave == "marle2024":
                st.session_state.admin = True
                st.session_state.show_login = False
                st.rerun()
            else: st.error("Contraseña incorrecta mi reina")

# --- VISTA PUBLICA - LO QUE VEN TUS CLIENTAS Y NUNCA SE BORRA ---
if not st.session_state.get('admin', False):
    st.markdown("<p style='text-align:center;margin-top:15px;letter-spacing:1px'>✨ Mis trabajos para mis reinas ✨</p>", unsafe_allow_html=True)
    buscar = st.text_input("", placeholder="Buscar clienta...")
    if not st.session_state.trabajos:
        st.markdown("<div class='card-delicada'><p style='text-align:center'>Pronto verás mi magia aquí 🌸</p></div>", unsafe_allow_html=True)
    for t in st.session_state.trabajos:
        if buscar.lower() in t['cliente'].lower() or buscar == "":
            st.markdown(f"<div class='card-delicada'><p style='margin:0;font-size:16px'><b>{t['cliente']}</b></p><p style='font-size:11px;letter-spacing:1px;color:#b07a8f !important'>{' • '.join(t['servicios']).upper()}</p></div>", unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                if os.path.exists(t['antes']): st.image(t['antes'], caption="Antes")
            with col_b:
                if os.path.exists(t['despues']): st.image(t['despues'], caption="Después ✨")
    st.stop()

# --- VISTA PRIVADA TUYA ---
st.markdown("<p style='text-align:center'>Hola, Marle 🌸 tu estudio te espera</p>", unsafe_allow_html=True)
tabs = st.tabs(["Registrar", "Historial", "Ganancias"])

with tabs[0]:
    st.markdown("<div class='card-delicada'>", unsafe_allow_html=True)
    st.markdown("#### Nueva Clienta")
    cliente = st.text_input("Nombre", placeholder="Ej. Yulieth")
    st.markdown("<p style='font-size:11px;letter-spacing:1px;text-transform:uppercase'>Servicios realizados</p>", unsafe_allow_html=True)
    kera = st.checkbox("Keratinas"); amino = st.checkbox("Aminoácidos"); blower = st.checkbox("Blower"); tinte = st.checkbox("Aplicación de Tinte"); puntas = st.checkbox("Corte de Puntas")
    servicios = [s for s,c in [("Keratinas",kera),("Aminoácidos",amino),("Blower",blower),("Aplicación de Tinte",tinte),("Corte de Puntas",puntas)] if c]
    precio = st.number_input("Valor cobrado", min_value=0, step=1000)
    productos = st.text_input("Productos usados (opcional)"); notas = st.text_area("Notas (opcional)")
    fa = st.file_uploader("Foto ANTES *", type=["jpg","png","jpeg"], key="fa")
    fd = st.file_uploader("Foto DESPUÉS *", type=["jpg","png","jpeg"], key="fd")
    if st.button("Guardar para siempre 💖", use_container_width=True):
        if not cliente or not precio or not servicios or not fa or not fd:
            st.error("Mi reina, completa nombre, servicios, valor y las 2 fotos")
        else:
            uid = str(uuid.uuid4())[:8]
            ra = f"imagenes/{uid}_antes.jpg"; rd = f"imagenes/{uid}_despues.jpg"
            with open(ra, "wb") as f: f.write(fa.getbuffer())
            with open(rd, "wb") as f: f.write(fd.getbuffer())
            st.session_state.trabajos.append({"cliente": cliente, "servicios": servicios, "precio": precio, "productos": productos, "notas": notas, "antes": ra, "despues": rd})
            guardar(st.session_state.trabajos, st.session_state.inversiones)
            st.success("Guardado para siempre, ya lo verán tus clientas 🌸")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    for t in st.session_state.trabajos:
        st.markdown(f"<div class='card-delicada'><b>{t['cliente']}</b> - {' • '.join(t['servicios'])} - ${t['precio']:,.0f}</div>", unsafe_allow_html=True)

with tabs[2]:
    total = sum([t['precio'] for t in st.session_state.trabajos])
    inv = sum([i['valor'] for i in st.session_state.inversiones])
    c1,c2,c3 = st.columns(3)
    c1.metric("Ingresos", f"${total:,.0f}"); c2.metric("Invertido", f"${inv:,.0f}"); c3.metric("Neta", f"${total-inv:,.0f}")
    prod = st.text_input("Producto comprado"); val = st.number_input("Costo", min_value=0, step=1000, key="inv2")
    if st.button("Guardar inversión"):
        if prod and val:
            st.session_state.inversiones.append({"producto": prod, "valor": val})
            guardar(st.session_state.trabajos, st.session_state.inversiones)
            st.success("Guardada")
