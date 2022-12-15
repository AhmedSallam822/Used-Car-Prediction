import streamlit as st
import pandas as pd
import joblib

def app():
    model = joblib.load('model.h5')
    st.set_page_config(page_title="Car Prediction ")
    st.title("Used Car Prediction")
    st.header("Epsilon Diploma Project")

    st.write("This project predicts Used Car Prices based on some features")

    
    year = st.number_input("Year", value=0)
    fuel = st.radio('Select Kind', ['Benzine', 'Natural Gas'])
    kilometers = st.number_input("Kilometers 0 - 200000", value=0)
    engine = st.radio("engine", ['1300CC', '1500CC', '1600CC'])
    transmission = st.radio('Select Type of Transmission', ['Manual', 'Automatic'])
    Age_of_Car = st.selectbox('Select Type of Transmission', ['Old', 'New'])
    body = st.selectbox('Select Type of body', ['Sedan', 'Hetchback','SUV'])
    brand = st.selectbox('Select Brand', ['Hyundai', 'Fiat','Chevrolet'])
    color = st.selectbox('Select Color', ['Beige', 'Black','Blue - Navy Blue', 'Brown', 'Burgundy','Gold', 'Gray', 'Green', 'Orange', 'Red','Silver','White','Yellow', 'other Color'])
    
    
    predict = st.button("Predict")
    if predict:
        df = pd.DataFrame.from_dict(
            {
                'Year':[year],
                'Fuel':[0 if fuel == 'Benzine' else 1],
                'Kilometers':[kilometers],
                'Engine':[1300 if engine == '1300CC' else (1500 if engine == '1500CC' else 1600)],
                'Transmission':[0 if transmission == 'Manual' else 1],
                'Age_of_Car':[0 if Age_of_Car == 'Old' else 1],
                'Body':[1 if body == 'Sedan' else (1 if body == 'Hetchback' else 1)],
                'Color':[1 if color == 'Beige' else (1 if body == 'Black' else (1 if body == 'Blue - Navy Blue' else (1 if body == 'Brown' else (1 if body == 'Burgundy' else (1 if body == 'Gold' else (1 if body == 'Gray' else (1 if body == 'Green' else (1 if body == 'Orange' else (1 if body == 'Red' else (1 if body == 'Silver' else (1 if body == 'White' else (1 if body == 'Yellow' else 1))))) )) )))))],

            }
        )

        st.write("Input Data: ")
        st.dataframe(df)

        pred = model.predict(df)
        st.write(F"Prediction: {pred}")

app()
