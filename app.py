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
    layout="centered"
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
# TÍTULO
# =====================
st.title("✈ CONSULTA T.O.")

st.write(
    "Digite o Part Number para localizar a T.O."
)

# =====================
# PESQUISA
# =====================
pesquisa = st.text_input(
    "Part Number"
)

# =====================
# RESULTADO
# =====================
if pesquisa:

    resultado = df[
        df.iloc[:, 0]
        .astype(str)
        .str.upper()
        == pesquisa.upper()
    ]

    st.divider()

    if not resultado.empty:

        to = resultado.iloc[0, 1]

        st.success("T.O. localizada com sucesso")

        st.markdown(
            f"""
            ## ✈ Resultado

            ### PN:
            `{pesquisa}`

            ### T.O.:
            `{to}`
            """
        )

    else:

        st.error(
            "Part Number não encontrado"
        )
```
