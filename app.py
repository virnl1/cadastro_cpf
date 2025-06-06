import streamlit as st
import dados
st.title("Cadastro de Clientes")

# Cadastro

st.header("Cadastrar Novo Cliente")

nome = st.text_input("Nome:")
cpf = st.text_input("CPF (somente números):")
email = st.text_input("Email:")
telefone = st.text_input("Telefone (somente números):")
import datetime
data_nascimento = st.date_input("Data de Nascimento:", min_value=datetime.date(1900, 1, 1))

if st.button("Cadastrar"):
    if cpf and nome and email and telefone and data_nascimento:
        dados.inserir_cliente(cpf, nome, email, telefone, str(data_nascimento))
        st.success("Cliente cadastrado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")

st.divider()

# Listar por nome
st.header("Listar Clientes por Nome")
nome_busca = st.text_input("Digite o nome do cliente:")
if st.button("Buscar"):
    if nome_busca:
        clientes = dados.buscar_por_nome(nome_busca)
        if clientes:
            st.table(clientes)
        else:
            st.warning("Nenhum cliente encontrado com esse nome.")
    else:
        st.error("Por favor, digite um nome para buscar.")


st.subheader("Remover Cliente")
id_remover = st.number_input("ID do Cliente a ser removido:", min_value=1, step=1)
if st.button("Remover Cliente"):
    dados.excluir_cliente(id_remover)
    st.success("Cliente removido com sucesso!")

# Listar Clientes
st.header("Listar Todos os Clientes")
clientes = dados.listar_clientes()
st.table(clientes)

