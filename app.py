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
# FUNDO (DISCRETO)
# =====================
page_bg = """
<style>

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

    filter: brightness(0.45);
    z-index: -1;
}

.stApp{
    background: rgba(0,0,0,0.60);
}

/* =====================
   HIERARQUIA VISUAL (IMPORTANTE)
   ===================== */

/* TÍTULO PRINCIPAL */
h1 {
    color: white !important;
    font-size: 34px !important;
    font-weight: 800 !important;
}

/* SUBTÍTULO */
.subtitle {
    color: rgba(255,255,255,0.8);
    font-size: 16px;
    margin-bottom: 20px;
}

/* BLOCO DE INPUT DESTACADO */
div[data-baseweb="input"] {
    background: white !important;
    border-radius: 10px;
    padding: 8px;
    border: 2px solid rgba(255,255,255,0.2);
}

/* TEXTO DENTRO DO INPUT */
input {
    color: black !important;
    font-weight: 600;
}

/* PLACEHOLDER */
input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* BOTÃO */
button {
    background: #ffffff !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
}

/* RESULTADO EM BLOCOS */
.stDataFrame {
    background: rgba(255,255,255,0.95) !important;
    border-radius: 10px;
    padding: 10px;
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
# HEADER CLARO
# =====================
st.title("✈ CONSULTA T.O.")

st.markdown(
    '<div class="subtitle">Digite o Part Number abaixo para consultar</div>',
    unsafe_allow_html=True
)

# =====================
# INPUT (AGORA CLARO)
# =====================
pesquisa = st.text_input("🔎 Part Number")

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
st.subheader("➕ Adicionar novo item")

with st.form("novo_item", clear_on_submit=True):

    pn = st.text_input("Digite o Part Number (PN)")
    to = st.text_input("Digite o T.O.")

    salvar = st.form_submit_button("SALVAR")

    if salvar:

        if pn and to:
            sheet.append_row([pn, to])
            st.success("Item salvo com sucesso ✔")
            st.rerun()
        else:
            st.warning("Preencha todos os campos")
