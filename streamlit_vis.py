import streamlit as st
import pandas as pd
import altair as alt
data = pd.read_csv('cleaned_healthy_cities.csv')
st.title("Healthy Lifestyle Cities: Happiness Classifier")
st.write("Discovering feature importance for predicting happiness across global cities.")

selected_feature = st.selectbox("Choose a feature to visualize:", data.columns)

bar = alt.Chart(data).mark_bar().encode(
    x=alt.X(selected_feature + ':Q'),
    y='count()',
    color=alt.Color('happiness_level:N', sort=['Low', 'Medium', 'High']),
    tooltip=[selected_feature, 'happiness_level']
).interactive()

st.altair_chart(bar, use_container_width=True)