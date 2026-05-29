page_bg = """
<style>

/* FUNDO */
[data-testid="stAppViewContainer"]{
background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/c_scale,w_2048/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;

/* menos agressivo */
filter: brightness(0.45) contrast(0.9) saturate(0.9);
}

/* HEADER TRANSPARENTE */
[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

/* CAMADA ESCURA MAIS FORTE (para leitura) */
.stApp::before{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background: rgba(0,0,0,0.65);
z-index: 0;
}

/* CONTEÚDO ACIMA */
.stApp > div {
position: relative;
z-index: 1;
}

/* ===== MELHORIA PRINCIPAL ===== */
/* CAIXAS (INPUT, FORM, DATAFRAME) */
div[data-baseweb="input"],
div[data-baseweb="select"],
.stTextInput,
.stForm,
.stDataFrame {

background: rgba(20, 20, 20, 0.65) !important;
border-radius: 10px;
backdrop-filter: blur(6px);
padding: 10px;
}

/* INPUT MAIS LEGÍVEL */
input {
color: white !important;
}

/* TEXTO */
h1, h2, h3, p, label, div {
color: white !important;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
background: rgba(0,0,0,0.55);
}

</style>
"""
