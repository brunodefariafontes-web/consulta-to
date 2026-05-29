page_bg = """
<style>

/* =====================
   FUNDO (NÃO MEXE)
   ===================== */
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

/* camada escura (segura) */
.stApp{
    background: rgba(0,0,0,0.60);
}

/* =====================
   TEXTO SEGURO (SÓ O NECESSÁRIO)
   ===================== */
h1, h2, h3 {
    color: white !important;
}

label {
    color: white !important;
    font-weight: 700 !important;
}

/* =====================
   🔥 INPUTS (PN / T.O.)
   ===================== */
.stTextInput input,
.stTextArea textarea,
input, textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
}

/* placeholder */
input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* =====================
   BOTÃO
   ===================== */
.stButton > button {
    background: white !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
}

</style>
"""
