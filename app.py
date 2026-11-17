import streamlit as st
from datetime import date

st.set_page_config(page_title="Marle Nails & Beauty", page_icon="💖", layout="wide")

st.title("👑 MARLE NAILS & BEAUTY 💖")
st.markdown("### Belleza que inspira ✨ Barranquilla")
st.markdown("---")

if 'servicios' not in st.session_state:
    st.session_state.servicios = []

menu = st.sidebar.selectbox("💅 Menú Marle", ["Ver Mi Negocio", "Agregar Servicio", "Borrar Servicio", "Mi Ganancia Total"])

if menu == "Ver Mi Negocio":
    st.subheader("📋 Historial de Servicios")
    if not st.session_state.servicios:
        st.info("Aún no hay servicios. ¡Agrega tu primera keratina! 💖")
    else:
        for i, s in enumerate(st.session_state.servicios):
            clienta = s.get("clienta","")
            servicio = s.get("servicio","")
            cobrado = s.get("cobrado",0)
            ganancia = s.get("ganancia",0)
            fecha = s.get("fecha","")
            st.write(f"{i} - {clienta} | {servicio} | Cobrado: ${cobrado} | Ganancia: ${ganancia} | {fecha}")

if menu == "Agregar Servicio":
    st.subheader("➕ Agregar Nuevo Servicio")
    with st.form("form"):
        clienta = st.text_input("Nombre de la Clienta")
        servicio = st.selectbox("Servicio", ["Aplicación de KERATINA", "Uñas", "Pestañas", "Otro"])
        inversion = st.number_input("Cuánto te costó (Inversión)", min_value=0, value=40500)
        cobrado = st.number_input("Cuánto cobraste", min_value=0, value=120000)
        fecha = st.date_input("Fecha", value=date.today())
        guardar = st.form_submit_button("💖 Guardar Servicio")
        if guardar:
            ganancia = cobrado - inversion
            st.session_state.servicios.append({
                "clienta": clienta,
                "servicio": servicio,
                "inversion": inversion,
                "cobrado": cobrado,
                "ganancia": ganancia,
                "fecha": str(fecha)
            })
            st.success(f"Servicio de {clienta} guardado! 💖")

if menu == "Borrar Servicio":
    st.subheader("🗑️ Borrar Servicios repetidos")
    if not st.session_state.servicios:
        st.info("No hay nada para borrar")
    else:
        for i, s in enumerate(st.session_state.servicios):
            st.write(f"{i} - {s.get('clienta')} | {s.get('servicio')}")
        st.divider()
        indice = st.number_input("Número de fila a borrar", min_value=0, max_value=len(st.session_state.servicios)-1, value=0)
        if st.button("🔴 BORRAR AHORA"):
            borrado = st.session_state.servicios.pop(indice)
            st.warning(f"Borraste la fila {indice}")
            st.rerun()

if menu == "Mi Ganancia Total":
    total = sum([s.get("ganancia",0) for s in st.session_state.servicios])
    st.metric("💰 Ganancia Total", f"${total:,.0f}")
    st.balloons()

st.divider()
st.markdown("💖 Contacto: +57 304 381 0896 | Barranquilla 💖")
