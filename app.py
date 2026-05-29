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
# FUNDO (FIX REAL PC + MOBILE IGUAL)
# =====================
page_bg = """
<style>

/* FUNDO FIXO REAL (resolve mobile) */
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

    filter: brightness(0.55) contrast(0.95);
    z-index: -1;
}

/* remove fundo padrão branco do Streamlit */
.stApp{
background: rgba(0,0,0,0.55);
}

/* HEADER */
[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

/* =====================
   PADRÃO VISUAL (BLOCO ÚNICO TIPO "PAINEL")
   ===================== */

/* tudo dentro do app fica alinhado em bloco */
.block-container{
max-width: 1100px;
padding-top: 2rem;
padding-bottom: 2rem;
}

/* caixas principais (input + form + tabela) */
div[data-baseweb="input"],
div[data-baseweb="select"],
.stTextInput,
.stForm,
.stDataFrame {
    background: rgba(20, 20, 20, 0.70) !important;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
}

/* INPUTS */
input, textarea {
    color: white !important;
    font-weight: 500;
}

/* placeholder */
input::placeholder {
    color: rgba(255, 255, 255, 0.5) !important;
}

/* TEXTO GERAL */
h1, h2, h3, p, label, span {
    color: rgba(255,255,255,0.92) !important;
}

/* SIDEBAR */
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
# TITULO
# =====================
st.title("✈ CONSULTA T.O.")
st.write("Pesquisa rápida de Part Number")

# =====================
# PESQUISA (BLOCO PADRÃO)
# =====================
with st.container():
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
# ADICIONAR ITEM (MESMO PADRÃO VISUAL)
# =====================
st.divider()
st.subheader("➕ Adicionar Novo Item")

with st.container():
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
