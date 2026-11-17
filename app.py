import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Marle Nails & Beauty", page_icon="💖", layout="wide")

st.title("👑 MARLE NAILS & BEAUTY 💖")
st.markdown("### Belleza que inspira ✨ Barranquilla")
st.markdown("---")

if 'servicios' not in st.session_state:
    st.session_state.servicios = []

menu = st.sidebar.selectbox("💅 Menú Marle", ["💖 Ver Mi Negocio", "➕ Agregar Servicio", "📊 Mi Ganancia Total"])

if menu == "💖 Ver Mi Negocio":
    st.subheader("📋 Historial de Servicios")
    if not st.session_state.servicios:
        st.info("Aún no hay servicios. ¡Agrega tu primera keratina! 💖")
    else:
        df = pd.DataFrame(st.session_state.servicios)
        st.dataframe(df, use_container_width=True)

elif menu == "➕ Agregar Servicio":
    st.subheader("✨ Nuevo Servicio a Cliente")
    with st.form("servicio"):
        nombre = st.text_input("Nombre de la clienta")
        servicio = st.selectbox("Servicio", ["Aplicación de KERATINA", "AMINOÁCIDOS", "BLOWER Profesional"])
        costo = st.number_input("¿Cuánto te costó el producto? (Inversión) $", min_value=0)
        cobrado = st.number_input("¿Cuánto le cobraste a la clienta? $", min_value=0)
        fecha = st.date_input("Fecha", value=date.today())
        guardar = st.form_submit_button("💖 Guardar Servicio")
        if guardar:
            ganancia = cobrado - costo
            st.session_state.servicios.append({
                "Clienta": nombre, "Servicio": servicio,
                "Inversión": costo, "Cobrado": cobrado,
                "Ganancia": ganancia, "Fecha": str(fecha)
            })
            st.success(f"¡Guardado! Ganaste ${ganancia:,.0f} con {nombre} 💖")

elif menu == "📊 Mi Ganancia Total":
    if not st.session_state.servicios:
        st.warning("No hay datos aún")
    else:
        df = pd.DataFrame(st.session_state.servicios)
        col1, col2, col3 = st.columns(3)
        col1.metric("💸 Invertido", f"${df['Inversión'].sum():,.0f}")
        col2.metric("💰 Cobrado", f"${df['Cobrado'].sum():,.0f}")
        col3.metric("✨ GANANCIA", f"${df['Ganancia'].sum():,.0f}")
        st.bar_chart(df.groupby("Servicio")["Ganancia"].sum())

st.markdown("---")
st.markdown("💖 Contacto: +57 304 381 0896 | Barranquilla 💖")
