import pickle
import streamlit as st
import pandas as pd
from plotly import graph_objs as go


# loading the trained model
pickle_gulamah = open("model_gulamah.pkl", "rb")
pickle_lisong = open("model_lisong.pkl", "rb")
pickle_lobster = open("model_lobster.pkl", "rb")
pickle_manyung = open("model_manyung.pkl", "rb")
pickle_nila = open("model_nila.pkl", "rb")
pickle_tengiri = open("model_tengiri.pkl", "rb")
pickle_tongkol = open("model_tongkol.pkl", "rb")
pickle_udang = open("model_udang.pkl", "rb")
model_gulamah = pickle.load(pickle_gulamah)
model_lisong = pickle.load(pickle_lisong)
model_lobster = pickle.load(pickle_lobster)
model_manyung = pickle.load(pickle_manyung)
model_nila = pickle.load(pickle_nila)
model_tengiri = pickle.load(pickle_tengiri)
model_tongkol = pickle.load(pickle_tongkol)
model_udang = pickle.load(pickle_udang)


@st.cache()

# defining the function which will make the prediction using the data which the user inputs
def prediction(ikan_type, months):
    # Pre-processing user input
    if ikan_type == "Gulamah":
        data = pd.read_csv(
            "gulamah.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_gulamah
    elif ikan_type == "Lisong":
        data = pd.read_csv(
            "lisong.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_lisong
    elif ikan_type == "Lobster":
        data = pd.read_csv(
            "lobster.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_lobster
    elif ikan_type == "Manyung":
        data = pd.read_csv(
            "manyung.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_manyung
    elif ikan_type == "Nila":
        data = pd.read_csv(
            "nila.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_nila
    elif ikan_type == "Tengiri":
        data = pd.read_csv(
            "tengiri.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_tengiri
    elif ikan_type == "Tongkol":
        data = pd.read_csv(
            "tongkol.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_tongkol
    elif ikan_type == "Udang":
        data = pd.read_csv(
            "udang.csv", index_col="Produksi Hasil Tangkap Laut", parse_dates=True
        )
        data.index.freq = "MS"
        model = model_udang

    # Making predictions
    start = len(data)
    end = len(data) + int(round(months)) - 1
    forecast = model.predict(start=start, end=end, dynamic=False, typ="levels")
    df_forecast = pd.DataFrame(forecast)
    df_forecast.index.freq = "MS"

    return df_forecast, data


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Forecasting Kebutuhan Ikan (Ton)</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    input_ikan = st.selectbox(
        "Jenis Ikan",
        (
            "Udang",
            "Lobster",
            "Nila",
            "Tengiri",
            "Manyung",
            "Gulamah",
            "Lisong",
            "Tongkol",
        ),
    )
    input_months = st.slider(
        "Number of months that will be predicted", min_value=0, max_value=6, step=1
    )
    # input_months = st.number_input('Number of months that will be predicted', step=1)
    result = ""
    data2 = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result, data = prediction(input_ikan, input_months)
        st.success(f"Forecasting results for the next {input_months} months :\n")
        st.write(result)

        data2 = data[[input_ikan]]
        data2 = pd.concat([data2, result])

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data2.iloc[0:48].index,
                y=data2[input_ikan].iloc[0:48],
                name="Data Actual",
            )
        )
        if input_ikan != "Manyung":
            fig.add_trace(
                go.Scatter(
                    x=data2.iloc[48:].index,
                    y=data2["predicted_mean"].iloc[48:],
                    name="Forecasts",
                )
            )
        else:
            fig.add_trace(
                go.Scatter(
                    x=data2.iloc[48:].index,
                    y=data2[data2.columns[0]].iloc[48:],
                    name="Forecasts",
                )
            )
            # kenapa ga muncul???? yg buat manyung
        fig.layout.update(title_text=input_ikan, xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
