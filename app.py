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

/* FUNDO */
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
   TÍTULO
   ===================== */
h1 {
    color: white !important;
    font-size: 34px;
    font-weight: 800;
}

/* =====================
   CARDS (MELHORA PRINCIPAL)
   ===================== */

/* CARD GERAL */
.block-card {
    background: rgba(255,255,255,0.92);
    padding: 18px;
    border-radius: 14px;
    margin-top: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* texto dentro dos cards */
.block-card label,
.block-card div,
.block-card span {
    color: #111 !important;
}

/* INPUTS DENTRO DO CARD */
.block-card input {
    background: white !important;
    color: black !important;
    font-weight: 600;
}

/* BOTÃO */
button {
    background: #111 !important;
    color: white !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
}

/* DATAFRAME */
.stDataFrame {
    background: rgba(255,255,255,0.95) !important;
    border-radius: 10px;
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
# HEADER
# =====================
st.title("✈ CONSULTA T.O.")

# =====================
# PN (AGORA DESTACADO)
# =====================
st.markdown('<div class="block-card">', unsafe_allow_html=True)

pesquisa = st.text_input("🔎 Digite o Part Number")

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

st.markdown('</div>', unsafe_allow_html=True)

# =====================
# ADICIONAR ITEM (OUTRO CARD)
# =====================
st.markdown('<div class="block-card">', unsafe_allow_html=True)

st.subheader("➕ Adicionar Novo Item")

with st.form("novo_item", clear_on_submit=True):

    pn = st.text_input("Part Number")
    to = st.text_input("T.O.")

    salvar = st.form_submit_button("SALVAR")

    if salvar:

        if pn and to:
            sheet.append_row([pn, to])
            st.success("Item salvo com sucesso ✔")
            st.rerun()
        else:
            st.warning("Preencha todos os campos")

st.markdown('</div>', unsafe_allow_html=True)
