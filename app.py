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
# FUNDO GRIPEN (DISCRETO E ESTÁVEL)
# =====================
page_bg = """
<style>

/* FUNDO PRINCIPAL */
[data-testid="stAppViewContainer"]{
background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/c_scale,w_2048/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;

/* suaviza imagem */
filter: brightness(0.55) contrast(0.95);
}

/* remove overlay antigo que pode quebrar layout */
.stApp::before{
display: none;
}

/* camada escura para leitura */
.stApp{
background: rgba(0,0,0,0.55);
}

/* HEADER */
[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

/* =====================
   TEXTOS (FORA DOS INPUTS)
   ===================== */

h1, h2, h3 {
color: white !important;
}

p, label {
color: rgba(255, 255, 255, 0.90) !important;
}

/* =====================
   INPUTS (LEGÍVEIS)
   ===================== */

div[data-baseweb="input"],
div[data-baseweb="select"],
.stTextInput,
.stForm,
.stDataFrame {
    background: rgba(20, 20, 20, 0.65) !important;
    border-radius: 10px;
    padding: 10px;
}

/* TEXTO DENTRO DOS INPUTS */
input, textarea {
    color: #111111 !important;
    font-weight: 500;
}

/* PLACEHOLDER */
input::placeholder {
    color: rgba(255, 255, 255, 0.5) !important;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
background: rgba(0,0,0,0.5);
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
# TITULO
# =====================
st.title("✈ CONSULTA T.O.")
st.write("Pesquisa rápida de Part Number")

# =====================
# PESQUISA
# =====================
pesquisa = st.text_input("Digite o Part Number")

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
