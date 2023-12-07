import streamlit as st
import joblib
import pandas as pd
import os


path_dir=os.path.dirname(os.path.abspath(__file__))
pkl_path_LR=os.path.join(path_dir, 'NN_Regressor.pkl')
pkl_path_NN_CLass_Model=os.path.join(path_dir, 'NN_Classificator.pkl')
pkl_path_Preprocessor_LR=os.path.join(path_dir, 'Preprocessor_reg.pkl')
pkl_path_Preprocessor_Class=os.path.join(path_dir, 'Preprocessor_class.pkl')


NN_Reg_Model = joblib.load(pkl_path_LR)
NN_CLass_Model = joblib.load(pkl_path_NN_CLass_Model)
Preprocessor_class = joblib.load(pkl_path_Preprocessor_Class)
Preprocessor_lr = joblib.load(pkl_path_Preprocessor_LR)

# Función para la página de bienvenida
def welcome_page():
    st.title('Bienvenido a la Aplicación Meteorológica')

    # Botones de la interfaz
    if st.button('¿Va a llover mañana?'):
        st.session_state.page = 'va_a_llover'  # Agrega la lógica de verificación

    if st.button('¿Cuánto va a llover mañana?'):
        st.session_state.page = 'Cuanto_va_llover'

def va_a_llover():
    st.title('Mañana, llueve o no ?')
    MinTemp = st.sidebar.text_input('Temp. Min', value='0.0')
    MaxTemp = st.sidebar.text_input('Temp. Max', value='0.0')
    rainfall = st.sidebar.text_input('Rainfall', value='0.0')
    evaporation = st.sidebar.text_input('Evaporation', value='0.0')
    sunshine = st.sidebar.text_input('Sunshine', value='0.0')
    windspeed = st.sidebar.text_input('WindSpeed', value='0.0')
    humidity = st.sidebar.text_input('Humidity', value='0.0')
    pressure = st.sidebar.text_input('Pressure', value='0.0')
    cloud = st.sidebar.text_input('Cloud', value='0.0')
    ano = st.sidebar.text_input('Año', value='0')
    mes = st.sidebar.text_input('Mes', value='0')
    dia = st.sidebar.text_input('Dia', value='0')
    rainfall = float(rainfall)
    MinTemp = float(MinTemp)
    MaxTemp = float(MaxTemp)
    evaporation = float(evaporation)
    sunshine = float(sunshine)
    windspeed = float(windspeed)
    humidity = float(humidity)
    pressure = float(pressure)
    cloud = float(cloud)
    ano = float(ano)
    mes = float(mes)
    dia = float(dia)

    st.sidebar.header('Input - Variables Categóricas')
    location = st.sidebar.selectbox('Location', ['Canberra', 'Sydney', 'Melbourne'])
    raintoday = st.sidebar.selectbox('RainToday', ['No', 'Yes'])
    winddir = st.sidebar.selectbox('WindDir', ['N', 'S', 'E', 'W'])
    input_data = pd.DataFrame({
        'MinTemp': [MinTemp],
        'MaxTemp': [MaxTemp],
        'Rainfall': [rainfall],
        'Evaporation': [evaporation],
        'Sunshine': [sunshine],
        'WindSpeed': [windspeed],
        'Humidity': [humidity],
        'Pressure': [pressure],
        'Cloud': [cloud],
        'Año': [ano],
        'Mes': [mes],
        'Dia': [dia],
        'Location': [location],
        'RainToday': [raintoday],
        'WindDir': [winddir],
    })
    if st.sidebar.button('Realizar Predicción'):
        input_data_Trans = Preprocessor_class.transform(input_data)
        prediction = NN_CLass_Model.predict(input_data_Trans)
        st.subheader('Resultado de la predicción:')
        if prediction == 1:
            st.write(f'Mañana va a llover 🌧️.')
        else:   
            st.write(f'Mañana no va a llover ☀️.')
    if st.button('Bienvenida'):
        st.session_state.page = 'welcome_page'
# Función para la página de predicción
def Cuanto_va_llover():
    st.title('Predicción de Lluvia')

    # Entrada de datos numéricos
    st.sidebar.header('Input - Variables Numéricas')
    MinTemp = st.sidebar.text_input('Temp. Min', value='0.0')
    MaxTemp = st.sidebar.text_input('Temp. Max', value='0.0')
    rainfall = st.sidebar.text_input('Rainfall', value='0.0')
    evaporation = st.sidebar.text_input('Evaporation', value='0.0')
    sunshine = st.sidebar.text_input('Sunshine', value='0.0')
    windspeed = st.sidebar.text_input('WindSpeed', value='0.0')
    humidity = st.sidebar.text_input('Humidity', value='0.0')
    pressure = st.sidebar.text_input('Pressure', value='0.0')
    cloud = st.sidebar.text_input('Cloud', value='0.0')
    ano = st.sidebar.text_input('Año', value='0')
    mes = st.sidebar.text_input('Mes', value='0')
    dia = st.sidebar.text_input('Dia', value='0')
    rainfall = float(rainfall)
    MinTemp = float(MinTemp)
    MaxTemp = float(MaxTemp)
    evaporation = float(evaporation)
    sunshine = float(sunshine)
    windspeed = float(windspeed)
    humidity = float(humidity)
    pressure = float(pressure)
    cloud = float(cloud)
    ano = float(ano)
    mes = float(mes)
    dia = float(dia)

    # Entrada de datos categóricos
    st.sidebar.header('Input - Variables Categóricas')
    location = st.sidebar.selectbox('Location', ['Canberra', 'Sydney', 'Melbourne'])
    raintoday = st.sidebar.selectbox('RainToday', ['No', 'Yes'])
    winddir = st.sidebar.selectbox('WindDir', ['N', 'S', 'E', 'W'])
    # Botón de predicción
    input_data = pd.DataFrame({
        'MinTemp': [MinTemp],
        'MaxTemp': [MaxTemp],
        'Rainfall': [rainfall],
        'Evaporation': [evaporation],
        'Sunshine': [sunshine],
        'WindSpeed': [windspeed],
        'Humidity': [humidity],
        'Pressure': [pressure],
        'Cloud': [cloud],
        'Año': [ano],
        'Mes': [mes],
        'Dia': [dia],
        'Location': [location],
        'RainToday': [raintoday],
        'WindDir': [winddir],
    })
    
    if st.sidebar.button('Realizar Predicción'):
        input_data_Trans = Preprocessor_lr.transform(input_data)
        prediction = NN_Reg_Model.predict(input_data_Trans)
        formatted_prediction = "{:.2f}".format(prediction[0][0])

        # Mostrar resultados
        st.subheader('Resultado de la predicción:')
        st.write(f'Para el día de mañana, el algoritmo predice que va a llover: {formatted_prediction}mm.')
    if st.button('Bienvenida'):
        st.session_state.page = 'welcome_page'


st.set_page_config(page_title='App de Predicción de Lluvia', page_icon=":partly_sunny:")

if 'page' not in st.session_state:
    st.session_state.page = 'welcome_page'  

if st.session_state.page == 'welcome_page':
    welcome_page()
elif st.session_state.page == 'Cuanto_va_llover':
    Cuanto_va_llover()
else:
    va_a_llover()




