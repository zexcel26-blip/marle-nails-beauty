import streamlit as st

st.set_page_config(page_title="MARLE NAILS BEAUTY", page_icon="💖")

st.markdown("<h1 style='text-align:center;color:#d63384'>💖 MARLE NAILS BEAUTY 💅</h1>", unsafe_allow_html=True)

st.subheader("Registrar Clienta - Varios servicios a la vez")

cliente = st.text_input("Nombre de la clienta *")

st.write("¿Qué servicios le hiciste? (marca varios)")
col1, col2 = st.columns(2)
with col1:
    kera = st.checkbox("Keratinas")
    amino = st.checkbox("Aminoácidos")
    blower = st.checkbox("Blower")
with col2:
    tinte = st.checkbox("Aplicación de Tinte")
    puntas = st.checkbox("Corte de Puntas")

servicios = []
if kera: servicios.append("Keratinas")
if amino: servicios.append("Aminoácidos")
if blower: servicios.append("Blower")
if tinte: servicios.append("Aplicación de Tinte")
if puntas: servicios.append("Corte de Puntas")

precio = st.number_input("Precio total que cobraste * (tú decides según el cabello)", min_value=0, step=1000, placeholder="Ej: 85000")

productos = st.text_input("Productos que usaste (opcional)", placeholder="Ej: Tinte 7.1, Olaplex")
notas = st.text_area("Notas (opcional)", placeholder="Ej: Cabello muy largo, volver en 15 días")

foto_antes = st.file_uploader("Foto ANTES *", type=["jpg","png","jpeg"])
foto_despues = st.file_uploader("Foto DESPUÉS *", type=["jpg","png","jpeg"])

if st.button("💖 Guardar Trabajo", use_container_width=True):
    if not cliente or not precio or not servicios or not foto_antes or not foto_despues:
        st.error("Mi reina, llena nombre, servicios, precio y las 2 fotos")
    else:
        st.success(f"¡Guardado mi reina! {cliente} - {' + '.join(servicios)} - ${precio}")
        st.write("**Servicios:**", ", ".join(servicios))
        st.write(f"**Cobrado:** ${precio}")
        if productos: st.write(f"**Productos:** {productos}")
        if notas: st.write(f"**Notas:** {notas}")
        c1, c2 = st.columns(2)
        with c1: st.image(foto_antes, caption="ANTES")
        with c2: st.image(foto_despues, caption="DESPUÉS")
