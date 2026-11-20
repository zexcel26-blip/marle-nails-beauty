import streamlit as st

st.set_page_config(page_title="MARLE NAILS BEAUTY", page_icon="🌸", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Poppins:wght@300;400&display=swap');
.stApp {
    background-color: #fdf6f8;
    background-image: radial-gradient(#f9d5e5 1px, transparent 1px);
    background-size: 25px 25px;
}
h1, h2, h3, h4 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 600 !important;
    color: #8e4a63 !important;
    letter-spacing: 1px;
}
p, label, div {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 300 !important;
    color: #6d4c5b !important;
}
.card-delicada {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    border-radius: 22px;
    padding: 24px;
    border: 1px solid #f9d5e5;
    box-shadow: 0 10px 30px rgba(142,74,99,0.06);
    margin-bottom: 18px;
}
.stButton>button {
    background: #8e4a63;
    color: #fff9fa !important;
    border-radius: 30px;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 400 !important;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-size: 12px !important;
    padding: 12px 20px;
    border: 1px solid #8e4a63;
    box-shadow: none;
}
.stButton>button:hover {
    background: transparent;
    color: #8e4a63 !important;
    border: 1px solid #8e4a63;
}
div[data-testid="stCheckbox"] {
    background: rgba(255,255,255,0.7);
    padding: 12px 15px;
    border-radius: 14px;
    border: 1px solid #f3d1de;
    margin-bottom: 8px;
}
div[data-testid="stMetric"] {
    background: white;
    border-radius: 20px;
    border: 1px solid #f9d5e5;
    padding: 20px;
}
hr {border: 0.5px solid #f9d5e5;}
</style>
""", unsafe_allow_html=True)

if 'admin' not in st.session_state:
    st.session_state.admin = False
if 'trabajos' not in st.session_state:
    st.session_state.trabajos = []

st.markdown("<h1 style='text-align:center;font-size:42px;margin-bottom:0'>MARLE NAILS BEAUTY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;letter-spacing:4px;font-size:11px;text-transform:uppercase;margin-top:5px;color:#b07a8f !important'>Delicate • Beauty • Studio</p>", unsafe_allow_html=True)
st.write("")

if not st.session_state.admin:
    st.markdown("<div class='card-delicada'><p style='text-align:center;letter-spacing:2px;text-transform:uppercase;font-size:12px'>Acceso Privado</p><h3 style='text-align:center;margin-top:0'>Bienvenida, Marle</h3></div>", unsafe_allow_html=True)
    clave = st.text_input("Contraseña", type="password", placeholder="••••")
    if st.button("ENTRAR", use_container_width=True):
        if clave == "marle2024":
            st.session_state.admin = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")
    st.stop()

st.markdown("<p style='text-align:center;font-size:13px;letter-spacing:1px'>Hola, Marle 🌸 tu estudio te espera</p>", unsafe_allow_html=True)

menu = st.tabs(["Registrar", "Historial", "Ganancias"])

with menu[0]:
    st.markdown("<div class='card-delicada'>", unsafe_allow_html=True)
    st.markdown("#### Nueva Clienta")
    cliente = st.text_input("Nombre", placeholder="Ej. Yulieth")

    st.markdown("<p style='font-size:12px;letter-spacing:1px;text-transform:uppercase;margin-top:15px'>Servicios Realizados</p>", unsafe_allow_html=True)
    st.caption("Selecciona los que realizaste en esta cita")
    
    kera = st.checkbox("Keratinas")
    amino = st.checkbox("Aminoácidos")
    blower = st.checkbox("Blower")
    tinte = st.checkbox("Aplicación de Tinte")
    puntas = st.checkbox("Corte de Puntas")

    servicios = []
    if kera: servicios.append("Keratinas")
    if amino: servicios.append("Aminoácidos")
    if blower: servicios.append("Blower")
    if tinte: servicios.append("Aplicación de Tinte")
    if puntas: servicios.append("Corte de Puntas")

    precio = st.number_input("Valor cobrado", min_value=0, step=1000, help="Tú defines según el cabello")
    productos = st.text_input("Productos utilizados", placeholder="Opcional")
    notas = st.text_area("Notas delicadas", placeholder="Ej. Cabello largo, tono deseado, cuidados...")

    col1, col2 = st.columns(2)
    with col1: foto_antes = st.file_uploader("Antes", type=["jpg","png","jpeg"], key="antes")
    with col2: foto_despues = st.file_uploader("Después", type=["jpg","png","jpeg"], key="despues")

    st.write("")
    if st.button("Guardar Trabajo", use_container_width=True):
        if not cliente or not precio or not servicios or not foto_antes or not foto_despues:
            st.error("Por favor completa nombre, servicios, valor y ambas fotos")
        else:
            trabajo = {"cliente": cliente, "servicios": servicios, "precio": precio, "productos": productos, "notas": notas, "antes": foto_antes, "despues": foto_despues}
            st.session_state.trabajos.append(trabajo)
            st.success(f"Guardado con amor: {cliente}")
    st.markdown("</div>", unsafe_allow_html=True)

with menu[1]:
    st.markdown("<p style='letter-spacing:2px;text-transform:uppercase;font-size:11px'>Galería</p>", unsafe_allow_html=True)
    buscar = st.text_input("", placeholder="Buscar clienta...")
    for t in st.session_state.trabajos:
        if buscar.lower() in t['cliente'].lower() or buscar == "":
            st.markdown(f"<div class='card-delicada'><p style='margin:0;font-size:16px'><b>{t['cliente']}</b></p><p style='margin:2px 0 0 0;font-size:12px;letter-spacing:1px;color:#b07a8f !important'>{'  •  '.join(t['servicios']).upper()}  —  ${t['precio']:,.0f}</p></div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1: st.image(t['antes'])
            with c2: st.image(t['despues'])

with menu[2]:
    st.markdown("<p style='letter-spacing:2px;text-transform:uppercase;font-size:11px'>Resumen</p>", unsafe_allow_html=True)
    total = sum([t['precio'] for t in st.session_state.trabajos])
    c1, c2 = st.columns(2)
    with c1: st.metric("Total", f"${total:,.0f}")
    with c2: st.metric("Clientas", len(st.session_state.trabajos))
    for t in st.session_state.trabajos:
        st.markdown(f"<div style='background:white;padding:12px 16px;border-radius:12px;border:1px solid #f9d5e5;margin-bottom:6px;display:flex;justify-content:space-between'><span style='font-size:13px'>{t['cliente']} — {' + '.join(t['servicios'])}</span><span style='font-size:13px;color:#8e4a63'>${t['precio']:,.0f}</span></div>", unsafe_allow_html=True)

st.write("")
if st.button("Cerrar sesión", use_container_width=True):
    st.session_state.admin = False
    st.rerun()
