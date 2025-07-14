import streamlit as st
from openai_promptlivre import enviar_prompt_livre

st.set_page_config(layout="wide", page_title="Prompt Livre - Agente Jurídico", initial_sidebar_state="expanded")
with st.sidebar:
    st.image("logo_eug.png", width=220)
    st.markdown(
        """
        <div style='background-color:#111124;padding:20px;border-radius:10px; text-align:center; margin-top: 10px;'>
            <a href='https://poc-goiania-v1.streamlit.app/' style='color:#fff;text-decoration:none;'><b>Análise Jurídica</b></a>
        </div>
        <div style='background-color:#111124;padding:20px;border-radius:10px; text-align:center; margin-top: 20px;'>
            <a href='/' style='color:#fff;text-decoration:none;'><b>Gerar Documentação</b></a>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.title("Prompt Livre")

st.markdown("Use o campo abaixo para digitar um prompt livre ou clique em um dos quebra-gelos abaixo:")

# Campo para prompt livre
prompt_text = st.text_area("Digite seu prompt", height=120)

col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.5, 2])
enviar = col1.button("Enviar")
quebra_termo = col2.button("Gerar Termo de referência")
quebra_minuta = col3.button("Gerar Minuta de Contrato")
quebra_edital = col4.button("Gerar Edital de Licitação")

resposta = None

if enviar and prompt_text.strip():
    with st.spinner("Consultando OpenAI..."):
        resposta = enviar_prompt_livre(prompt_text.strip())
elif quebra_termo:
    prompt_padrao = (
        "Gerar termo de referencia para aquisição de equipamentos de informática pela Prefeitura de Goiânia, "
        "com prazo de 12 meses, valor global de R$ 300.000,00, pagamento em até 30 dias, garantias legais, "
        "aplicação das penalidades previstas na Lei nº 14.133/2021, e fiscalização pelo Departamento de TI."
    )
    with st.spinner("Consultando OpenAI..."):
        resposta = enviar_prompt_livre(prompt_padrao)
elif quebra_minuta:
    prompt_padrao = (
        "Gerar minuta de contrato detalhada para aquisição de equipamentos pela Prefeitura de Goiânia, "
        "com prazo de 12 meses, valor global de R$ 300.000,00, pagamento em até 30 dias, garantias legais, "
        "aplicação das penalidades previstas na Lei nº 14.133/2021, e fiscalização pelo Departamentos competentes."
    )
    with st.spinner("Consultando OpenAI..."):
        resposta = enviar_prompt_livre(prompt_padrao)
elif quebra_edital:
    prompt_padrao = (
        "Gerar edital de licitação para aquisição de equipamentos de informática pela Prefeitura de Goiânia, "
        "com prazo de 12 meses, valor global de R$ 300.000,00, pagamento em até 30 dias, garantias legais, "
        "aplicação das penalidades previstas na Lei nº 14.133/2021, e fiscalização pelo Departamento de TI."
    )
    with st.spinner("Consultando OpenAI..."):
        resposta = enviar_prompt_livre(prompt_padrao)

if resposta:
    st.markdown("---")
    st.markdown("#### Resposta:")
    st.markdown(resposta, unsafe_allow_html=True)
