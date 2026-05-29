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
# CSS FINAL (FUNDO D'ÁGUA FRACO)
# =====================
st.markdown("""
<style>

/* =====================
   FUNDO D'ÁGUA (BEM FRACO)
   ===================== */
.stApp {
    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/f_auto,dpr_auto,q_auto,fl_progressive/w_2048,h_1152,c_scale/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    /* efeito marca d'água */
    background-blend-mode: overlay;
    background-color: rgba(0, 0, 0, 0.75);
}

/* =====================
   INPUTS (BRANCO + PRETO)
   ===================== */
.stTextInput input,
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border: 1px solid #d0d0d0 !important;
    border-radius: 6px !important;
}

/* Streamlit inputs internos */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* placeholder */
input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* BOTÃO */
.stButton > button {
    background: #ffffff !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border-radius: 6px;
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
