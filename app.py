import streamlit as st
from datetime import date

st.set_page_config(page_title="Marle Nails & Beauty", page_icon="💖", layout="wide")

st.title("👑 MARLE NAILS & BEAUTY 💖")
st.markdown("### Belleza que inspira ✨ Barranquilla - Donde tu cabello brilla")
st.markdown("---")

if 'servicios' not in st.session_state:
    st.session_state.servicios = []
if 'galeria' not in st.session_state:
    st.session_state.galeria = []

menu = st.sidebar.selectbox("💅 Menú Marle", ["Ver Mi Negocio", "Agregar Servicio", "📸 Galería Antes y Después", "Borrar Servicio", "Mi Ganancia Total"])

if menu == "Ver Mi Negocio":
    st.subheader("📋 Historial de Servicios")
    if not st.session_state.servicios:
        st.info("Aún no hay servicios. ¡Agrega tu primera keratina! 💖")
    else:
        for i, s in enumerate(st.session_state.servicios):
            st.write(f"{i} - {s.get('clienta')} | {s.get('servicio')} | Cobrado: ${s.get('cobrado')} | Ganancia: ${s.get('ganancia')} | {s.get('fecha')}")

if menu == "Agregar Servicio":
    st.subheader("➕ Agregar Nuevo Servicio")
    with st.form("form"):
        clienta = st.text_input("Nombre de la Clienta")
        servicio = st.selectbox("Servicio", ["Aplicación de KERATINA", "Uñas", "Pestañas", "Otro"])
        inversion = st.number_input("Cuánto te costó (Inversión)", min_value=0, value=40500)
        cobrado = st.number_input("Cuánto cobraste", min_value=0, value=120000)
        fecha = st.date_input("Fecha", value=date.today())
        guardar = st.form_submit_button("💖 Guardar Servicio")
        if guardar and clienta:
            ganancia = cobrado - inversion
            st.session_state.servicios.append({
                "clienta": clienta, "servicio": servicio, "inversion": inversion,
                "cobrado": cobrado, "ganancia": ganancia, "fecha": str(fecha)
            })
            st.success(f"¡Servicio de {clienta} guardado! 💖")
            st.balloons()

if menu == "📸 Galería Antes y Después":
    st.subheader("📸 Galería de Transformaciones Marle")
    st.markdown("Aquí subes las fotos del cabello para que tus clientas vean tu arte 💖")

    with st.form("form_fotos"):
        clienta_foto = st.text_input("Nombre de la clienta de la foto")
        servicio_foto = st.selectbox("Qué le hiciste", ["KERATINA", "Uñas", "Pestañas", "Otro"])
        col1, col2 = st.columns(2)
        with col1:
            antes = st.file_uploader("📷 Foto ANTES", type=["jpg","jpeg","png"])
        with col2:
            despues = st.file_uploader("✨ Foto DESPUÉS", type=["jpg","jpeg","png"])
        subir = st.form_submit_button("💖 Subir a la Galería")

        if subir:
            if antes and despues and clienta_foto:
                st.session_state.galeria.append({
                    "clienta": clienta_foto,
                    "servicio": servicio_foto,
                    "antes": antes,
                    "despues": despues
                })
                st.success(f"¡Fotos de {clienta_foto} agregadas! 💖")
            else:
                st.warning("Porfa sube las 2 fotos y el nombre 🙏")

    st.divider()
    st.subheader("✨ Resultados Reales de Marle Nails")
    if not st.session_state.galeria:
        st.info("Aún no hay fotos. ¡Sube tu primer antes y después!")
    else:
        for item in reversed(st.session_state.galeria):
            st.markdown(f"#### 👑 {item['clienta']} - {item['servicio']}")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**ANTES** 😱")
                st.image(item['antes'], use_container_width=True)
            with c2:
                st.markdown("**DESPUÉS** 😍✨")
                st.image(item['despues'], use_container_width=True)
            st.divider()

if menu == "Borrar Servicio":
    st.subheader("🗑️ Borrar")
    tab1, tab2 = st.tabs(["Borrar Servicios", "Borrar Fotos Galería"])
    with tab1:
        if not st.session_state.servicios:
            st.info("No hay servicios para borrar")
        else:
            for i, s in enumerate(st.session_state.servicios):
                st.write(f"{i} - {s.get('clienta')} | {s.get('servicio')}")
            indice = st.number_input("Número de fila a borrar", min_value=0, max_value=len(st.session_state.servicios)-1, value=0, key="borrar_serv")
            if st.button("🔴 BORRAR SERVICIO"):
                st.session_state.servicios.pop(indice)
                st.rerun()
    with tab2:
        if not st.session_state.galeria:
            st.info("No hay fotos para borrar")
        else:
            for i, g in enumerate(st.session_state.galeria):
                st.write(f"{i} - {g.get('clienta')} - {g.get('servicio')}")
            indice_f = st.number_input("Número de foto a borrar", min_value=0, max_value=len(st.session_state.galeria)-1, value=0, key="borrar_foto")
            if st.button("🔴 BORRAR FOTO"):
                st.session_state.galeria.pop(indice_f)
                st.rerun()

if menu == "Mi Ganancia Total":
    total = sum([s.get("ganancia",0) for s in st.session_state.servicios])
    st.metric("💰 Ganancia Total", f"${total:,.0f}")
    st.balloons()

st.divider()
st.markdown("💖 Contacto: +57 304 381 0896 | Barranquilla 💖")
