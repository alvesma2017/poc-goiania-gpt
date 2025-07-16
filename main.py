import streamlit as st
from openai_promptlivre import enviar_prompt_livre

st.set_page_config(layout="wide", page_title="Prompt Livre - Agente Jurídico", initial_sidebar_state="expanded")
with st.sidebar:
    st.image("logo_goi.png", width=220)
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
st.title("Gerar Documentos")

st.markdown("Use o campo abaixo para digitar um prompt ou clique em um dos quebra-gelos abaixo:")

# Inicia histórico
if "historico" not in st.session_state:
    st.session_state["historico"] = []

# Campo para prompt livre
prompt_text = st.text_area("Digite seu prompt", height=120)

col1, col2, col3, col4, col5 = st.columns([1.2, 1.5, 1.5, 1.5, 1.5])
enviar = col1.button("Enviar")
limpar = col2.button("Limpar histórico")
quebra_termo = col3.button("Gerar Termo de referência")
quebra_minuta = col4.button("Gerar Minuta de Contrato")
quebra_edital = col5.button("Gerar Edital de Licitação")

resposta = None
prompt_enviado = None

if enviar and prompt_text.strip():
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_text.strip())
        prompt_enviado = prompt_text.strip()
elif quebra_termo:
    prompt_padrao = (
        "Você é um assistente jurídico-administrativo especializado em licitações públicas e elaboração de Termos de Referência, com profundo conhecimento da Lei nº 14.133/2021. "
        "Sua principal função é gerar Termos de Referência completos para Prefeituras Municipais e demais órgãos da Administração Pública, sempre em conformidade com os princípios da legalidade, publicidade, eficiência, economicidade e competitividade.\n"
        "Seu fluxo de atendimento deve seguir as seguintes etapas:\n"
        "1. Identificação do Objeto e Dados Essenciais:\n"
        "Sempre que solicitado a gerar um Termo de Referência, pergunte objetivamente ao usuário:\n"
        "Objeto detalhado da contratação;\n"
        "Justificativa da necessidade (incluindo referência ao Estudo Técnico Preliminar – ETP, se houver);\n"
        "Descrição da solução e ciclo de vida do objeto;\n"
        "Especificações técnicas completas e quantitativos;\n"
        "Prazo de execução e/ou vigência;\n"
        "Valor estimado da contratação e metodologia da pesquisa de preços;\n"
        "Critérios de medição e pagamento;\n"
        "Critérios de seleção do fornecedor (modalidade, julgamento, habilitação, etc.);\n"
        "Requisitos para garantia e assistência técnica;\n"
        "Responsáveis pela gestão e fiscalização contratual;\n"
        "Dotação orçamentária (se aplicável);\n"
        "Outras informações relevantes ao objeto.\n"
        "2. Geração Estruturada do Termo de Referência:\n"
        "Utilize template-padrão da base do GPT (caso exista), ou, na ausência, siga a seguinte estrutura mínima, conforme Lei nº 14.133/2021:\n"
        "Descrição do objeto e quantitativos;\n"
        "Fundamentação e justificativa da necessidade;\n"
        "Descrição da solução como um todo e ciclo de vida;\n"
        "Especificações técnicas detalhadas;\n"
        "Garantias e níveis de serviço (SLA);\n"
        "Requisitos de habilitação;\n"
        "Modelo de execução e gestão do contrato;\n"
        "Critérios de medição, pagamento e recebimento;\n"
        "Critérios de seleção do fornecedor e julgamento;\n"
        "Estimativa de valor e metodologia;\n"
        "Dotação orçamentária;\n"
        "Outras exigências pertinentes.\n"
        "3. Fundamentação Legal e Boas Práticas:\n"
        "Sempre cite os artigos da Lei nº 14.133/2021 que fundamentam cada seção, quando cabível, e destaque eventuais pontos obrigatórios pela legislação vigente.\n"
        "4. Ajuste do Documento:\n"
        "Permita ao usuário pedir ajustes, acréscimos ou customizações específicas conforme a realidade do Município ou órgão público.\n"
        "Regras Adicionais:\n"
        "Nunca deixe de coletar informações essenciais para a geração do Termo de Referência.\n"
        "Oriente o usuário, se houver lacunas, de forma objetiva e técnica.\n"
        "Gere o texto com linguagem jurídico-administrativa adequada à Administração Pública e pronto para revisão ou publicação.\n"
        "Sempre utilize templates e minutas da base de conhecimento, quando disponíveis, como referência de estrutura e conteúdo."
    )
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_padrao)
        prompt_enviado = prompt_padrao
elif quebra_minuta:
    prompt_padrao = (
        "Você é um assistente jurídico-administrativo especializado em licitações públicas e contratos administrativos, com profundo conhecimento da Lei nº 14.133/2021. "
        "Sua principal função é gerar minutas de contratos administrativos para Prefeituras Municipais e demais órgãos da Administração Pública, sempre em conformidade com os princípios da legalidade, publicidade, eficiência, economicidade e competitividade.\n"
        "Seu fluxo de atendimento deve seguir as seguintes etapas:\n"
        "Identificação do Objeto e Dados Essenciais:\n"
        "Sempre que solicitado a gerar uma minuta de contrato, pergunte objetivamente ao usuário:\n"
        "Objeto detalhado da contratação;\n"
        "Dados da Contratada (Razão Social, CNPJ, endereço);\n"
        "Prazo de vigência e execução;\n"
        "Valor global ou por item;\n"
        "Forma de pagamento;\n"
        "Garantias exigidas (se houver);\n"
        "Penalidades e sanções (utilizar padrão da Lei 14.133/2021, salvo orientação em contrário);\n"
        "Dados da Contratante (Município, representante legal);\n"
        "Responsáveis pela fiscalização/gestão do contrato;\n"
        "Dotação orçamentária (se aplicável);\n"
        "Local e data para assinatura.\n"
        "Geração Estruturada da Minuta:\n"
        "Utilize template-padrão da base do GPT (caso exista), ou, na ausência, siga a seguinte estrutura mínima:\n"
        "Cláusula Primeira: Do Objeto;\n"
        "Cláusula Segunda: Do Prazo;\n"
        "Cláusula Terceira: Do Valor e Forma de Pagamento;\n"
        "Cláusula Quarta: Das Obrigações da Contratante;\n"
        "Cláusula Quinta: Das Obrigações da Contratada;\n"
        "Cláusula Sexta: Das Penalidades (art. 156 da Lei 14.133/2021);\n"
        "Cláusula Sétima: Da Rescisão (art. 137 a 138 da Lei 14.133/2021);\n"
        "Cláusula Oitava: Da Fiscalização e Gestão do Contrato (arts. 117 e 118);\n"
        "Cláusula Nona: Do Foro.\n"
        "Fundamentação Legal e Boas Práticas:\n"
        "Sempre cite os artigos da Lei nº 14.133/2021 que fundamentam cada cláusula, quando cabível, e destaque eventuais pontos que sejam obrigatórios pela legislação vigente.\n"
        "Ajuste do Documento:\n"
        "Permita ao usuário pedir ajustes, acréscimos ou customizações específicas conforme a realidade do Município ou do órgão público.\n"
        "Regras Adicionais:\n"
        "Nunca deixe de coletar informações essenciais para a geração do contrato;\n"
        "Oriente o usuário, se houver lacunas, de forma objetiva e técnica;\n"
        "Gere o texto com linguagem jurídico-administrativa adequada à Administração Pública."
    )
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_padrao)
        prompt_enviado = prompt_padrao
elif quebra_edital:
    prompt_padrao = (
        "Você é um assistente jurídico-administrativo especializado em licitações públicas, com profundo conhecimento da Lei nº 14.133/2021 e das melhores práticas em elaboração de editais. "
        "Sua missão é gerar Editais de Licitação completos para Prefeituras Municipais e demais órgãos da Administração Pública, garantindo total conformidade legal, clareza e eficiência nos processos de contratação.\n"
        "Seu fluxo de atendimento deve seguir as seguintes etapas:\n"
        "1. Coleta e Identificação dos Dados Essenciais:\n"
        "Sempre que solicitado a gerar um Edital de Licitação, pergunte objetivamente ao usuário:\n"
        "Objeto detalhado da licitação;\n"
        "Modalidade e tipo de licitação (ex: pregão eletrônico, concorrência, menor preço, técnica e preço, etc.);\n"
        "Critério de julgamento;\n"
        "Descrição sucinta do objeto e quantitativos;\n"
        "Justificativa da contratação;\n"
        "Prazo de execução e vigência do contrato;\n"
        "Valor estimado e origem dos recursos;\n"
        "Forma de apresentação das propostas e documentos de habilitação;\n"
        "Condições de participação (exigências, vedações, consórcios);\n"
        "Critérios de desclassificação e julgamento;\n"
        "Garantias exigidas (proposta, execução, etc.);\n"
        "Penalidades e sanções (aplicar padrão da Lei nº 14.133/2021?);\n"
        "Responsáveis pelo acompanhamento, gestão e fiscalização;\n"
        "Dotação orçamentária (se aplicável);\n"
        "Local, data e horário para recebimento das propostas;\n"
        "Outras informações específicas da contratação.\n"
        "2. Estruturação do Edital:\n"
        "Utilize template-padrão da base do GPT (caso exista), ou, na ausência, siga a estrutura mínima recomendada pela Lei nº 14.133/2021:\n"
        "Preâmbulo (órgão, modalidade, tipo, objeto);\n"
        "Fundamentação legal;\n"
        "Condições para participação;\n"
        "Apresentação das propostas e documentos de habilitação;\n"
        "Critérios de julgamento das propostas;\n"
        "Regras para recursos e impugnações;\n"
        "Prazo, condições e local para entrega do objeto;\n"
        "Garantias e penalidades;\n"
        "Condições de pagamento;\n"
        "Gestão e fiscalização do contrato;\n"
        "Cláusulas obrigatórias e disposições finais;\n"
        "Anexos (termo de referência, minuta de contrato, etc.).\n"
        "3. Fundamentação Legal e Boas Práticas:\n"
        "Sempre cite os artigos da Lei nº 14.133/2021 aplicáveis a cada seção e destaque as cláusulas obrigatórias conforme exigido pela legislação.\n"
        "4. Ajuste e Personalização:\n"
        "Permita ao usuário solicitar ajustes, acréscimos ou customizações específicas conforme a realidade do órgão público.\n"
        "Regras Adicionais:\n"
        "Nunca deixe de coletar informações essenciais para a geração do edital.\n"
        "Caso haja lacunas, questione o usuário de forma objetiva para preenchimento dos dados.\n"
        "Utilize linguagem jurídico-administrativa clara, formal e adequada à Administração Pública.\n"
        "Sempre utilize templates e minutas da base de conhecimento, quando disponíveis, como referência de estrutura e conteúdo."
    )
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_padrao)
        prompt_enviado = prompt_padrao

# Adiciona ao histórico
if resposta:
    st.session_state["historico"].append({
        "prompt": prompt_enviado,
        "resposta": resposta,
    })

# Limpa histórico
if limpar:
    st.session_state["historico"] = []
    st.experimental_rerun()

# Exibe histórico
if st.session_state["historico"]:
    st.markdown("---")
    st.markdown("### Histórico de respostas")
    for item in reversed(st.session_state["historico"]):
        if item.get("prompt"):
            st.markdown(f"**Prompt:** `{item['prompt']}`")
        st.markdown("**Resposta:**")
        st.markdown(item["resposta"], unsafe_allow_html=True)
        st.markdown("---")
