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
    data_cases_spain = '{"Host":"www.epdata.es","Guid":"476812f9-73a2-4b5f-a74c-4824bc8b4a17","Formato":"json"}'
    data_deaths_accum_spain = '{"Host":"www.epdata.es","Guid":"b2568be9-c6b6-4056-86d6-02c6d45b1696","Formato":"json"}'
    data_recovered_accum_spain = '{"Host":"www.epdata.es","Guid":"58d0919c-8ad1-4a3f-9255-55f5b116da23","Formato":"json"}'
    data_cases_madrid = '{"Host":"www.epdata.es","Guid":"ebb8e9f0-2c01-4090-bc03-569a348f45dc-304","Formato":"json"}'
    data_deaths_madrid = '{"Host":"www.epdata.es","Guid":"81d9b17a-6b10-40de-a592-981cc548c6f2","Formato":"json"}'

    response_cases_spain = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = data_cases_spain).json()
    response_deaths_accum_spain = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = data_deaths_accum_spain).json()
    response_recovered_accum_spain = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = data_recovered_accum_spain).json()

    response_cases_madrid = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = data_cases_madrid).json()
    response_deaths_madrid = requests.post('https://www.epdata.es/oembed/get/', headers = headers, data = data_deaths_madrid).json()

    # Dictionaries and constants
    day_init_quarantine = 44
    day14_init_quarantine = 59
    day14_strict_quarantine = 73
    first_day_to_plot = 33
    last_day_to_plot = 75
    
    # Create raw dataframe

    raw_cases_spain = pd.read_json(response_cases_spain)
    raw_deaths_accum_spain = pd.read_json(response_deaths_accum_spain)
    raw_recovered_accum_spain = pd.read_json(response_recovered_accum_spain)

    raw_cases_madrid = pd.read_json(response_cases_madrid)
    raw_deaths_madrid = pd.read_json(response_deaths_madrid)

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


    # Create dataframe Madrid

    df_cases_madrid = createDataframeFromJson(raw_cases_madrid)
    df_cases_madrid.rename(columns={'Cases': 'Cases_Madrid'}, inplace= True)
    df_deaths_madrid = createDataframeFromJson(raw_deaths_madrid)
    df_deaths_madrid.rename(columns={'Cases': 'Deaths_Madrid'}, inplace= True)

    df_madrid = pd.merge(df_cases_madrid[['Period', 'Day','Cases_Madrid']],
                    df_deaths_madrid[['Period', 'Deaths_Madrid']],
                    on='Period', 
                    how='left')

    # Create dataframe global

    df_global = pd.merge(df_spain[['Period', 'Day','Cases_Spain','DeathsAccum_Spain', 'RecoveredAccum_Spain']], 
                        df_madrid[['Period', 'Cases_Madrid', 'Deaths_Madrid']],
                        on = 'Period',
                        how = 'left')
    # Compute missing fields and metrics

    # Deaths and recovered in Spain from accumulative data
    df_global['Deaths_Spain'] = fromAccumToSingleValues(df_global['DeathsAccum_Spain'].values)
    df_global['Recovered_Spain'] = fromAccumToSingleValues(df_global['RecoveredAccum_Spain'].values)

    # Cumulative sum Madrid
    df_global['CasesAccum_Madrid'] = df_global['Cases_Madrid'].cumsum()
    df_global['DeathsAccum_Madrid'] = df_global['Deaths_Madrid'].cumsum()

    # Variation rates Madrid
    df_global['Cases_VariationRate_Madrid'] = df_global['Cases_Madrid'].pct_change() * 100
    df_global['Deaths_VariationRate_Madrid'] = df_global['Deaths_Madrid'].pct_change() * 100
    df_global['CasesAccum_VariationRate_Madrid'] = df_global['CasesAccum_Madrid'].pct_change() * 100
    df_global['DeathsAccum_VariationRate_Madrid'] = df_global['DeathsAccum_Madrid'].pct_change() * 100

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
    if yScale != 'log':
        st.line_chart(chart_data)
    # Dictionaries and constants
    day_init_quarantine = 44
    day14_init_quarantine = 59
    day14_strict_quarantine = 73
    first_day_to_plot = 33
    last_day_to_plot = 75

    plt.figure(figsize=(20,10))
    plt.plot(df_global['Day'], df_global[yCases], color = 'r', marker='o', linestyle='solid', linewidth=2, markersize=5, label='Cases')
    plt.plot(df_global['Day'], df_global[yDeaths], color = 'k', marker='o', linestyle='solid', linewidth=2, markersize=5, label='Deaths')
    if yRecovered != 'null':
        plt.plot(df_global['Day'], df_global[yRecovered], color = 'g', marker='o', linestyle='solid', linewidth=2, markersize=5, label='Recovered')
    plt.title(title, fontsize = 20)
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

    chart_data = pd.DataFrame({
        xData: df_global[xData],
        yData: df_global[yData]
    })
    chart_data = chart_data.set_index(df_global['Period'])
    st.write("### " + title, chart_data.sort_index())
    if yScale != 'log':
        st.line_chart(chart_data)
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
    return st.pyplot()


def main():
    st.title('Coronavirus COVID-19 en Spain y Madrid')

    df_global = getData()

    page = st.sidebar.selectbox("Elige una pagina", [
        'Tabla con los resultados obtenidos',
        'Grafica de casos, muertes y recuperaciones acumulados en Spain',
        'Grafica de casos, muertes y recuperaciones acumulados en Spain (log scale)',
        'Grafica de casos, muertes y recuperaciones acumulados en Madrid',
        'Grafica de casos, muertes y recuperaciones acumulados en Madrid (log scale)',
        'Grafica de casos en Spain',
        'Grafica de casos en Spain (log scale)',
        'Grafica de casos acumulados en Spain',
        'Grafica de casos acumulados en Spain (log scale)',
        'Grafica de variacion de casos en Spain',
        'Grafica de variacion para casos acumulados en Spain',
        'Grafica de muertes en Spain',
        'Grafica de muertes en Spain (log scale)',
        'Grafica de muertes acumuladas en Spain',
        'Grafica de muertes acumuladas en Spain (log scale)',
        'Grafica de variacion de muertes es Spain',
        'Grafica de variacion de muertes en Spain (log scale)',
        'Grafica de recuperaciones en Spain',
        'Grafica de recuperaciones en Spain (log scale)',
        'Grafica de recuperaciones acumuladas en Spain',
        'Grafica de recuperaciones acumuladas en Spain (log scale)',
        'Grafica de variaciones de recuperacion en Spain',
        'Grafica de variaciones de recuperacion es Spain (log scale)',
        'Grafica de casos en Madrid',
        'Grafica de casos en Madrid (log scale)',
        'Grafica de casos acumulados en Madrid',
        'Grafica de casos acumulados en Madrid',
        'Grafica de variaciones de casos en Madrid',
        'Grafica de variaciones de casos en Madrid (log scale)',
        'Grafica de muertos en Madrid',
        'Grafica de muertos en Madrid (log scale)',
        'Grafica de muertos acumulados en Madrid',
        'Grafica de muertos acumulados en Madrid (log scale)',
        'Grafica de variaciones de muertos en Madrid',
        'Grafica de variaciones de muertos en Madrid (log scale)'
    ])

    if page == 'Tabla con los resultados obtenidos':
        TodaysDate = time.strftime("%d-%m-%Y")
        df_table = df_global
        df_table = df_table.set_index("Period")
        data_table = df_table.loc[df_table.index]
        st.write("### Tabla con los resultados obtenidos a dia " + TodaysDate, data_table.sort_index())
        # Select only the days after the first 50 deaths in Spain

    elif page == 'Grafica de casos, muertes y recuperaciones acumulados en Spain':
        st.write("### Grafica de casos, muertes y recuperaciones acumulados en Spain")
        createOverviewPlot(df_global, 'CasesAccum_Spain','DeathsAccum_Spain','RecoveredAccum_Spain','Spain','linear')

    elif page == 'Grafica de casos, muertes y recuperaciones acumulados en Spain (log scale)':
        st.write("### Grafica de casos, muertes y recuperaciones acumulados en Spain (log scale)")
        createOverviewPlot(df_global, 'CasesAccum_Spain','DeathsAccum_Spain','RecoveredAccum_Spain','Spain (log scale)','log')

    elif page == 'Grafica de casos, muertes y recuperaciones acumulados en Madrid':
        st.write("### Grafica de casos, muertes y recuperaciones acumulados en Madrid")
        createOverviewPlot(df_global, 'CasesAccum_Madrid','DeathsAccum_Madrid','null','Madrid','linear')

    elif page == 'Grafica de casos, muertes y recuperaciones acumulados en Madrid (log scale)':
        st.write("### Grafica de casos, muertes y recuperaciones acumulados en Madrid (log scale)")
        createOverviewPlot(df_global, 'CasesAccum_Madrid','DeathsAccum_Madrid','null','Madrid (log scale)','log')

    elif page == 'Grafica de casos en Spain':
        st.write("### Grafica de casos en Spain")
        createSinglePlot(df_global, 'Day', 'Cases_Spain','Cases','Daily cases - Spain', 'Cases','linear')

    elif page == 'Grafica de casos en Spain (log scale)':
        st.write("### Grafica de casos en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'Cases_Spain','Cases','Daily cases - Spain (log scale)', 'Cases','log')

    elif page == 'Grafica de casos acumulados en Spain':
        st.write("### Grafica de casos acumulados en Spain")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Spain','Cases','Accumulated daily cases - Spain', 'Cases','linear')

    elif page == 'Grafica de casos acumulados en Spain (log scale)':
        st.write("### Grafica de casos acumulados en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Spain','Cases','Accumulated daily cases - Spain (log scale)', 'Cases','log')

    elif page == 'Grafica de variacion de casos en Spain':
        st.write("### Grafica de variacion de casos en Spain")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Spain','Variation rate','Variation rate (daily cases) - Spain', 'Variation rate (%)','linear')

    elif page == 'Grafica de variacion para casos acumulados en Spain':
        st.write("### Grafica de variacion para casos acumulados en Spain")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Spain','Variation rate','Variation rate (accumulated daily cases) - Spain', 'Variation rate (%)','linear')

    elif page == 'Grafica de muertes en Spain':
        st.write("### Grafica de muertes en Spain")
        createSinglePlot(df_global, 'Day', 'Deaths_Spain','Deaths','Daily deaths - Spain', 'Deaths','linear')

    elif page == 'Grafica de muertes en Spain (log scale)':
        st.write("### Grafica de muertes en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'Deaths_Spain','Deaths','Daily deaths - Spain (log scale)', 'Deaths','log')

    elif page == 'Grafica de muertes acumuladas en Spain':
        st.write("### Grafica de muertes acumuladas en Spain")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Spain','Deaths','Accumulated daily deaths - Spain', 'Deaths','linear')

    elif page == 'Grafica de muertes acumuladas en Spain (log scale)':
        st.write("### Grafica de muertes acumuladas en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Spain','Deaths','Accumulated daily deaths - Spain (log scale)', 'Deaths','log')

    elif page == 'Grafica de variacion de muertes es Spain':
        st.write("### Grafica de variacion de muertes es Spain")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Spain','Variation rate','Variation rate (daily deaths) - Spain', 'Variation rate (%)','linear')

    elif page == 'Grafica de variacion de muertes en Spain (log scale)':
        st.write("### Grafica de variacion de muertes en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Spain','Variation rate','Variation rate (accumulated daily deaths) - Spain', 'Variation rate (%)','linear')

    elif page == 'Grafica de recuperaciones en Spain':
        st.write("### Grafica de recuperaciones en Spain")
        createSinglePlot(df_global, 'Day', 'Recovered_Spain','Recovered','Daily recovered - Spain', 'Recovered','linear')

    elif page == 'Grafica de recuperaciones en Spain (log scale)':
        st.write("### Grafica de recuperaciones en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'Recovered_Spain','Recovered','Daily recovered - Spain (log scale)', 'Recovered','log')

    elif page == 'Grafica de recuperaciones acumuladas en Spain':
        st.write("### Grafica de recuperaciones acumuladas en Spain")
        createSinglePlot(df_global, 'Day', 'RecoveredAccum_Spain','Recovered','Accumulated daily recovered - Spain', 'Recovered','linear')

    elif page == 'Grafica de recuperaciones acumuladas en Spain (log scale)':
        st.write("### Grafica de recuperaciones acumuladas en Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'RecoveredAccum_Spain','Recovered','Accumulated daily recovered - Spain (log scale)', 'Recovered','log')

    elif page == 'Grafica de variaciones de recuperacion en Spain':
        st.write("### Grafica de variaciones de recuperacion en Spain")
        createSinglePlot(df_global, 'Day', 'Recovered_VariationRate_Spain','Variation rate','Variation rate (daily recovered) - Spain', 'Variation rate (%)','linear')

    elif page == 'Grafica de variaciones de recuperacion es Spain (log scale)':
        st.write("### Grafica de variaciones de recuperacion es Spain (log scale)")
        createSinglePlot(df_global, 'Day', 'RecoveredAccum_VariationRate_Spain','Variation rate','Variation rate (accumulated daily recovered) - Spain', 'Variation rate (%)','linear')

    elif page == 'Grafica de casos en Madrid':
        st.write("### Grafica de casos en Madrid")
        createSinglePlot(df_global, 'Day', 'Cases_Madrid','Cases','Daily cases - Madrid', 'Cases','linear')

    elif page == 'Grafica de casos en Madrid (log scale)':
        st.write("### Grafica de casos en Madrid (log scale)")
        createSinglePlot(df_global, 'Day', 'Cases_Madrid','Cases','Daily cases - Madrid (log scale)', 'Cases','log')

    elif page == 'Grafica de casos acumulados en Madrid':
        st.write("### Grafica de casos acumulados en Madrid")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Madrid','Cases','Accumulated daily cases - Madrid', 'Cases','linear')

    elif page == 'Grafica de casos acumulados en Madrid':
        st.write("### Grafica de casos acumulados en Madrid")
        createSinglePlot(df_global, 'Day', 'CasesAccum_Madrid','Cases','Accumulated daily cases - Madrid (log scale)', 'Cases','log')

    elif page == 'Grafica de variaciones de casos en Madrid':
        st.write("### Grafica de variaciones de casos en Madrid")
        createSinglePlot(df_global, 'Day', 'Cases_VariationRate_Madrid','Variation rate','Variation rate (daily cases) - Madrid', 'Variation rate (%)','linear')

    elif page == 'Grafica de variaciones de casos en Madrid (log scale)':
        st.write("### Grafica de variaciones de casos en Madrid (log scale)")
        createSinglePlot(df_global, 'Day', 'CasesAccum_VariationRate_Madrid','Variation rate','Variation rate (accumulated daily cases) - Madrid', 'Variation rate (%)','linear')

    elif page == 'Grafica de muertos en Madrid':
        st.write("### Grafica de muertos en Madrid")
        createSinglePlot(df_global, 'Day', 'Deaths_Madrid','Deaths','Daily deaths - Madrid', 'Deaths','linear')

    elif page == 'Grafica de muertos en Madrid (log scale)':
        st.write("### Grafica de muertos en Madrid (log scale)")
        createSinglePlot(df_global, 'Day', 'Deaths_Madrid','Deaths','Daily deaths - Madrid (log scale)', 'Deaths','log')

    elif page == 'Grafica de muertos acumulados en Madrid':
        st.write("### Grafica de muertos acumulados en Madrid")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Madrid','Deaths','Accumulated daily deaths - Madrid', 'Deaths','linear')

    elif page == 'Grafica de muertos acumulados en Madrid (log scale)':
        st.write("### Grafica de muertos acumulados en Madrid (log scale)")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_Madrid','Deaths','Accumulated daily deaths - Madrid (log scale)', 'Deaths','log')

    elif page == 'Grafica de variaciones de muertos en Madrid':
        st.write("### Grafica de variaciones de muertos en Madrid")
        createSinglePlot(df_global, 'Day', 'Deaths_VariationRate_Madrid','Variation rate','Variation rate (daily deaths) - Madrid', 'Variation rate (%)','linear')

    elif page == 'Grafica de variaciones de muertos en Madrid (log scale)':
        st.write("### Grafica de variaciones de muertos en Madrid (log scale)")
        createSinglePlot(df_global, 'Day', 'DeathsAccum_VariationRate_Madrid','Variation rate','Variation rate (accumulated daily deaths) - Madrid', 'Variation rate (%)','linear')

if __name__ == '__main__':
    main()