import streamlit as st
import pyttsx3
import pygame

pygame.mixer.init()
engine = pyttsx3.init()

textos = 'De tudo, ao meu amor serei atento. '\
         'Antes, e com tal zelo, e sempre, e tanto. '\
         'Que mesmo em face do maior encanto. '\
         'Dele se encante mais meu pensamento.'


def _inicializar():
    icon = ":fish:"
    st.set_page_config(page_title='Reproduzirer',
                       initial_sidebar_state='expanded',
                       layout='wide',
                       page_icon=icon)

    st.header('Texto pra Voz - Python')
    st.caption('reprodução de áudio: pyttsx3')
    st.caption('controle de áudio: pygame')
    st.markdown('** Texto: **')
    st.markdown(textos)


def _reproduzir():
    outfile = "audio.wav"
    engine.save_to_file(textos, outfile)
    engine.runAndWait()
    pygame.mixer.music.load(outfile)
    pygame.mixer.music.play()


def _parar():
    pygame.mixer.music.stop()


def _pausar():
    pygame.mixer.music.pause()


def _continuar():
    pygame.mixer.music.unpause()

_inicializar()

colunas = st.empty()
control = st.empty()
controle = control.radio('Controles', options=['Parar', 'Reproduzir', 'Pausar', 'Continuar'], index=0)

if controle == 'Reproduzir':
    _reproduzir()

elif controle == 'Pausar':
    _pausar()

elif controle == 'Continuar':
    _continuar()

elif controle == 'Parar':
    _parar()
