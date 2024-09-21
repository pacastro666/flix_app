import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService();
    actor = actor_service.get_actors()

    if actor:
        st.write('Lista de Atores/Atrizes:')
        actor_df = pd.json_normalize(actor)


        AgGrid(
            data=actor_df,
            reload_data=True,
            key='actor_grid',
            )
    else:
        st.warning('Nenhum Ator/atriz encontrado.')
            

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label="Data de Nascimento",
        value=datetime.today(),
        min_value=datetime(1600,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = ['BRASIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar Ator/Atriz!!')
    

