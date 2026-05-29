import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# =====================
# ESTILO FAB / GRIPEN
# =====================
page_bg = """
<style>

[data-testid="stAppViewContainer"]{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/2/2d/Saab_JAS_39_Gripen_-_RIAT_2013_%289528781376%29.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

.stApp{
background: rgba(0,0,0,0.70);
color: white;
}

h1, h2, h3, p, label, div{
color: white !important;
}

[data-testid="stSidebar"]{
background: rgba(0,0,0,0.5);
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# =====================
# CONFIG
# =====================
st.set_page_config(
    page_title="Consulta T.O.",
    page_icon="✈",
    layout="wide"
)

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

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Bras%C3%A3o_da_For%C3%A7a_A%C3%A9rea_Brasileira.svg/800px-Bras%C3%A3o_da_For%C3%A7a_A%C3%A9rea_Brasileira.svg.png",
    width=120
)

st.write(
    "Pesquisa rápida de Part Number"
)

# =====================
# PESQUISA
# =====================
pesquisa = st.text_input(
    "Digite o Part Number"
)

# =====================
# RESULTADO
# =====================
if pesquisa:

    resultado = df[
        df.iloc[:, 0]
        .astype(str)
        .str.contains(
            pesquisa,
            case=False,
            na=False
        )
    ]

    if not resultado.empty:

        st.success(
            f"{len(resultado)} resultado(s) encontrado(s)"
        )

        st.dataframe(
            resultado,
            use_container_width=True
        )

    else:

        st.error(
            "Nenhum Part Number encontrado"
        )

# =====================
# ADICIONAR ITEM
# =====================
st.divider()

st.subheader("➕ Adicionar Novo Item")

with st.form(
    "novo_item",
    clear_on_submit=True
):

    pn = st.text_input(
        "Part Number"
    )

    to = st.text_input(
        "T.O."
    )

    salvar = st.form_submit_button(
        "Salvar"
    )

    if salvar:

        if pn and to:

            sheet.append_row([
                pn,
                to
            ])

            st.success(
                "Item salvo com sucesso ✔"
            )

            st.rerun()

        else:

            st.warning(
                "Preencha todos os campos"
            )
