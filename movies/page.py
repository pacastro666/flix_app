import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
       st.write('Lista de Filmes')

       movies_df = pd.json_normalize(movies)
       movies_df = movies_df.drop(columns=['actors', 'genre.id'])
    

       AgGrid(
           data=movies_df,
           reload_data=True,
           key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado')
    
    st.title('Cadastrar Novo Filme')

    title = st.text_input('Título')

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )

    

        
