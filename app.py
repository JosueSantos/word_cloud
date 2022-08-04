import streamlit as st

from creater_word_cloud import CreaterWordCloud

def main():
    st.header('Word Cloud - Nuvem de Palavras')
    st.write('A nuvem de palavras é uma seleção das palavras que mais se repetem em um determinado texto.')

    st.caption("Você pode criar a sua nuvem de palavras!")

    title = st.text_input("Título da Nuvem de Palavras")
    txt = st.text_area('Texto para a nuvem de palavras', max_chars=None)
    qtn = st.number_input("Quantidade de palavras na nuvem", value=50)

    if(txt):
        with st.spinner('Aguarde um pouco...'):
            wordcloud = CreaterWordCloud()
            plt = wordcloud.create(txt, title, qtn)
        
            st.pyplot(plt)

if __name__ == '__main__':
    main()