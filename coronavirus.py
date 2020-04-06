import sys
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import time
import matplotlib
import streamlit as st
import altair as alt
import time

if sys.version_info[0] < 3:
    reload(sys) # noqa: F821 pylint:disable=undefined-variable
    sys.setdefaultencoding("utf-8")
# Functions
@st.cache
def getData():
    plt.style.use('fivethirtyeight')
    headers = {
        'authority': 'www.epdata.es',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.epdata.es',
        'sec-fetch-site': 'same-origin',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    }
    common_init = '{"Host":"www.epdata.es",'
    common_end = ',"Formato":"json"}'

    # Spain
    cases_spain = '"Guid":"476812f9-73a2-4b5f-a74c-4824bc8b4a17"'
    deaths_accum_spain = '"Guid":"b2568be9-c6b6-4056-86d6-02c6d45b1696"'
    recovered_accum_spain = '"Guid":"58d0919c-8ad1-4a3f-9255-55f5b116da23"'

    response_cases_spain = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_spain + common_end).json()
    response_deaths_accum_spain = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_accum_spain + common_end).json()
    response_recovered_accum_spain = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + recovered_accum_spain + common_end).json()


   # Andalucia
    cases_andalucia = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-290"'
    deaths_andalucia = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-290"'

    response_cases_andalucia = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_andalucia + common_end).json()
    response_deaths_andalucia = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_andalucia + common_end).json()

    # Aragon
    cases_aragon = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-291"'
    deaths_aragon = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-291"'

    response_cases_aragon = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_aragon + common_end).json()
    response_deaths_aragon = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_aragon + common_end).json()

    # Asturias
    cases_asturias = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-292"'
    deaths_asturias = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-292"'

    response_cases_asturias = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_asturias + common_end).json()
    response_deaths_asturias = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_asturias + common_end).json()

    # Canarias
    cases_canarias = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-293"'
    deaths_canarias = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-293"'

    response_cases_canarias = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_canarias + common_end).json()
    response_deaths_canarias = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_canarias + common_end).json()

    # Cantabria
    cases_cantabria = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-294"'
    deaths_cantabria = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-294"'

    response_cases_cantabria  = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_cantabria  + common_end).json()
    response_deaths_cantabria  = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_cantabria  + common_end).json()

    # Castilla y Leon
    cases_castilla_y_leon = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-295"'
    deaths_castilla_y_leon = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-295"'

    response_cases_castilla_y_leon = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_castilla_y_leon + common_end).json()
    response_deaths_castilla_y_leon = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_castilla_y_leon + common_end).json()

    # Castilla La Mancha
    cases_castilla_la_mancha = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-296"'
    deaths_castilla_la_mancha = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-296"'

    response_cases_castilla_la_mancha= requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_castilla_la_mancha+ common_end).json()
    response_deaths_castilla_la_mancha= requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_castilla_la_mancha+ common_end).json()

    # Catalunya
    cases_catalunya = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-297"'
    deaths_catalunya = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-297"'

    response_cases_catalunya  = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_catalunya  + common_end).json()
    response_deaths_catalunya  = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_catalunya  + common_end).json()

    # Ceuta
    cases_ceuta = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-298"'
    deaths_ceuta = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-298"'

    response_cases_ceuta = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_ceuta + common_end).json()
    response_deaths_ceuta = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_ceuta + common_end).json()

    # Comunidad Valenciana
    cases_comunidad_valenciana = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-299"'
    deaths_comunidad_valenciana = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-299"'

    response_cases_comunidad_valenciana  = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_comunidad_valenciana  + common_end).json()
    response_deaths_comunidad_valenciana  = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_comunidad_valenciana  + common_end).json()

    # Extremadura
    cases_extremadura = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-300"'
    deaths_extremadura = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-300"'

    response_cases_extremadura = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_extremadura + common_end).json()
    response_deaths_extremadura = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_extremadura + common_end).json()

    # Galicia
    cases_galicia = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-301"'
    deaths_galicia = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-301"'

    response_cases_galicia = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_galicia + common_end).json()
    response_deaths_galicia = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_galicia + common_end).json()

    # Islas Baleares
    cases_islas_baleares = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-302"'
    deaths_islas_baleares = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-302"'

    response_cases_islas_baleares = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_islas_baleares + common_end).json()
    response_deaths_islas_baleares = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_islas_baleares + common_end).json()

    # La Rioja
    cases_la_rioja = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-303"'
    deaths_la_rioja = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-303"'

    response_cases_la_rioja = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_la_rioja + common_end).json()
    response_deaths_la_rioja = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_la_rioja + common_end).json()

    # Madrid
    cases_madrid = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-304"'
    deaths_madrid = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-304"'

    response_cases_madrid = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_madrid + common_end).json()
    response_deaths_madrid = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_madrid + common_end).json()

    # Melilla
    cases_melilla = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-305"'
    deaths_melilla = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-305"'

    response_cases_melilla = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_melilla + common_end).json()
    response_deaths_melilla = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_melilla + common_end).json()

    # Murcia
    cases_murcia = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-306"'
    deaths_murcia = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-306"'

    response_cases_murcia = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_murcia + common_end).json()
    response_deaths_murcia = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_murcia + common_end).json()

    # Navarra
    cases_navarra = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-307"'
    deaths_navarra = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-307"'

    response_cases_navarra = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_navarra + common_end).json()
    response_deaths_navarra = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_navarra + common_end).json()

    # Pais Vasco
    cases_pais_vasco = '"Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-308"'
    deaths_pais_vasco = '"Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2-308"'

    response_cases_pais_vasco = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + cases_pais_vasco + common_end).json()
    response_deaths_pais_vasco = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = common_init + deaths_pais_vasco + common_end).json()

    # Dictionaries and constants
    day_init_quarantine = 44
    day14_init_quarantine = 59
    day14_strict_quarantine = 73
    first_day_to_plot = 33
    last_day_to_plot = 75
    
    # Create raw dataframe

    # Spain
    raw_cases_spain = pd.read_json(response_cases_spain)
    raw_deaths_accum_spain = pd.read_json(response_deaths_accum_spain)
    raw_recovered_accum_spain = pd.read_json(response_recovered_accum_spain)

    # Andalucia
    raw_cases_andalucia = pd.read_json(response_cases_andalucia)
    raw_deaths_andalucia = pd.read_json(response_deaths_andalucia)

    # Aragon
    raw_cases_aragon = pd.read_json(response_cases_aragon)
    raw_deaths_aragon = pd.read_json(response_deaths_aragon)

    # Asturias
    raw_cases_asturias = pd.read_json(response_cases_asturias)
    raw_deaths_asturias = pd.read_json(response_deaths_asturias)

    # Canarias
    raw_cases_canarias = pd.read_json(response_cases_canarias)
    raw_deaths_canarias = pd.read_json(response_deaths_canarias)

    # Cantabria
    raw_cases_cantabria = pd.read_json(response_cases_cantabria)
    raw_deaths_cantabria = pd.read_json(response_deaths_cantabria)

    # Castilla y Leon
    raw_cases_castilla_y_leon = pd.read_json(response_cases_castilla_y_leon)
    raw_deaths_castilla_y_leon = pd.read_json(response_deaths_castilla_y_leon)

    # Castilla La Mancha
    raw_cases_castilla_la_mancha = pd.read_json(response_cases_castilla_la_mancha)
    raw_deaths_castilla_la_mancha = pd.read_json(response_deaths_castilla_la_mancha)

    # Catalunya
    raw_cases_catalunya = pd.read_json(response_cases_catalunya)
    raw_deaths_catalunya = pd.read_json(response_deaths_catalunya)

    # Ceuta
    raw_cases_ceuta = pd.read_json(response_cases_ceuta)
    raw_deaths_ceuta = pd.read_json(response_deaths_ceuta)

    # Comunidad Valenciana
    raw_cases_comunidad_valenciana = pd.read_json(response_cases_comunidad_valenciana )
    raw_deaths_comunidad_valenciana = pd.read_json(response_deaths_comunidad_valenciana )

    # Extremadura
    raw_cases_extremadura = pd.read_json(response_cases_extremadura)
    raw_deaths_extremadura = pd.read_json(response_deaths_extremadura)

    # Galicia
    raw_cases_galicia = pd.read_json(response_cases_galicia)
    raw_deaths_galicia = pd.read_json(response_deaths_galicia)

    # Islas Baleares
    raw_cases_islas_baleares = pd.read_json(response_cases_islas_baleares)
    raw_deaths_islas_baleares = pd.read_json(response_deaths_islas_baleares)

    # La Rioja
    raw_cases_la_rioja = pd.read_json(response_cases_la_rioja)
    raw_deaths_la_rioja = pd.read_json(response_deaths_la_rioja)

    # Madrid
    raw_cases_madrid = pd.read_json(response_cases_madrid)
    raw_deaths_madrid = pd.read_json(response_deaths_madrid)

    # Melilla
    raw_cases_melilla = pd.read_json(response_cases_melilla)
    raw_deaths_melilla = pd.read_json(response_deaths_melilla)

    # Murcia
    raw_cases_murcia = pd.read_json(response_cases_murcia)
    raw_deaths_murcia = pd.read_json(response_deaths_murcia)

    # Navarra
    raw_cases_navarra = pd.read_json(response_cases_navarra)
    raw_deaths_navarra = pd.read_json(response_deaths_navarra)

    # Pais Vasco
    raw_cases_pais_vasco = pd.read_json(response_cases_pais_vasco)
    raw_deaths_pais_vasco = pd.read_json(response_deaths_pais_vasco)

    # Create dataframe Spain

    df_cases_spain = createDataframeFromJson(raw_cases_spain)
    df_cases_spain.rename(columns={'Cases': 'Cases_Spain'}, inplace= True)
    df_deaths_accum_spain = createDataframeFromJson(raw_deaths_accum_spain)
    df_deaths_accum_spain.rename(columns={'Cases': 'DeathsAccum_Spain'}, inplace= True)
    df_recovered_accum_spain = createDataframeFromJson(raw_recovered_accum_spain)
    df_recovered_accum_spain.rename(columns={'Cases': 'RecoveredAccum_Spain'}, inplace= True)

    df_spain0 = pd.merge(df_cases_spain[['Period', 'Day','Cases_Spain']],
                    df_deaths_accum_spain[['Period', 'DeathsAccum_Spain']],
                    on='Period', 
                    how='left')
    df_spain = pd.merge(df_spain0[['Period', 'Day','Cases_Spain','DeathsAccum_Spain']],
                    df_recovered_accum_spain[['Period', 'RecoveredAccum_Spain']],
                    on='Period', 
                    how='left')


    # Create dataframe Andalucia

    df_cases_andalucia = createDataframeFromJson(raw_cases_andalucia)
    df_cases_andalucia.rename(columns={'Cases': 'Cases_Andalucia'}, inplace= True)
    df_deaths_andalucia = createDataframeFromJson(raw_deaths_andalucia)
    df_deaths_andalucia.rename(columns={'Cases': 'Deaths_Andalucia'}, inplace= True)

    df_andalucia = pd.merge(df_cases_andalucia[['Period', 'Day','Cases_Andalucia']],
                    df_deaths_andalucia[['Period', 'Deaths_Andalucia']],
                    on='Period', 
                    how='left')

    # Create dataframe Aragon

    df_cases_aragon = createDataframeFromJson(raw_cases_aragon)
    df_cases_aragon.rename(columns={'Cases': 'Cases_Aragon'}, inplace= True)
    df_deaths_aragon = createDataframeFromJson(raw_deaths_aragon)
    df_deaths_aragon.rename(columns={'Cases': 'Deaths_Aragon'}, inplace= True)

    df_aragon = pd.merge(df_cases_aragon[['Period', 'Day','Cases_Aragon']],
                    df_deaths_aragon[['Period', 'Deaths_Aragon']],
                    on='Period', 
                    how='left')

    # Create dataframe Asturias

    df_cases_asturias = createDataframeFromJson(raw_cases_asturias)
    df_cases_asturias.rename(columns={'Cases': 'Cases_Asturias'}, inplace= True)
    df_deaths_asturias = createDataframeFromJson(raw_deaths_asturias)
    df_deaths_asturias.rename(columns={'Cases': 'Deaths_Asturias'}, inplace= True)

    df_asturias = pd.merge(df_cases_asturias[['Period', 'Day','Cases_Asturias']],
                    df_deaths_asturias[['Period', 'Deaths_Asturias']],
                    on='Period', 
                    how='left')

    # Create dataframe Canarias

    df_cases_canarias = createDataframeFromJson(raw_cases_canarias)
    df_cases_canarias.rename(columns={'Cases': 'Cases_Canarias'}, inplace= True)
    df_deaths_canarias = createDataframeFromJson(raw_deaths_canarias)
    df_deaths_canarias.rename(columns={'Cases': 'Deaths_Canarias'}, inplace= True)

    df_canarias = pd.merge(df_cases_canarias[['Period', 'Day','Cases_Canarias']],
                    df_deaths_canarias[['Period', 'Deaths_Canarias']],
                    on='Period', 
                    how='left')

    # Create dataframe Cantabria

    df_cases_cantabria = createDataframeFromJson(raw_cases_cantabria)
    df_cases_cantabria.rename(columns={'Cases': 'Cases_Cantabria'}, inplace= True)
    df_deaths_cantabria = createDataframeFromJson(raw_deaths_cantabria)
    df_deaths_cantabria.rename(columns={'Cases': 'Deaths_Cantabria'}, inplace= True)

    df_cantabria = pd.merge(df_cases_cantabria[['Period', 'Day','Cases_Cantabria']],
                    df_deaths_cantabria[['Period', 'Deaths_Cantabria']],
                    on='Period', 
                    how='left')

    # Create dataframe Castilla y Leon

    df_cases_castilla_y_leon = createDataframeFromJson(raw_cases_castilla_y_leon)
    df_cases_castilla_y_leon.rename(columns={'Cases': 'Cases_Castilla_y_Leon'}, inplace= True)
    df_deaths_castilla_y_leon = createDataframeFromJson(raw_deaths_castilla_y_leon)
    df_deaths_castilla_y_leon.rename(columns={'Cases': 'Deaths_Castilla_y_Leon'}, inplace= True)

    df_castilla_y_leon = pd.merge(df_cases_castilla_y_leon[['Period', 'Day','Cases_Castilla_y_Leon']],
                    df_deaths_castilla_y_leon[['Period', 'Deaths_Castilla_y_Leon']],
                    on='Period', 
                    how='left')

    # Create dataframe Castilla La Mancha

    df_cases_castilla_la_mancha = createDataframeFromJson(raw_cases_castilla_la_mancha)
    df_cases_castilla_la_mancha.rename(columns={'Cases': 'Cases_Castilla_La_Mancha'}, inplace= True)
    df_deaths_castilla_la_mancha = createDataframeFromJson(raw_deaths_castilla_la_mancha)
    df_deaths_castilla_la_mancha.rename(columns={'Cases': 'Deaths_Castilla_La_Mancha'}, inplace= True)

    df_castilla_la_mancha = pd.merge(df_cases_castilla_la_mancha[['Period', 'Day','Cases_Castilla_La_Mancha']],
                    df_deaths_castilla_la_mancha[['Period', 'Deaths_Castilla_La_Mancha']],
                    on='Period', 
                    how='left')

    # Create dataframe Catalunya

    df_cases_catalunya = createDataframeFromJson(raw_cases_catalunya)
    df_cases_catalunya.rename(columns={'Cases': 'Cases_Catalunya'}, inplace= True)
    df_deaths_catalunya = createDataframeFromJson(raw_deaths_catalunya)
    df_deaths_catalunya.rename(columns={'Cases': 'Deaths_Catalunya'}, inplace= True)

    df_catalunya = pd.merge(df_cases_catalunya[['Period', 'Day','Cases_Catalunya']],
                    df_deaths_catalunya[['Period', 'Deaths_Catalunya']],
                    on='Period', 
                    how='left')

    # Create dataframe Ceuta

    df_cases_ceuta = createDataframeFromJson(raw_cases_ceuta)
    df_cases_ceuta.rename(columns={'Cases': 'Cases_Ceuta'}, inplace= True)
    df_deaths_ceuta = createDataframeFromJson(raw_deaths_ceuta)
    df_deaths_ceuta.rename(columns={'Cases': 'Deaths_Ceuta'}, inplace= True)

    df_ceuta = pd.merge(df_cases_ceuta[['Period', 'Day','Cases_Ceuta']],
                    df_deaths_ceuta[['Period', 'Deaths_Ceuta']],
                    on='Period', 
                    how='left')

    # Create dataframe Comunidad Valenciana

    df_cases_comunidad_valenciana = createDataframeFromJson(raw_cases_comunidad_valenciana)
    df_cases_comunidad_valenciana.rename(columns={'Cases': 'Cases_Comunidad_Valenciana'}, inplace= True)
    df_deaths_comunidad_valenciana = createDataframeFromJson(raw_deaths_comunidad_valenciana)
    df_deaths_comunidad_valenciana.rename(columns={'Cases': 'Deaths_Comunidad_Valenciana'}, inplace= True)

    df_comunidad_valenciana = pd.merge(df_cases_comunidad_valenciana[['Period', 'Day','Cases_Comunidad_Valenciana']],
                    df_deaths_comunidad_valenciana[['Period', 'Deaths_Comunidad_Valenciana']],
                    on='Period', 
                    how='left')

    # Create dataframe Extremadura

    df_cases_extremadura = createDataframeFromJson(raw_cases_extremadura)
    df_cases_extremadura.rename(columns={'Cases': 'Cases_Extremadura'}, inplace= True)
    df_deaths_extremadura = createDataframeFromJson(raw_deaths_extremadura)
    df_deaths_extremadura.rename(columns={'Cases': 'Deaths_Extremadura'}, inplace= True)

    df_extremadura = pd.merge(df_cases_extremadura[['Period', 'Day','Cases_Extremadura']],
                    df_deaths_extremadura[['Period', 'Deaths_Extremadura']],
                    on='Period', 
                    how='left')

    # Create dataframe Galicia

    df_cases_galicia = createDataframeFromJson(raw_cases_galicia)
    df_cases_galicia.rename(columns={'Cases': 'Cases_Galicia'}, inplace= True)
    df_deaths_galicia = createDataframeFromJson(raw_deaths_galicia)
    df_deaths_galicia.rename(columns={'Cases': 'Deaths_Galicia'}, inplace= True)

    df_galicia = pd.merge(df_cases_galicia[['Period', 'Day','Cases_Galicia']],
                    df_deaths_galicia[['Period', 'Deaths_Galicia']],
                    on='Period', 
                    how='left')

    # Create dataframe Islas Baleares

    df_cases_islas_baleares = createDataframeFromJson(raw_cases_islas_baleares)
    df_cases_islas_baleares.rename(columns={'Cases': 'Cases_Islas_Baleares'}, inplace= True)
    df_deaths_islas_baleares = createDataframeFromJson(raw_deaths_islas_baleares)
    df_deaths_islas_baleares.rename(columns={'Cases': 'Deaths_Islas_Baleares'}, inplace= True)

    df_islas_baleares = pd.merge(df_cases_islas_baleares[['Period', 'Day','Cases_Islas_Baleares']],
                    df_deaths_islas_baleares[['Period', 'Deaths_Islas_Baleares']],
                    on='Period', 
                    how='left')

    # Create dataframe La Rioja

    df_cases_la_rioja = createDataframeFromJson(raw_cases_la_rioja)
    df_cases_la_rioja.rename(columns={'Cases': 'Cases_La_Rioja'}, inplace= True)
    df_deaths_la_rioja = createDataframeFromJson(raw_deaths_la_rioja)
    df_deaths_la_rioja.rename(columns={'Cases': 'Deaths_La_Rioja'}, inplace= True)

    df_la_rioja = pd.merge(df_cases_la_rioja[['Period', 'Day','Cases_La_Rioja']],
                    df_deaths_la_rioja[['Period', 'Deaths_La_Rioja']],
                    on='Period', 
                    how='left')

    # Create dataframe Madrid

    df_cases_madrid = createDataframeFromJson(raw_cases_madrid)
    df_cases_madrid.rename(columns={'Cases': 'Cases_Madrid'}, inplace= True)
    df_deaths_madrid = createDataframeFromJson(raw_deaths_madrid)
    df_deaths_madrid.rename(columns={'Cases': 'Deaths_Madrid'}, inplace= True)

    df_madrid = pd.merge(df_cases_madrid[['Period', 'Day','Cases_Madrid']],
                    df_deaths_madrid[['Period', 'Deaths_Madrid']],
                    on='Period', 
                    how='left')

    # Create dataframe Melilla

    df_cases_melilla = createDataframeFromJson(raw_cases_melilla)
    df_cases_melilla.rename(columns={'Cases': 'Cases_Melilla'}, inplace= True)
    df_deaths_melilla = createDataframeFromJson(raw_deaths_melilla)
    df_deaths_melilla.rename(columns={'Cases': 'Deaths_Melilla'}, inplace= True)

    df_melilla = pd.merge(df_cases_melilla[['Period', 'Day','Cases_Melilla']],
                    df_deaths_melilla[['Period', 'Deaths_Melilla']],
                    on='Period', 
                    how='left')

    # Create dataframe Murcia

    df_cases_murcia = createDataframeFromJson(raw_cases_murcia)
    df_cases_murcia.rename(columns={'Cases': 'Cases_Murcia'}, inplace= True)
    df_deaths_murcia = createDataframeFromJson(raw_deaths_murcia)
    df_deaths_murcia.rename(columns={'Cases': 'Deaths_Murcia'}, inplace= True)

    df_murcia = pd.merge(df_cases_murcia[['Period', 'Day','Cases_Murcia']],
                    df_deaths_murcia[['Period', 'Deaths_Murcia']],
                    on='Period', 
                    how='left')

    # Create dataframe Navarra

    df_cases_navarra = createDataframeFromJson(raw_cases_navarra)
    df_cases_navarra.rename(columns={'Cases': 'Cases_Navarra'}, inplace= True)
    df_deaths_navarra = createDataframeFromJson(raw_deaths_navarra)
    df_deaths_navarra.rename(columns={'Cases': 'Deaths_Navarra'}, inplace= True)

    df_navarra = pd.merge(df_cases_navarra[['Period', 'Day','Cases_Navarra']],
                    df_deaths_navarra[['Period', 'Deaths_Navarra']],
                    on='Period', 
                    how='left')

    # Create dataframe Pais Vasco

    df_cases_pais_vasco = createDataframeFromJson(raw_cases_pais_vasco)
    df_cases_pais_vasco.rename(columns={'Cases': 'Cases_Pais_Vasco'}, inplace= True)
    df_deaths_pais_vasco = createDataframeFromJson(raw_deaths_pais_vasco)
    df_deaths_pais_vasco.rename(columns={'Cases': 'Deaths_Pais_Vasco'}, inplace= True)

    df_pais_vasco = pd.merge(df_cases_pais_vasco[['Period', 'Day','Cases_Pais_Vasco']],
                    df_deaths_pais_vasco[['Period', 'Deaths_Pais_Vasco']],
                    on='Period', 
                    how='left')

    # Create dataframe global

    df_global = df_spain[['Period', 'Day','Cases_Spain','DeathsAccum_Spain', 'RecoveredAccum_Spain']].merge(
                df_andalucia[['Period', 'Cases_Andalucia', 'Deaths_Andalucia']], on = 'Period', how = 'left').merge(
                df_aragon[['Period', 'Cases_Aragon', 'Deaths_Aragon']], on = 'Period', how = 'left').merge(
                df_asturias[['Period', 'Cases_Asturias', 'Deaths_Asturias']], on = 'Period', how = 'left').merge(
                df_canarias[['Period', 'Cases_Canarias', 'Deaths_Canarias']], on = 'Period', how = 'left').merge(
                df_cantabria[['Period', 'Cases_Cantabria', 'Deaths_Cantabria']], on = 'Period', how = 'left').merge(
                df_castilla_y_leon[['Period', 'Cases_Castilla_y_Leon', 'Deaths_Castilla_y_Leon']], on = 'Period', how = 'left').merge(
                df_castilla_la_mancha[['Period', 'Cases_Castilla_La_Mancha', 'Deaths_Castilla_La_Mancha']], on = 'Period', how = 'left').merge(
                df_catalunya[['Period', 'Cases_Catalunya', 'Deaths_Catalunya']], on = 'Period', how = 'left').merge(
                df_ceuta[['Period', 'Cases_Ceuta', 'Deaths_Ceuta']], on = 'Period', how = 'left').merge(
                df_comunidad_valenciana[['Period', 'Cases_Comunidad_Valenciana', 'Deaths_Comunidad_Valenciana']], on = 'Period', how = 'left').merge(
                df_extremadura[['Period', 'Cases_Extremadura', 'Deaths_Extremadura']], on = 'Period', how = 'left').merge(
                df_galicia[['Period', 'Cases_Galicia', 'Deaths_Galicia']], on = 'Period', how = 'left').merge(
                df_islas_baleares[['Period', 'Cases_Islas_Baleares', 'Deaths_Islas_Baleares']], on = 'Period', how = 'left').merge(
                df_la_rioja[['Period', 'Cases_La_Rioja', 'Deaths_La_Rioja']], on = 'Period', how = 'left').merge(
                df_madrid[['Period', 'Cases_Madrid', 'Deaths_Madrid']], on = 'Period', how = 'left').merge(
                df_melilla[['Period', 'Cases_Melilla', 'Deaths_Melilla']], on = 'Period', how = 'left').merge(
                df_murcia[['Period', 'Cases_Murcia', 'Deaths_Murcia']], on = 'Period', how = 'left').merge(
                df_navarra[['Period', 'Cases_Navarra', 'Deaths_Navarra']], on = 'Period', how = 'left').merge(
                df_pais_vasco[['Period', 'Cases_Pais_Vasco', 'Deaths_Pais_Vasco']])

    # Compute missing fields and metrics

    # Deaths and recovered in Spain from accumulative data
    df_global['Deaths_Spain'] = fromAccumToSingleValues(df_global['DeathsAccum_Spain'].values)
    df_global['Recovered_Spain'] = fromAccumToSingleValues(df_global['RecoveredAccum_Spain'].values)

    # Cumulative sum Andalucia
    df_global['CasesAccum_Andalucia'] = df_global['Cases_Andalucia'].cumsum()
    df_global['DeathsAccum_Andalucia'] = df_global['Deaths_Andalucia'].cumsum()

    # Cumulative sum Aragon
    df_global['CasesAccum_Aragon'] = df_global['Cases_Aragon'].cumsum()
    df_global['DeathsAccum_Aragon'] = df_global['Deaths_Aragon'].cumsum()
    
    # Cumulative sum Asturias
    df_global['CasesAccum_Asturias'] = df_global['Cases_Asturias'].cumsum()
    df_global['DeathsAccum_Asturias'] = df_global['Deaths_Asturias'].cumsum()
    
    # Cumulative sum Canarias
    df_global['CasesAccum_Canarias'] = df_global['Cases_Canarias'].cumsum()
    df_global['DeathsAccum_Canarias'] = df_global['Deaths_Canarias'].cumsum()
    
    # Cumulative sum Cantabria
    df_global['CasesAccum_Cantabria'] = df_global['Cases_Cantabria'].cumsum()
    df_global['DeathsAccum_Cantabria'] = df_global['Deaths_Cantabria'].cumsum()
    
    # Cumulative sum Castilla y Leon
    df_global['CasesAccum_Castilla_y_Leon'] = df_global['Cases_Castilla_y_Leon'].cumsum()
    df_global['DeathsAccum_Castilla_y_Leon'] = df_global['Deaths_Castilla_y_Leon'].cumsum()
    
    # Cumulative sum Castilla La Mancha
    df_global['CasesAccum_Castilla_La_Mancha'] = df_global['Cases_Castilla_La_Mancha'].cumsum()
    df_global['DeathsAccum_Castilla_La_Mancha'] = df_global['Deaths_Castilla_La_Mancha'].cumsum()
    
    # Cumulative sum Catalunya
    df_global['CasesAccum_Catalunya'] = df_global['Cases_Catalunya'].cumsum()
    df_global['DeathsAccum_Catalunya'] = df_global['Deaths_Catalunya'].cumsum()
    
    # Cumulative sum Ceuta
    df_global['CasesAccum_Ceuta'] = df_global['Cases_Ceuta'].cumsum()
    df_global['DeathsAccum_Ceuta'] = df_global['Deaths_Ceuta'].cumsum()
    
    # Cumulative sum Comunidad Valenciana
    df_global['CasesAccum_Comunidad_Valenciana'] = df_global['Cases_Comunidad_Valenciana'].cumsum()
    df_global['DeathsAccum_Comunidad_Valenciana'] = df_global['Deaths_Comunidad_Valenciana'].cumsum()
    
    # Cumulative sum Extremadura
    df_global['CasesAccum_Extremadura'] = df_global['Cases_Extremadura'].cumsum()
    df_global['DeathsAccum_Extremadura'] = df_global['Deaths_Extremadura'].cumsum()
    
    # Cumulative sum Galicia
    df_global['CasesAccum_Galicia'] = df_global['Cases_Galicia'].cumsum()
    df_global['DeathsAccum_Galicia'] = df_global['Deaths_Galicia'].cumsum()
    
    # Cumulative sum Islas Baleares
    df_global['CasesAccum_Islas_Baleares'] = df_global['Cases_Islas_Baleares'].cumsum()
    df_global['DeathsAccum_Islas_Baleares'] = df_global['Deaths_Islas_Baleares'].cumsum()
    
    # Cumulative sum La Rioja
    df_global['CasesAccum_La_Rioja'] = df_global['Cases_La_Rioja'].cumsum()
    df_global['DeathsAccum_La_Rioja'] = df_global['Deaths_La_Rioja'].cumsum()
    
    # Cumulative sum Madrid
    df_global['CasesAccum_Madrid'] = df_global['Cases_Madrid'].cumsum()
    df_global['DeathsAccum_Madrid'] = df_global['Deaths_Madrid'].cumsum()
    
    # Cumulative sum Melilla
    df_global['CasesAccum_Melilla'] = df_global['Cases_Melilla'].cumsum()
    df_global['DeathsAccum_Melilla'] = df_global['Deaths_Melilla'].cumsum()
    
    # Cumulative sum Murcia
    df_global['CasesAccum_Murcia'] = df_global['Cases_Murcia'].cumsum()
    df_global['DeathsAccum_Murcia'] = df_global['Deaths_Murcia'].cumsum()
    
    # Cumulative sum Navarra
    df_global['CasesAccum_Navarra'] = df_global['Cases_Navarra'].cumsum()
    df_global['DeathsAccum_Navarra'] = df_global['Deaths_Navarra'].cumsum()
    
    # Cumulative sum Pais Vasco
    df_global['CasesAccum_Pais_Vasco'] = df_global['Cases_Pais_Vasco'].cumsum()
    df_global['DeathsAccum_Pais_Vasco'] = df_global['Deaths_Pais_Vasco'].cumsum()

    # Variation rates Andalucia
    df_global['Cases_VariationRate_Andalucia'] = df_global['Cases_Andalucia'].pct_change() * 100
    df_global['Deaths_VariationRate_Andalucia'] = df_global['Deaths_Andalucia'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Andalucia'] = df_global['CasesAccum_Andalucia'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Andalucia'] = df_global['DeathsAccum_Andalucia'].pct_change() * 100

    # Variation rates Aragon
    df_global['Cases_VariationRate_Aragon'] = df_global['Cases_Aragon'].pct_change() * 100
    df_global['Deaths_VariationRate_Aragon'] = df_global['Deaths_Aragon'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Aragon'] = df_global['CasesAccum_Aragon'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Aragon'] = df_global['DeathsAccum_Aragon'].pct_change() * 100

    # Variation rates Asturias
    df_global['Cases_VariationRate_Asturias'] = df_global['Cases_Asturias'].pct_change() * 100
    df_global['Deaths_VariationRate_Asturias'] = df_global['Deaths_Asturias'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Asturias'] = df_global['CasesAccum_Asturias'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Asturias'] = df_global['DeathsAccum_Asturias'].pct_change() * 100

    # Variation rates Canarias
    df_global['Cases_VariationRate_Canarias'] = df_global['Cases_Canarias'].pct_change() * 100
    df_global['Deaths_VariationRate_Canarias'] = df_global['Deaths_Canarias'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Canarias'] = df_global['CasesAccum_Canarias'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Canarias'] = df_global['DeathsAccum_Canarias'].pct_change() * 100

    # Variation rates Cantabria
    df_global['Cases_VariationRate_Cantabria'] = df_global['Cases_Cantabria'].pct_change() * 100
    df_global['Deaths_VariationRate_Cantabria'] = df_global['Deaths_Cantabria'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Cantabria'] = df_global['CasesAccum_Cantabria'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Cantabria'] = df_global['DeathsAccum_Cantabria'].pct_change() * 100

    # Variation rates Castilla y Leon
    df_global['Cases_VariationRate_Castilla_y_Leon'] = df_global['Cases_Castilla_y_Leon'].pct_change() * 100
    df_global['Deaths_VariationRate_Castilla_y_Leon'] = df_global['Deaths_Castilla_y_Leon'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Castilla_y_Leon'] = df_global['CasesAccum_Castilla_y_Leon'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Castilla_y_Leon'] = df_global['DeathsAccum_Castilla_y_Leon'].pct_change() * 100

    # Variation rates Castilla La Mancha
    df_global['Cases_VariationRate_Castilla_La_Mancha'] = df_global['Cases_Castilla_La_Mancha'].pct_change() * 100
    df_global['Deaths_VariationRate_Castilla_La_Mancha'] = df_global['Deaths_Castilla_La_Mancha'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Castilla_La_Mancha'] = df_global['CasesAccum_Castilla_La_Mancha'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Castilla_La_Mancha'] = df_global['DeathsAccum_Castilla_La_Mancha'].pct_change() * 100

    # Variation rates Catalunya
    df_global['Cases_VariationRate_Catalunya'] = df_global['Cases_Catalunya'].pct_change() * 100
    df_global['Deaths_VariationRate_Catalunya'] = df_global['Deaths_Catalunya'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Catalunya'] = df_global['CasesAccum_Catalunya'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Catalunya'] = df_global['DeathsAccum_Catalunya'].pct_change() * 100

    # Variation rates Ceuta
    df_global['Cases_VariationRate_Ceuta'] = df_global['Cases_Ceuta'].pct_change() * 100
    df_global['Deaths_VariationRate_Ceuta'] = df_global['Deaths_Ceuta'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Ceuta'] = df_global['CasesAccum_Ceuta'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Ceuta'] = df_global['DeathsAccum_Ceuta'].pct_change() * 100

    # Variation rates Comunidad Valenciana
    df_global['Cases_VariationRate_Comunidad_Valenciana'] = df_global['Cases_Comunidad_Valenciana'].pct_change() * 100
    df_global['Deaths_VariationRate_Comunidad_Valenciana'] = df_global['Deaths_Comunidad_Valenciana'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Comunidad_Valenciana'] = df_global['CasesAccum_Comunidad_Valenciana'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Comunidad_Valenciana'] = df_global['DeathsAccum_Comunidad_Valenciana'].pct_change() * 100

    # Variation rates Extremadura
    df_global['Cases_VariationRate_Extremadura'] = df_global['Cases_Extremadura'].pct_change() * 100
    df_global['Deaths_VariationRate_Extremadura'] = df_global['Deaths_Extremadura'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Extremadura'] = df_global['CasesAccum_Extremadura'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Extremadura'] = df_global['DeathsAccum_Extremadura'].pct_change() * 100

    # Variation rates Galicia
    df_global['Cases_VariationRate_Galicia'] = df_global['Cases_Galicia'].pct_change() * 100
    df_global['Deaths_VariationRate_Galicia'] = df_global['Deaths_Galicia'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Galicia'] = df_global['CasesAccum_Galicia'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Galicia'] = df_global['DeathsAccum_Galicia'].pct_change() * 100

    # Variation rates Islas Baleares
    df_global['Cases_VariationRate_Islas_Baleares'] = df_global['Cases_Islas_Baleares'].pct_change() * 100
    df_global['Deaths_VariationRate_Islas_Baleares'] = df_global['Deaths_Islas_Baleares'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Islas_Baleares'] = df_global['CasesAccum_Islas_Baleares'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Islas_Baleares'] = df_global['DeathsAccum_Islas_Baleares'].pct_change() * 100

    # Variation rates La Rioja
    df_global['Cases_VariationRate_La_Rioja'] = df_global['Cases_La_Rioja'].pct_change() * 100
    df_global['Deaths_VariationRate_La_Rioja'] = df_global['Deaths_La_Rioja'].pct_change() * 100
    df_global['CasesAccum_VariationRate_La_Rioja'] = df_global['CasesAccum_La_Rioja'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_La_Rioja'] = df_global['DeathsAccum_La_Rioja'].pct_change() * 100

    # Variation rates Madrid
    df_global['Cases_VariationRate_Madrid'] = df_global['Cases_Madrid'].pct_change() * 100
    df_global['Deaths_VariationRate_Madrid'] = df_global['Deaths_Madrid'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Madrid'] = df_global['CasesAccum_Madrid'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Madrid'] = df_global['DeathsAccum_Madrid'].pct_change() * 100

    # Variation rates Melilla
    df_global['Cases_VariationRate_Melilla'] = df_global['Cases_Melilla'].pct_change() * 100
    df_global['Deaths_VariationRate_Melilla'] = df_global['Deaths_Melilla'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Melilla'] = df_global['CasesAccum_Melilla'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Melilla'] = df_global['DeathsAccum_Melilla'].pct_change() * 100

    # Variation rates Murcia
    df_global['Cases_VariationRate_Murcia'] = df_global['Cases_Murcia'].pct_change() * 100
    df_global['Deaths_VariationRate_Murcia'] = df_global['Deaths_Murcia'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Murcia'] = df_global['CasesAccum_Murcia'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Murcia'] = df_global['DeathsAccum_Murcia'].pct_change() * 100

    # Variation rates Navarra
    df_global['Cases_VariationRate_Navarra'] = df_global['Cases_Navarra'].pct_change() * 100
    df_global['Deaths_VariationRate_Navarra'] = df_global['Deaths_Navarra'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Navarra'] = df_global['CasesAccum_Navarra'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Navarra'] = df_global['DeathsAccum_Navarra'].pct_change() * 100

    # Variation rates Pais Vasco
    df_global['Cases_VariationRate_Pais_Vasco'] = df_global['Cases_Pais_Vasco'].pct_change() * 100
    df_global['Deaths_VariationRate_Pais_Vasco'] = df_global['Deaths_Pais_Vasco'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Pais_Vasco'] = df_global['CasesAccum_Pais_Vasco'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Pais_Vasco'] = df_global['DeathsAccum_Pais_Vasco'].pct_change() * 100


    # Cumulative sum Spain
    df_global['CasesAccum_Spain'] = df_global['Cases_Spain'].cumsum()

    # Variation rates Spain
    df_global['Cases_VariationRate_Spain'] = df_global['Deaths_Spain'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Spain'] = df_global['CasesAccum_Spain'].pct_change() * 100
    df_global['Deaths_VariationRate_Spain'] = df_global['Deaths_Spain'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Spain'] = df_global['DeathsAccum_Spain'].pct_change() * 100
    df_global['Recovered_VariationRate_Spain'] = df_global['Recovered_Spain'].pct_change() * 100
    df_global['RecoveredAccum_VariationRate_Spain'] = df_global['RecoveredAccum_Spain'].pct_change() * 100

    # mask = (df_global['Day'] > first_day_to_plot)
    # df_global = df_global.loc[mask]
    df_global.head()
    return df_global

@st.cache
def createDataframeFromJson(raw_data):
    dict_months = {'Enero':1, 'Febrero':2, 'Marzo':3, 'Abril':4, 'Mayo':5, 'Junio':6, 'Julio':7, 'Agosto':8, 'Septiembre':9, 'Octubre':10, 'Noviembre':11, 'Diciembre':12}
    number_days_monitored = len(raw_data['Respuesta'][0]['Metricas'][0]['Datos'])
    list_cases_dates = []
    for day in range(number_days_monitored):
        date = raw_data['Respuesta'][0]['Metricas'][0]['Datos'][day]['Parametro']
        cases = raw_data['Respuesta'][0]['Metricas'][0]['Datos'][day]['Valor']
        list_cases_dates.append([date, cases])     
    df0 = pd.DataFrame(list_cases_dates, columns = ['Date' , 'Cases'])
    df0[['Day', 'Month']] = df0['Date'].str.extract(r'([\d]+) \((.*?)\)')
    df0.replace({'Month': dict_months}, inplace= True)
    df0['Period'] = '2020' + '/' + df0['Month'].astype(str) + '/' + df0['Day'].astype(str)
    df0['Period'] = df0['Period'].apply(lambda x: datetime.strptime(x, '%Y/%m/%d'))
    df0.drop(['Date', 'Day', 'Month'], axis=1, inplace = True)
    df0.sort_values(by=['Period'], inplace = True)
    df0['Day'] = range(number_days_monitored)
    return df0

@st.cache
def fromAccumToSingleValues(x):
    y = np.zeros(len(x))
    for i in np.arange(len(x)-1,0,-1):
        y[i] = x[i] - x[i-1]
    return y

def createOverviewPlot(df_global, yCases, yDeaths, yRecovered, title, yScale):
    if yRecovered != 'null':
        chart_data = pd.DataFrame({
            'Cases': df_global[yCases],
            'Death': df_global[yDeaths],
            'Recovered': df_global[yRecovered]
        })
    else:
        chart_data = pd.DataFrame({
            'Cases': df_global[yCases],
            'Death': df_global[yDeaths]
        })
    chart_data = chart_data.set_index(df_global['Period'])
    st.write("### " + title, chart_data.sort_index())
    chart = st.line_chart(chart_data.iloc[:1])
    for i in range(2,df_global['Day'].count()):
        chart.add_rows(chart_data.iloc[:i])
        time.sleep(0.05)
    chart.add_rows(chart_data.tail(1))
        

    # Dictionaries and constants
    day_init_quarantine = 44
    day14_init_quarantine = 59
    day14_strict_quarantine = 73
    first_day_to_plot = 33
    last_day_to_plot = 75

    if yScale == 'log':
        plt.figure(figsize=(20,10))
        plt.plot(df_global['Day'], df_global[yCases], color = 'r', marker='o', linestyle='solid', linewidth=2, markersize=5, label='Cases')
        plt.plot(df_global['Day'], df_global[yDeaths], color = 'k', marker='o', linestyle='solid', linewidth=2, markersize=5, label='Deaths')
        if yRecovered != 'null':
            plt.plot(df_global['Day'], df_global[yRecovered], color = 'g', marker='o', linestyle='solid', linewidth=2, markersize=5, label='Recovered')
        plt.title(title + ' (log scale)', fontsize = 20)
        plt.xlabel('Day', fontsize=15)
        plt.yscale(yScale)
        plt.axvline(day_init_quarantine, 0, 1, color = 'g', alpha = .5, linewidth=2, linestyle = 'dashed',label = 'Day 0 "soft" quarantine')
        plt.axvline(day14_init_quarantine, 0, 1, color = 'r', alpha = .5, linewidth=2, linestyle = 'dashed',label = 'Day 0 "strict" quarantine')
        plt.axvspan(day_init_quarantine, day14_init_quarantine, facecolor='g', alpha=0.15)
        plt.axvspan(day14_init_quarantine, day14_strict_quarantine, facecolor='r', alpha=0.15)
        plt.xlim(first_day_to_plot,last_day_to_plot)
        plt.legend(fontsize=12)
        st.pyplot()

def createSinglePlot(df_global, xData, yData, labelData, title, yLabel, yScale):
    # Dictionaries and constants
    day_init_quarantine = 44
    day14_init_quarantine = 59
    day14_strict_quarantine = 73
    first_day_to_plot = 33
    last_day_to_plot = 75

    datas = pd.DataFrame({
        yData: df_global[yData]
    })
    datas = datas.set_index(df_global['Period'])
    st.write("### " + title, datas.sort_index())

    lastRows = datas.iloc[:1]
    chart = st.line_chart(lastRows)
    for i in range(2,df_global['Day'].count()):
        lastRows = datas.iloc[:i]
        chart.add_rows(lastRows)
        time.sleep(0.05)
    chart.add_rows(datas[yData].tail(1))

    if yScale == 'log':
        title = title + ' (log scale)'

    if yScale == 'log' or yLabel == 'Variation rate (%)':
        plt.figure(figsize=(20,10))
        plt.plot(df_global[xData], df_global[yData], color = 'navy', marker='o', linestyle='dashed',
        linewidth=2, markersize=12, label=labelData)
        plt.axvline(day_init_quarantine, 0, 1, color = 'g', alpha = .5, label = 'Day 0 "soft" quarantine')
        plt.axvline(day14_init_quarantine, 0, 1, color = 'r', alpha = .5, label = 'Day 0 "strict" quarantine')
        plt.axvspan(day_init_quarantine, day14_init_quarantine, facecolor='g', alpha=0.15)
        plt.axvspan(day14_init_quarantine, day14_strict_quarantine, facecolor='r', alpha=0.15)
        plt.xlim(first_day_to_plot,last_day_to_plot)
        plt.title(title, fontsize = 24)
        plt.xlabel('Day', fontsize=20)
        plt.ylabel(yLabel, fontsize=20)
        plt.legend(fontsize=15)
        plt.yscale(yScale)
        st.pyplot()

def main():
    TodaysDate = time.strftime("%d-%m-%Y")

    st.title('COVID-19 in Spain and CCAA on ' + TodaysDate)

    df_global = getData()

    st.line_chart(df_global)

    page = st.sidebar.selectbox("Choose a page", [
        'Table with the results obtained',
        'Spain',
        'Andalucia',
        'Aragon',
        'Asturias',
        'Canarias',
        'Cantabria',
        'Castilla y Leon',
        'Castilla La Mancha',
        'Catalunya',
        'Ceuta',
        'Comunidad Valenciana',
        'Extremadura',
        'Galicia',
        'Islas Baleares',
        'La Rioja',
        'Madrid',
        'Melilla',
        'Murcia',
        'Navarra',
        'Pais Vasco',
        'Daily cases - Spain',
        'Accumulated daily cases - Spain',
        'Variation rate (daily cases) - Spain',
        'Variation rate (accumulated daily cases) - Spain',
        'Daily deaths - Spain',
        'Accumulated daily deaths - Spain',
        'Variation rate (daily deaths) - Spain',
        'Variation rate (accumulated daily deaths) - Spain',
        'Daily recovered - Spain',
        'Accumulated daily recovered - Spain',
        'Variation rate (daily recovered) - Spain',
        'Variation rate (accumulated daily recovered) - Spain',
        'Daily cases - Andalucia',
        'Accumulated daily cases - Andalucia',
        'Variation rate (daily cases) - Andalucia',
        'Variation rate (accumulated daily cases) - Andalucia',
        'Daily deaths - Andalucia',
        'Accumulated daily deaths - Andalucia',
        'Variation rate (daily deaths) - Andalucia',
        'Variation rate (accumulated daily deaths) - Andalucia'    
        'Daily cases - Aragon',
        'Accumulated daily cases - Aragon',
        'Variation rate (daily cases) - Aragon',
        'Variation rate (accumulated daily cases) - Aragon',
        'Daily deaths - Aragon',
        'Accumulated daily deaths - Aragon',
        'Variation rate (daily deaths) - Aragon',
        'Variation rate (accumulated daily deaths) - Aragon'    
        'Daily cases - Asturias',
        'Accumulated daily cases - Asturias',
        'Variation rate (daily cases) - Asturias',
        'Variation rate (accumulated daily cases) - Asturias',
        'Daily deaths - Asturias',
        'Accumulated daily deaths - Asturias',
        'Variation rate (daily deaths) - Asturias',
        'Variation rate (accumulated daily deaths) - Asturias'    
        'Daily cases - Canarias',
        'Accumulated daily cases - Canarias',
        'Variation rate (daily cases) - Canarias',
        'Variation rate (accumulated daily cases) - Canarias',
        'Daily deaths - Canarias',
        'Accumulated daily deaths - Canarias',
        'Variation rate (daily deaths) - Canarias',
        'Variation rate (accumulated daily deaths) - Canarias'    
        'Daily cases - Cantabria',
        'Accumulated daily cases - Cantabria',
        'Variation rate (daily cases) - Cantabria',
        'Variation rate (accumulated daily cases) - Cantabria',
        'Daily deaths - Cantabria',
        'Accumulated daily deaths - Cantabria',
        'Variation rate (daily deaths) - Cantabria',
        'Variation rate (accumulated daily deaths) - Cantabria'    
        'Daily cases - Castilla y Leon',
        'Accumulated daily cases - Castilla y Leon',
        'Variation rate (daily cases) - Castilla y Leon',
        'Variation rate (accumulated daily cases) - Castilla y Leon',
        'Daily deaths - Castilla y Leon',
        'Accumulated daily deaths - Castilla y Leon',
        'Variation rate (daily deaths) - Castilla y Leon',
        'Variation rate (accumulated daily deaths) - Castilla y Leon'    
        'Daily cases - Castilla La Mancha',
        'Accumulated daily cases - Castilla La Mancha',
        'Variation rate (daily cases) - Castilla La Mancha',
        'Variation rate (accumulated daily cases) - Castilla La Mancha',
        'Daily deaths - Castilla La Mancha',
        'Accumulated daily deaths - Castilla La Mancha',
        'Variation rate (daily deaths) - Castilla La Mancha',
        'Variation rate (accumulated daily deaths) - Castilla La Mancha'    
        'Daily cases - Catalunya',
        'Accumulated daily cases - Catalunya',
        'Variation rate (daily cases) - Catalunya',
        'Variation rate (accumulated daily cases) - Catalunya',
        'Daily deaths - Catalunya',
        'Accumulated daily deaths - Catalunya',
        'Variation rate (daily deaths) - Catalunya',
        'Variation rate (accumulated daily deaths) - Catalunya'    
        'Daily cases - Ceuta',
        'Accumulated daily cases - Ceuta',
        'Variation rate (daily cases) - Ceuta',
        'Variation rate (accumulated daily cases) - Ceuta',
        'Daily deaths - Ceuta',
        'Accumulated daily deaths - Ceuta',
        'Variation rate (daily deaths) - Ceuta',
        'Variation rate (accumulated daily deaths) - Ceuta'    
        'Daily cases - Comunidad Valenciana',
        'Accumulated daily cases - Comunidad Valenciana',
        'Variation rate (daily cases) - Comunidad Valenciana',
        'Variation rate (accumulated daily cases) - Comunidad Valenciana',
        'Daily deaths - Comunidad Valenciana',
        'Accumulated daily deaths - Comunidad Valenciana',
        'Variation rate (daily deaths) - Comunidad Valenciana',
        'Variation rate (accumulated daily deaths) - Comunidad Valenciana'    
        'Daily cases - Extremadura',
        'Accumulated daily cases - Extremadura',
        'Variation rate (daily cases) - Extremadura',
        'Variation rate (accumulated daily cases) - Extremadura',
        'Daily deaths - Extremadura',
        'Accumulated daily deaths - Extremadura',
        'Variation rate (daily deaths) - Extremadura',
        'Variation rate (accumulated daily deaths) - Extremadura'    
        'Daily cases - Galicia',
        'Accumulated daily cases - Galicia',
        'Variation rate (daily cases) - Galicia',
        'Variation rate (accumulated daily cases) - Galicia',
        'Daily deaths - Galicia',
        'Accumulated daily deaths - Galicia',
        'Variation rate (daily deaths) - Galicia',
        'Variation rate (accumulated daily deaths) - Galicia'    
        'Daily cases - Islas Baleares',
        'Accumulated daily cases - Islas Baleares',
        'Variation rate (daily cases) - Islas Baleares',
        'Variation rate (accumulated daily cases) - Islas Baleares',
        'Daily deaths - Islas Baleares',
        'Accumulated daily deaths - Islas Baleares',
        'Variation rate (daily deaths) - Islas Baleares',
        'Variation rate (accumulated daily deaths) - Islas Baleares'    
        'Daily cases - La Rioja',
        'Accumulated daily cases - La Rioja',
        'Variation rate (daily cases) - La Rioja',
        'Variation rate (accumulated daily cases) - La Rioja',
        'Daily deaths - La Rioja',
        'Accumulated daily deaths - La Rioja',
        'Variation rate (daily deaths) - La Rioja',
        'Variation rate (accumulated daily deaths) - La Rioja'    
        'Daily cases - Madrid',
        'Accumulated daily cases - Madrid',
        'Variation rate (daily cases) - Madrid',
        'Variation rate (accumulated daily cases) - Madrid',
        'Daily deaths - Madrid',
        'Accumulated daily deaths - Madrid',
        'Variation rate (daily deaths) - Madrid',
        'Variation rate (accumulated daily deaths) - Madrid'    
        'Daily cases - Melilla',
        'Accumulated daily cases - Melilla',
        'Variation rate (daily cases) - Melilla',
        'Variation rate (accumulated daily cases) - Melilla',
        'Daily deaths - Melilla',
        'Accumulated daily deaths - Melilla',
        'Variation rate (daily deaths) - Melilla',
        'Variation rate (accumulated daily deaths) - Melilla'    
        'Daily cases - Murcia',
        'Accumulated daily cases - Murcia',
        'Variation rate (daily cases) - Murcia',
        'Variation rate (accumulated daily cases) - Murcia',
        'Daily deaths - Murcia',
        'Accumulated daily deaths - Murcia',
        'Variation rate (daily deaths) - Murcia',
        'Variation rate (accumulated daily deaths) - Murcia'    
        'Daily cases - Navarra',
        'Accumulated daily cases - Navarra',
        'Variation rate (daily cases) - Navarra',
        'Variation rate (accumulated daily cases) - Navarra',
        'Daily deaths - Navarra',
        'Accumulated daily deaths - Navarra',
        'Variation rate (daily deaths) - Navarra',
        'Variation rate (accumulated daily deaths) - Navarra'    
        'Daily cases - Pais Vasco',
        'Accumulated daily cases - Pais Vasco',
        'Variation rate (daily cases) - Pais Vasco',
        'Variation rate (accumulated daily cases) - Pais Vasco',
        'Daily deaths - Pais Vasco',
        'Accumulated daily deaths - Pais Vasco',
        'Variation rate (daily deaths) - Pais Vasco',
        'Variation rate (accumulated daily deaths) - Pais Vasco'
    ])

    if page == 'Table with the results obtained':
        df_table = df_global
        df_table = df_table.set_index("Period")
        data_table = df_table.loc[df_table.index]
        st.write("### Table with the results obtained to date " + TodaysDate, data_table.sort_index())
        # Select only the days after the first 50 deaths in Spain

    elif page == 'Spain':
        st.write("### Cases, deaths and recoveries accumulated in Spain")
        createOverviewPlot(df_global, 'CasesAccum_Spain','DeathsAccum_Spain','RecoveredAccum_Spain','Spain','log')

    elif page == 'Andalucia':
        st.write("### Cases, deaths and recoveries accumulated in Andalucia")
        createOverviewPlot(df_global, 'CasesAccum_Andalucia','DeathsAccum_Andalucia','null','Andalucia','log')
    
    elif page == 'Aragon':
        st.write("### Cases, deaths and recoveries accumulated in Aragon")
        createOverviewPlot(df_global, 'CasesAccum_Aragon','DeathsAccum_Aragon','null','Aragon','log')
    
    elif page == 'Asturias':
        st.write("### Cases, deaths and recoveries accumulated in Asturias")
        createOverviewPlot(df_global, 'CasesAccum_Asturias','DeathsAccum_Asturias','null','Asturias','log')
    
    elif page == 'Canarias':
        st.write("### Cases, deaths and recoveries accumulated in Canarias")
        createOverviewPlot(df_global, 'CasesAccum_Canarias','DeathsAccum_Canarias','null','Canarias','log')
    
    elif page == 'Cantabria':
        st.write("### Cases, deaths and recoveries accumulated in Cantabria")
        createOverviewPlot(df_global, 'CasesAccum_Cantabria','DeathsAccum_Cantabria','null','Cantabria','log')
    
    elif page == 'Castilla y Leon':
        st.write("### Cases, deaths and recoveries accumulated in Castilla y Leon")
        createOverviewPlot(df_global, 'CasesAccum_Castilla_y_Leon','DeathsAccum_Castilla_y_Leon','null','Castilla y Leon','log')
    
    elif page == 'Castilla La Mancha':
        st.write("### Cases, deaths and recoveries accumulated in Castilla La Mancha")
        createOverviewPlot(df_global, 'CasesAccum_Castilla_La_Mancha','DeathsAccum_Castilla_La_Mancha','null','Castilla La Mancha','log')
    
    elif page == 'Catalunya':
        st.write("### Cases, deaths and recoveries accumulated in Catalunya")
        createOverviewPlot(df_global, 'CasesAccum_Catalunya','DeathsAccum_Catalunya','null','Catalunya','log')
    
    elif page == 'Ceuta':
        st.write("### Cases, deaths and recoveries accumulated in Ceuta")
        createOverviewPlot(df_global, 'CasesAccum_Ceuta','DeathsAccum_Ceuta','null','Ceuta','log')
    
    elif page == 'Comunidad Valenciana':
        st.write("### Cases, deaths and recoveries accumulated in Comunidad Valenciana")
        createOverviewPlot(df_global, 'CasesAccum_Comunidad_Valenciana','DeathsAccum_Comunidad_Valenciana','null','Comunidad Valenciana','log')
    
    elif page == 'Extremadura':
        st.write("### Cases, deaths and recoveries accumulated in Extremadura")
        createOverviewPlot(df_global, 'CasesAccum_Extremadura','DeathsAccum_Extremadura','null','Extremadura','log')
    
    elif page == 'Galicia':
        st.write("### Cases, deaths and recoveries accumulated in Galicia")
        createOverviewPlot(df_global, 'CasesAccum_Galicia','DeathsAccum_Galicia','null','Galicia','log')
    
    elif page == 'Islas Baleares':
        st.write("### Cases, deaths and recoveries accumulated in Islas Baleares")
        createOverviewPlot(df_global, 'CasesAccum_Islas_Baleares','DeathsAccum_Islas_Baleares','null','Islas Baleares','log')
    
    elif page == 'La Rioja':
        st.write("### Cases, deaths and recoveries accumulated in La Rioja")
        createOverviewPlot(df_global, 'CasesAccum_La_Rioja','DeathsAccum_La_Rioja','null','La Rioja','log')
    
    elif page == 'Madrid':
        st.write("### Cases, deaths and recoveries accumulated in Madrid")
        createOverviewPlot(df_global, 'CasesAccum_Madrid','DeathsAccum_Madrid','null','Madrid','log')
    
    elif page == 'Melilla':
        st.write("### Cases, deaths and recoveries accumulated in Melilla")
        createOverviewPlot(df_global, 'CasesAccum_Melilla','DeathsAccum_Melilla','null','Melilla','log')
    
    elif page == 'Murcia':
        st.write("### Cases, deaths and recoveries accumulated in Murcia")
        createOverviewPlot(df_global, 'CasesAccum_Murcia','DeathsAccum_Murcia','null','Murcia','log')
    
    elif page == 'Navarra':
        st.write("### Cases, deaths and recoveries accumulated in Navarra")
        createOverviewPlot(df_global, 'CasesAccum_Navarra','DeathsAccum_Navarra','null','Navarra','log')
    
    elif page == 'Pais Vasco':
        st.write("### Cases, deaths and recoveries accumulated in Pais Vasco")
        createOverviewPlot(df_global, 'CasesAccum_Pais_Vasco','DeathsAccum_Pais_Vasco','null','Pais Vasco','log')

    elif page == 'Daily cases - Spain':
        st.write("### Daily cases - Spain")
        createSinglePlot(df_global, 'Day', 'Cases_Spain','Cases','Daily cases - Spain', 'Cases','log')

    elif page == 'Accumulated daily cases - Spain':
        st.write("### Accumulated daily cases - Spain")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Spain','Cases','Accumulated daily cases - Spain', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Spain':
        st.write("### Variation rate (daily cases) - Spain")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Spain','Variation rate','Variation rate (daily cases) - Spain', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Spain':
        st.write("### Variation rate (accumulated daily cases) - Spain")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Spain','Variation rate','Variation rate (accumulated daily cases) - Spain', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Spain':
        st.write("### Daily deaths - Spain")
        createSinglePlot(df_global, 'Day', 'Deaths_Spain','Deaths','Daily deaths - Spain', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Spain':
        st.write("### Accumulated daily deaths - Spain")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Spain','Deaths','Accumulated daily deaths - Spain', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Spain':
        st.write("### Variation rate (daily deaths) - Spain")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Spain','Variation rate','Variation rate (daily deaths) - Spain', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Spain':
        st.write("### Variation rate (accumulated daily deaths) - Spain")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Spain','Variation rate','Variation rate (accumulated daily deaths) - Spain', 'Variation rate (%)','linear')

    elif page == 'Daily recovered - Spain':
        st.write("### Daily recovered - Spain")
        createSinglePlot(df_global, 'Day', 'Recovered_Spain','Recovered','Daily recovered - Spain', 'Recovered','log')

    elif page == 'Accumulated daily recovered - Spain':
        st.write("### Accumulated daily recovered - Spain")
        createSinglePlot(df_global, 'Day', 'RecoveredAccum_Spain','Recovered','Accumulated daily recovered - Spain', 'Recovered','log')

    elif page == 'Variation rate (daily recovered) - Spain':
        st.write("### Variation rate (daily recovered) - Spain")
        createSinglePlot(df_global, 'Day', 'Recovered_VariationRate_Spain','Variation rate','Variation rate (daily recovered) - Spain', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily recovered) - Spain':
        st.write("### Variation rate (accumulated daily recovered) - Spain")
        createSinglePlot(df_global, 'Day', 'RecoveredAccum_VariationRate_Spain','Variation rate','Variation rate (accumulated daily recovered) - Spain', 'Variation rate (%)','linear')

    elif page == 'Daily cases - Andalucia':
        st.write("### Daily cases - Andalucia")
        createSinglePlot(df_global, 'Day', 'Cases_Andalucia','Cases','Daily cases - Andalucia', 'Cases','log')

    elif page == 'Accumulated daily cases - Andalucia':
        st.write("### Accumulated daily cases - Andalucia")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Andalucia','Cases','Accumulated daily cases - Andalucia', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Andalucia':
        st.write("### Variation rate (daily cases) - Andalucia")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Andalucia','Variation rate','Variation rate (daily cases) - Andalucia', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Andalucia':
        st.write("### Variation rate (accumulated daily cases) - Andalucia")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Andalucia','Variation rate','Variation rate (accumulated daily cases) - Andalucia', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Andalucia':
        st.write("### Daily deaths - Andalucia")
        createSinglePlot(df_global, 'Day', 'Deaths_Andalucia','Deaths','Daily deaths - Andalucia', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Andalucia':
        st.write("### Accumulated daily deaths - Andalucia")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Andalucia','Deaths','Accumulated daily deaths - Andalucia', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Andalucia':
        st.write("### Variation rate (daily deaths) - Andalucia")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Andalucia','Variation rate','Variation rate (daily deaths) - Andalucia', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Andalucia':
        st.write("### Variation rate (accumulated daily deaths) - Andalucia")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Andalucia','Variation rate','Variation rate (accumulated daily deaths) - Andalucia', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Aragon':
        st.write("### Daily cases - Aragon")
        createSinglePlot(df_global, 'Day', 'Cases_Aragon','Cases','Daily cases - Aragon', 'Cases','log')

    elif page == 'Accumulated daily cases - Aragon':
        st.write("### Accumulated daily cases - Aragon")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Aragon','Cases','Accumulated daily cases - Aragon', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Aragon':
        st.write("### Variation rate (daily cases) - Aragon")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Aragon','Variation rate','Variation rate (daily cases) - Aragon', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Aragon':
        st.write("### Variation rate (accumulated daily cases) - Aragon")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Aragon','Variation rate','Variation rate (accumulated daily cases) - Aragon', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Aragon':
        st.write("### Daily deaths - Aragon")
        createSinglePlot(df_global, 'Day', 'Deaths_Aragon','Deaths','Daily deaths - Aragon', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Aragon':
        st.write("### Accumulated daily deaths - Aragon")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Aragon','Deaths','Accumulated daily deaths - Aragon', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Aragon':
        st.write("### Variation rate (daily deaths) - Aragon")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Aragon','Variation rate','Variation rate (daily deaths) - Aragon', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Aragon':
        st.write("### Variation rate (accumulated daily deaths) - Aragon")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Aragon','Variation rate','Variation rate (accumulated daily deaths) - Aragon', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Asturias':
        st.write("### Daily cases - Asturias")
        createSinglePlot(df_global, 'Day', 'Cases_Asturias','Cases','Daily cases - Asturias', 'Cases','log')

    elif page == 'Accumulated daily cases - Asturias':
        st.write("### Accumulated daily cases - Asturias")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Asturias','Cases','Accumulated daily cases - Asturias', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Asturias':
        st.write("### Variation rate (daily cases) - Asturias")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Asturias','Variation rate','Variation rate (daily cases) - Asturias', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Asturias':
        st.write("### Variation rate (accumulated daily cases) - Asturias")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Asturias','Variation rate','Variation rate (accumulated daily cases) - Asturias', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Asturias':
        st.write("### Daily deaths - Asturias")
        createSinglePlot(df_global, 'Day', 'Deaths_Asturias','Deaths','Daily deaths - Asturias', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Asturias':
        st.write("### Accumulated daily deaths - Asturias")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Asturias','Deaths','Accumulated daily deaths - Asturias', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Asturias':
        st.write("### Variation rate (daily deaths) - Asturias")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Asturias','Variation rate','Variation rate (daily deaths) - Asturias', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Asturias':
        st.write("### Variation rate (accumulated daily deaths) - Asturias")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Asturias','Variation rate','Variation rate (accumulated daily deaths) - Asturias', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Canarias':
        st.write("### Daily cases - Canarias")
        createSinglePlot(df_global, 'Day', 'Cases_Canarias','Cases','Daily cases - Canarias', 'Cases','log')

    elif page == 'Accumulated daily cases - Canarias':
        st.write("### Accumulated daily cases - Canarias")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Canarias','Cases','Accumulated daily cases - Canarias', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Canarias':
        st.write("### Variation rate (daily cases) - Canarias")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Canarias','Variation rate','Variation rate (daily cases) - Canarias', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Canarias':
        st.write("### Variation rate (accumulated daily cases) - Canarias")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Canarias','Variation rate','Variation rate (accumulated daily cases) - Canarias', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Canarias':
        st.write("### Daily deaths - Canarias")
        createSinglePlot(df_global, 'Day', 'Deaths_Canarias','Deaths','Daily deaths - Canarias', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Canarias':
        st.write("### Accumulated daily deaths - Canarias")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Canarias','Deaths','Accumulated daily deaths - Canarias', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Canarias':
        st.write("### Variation rate (daily deaths) - Canarias")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Canarias','Variation rate','Variation rate (daily deaths) - Canarias', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Canarias':
        st.write("### Variation rate (accumulated daily deaths) - Canarias")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Canarias','Variation rate','Variation rate (accumulated daily deaths) - Canarias', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Cantabria':
        st.write("### Daily cases - Cantabria")
        createSinglePlot(df_global, 'Day', 'Cases_Cantabria','Cases','Daily cases - Cantabria', 'Cases','log')

    elif page == 'Accumulated daily cases - Cantabria':
        st.write("### Accumulated daily cases - Cantabria")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Cantabria','Cases','Accumulated daily cases - Cantabria', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Cantabria':
        st.write("### Variation rate (daily cases) - Cantabria")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Cantabria','Variation rate','Variation rate (daily cases) - Cantabria', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Cantabria':
        st.write("### Variation rate (accumulated daily cases) - Cantabria")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Cantabria','Variation rate','Variation rate (accumulated daily cases) - Cantabria', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Cantabria':
        st.write("### Daily deaths - Cantabria")
        createSinglePlot(df_global, 'Day', 'Deaths_Cantabria','Deaths','Daily deaths - Cantabria', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Cantabria':
        st.write("### Accumulated daily deaths - Cantabria")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Cantabria','Deaths','Accumulated daily deaths - Cantabria', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Cantabria':
        st.write("### Variation rate (daily deaths) - Cantabria")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Cantabria','Variation rate','Variation rate (daily deaths) - Cantabria', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Cantabria':
        st.write("### Variation rate (accumulated daily deaths) - Cantabria")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Cantabria','Variation rate','Variation rate (accumulated daily deaths) - Cantabria', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Castilla y Leon':
        st.write("### Daily cases - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'Cases_Castilla_y_Leon','Cases','Daily cases - Castilla y Leon', 'Cases','log')

    elif page == 'Accumulated daily cases - Castilla y Leon':
        st.write("### Accumulated daily cases - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Castilla_y_Leon','Cases','Accumulated daily cases - Castilla y Leon', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Castilla y Leon':
        st.write("### Variation rate (daily cases) - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Castilla_y_Leon','Variation rate','Variation rate (daily cases) - Castilla y Leon', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Castilla y Leon':
        st.write("### Variation rate (accumulated daily cases) - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Castilla_y_Leon','Variation rate','Variation rate (accumulated daily cases) - Castilla y Leon', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Castilla y Leon':
        st.write("### Daily deaths - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'Deaths_Castilla_y_Leon','Deaths','Daily deaths - Castilla y Leon', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Castilla y Leon':
        st.write("### Accumulated daily deaths - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Castilla_y_Leon','Deaths','Accumulated daily deaths - Castilla y Leon', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Castilla y Leon':
        st.write("### Variation rate (daily deaths) - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Castilla_y_Leon','Variation rate','Variation rate (daily deaths) - Castilla y Leon', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Castilla y Leon':
        st.write("### Variation rate (accumulated daily deaths) - Castilla y Leon")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Castilla_y_Leon','Variation rate','Variation rate (accumulated daily deaths) - Castilla y Leon', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Castilla La Mancha':
        st.write("### Daily cases - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'Cases_Castilla_La_Mancha','Cases','Daily cases - Castilla La Mancha', 'Cases','log')

    elif page == 'Accumulated daily cases - Castilla La Mancha':
        st.write("### Accumulated daily cases - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Castilla_La_Mancha','Cases','Accumulated daily cases - Castilla La Mancha', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Castilla La Mancha':
        st.write("### Variation rate (daily cases) - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Castilla_La_Mancha','Variation rate','Variation rate (daily cases) - Castilla La Mancha', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Castilla La Mancha':
        st.write("### Variation rate (accumulated daily cases) - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Castilla_La_Mancha','Variation rate','Variation rate (accumulated daily cases) - Castilla La Mancha', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Castilla La Mancha':
        st.write("### Daily deaths - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'Deaths_Castilla La Mancha','Deaths','Daily deaths - Castilla La Mancha', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Castilla La Mancha':
        st.write("### Accumulated daily deaths - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Castilla_La_Mancha','Deaths','Accumulated daily deaths - Castilla La Mancha', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Castilla La Mancha':
        st.write("### Variation rate (daily deaths) - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Castilla_La_Mancha','Variation rate','Variation rate (daily deaths) - Castilla La Mancha', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Castilla La Mancha':
        st.write("### Variation rate (accumulated daily deaths) - Castilla La Mancha")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Castilla_La_Mancha','Variation rate','Variation rate (accumulated daily deaths) - Castilla La Mancha', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Catalunya':
        st.write("### Daily cases - Catalunya")
        createSinglePlot(df_global, 'Day', 'Cases_Catalunya','Cases','Daily cases - Catalunya', 'Cases','log')

    elif page == 'Accumulated daily cases - Catalunya':
        st.write("### Accumulated daily cases - Catalunya")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Catalunya','Cases','Accumulated daily cases - Catalunya', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Catalunya':
        st.write("### Variation rate (daily cases) - Catalunya")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Catalunya','Variation rate','Variation rate (daily cases) - Catalunya', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Catalunya':
        st.write("### Variation rate (accumulated daily cases) - Catalunya")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Catalunya','Variation rate','Variation rate (accumulated daily cases) - Catalunya', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Catalunya':
        st.write("### Daily deaths - Catalunya")
        createSinglePlot(df_global, 'Day', 'Deaths_Catalunya','Deaths','Daily deaths - Catalunya', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Catalunya':
        st.write("### Accumulated daily deaths - Catalunya")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Catalunya','Deaths','Accumulated daily deaths - Catalunya', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Catalunya':
        st.write("### Variation rate (daily deaths) - Catalunya")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Catalunya','Variation rate','Variation rate (daily deaths) - Catalunya', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Catalunya':
        st.write("### Variation rate (accumulated daily deaths) - Catalunya")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Catalunya','Variation rate','Variation rate (accumulated daily deaths) - Catalunya', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Ceuta':
        st.write("### Daily cases - Ceuta")
        createSinglePlot(df_global, 'Day', 'Cases_Ceuta','Cases','Daily cases - Ceuta', 'Cases','log')

    elif page == 'Accumulated daily cases - Ceuta':
        st.write("### Accumulated daily cases - Ceuta")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Ceuta','Cases','Accumulated daily cases - Ceuta', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Ceuta':
        st.write("### Variation rate (daily cases) - Ceuta")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Ceuta','Variation rate','Variation rate (daily cases) - Ceuta', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Ceuta':
        st.write("### Variation rate (accumulated daily cases) - Ceuta")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Ceuta','Variation rate','Variation rate (accumulated daily cases) - Ceuta', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Ceuta':
        st.write("### Daily deaths - Ceuta")
        createSinglePlot(df_global, 'Day', 'Deaths_Ceuta','Deaths','Daily deaths - Ceuta', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Ceuta':
        st.write("### Accumulated daily deaths - Ceuta")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Ceuta','Deaths','Accumulated daily deaths - Ceuta', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Ceuta':
        st.write("### Variation rate (daily deaths) - Ceuta")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Ceuta','Variation rate','Variation rate (daily deaths) - Ceuta', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Ceuta':
        st.write("### Variation rate (accumulated daily deaths) - Ceuta")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Ceuta','Variation rate','Variation rate (accumulated daily deaths) - Ceuta', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Comunidad Valenciana':
        st.write("### Daily cases - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'Cases_Comunidad_Valenciana','Cases','Daily cases - Comunidad Valenciana', 'Cases','log')

    elif page == 'Accumulated daily cases - Comunidad Valenciana':
        st.write("### Accumulated daily cases - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Comunidad_Valenciana','Cases','Accumulated daily cases - Comunidad Valenciana', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Comunidad Valenciana':
        st.write("### Variation rate (daily cases) - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Comunidad_Valenciana','Variation rate','Variation rate (daily cases) - Comunidad Valenciana', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Comunidad Valenciana':
        st.write("### Variation rate (accumulated daily cases) - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Comunidad_Valenciana','Variation rate','Variation rate (accumulated daily cases) - Comunidad Valenciana', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Comunidad Valenciana':
        st.write("### Daily deaths - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'Deaths_Comunidad_Valenciana','Deaths','Daily deaths - Comunidad Valenciana', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Comunidad Valenciana':
        st.write("### Accumulated daily deaths - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Comunidad_Valenciana','Deaths','Accumulated daily deaths - Comunidad Valenciana', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Comunidad Valenciana':
        st.write("### Variation rate (daily deaths) - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Comunidad_Valenciana','Variation rate','Variation rate (daily deaths) - Comunidad Valenciana', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Comunidad Valenciana':
        st.write("### Variation rate (accumulated daily deaths) - Comunidad Valenciana")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Comunidad_Valenciana','Variation rate','Variation rate (accumulated daily deaths) - Comunidad Valenciana', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Extremadura':
        st.write("### Daily cases - Extremadura")
        createSinglePlot(df_global, 'Day', 'Cases_Extremadura','Cases','Daily cases - Extremadura', 'Cases','log')

    elif page == 'Accumulated daily cases - Extremadura':
        st.write("### Accumulated daily cases - Extremadura")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Extremadura','Cases','Accumulated daily cases - Extremadura', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Extremadura':
        st.write("### Variation rate (daily cases) - Extremadura")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Extremadura','Variation rate','Variation rate (daily cases) - Extremadura', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Extremadura':
        st.write("### Variation rate (accumulated daily cases) - Extremadura")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Extremadura','Variation rate','Variation rate (accumulated daily cases) - Extremadura', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Extremadura':
        st.write("### Daily deaths - Extremadura")
        createSinglePlot(df_global, 'Day', 'Deaths_Extremadura','Deaths','Daily deaths - Extremadura', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Extremadura':
        st.write("### Accumulated daily deaths - Extremadura")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Extremadura','Deaths','Accumulated daily deaths - Extremadura', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Extremadura':
        st.write("### Variation rate (daily deaths) - Extremadura")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Extremadura','Variation rate','Variation rate (daily deaths) - Extremadura', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Extremadura':
        st.write("### Variation rate (accumulated daily deaths) - Extremadura")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Extremadura','Variation rate','Variation rate (accumulated daily deaths) - Extremadura', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Galicia':
        st.write("### Daily cases - Galicia")
        createSinglePlot(df_global, 'Day', 'Cases_Galicia','Cases','Daily cases - Galicia', 'Cases','log')

    elif page == 'Accumulated daily cases - Galicia':
        st.write("### Accumulated daily cases - Galicia")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Galicia','Cases','Accumulated daily cases - Galicia', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Galicia':
        st.write("### Variation rate (daily cases) - Galicia")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Galicia','Variation rate','Variation rate (daily cases) - Galicia', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Galicia':
        st.write("### Variation rate (accumulated daily cases) - Galicia")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Galicia','Variation rate','Variation rate (accumulated daily cases) - Galicia', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Galicia':
        st.write("### Daily deaths - Galicia")
        createSinglePlot(df_global, 'Day', 'Deaths_Galicia','Deaths','Daily deaths - Galicia', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Galicia':
        st.write("### Accumulated daily deaths - Galicia")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Galicia','Deaths','Accumulated daily deaths - Galicia', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Galicia':
        st.write("### Variation rate (daily deaths) - Galicia")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Galicia','Variation rate','Variation rate (daily deaths) - Galicia', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Galicia':
        st.write("### Variation rate (accumulated daily deaths) - Galicia")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Galicia','Variation rate','Variation rate (accumulated daily deaths) - Galicia', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Islas Baleares':
        st.write("### Daily cases - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'Cases_Islas_Baleares','Cases','Daily cases - Islas Baleares', 'Cases','log')

    elif page == 'Accumulated daily cases - Islas Baleares':
        st.write("### Accumulated daily cases - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Islas_Baleares','Cases','Accumulated daily cases - Islas Baleares', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Islas Baleares':
        st.write("### Variation rate (daily cases) - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Islas_Baleares','Variation rate','Variation rate (daily cases) - Islas Baleares', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Islas Baleares':
        st.write("### Variation rate (accumulated daily cases) - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Islas_Baleares','Variation rate','Variation rate (accumulated daily cases) - Islas Baleares', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Islas Baleares':
        st.write("### Daily deaths - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'Deaths_Islas_Baleares','Deaths','Daily deaths - Islas Baleares', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Islas Baleares':
        st.write("### Accumulated daily deaths - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Islas_Baleares','Deaths','Accumulated daily deaths - Islas Baleares', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Islas Baleares':
        st.write("### Variation rate (daily deaths) - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Islas_Baleares','Variation rate','Variation rate (daily deaths) - Islas Baleares', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Islas Baleares':
        st.write("### Variation rate (accumulated daily deaths) - Islas Baleares")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Islas_Baleares','Variation rate','Variation rate (accumulated daily deaths) - Islas Baleares', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - La Rioja':
        st.write("### Daily cases - La Rioja")
        createSinglePlot(df_global, 'Day', 'Cases_La_Rioja','Cases','Daily cases - La Rioja', 'Cases','log')

    elif page == 'Accumulated daily cases - La Rioja':
        st.write("### Accumulated daily cases - La Rioja")
        createSinglePlot(df_global, 'Day', 'CasesAccum_La_Rioja','Cases','Accumulated daily cases - La Rioja', 'Cases','log')

    elif page == 'Variation rate (daily cases) - La Rioja':
        st.write("### Variation rate (daily cases) - La Rioja")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_La_Rioja','Variation rate','Variation rate (daily cases) - La Rioja', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - La Rioja':
        st.write("### Variation rate (accumulated daily cases) - La Rioja")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_La_Rioja','Variation rate','Variation rate (accumulated daily cases) - La Rioja', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - La Rioja':
        st.write("### Daily deaths - La Rioja")
        createSinglePlot(df_global, 'Day', 'Deaths_La_Rioja','Deaths','Daily deaths - La Rioja', 'Deaths','log')

    elif page == 'Accumulated daily deaths - La Rioja':
        st.write("### Accumulated daily deaths - La Rioja")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_La_Rioja','Deaths','Accumulated daily deaths - La Rioja', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - La Rioja':
        st.write("### Variation rate (daily deaths) - La Rioja")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_La_Rioja','Variation rate','Variation rate (daily deaths) - La Rioja', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - La Rioja':
        st.write("### Variation rate (accumulated daily deaths) - La Rioja")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_La_Rioja','Variation rate','Variation rate (accumulated daily deaths) - La Rioja', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Madrid':
        st.write("### Daily cases - Madrid")
        createSinglePlot(df_global, 'Day', 'Cases_Madrid','Cases','Daily cases - Madrid', 'Cases','log')

    elif page == 'Accumulated daily cases - Madrid':
        st.write("### Accumulated daily cases - Madrid")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Madrid','Cases','Accumulated daily cases - Madrid', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Madrid':
        st.write("### Variation rate (daily cases) - Madrid")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Madrid','Variation rate','Variation rate (daily cases) - Madrid', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Madrid':
        st.write("### Variation rate (accumulated daily cases) - Madrid")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Madrid','Variation rate','Variation rate (accumulated daily cases) - Madrid', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Madrid':
        st.write("### Daily deaths - Madrid")
        createSinglePlot(df_global, 'Day', 'Deaths_Madrid','Deaths','Daily deaths - Madrid', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Madrid':
        st.write("### Accumulated daily deaths - Madrid")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Madrid','Deaths','Accumulated daily deaths - Madrid', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Madrid':
        st.write("### Variation rate (daily deaths) - Madrid")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Madrid','Variation rate','Variation rate (daily deaths) - Madrid', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Madrid':
        st.write("### Variation rate (accumulated daily deaths) - Madrid")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Madrid','Variation rate','Variation rate (accumulated daily deaths) - Madrid', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Melilla':
        st.write("### Daily cases - Melilla")
        createSinglePlot(df_global, 'Day', 'Cases_Melilla','Cases','Daily cases - Melilla', 'Cases','log')

    elif page == 'Accumulated daily cases - Melilla':
        st.write("### Accumulated daily cases - Melilla")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Melilla','Cases','Accumulated daily cases - Melilla', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Melilla':
        st.write("### Variation rate (daily cases) - Melilla")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Melilla','Variation rate','Variation rate (daily cases) - Melilla', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Melilla':
        st.write("### Variation rate (accumulated daily cases) - Melilla")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Melilla','Variation rate','Variation rate (accumulated daily cases) - Melilla', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Melilla':
        st.write("### Daily deaths - Melilla")
        createSinglePlot(df_global, 'Day', 'Deaths_Melilla','Deaths','Daily deaths - Melilla', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Melilla':
        st.write("### Accumulated daily deaths - Melilla")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Melilla','Deaths','Accumulated daily deaths - Melilla', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Melilla':
        st.write("### Variation rate (daily deaths) - Melilla")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Melilla','Variation rate','Variation rate (daily deaths) - Melilla', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Melilla':
        st.write("### Variation rate (accumulated daily deaths) - Melilla")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Melilla','Variation rate','Variation rate (accumulated daily deaths) - Melilla', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Murcia':
        st.write("### Daily cases - Murcia")
        createSinglePlot(df_global, 'Day', 'Cases_Murcia','Cases','Daily cases - Murcia', 'Cases','log')

    elif page == 'Accumulated daily cases - Murcia':
        st.write("### Accumulated daily cases - Murcia")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Murcia','Cases','Accumulated daily cases - Murcia', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Murcia':
        st.write("### Variation rate (daily cases) - Murcia")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Murcia','Variation rate','Variation rate (daily cases) - Murcia', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Murcia':
        st.write("### Variation rate (accumulated daily cases) - Murcia")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Murcia','Variation rate','Variation rate (accumulated daily cases) - Murcia', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Murcia':
        st.write("### Daily deaths - Murcia")
        createSinglePlot(df_global, 'Day', 'Deaths_Murcia','Deaths','Daily deaths - Murcia', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Murcia':
        st.write("### Accumulated daily deaths - Murcia")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Murcia','Deaths','Accumulated daily deaths - Murcia', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Murcia':
        st.write("### Variation rate (daily deaths) - Murcia")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Murcia','Variation rate','Variation rate (daily deaths) - Murcia', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Murcia':
        st.write("### Variation rate (accumulated daily deaths) - Murcia")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Murcia','Variation rate','Variation rate (accumulated daily deaths) - Murcia', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Navarra':
        st.write("### Daily cases - Navarra")
        createSinglePlot(df_global, 'Day', 'Cases_Navarra','Cases','Daily cases - Navarra', 'Cases','log')

    elif page == 'Accumulated daily cases - Navarra':
        st.write("### Accumulated daily cases - Navarra")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Navarra','Cases','Accumulated daily cases - Navarra', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Navarra':
        st.write("### Variation rate (daily cases) - Navarra")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Navarra','Variation rate','Variation rate (daily cases) - Navarra', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Navarra':
        st.write("### Variation rate (accumulated daily cases) - Navarra")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Navarra','Variation rate','Variation rate (accumulated daily cases) - Navarra', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Navarra':
        st.write("### Daily deaths - Navarra")
        createSinglePlot(df_global, 'Day', 'Deaths_Navarra','Deaths','Daily deaths - Navarra', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Navarra':
        st.write("### Accumulated daily deaths - Navarra")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Navarra','Deaths','Accumulated daily deaths - Navarra', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Navarra':
        st.write("### Variation rate (daily deaths) - Navarra")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Navarra','Variation rate','Variation rate (daily deaths) - Navarra', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Navarra':
        st.write("### Variation rate (accumulated daily deaths) - Navarra")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Navarra','Variation rate','Variation rate (accumulated daily deaths) - Navarra', 'Variation rate (%)','linear')
        
    elif page == 'Daily cases - Pais Vasco':
        st.write("### Daily cases - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'Cases_Pais_Vasco','Cases','Daily cases - Pais Vasco', 'Cases','log')

    elif page == 'Accumulated daily cases - Pais Vasco':
        st.write("### Accumulated daily cases - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Pais_Vasco','Cases','Accumulated daily cases - Pais Vasco', 'Cases','log')

    elif page == 'Variation rate (daily cases) - Pais Vasco':
        st.write("### Variation rate (daily cases) - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Pais_Vasco','Variation rate','Variation rate (daily cases) - Pais Vasco', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily cases) - Pais Vasco':
        st.write("### Variation rate (accumulated daily cases) - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Pais_Vasco','Variation rate','Variation rate (accumulated daily cases) - Pais Vasco', 'Variation rate (%)','linear')

    elif page == 'Daily deaths - Pais Vasco':
        st.write("### Daily deaths - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'Deaths_Pais_Vasco','Deaths','Daily deaths - Pais Vasco', 'Deaths','log')

    elif page == 'Accumulated daily deaths - Pais Vasco':
        st.write("### Accumulated daily deaths - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Pais_Vasco','Deaths','Accumulated daily deaths - Pais Vasco', 'Deaths','log')

    elif page == 'Variation rate (daily deaths) - Pais Vasco':
        st.write("### Variation rate (daily deaths) - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Pais_Vasco','Variation rate','Variation rate (daily deaths) - Pais Vasco', 'Variation rate (%)','linear')

    elif page == 'Variation rate (accumulated daily deaths) - Pais Vasco':
        st.write("### Variation rate (accumulated daily deaths) - Pais Vasco")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Pais_Vasco','Variation rate','Variation rate (accumulated daily deaths) - Pais Vasco', 'Variation rate (%)','linear')
        

if __name__ == '__main__':
    main()