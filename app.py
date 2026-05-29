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
# FUNDO (MESMA BASE ANTERIOR)
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

/* fundo geral escuro */
.stApp{
    background: rgba(0,0,0,0.60);
}

/* HEADER */
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

/* =====================
   TEXTO (MANTIDO LIMPO)
   ===================== */
h1, h2, h3 {
    color: white !important;
}

p, label, span {
    color: rgba(255,255,255,0.90) !important;
}

/* =====================
   🔥 CORREÇÃO PRINCIPAL (PN VISÍVEL)
   ===================== */

/* INPUTS mais escuros (melhor contraste com fundo) */
div[data-baseweb="input"],
div[data-baseweb="select"],
.stTextInput,
.stForm,
.stDataFrame {
    background: rgba(25, 25, 25, 0.75) !important;
    border-radius: 10px;
    padding: 10px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* TEXTO DO INPUT (AGORA LEGÍVEL SEM SUMIR) */
input, textarea {
    color: white !important;
    font-weight: 600;
}

/* placeholder suave */
input::placeholder {
    color: rgba(255,255,255,0.5) !important;
}

/* BOTÃO VISÍVEL */
button {
    color: black !important;
    font-weight: 700 !important;
    background: rgba(255,255,255,0.95) !important;
    border-radius: 8px !important;
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
# PESQUISA (CLARA AGORA)
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
