st.markdown("""
<style>

/* =====================
   FUNDO REAL (FORÇADO NO BODY)
   ===================== */
html, body, .stApp {
    height: 100%;import streamlit as st
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
# CSS LIMPO (SÓ TEXTO BRANCO NO FIXO)
# =====================
st.markdown("""
<style>

/* títulos */
h1, h2, h3 {
    color: #ffffff !important;
}

/* textos fixos */
p, span, label {
    color: #ffffff !important;
}

/* botão texto branco */
.stButton > button {
    color: #ffffff !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

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
}

/* camada principal do Streamlit */
.stApp {
    background: transparent !important;
}

/* fundo aplicado no HTML inteiro */
body {
    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/f_auto,dpr_auto,q_auto,fl_progressive/w_2048,h_1152,c_scale/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    /* escurecimento pra leitura */
    background-color: rgba(0,0,0,0.70);
    background-blend-mode: darken;
}

/* =====================
   TEXTO FIXO BRANCO
   ===================== */
h1, h2, h3, p, span, label {
    color: white !important;
}

/* botão branco */
.stButton > button {
    color: white !important;
    font-weight: 700 !important;
}

/* inputs continuam normais */
</style>
""", unsafe_allow_html=True)
