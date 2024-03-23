from utilities.helper import categoricals_map, numericals_minmax, model_names, predict, metrics_result
import streamlit as st

###### Variables
job = None
marital = None
education = None
previous = None
salary = None
balance = None
duration = None
pdays = None
response = None

##### The App

st.title('Deposit Prediction for Bank Marketing', anchor=None)

# Sidebar for EDA and Dataset
st.sidebar.write("""
    [Exploratory Data Analysis](https://github.com/Varshitha-Neelapu/Bank-Marketing/edit/main/Bank_Marketing_with_ML.ipynb)
""")
st.sidebar.write("""
    [Dataset](https://archive.ics.uci.edu/static/public/222/bank+marketing.zip)
""")

with st.container():

    st.header('Response Predictor')


    col1, col2 = st.columns(2)

    with col1:
        job = st.selectbox('job'.title(), categoricals_map['job'].keys())
        marital = st.selectbox('marital'.title(), categoricals_map['marital'].keys())
        education = st.selectbox('education'.title(), categoricals_map['education'].keys())
        previous = st.selectbox('previous'.title(), categoricals_map['previous'].keys())

    with col2:
        salary = st.slider('salary'.title(), min_value=numericals_minmax['salary'][0], max_value=numericals_minmax['salary'][1])
        balance = st.slider('balance'.title(), min_value=numericals_minmax['balance'][0], max_value=numericals_minmax['balance'][1])
        duration = st.slider('duration'.title(), min_value=numericals_minmax['duration'][0], max_value=numericals_minmax['duration'][1])
        pdays = st.slider('pdays'.title(), min_value=numericals_minmax['pdays'][0], max_value=numericals_minmax['pdays'][1])

    modelname = st.selectbox('Model', model_names)

    if st.button('Predict'):
        response = predict({
            'job': job,
            'marital': marital,
            'education': education,
            'previous': previous,
            'salary': salary,
            'balance': balance,
            'duration': duration,
            'pdays': pdays,
        }, modelname)

    if response != None:
        st.metric('Response', response, delta=None, delta_color="normal")


