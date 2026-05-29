import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# =====================
# CONFIG
# =====================
st.set_page_config(
    page_title="Consulta T.O.",
    page_icon="✈",
    layout="wide"
)

# =====================
# FUNDO (MANTIDO IGUAL)
# =====================
page_bg = """
<style>

/* FUNDO GRIPEN */
[data-testid="stAppViewContainer"]::before{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/c_scale,w_2048/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    filter: brightness(0.50) contrast(0.95);
    z-index: -1;
}

/* fundo geral */
.stApp{
    background: rgba(0,0,0,0.60);
}

/* HEADER */
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

/* =====================
   TEXTO GERAL (MANTIDO)
   ===================== */
h1, h2, h3 {
    color: white !important;
}

p, label, span {
    color: rgba(255,255,255,0.90) !important;
}

/* =====================
   🔥 CORREÇÃO SOMENTE DO PN/T.O.
   ===================== */

/* campo real do Streamlit */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #ffffff !important;
    font-weight: 600;
}

/* fallback garantido */
.stTextInput input,
.stTextArea textarea {
    color: #ffffff !important;
    font-weight: 600;
}

/* placeholder (opcional, só pra não sumir) */
input::placeholder {
    color: rgba(255,255,255,0.5) !important;
}

/* SIDEBAR (MANTIDO) */
[data-testid="stSidebar"]{
    background: rgba(0,0,0,0.55);
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# =====================
# GOOGLE SHEETS
# =====================
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    dict(st.secrets),
    scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1jyuXzwx2x_piaro5yY7EJs7F_Ofa8u-fVnc-NGjeK5w"
).sheet1

# =====================
# DADOS
# =====================
dados = sheet.get_all_records()
df = pd.DataFrame(dados)

# =====================
# TÍTULO
# =====================
st.title("✈ CONSULTA T.O.")
st.write("Pesquisa rápida de Part Number")

# =====================
# PESQUISA
# =====================
pesquisa = st.text_input("🔎 Digite o Part Number")

# =====================
# RESULTADO
# =====================
if pesquisa:

    resultado = df[
        df.iloc[:, 0]
        .astype(str)
        .str.contains(pesquisa, case=False, na=False)
    ]

    if not resultado.empty:
        st.success(f"{len(resultado)} resultado(s) encontrado(s)")
        st.dataframe(resultado, use_container_width=True)
    else:
        st.error("Nenhum Part Number encontrado")

# =====================
# ADICIONAR ITEM
# =====================
st.divider()
st.subheader("➕ Adicionar Novo Item")

with st.form("novo_item", clear_on_submit=True):

    pn = st.text_input("Part Number")
    to = st.text_input("T.O.")

    salvar = st.form_submit_button("Salvar")

    if salvar:

        if pn and to:
            sheet.append_row([pn, to])
            st.success("Item salvo com sucesso ✔")
            st.rerun()
        else:
            st.warning("Preencha todos os campos")
