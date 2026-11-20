import streamlit as st
import os, json, uuid

st.set_page_config(page_title="MARLE NAILS BEAUTY", page_icon="🌸", layout="centered")

os.makedirs("imagenes", exist_ok=True)
ARCHIVO = "imagenes/datos.json"

def cargar():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r") as f:
                return json.load(f)
        except:
            return {"trabajos": [], "inversiones": []}
    return {"trabajos": [], "inversiones": []}

def guardar(trabajos, inversiones):
    with open(ARCHIVO, "w") as f:
        json.dump({"trabajos": trabajos, "inversiones": inversiones}, f)

datos = cargar()
if 'trabajos' not in st.session_state:
    st.session_state.trabajos = datos["trabajos"]
if 'inversiones' not in st.session_state:
    st.session_state.inversiones = datos["inversiones"]
if 'editando' not in st.session_state:
    st.session_state.editando = None

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Poppins:wght@300;400&display=swap');
.stApp {background-color: #fdf6f8; background-image: radial-gradient(#f9d5e5 1px, transparent 1px); background-size: 28px 28px;}
h1,h2,h3 {font-family: 'Cormorant Garamond', serif !important; color: #8e4a63 !important;}
p, label, div {font-family: 'Poppins', sans-serif !important; font-weight: 300 !important; color: #6d4c5b !important;}
.card-delicada {background: rgba(255,255,255,0.95); border-radius: 22px; padding: 22px; border: 1px solid #f9d5e5; box-shadow: 0 10px 30px rgba(142,74,99,0.06); margin-bottom: 14px;}
.stButton>button {background: #8e4a63 !important; color: white !important; border-radius: 30px; letter-spacing: 1px; text-transform: uppercase; font-size: 11px !important; padding: 8px 16px; border: 1px solid #8e4a63 !important;}
.stButton>button * {color: white !important;}
.contact-card {background: white; border-radius: 20px; padding: 18px; border: 1px solid #f9d5e5; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;font-size:42px;margin-bottom:0'>MARLE NAILS BEAUTY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;letter-spacing:4px;font-size:11px;text-transform:uppercase;margin-top:5px;color:#b07a8f !important'>Delicate • Beauty • Studio</p>", unsafe_allow_html=True)

st.markdown("""
<div class="contact-card">
<p style="margin:0;letter-spacing:2px;text-transform:uppercase;font-size:11px">CONTACTAME MI REINA</p>
<p style="margin:10px 0;font-size:14px">+57 3043810896<br>Barranquilla - A domicilio y en estudio</p>
</div>
""", unsafe_allow_html=True)
st.link_button("💬 ESCRIBEME POR WHATSAPP", "https://wa.me/573043810896", use_container_width=True)
st.write("")

c1, c2 = st.columns([3,1])
with c2:
    if not st.session_state.get('admin', False):
        if st.button("🔐 Admin"):
            st.session_state.show_login = True
    else:
        if st.button("CERRAR"):
            st.session_state.admin = False
            st.rerun()

if not st.session_state.get('admin', False) and st.session_state.get('show_login', False):
    st.markdown("<div class='card-delicada'><b>Acceso privado solo para Marle</b></div>", unsafe_allow_html=True)
    clave = st.text_input("Contraseña", type="password")
    if st.button("ENTRAR A MI PRIVADO"):
        if clave == "marle2024":
            st.session_state.admin = True
            st.session_state.show_login = False
            st.rerun()
        else:
            st.error("Contraseña incorrecta mi reina")

# VISTA PUBLICA
if not st.session_state.get('admin', False):
    st.markdown("<p style='text-align:center;margin-top:15px'>✨ Mis trabajos para mis reinas ✨</p>", unsafe_allow_html=True)
    if not st.session_state.trabajos:
        st.markdown("<div class='card-delicada'><p style='text-align:center'>Pronto verás mi magia aquí 🌸</p></div>", unsafe_allow_html=True)
    for t in st.session_state.trabajos:
        st.markdown(f"<div class='card-delicada'><p style='margin:0;font-size:16px'><b>{t['cliente']}</b></p><p style='font-size:11px;letter-spacing:1px;color:#b07a8f !important'>{' • '.join(t['servicios']).upper()}</p></div>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            if os.path.exists(t['antes']):
                st.image(t['antes'], caption="Antes")
        with col_b:
            if os.path.exists(t['despues']):
                st.image(t['despues'], caption="Después ✨")
    st.stop()

# VISTA PRIVADA
tabs = st.tabs(["Registrar", "Historial / Editar", "Ganancias"])

with tabs[0]:
    # Si está editando, cargar datos
    if st.session_state.editando is not None:
        t_edit = st.session_state.trabajos[st.session_state.editando]
        st.warning(f"✏️ Editando a: {t_edit['cliente']}")
        cliente_default = t_edit['cliente']
        precio_default = t_edit['precio']
        inversion_default = t_edit.get('inversion',0)
        productos_default = t_edit.get('productos','')
        notas_default = t_edit.get('notas','')
    else:
        cliente_default = ""
        precio_default = 0
        inversion_default = 0
        productos_default = ""
        notas_default = ""

    with st.container():
        st.markdown("<div class='card-delicada'>", unsafe_allow_html=True)
        cliente = st.text_input("Nombre", value=cliente_default, placeholder="Ej. Yulieth")
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
        
        col_val1, col_val2 = st.columns(2)
        with col_val1:
            precio = st.number_input("Valor cobrado *", min_value=0, step=1000, value=precio_default)
        with col_val2:
            inversion = st.number_input("Valor de inversión *", min_value=0, step=1000, value=inversion_default)
        
        if precio and inversion:
            st.info(f"💰 Ganancia: ${precio - inversion:,.0f}")
        
        productos = st.text_input("Productos usados (opcional)", value=productos_default)
        notas = st.text_area("Notas (opcional)", value=notas_default)
        fa = st.file_uploader("Foto ANTES (si no cambias, deja vacío)", type=["jpg","png","jpeg"], key="fa")
        fd = st.file_uploader("Foto DESPUÉS (si no cambias, deja vacío)", type=["jpg","png","jpeg"], key="fd")
        
        if st.session_state.editando is None:
            if st.button("GUARDAR PARA SIEMPRE 💖", use_container_width=True):
                if not cliente or not precio or not servicios or not fa or not fd:
                    st.error("Completa todo mi reina")
                else:
                    uid = str(uuid.uuid4())[:8]
                    ra = f"imagenes/{uid}_antes.jpg"
                    rd = f"imagenes/{uid}_despues.jpg"
                    with open(ra, "wb") as f: f.write(fa.getbuffer())
                    with open(rd, "wb") as f: f.write(fd.getbuffer())
                    st.session_state.trabajos.append({"cliente": cliente, "servicios": servicios, "precio": precio, "inversion": inversion, "productos": productos, "notas": notas, "antes": ra, "despues": rd})
                    guardar(st.session_state.trabajos, st.session_state.inversiones)
                    st.success("Guardado 🌸")
                    st.rerun()
        else:
            col_g, col_c = st.columns(2)
            with col_g:
                if st.button("✅ ACTUALIZAR", use_container_width=True):
                    t = st.session_state.trabajos[st.session_state.editando]
                    t['cliente'] = cliente
                    t['servicios'] = servicios if servicios else t['servicios']
                    t['precio'] = precio
                    t['inversion'] = inversion
                    t['productos'] = productos
                    t['notas'] = notas
                    if fa:
                        with open(t['antes'], "wb") as f: f.write(fa.getbuffer())
                    if fd:
                        with open(t['despues'], "wb") as f: f.write(fd.getbuffer())
                    guardar(st.session_state.trabajos, st.session_state.inversiones)
                    st.session_state.editando = None
                    st.success("Actualizado!")
                    st.rerun()
            with col_c:
                if st.button("❌ CANCELAR", use_container_width=True):
                    st.session_state.editando = None
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("#### Tus registros - Edita o Elimina si se repitió")
    if not st.session_state.trabajos:
        st.write("No hay registros aún")
    else:
        for idx, t in enumerate(st.session_state.trabajos):
            inv = t.get('inversion',0)
            gan = t.get('precio',0) - inv
            st.markdown(f"<div class='card-delicada'><b>{t['cliente']}</b> - {' • '.join(t['servicios'])}<br>Cobrado: ${t['precio']:,.0f} - Invertido: ${inv:,.0f} - <b>Ganancia: ${gan:,.0f}</b></div>", unsafe_allow_html=True)
            ce1, ce2 = st.columns(2)
            with ce1:
                if st.button(f"✏️ EDITAR", key=f"edit_{idx}", use_container_width=True):
                    st.session_state.editando = idx
                    st.rerun()
            with ce2:
                if st.button(f"🗑️ ELIMINAR", key=f"del_{idx}", use_container_width=True):
                    # borrar fotos
                    try:
                        if os.path.exists(t['antes']): os.remove(t['antes'])
                        if os.path.exists(t['despues']): os.remove(t['despues'])
                    except:
                        pass
                    st.session_state.trabajos.pop(idx)
                    guardar(st.session_state.trabajos, st.session_state.inversiones)
                    st.success("Eliminado")
                    st.rerun()

with tabs[2]:
    total_cobrado = sum([t['precio'] for t in st.session_state.trabajos])
    total_inversion = sum([t.get('inversion',0) for t in st.session_state.trabajos])
    total_ganancia = total_cobrado - total_inversion
    c1,c2,c3 = st.columns(3)
    c1.metric("Cobrado", f"${total_cobrado:,.0f}")
    c2.metric("Invertido", f"${total_inversion:,.0f}")
    c3.metric("Ganancia Real", f"${total_ganancia:,.0f}")
