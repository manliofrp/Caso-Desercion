import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Employees App')
st.header("using streamlit")
st.write("Dashboard (employees).")

@st.cache
def load_data(nrows):
    data = pd.read_csv("Employees.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state = st.text('Loading employees data...')
data = load_data(501)
data_load_state.text("Done!")

agree = st.sidebar.checkbox("Data description")
if agree:
    st.header("Show Dataframe Overview")
    st.dataframe(data)

agree2= st.sidebar.checkbox("Histplot by Age")
if agree2:
    fig, ax = plt.subplots()
    ax.hist(data.Age)
    st.header("Histplot of employees Age")
    st.pyplot(fig)
    st.markdown("_")

agree3= st.sidebar.checkbox("employees per unit")
if agree3:
    fig, ax = plt.subplots()
    ax.hist(data.Unit)
    st.header("Histplot of employees")
    st.pyplot(fig)
    st.markdown("_")

agree4= st.sidebar.checkbox("City chart and Attrition rate")
if agree4:
    fig, ax = plt.subplots()
    y= data["Attrition_rate"]
    x=data["Hometown"]
    ax.barh(x,y)
    ax.set_ylabel("City")
    ax.set_xlabel("Attrition_rate")
    st.header("Attrition_rate by city")
    st.pyplot(fig)
    st.markdown("_")

agree5= st.sidebar.checkbox("graphic: age and attrition rate")
if agree5:
    fig, ax = plt.subplots()
    y= data["Attrition_rate"]
    x=data["Age"]
    ax.barh(x,y)
    ax.set_ylabel("Age")
    ax.set_xlabel("Attrition rate")
    st.header("Attrition rate by age")
    st.pyplot(fig)
    st.markdown("_")

agree6= st.sidebar.checkbox("Graphic: attrition rate and time of service")
if agree6:
    fig, ax = plt.subplots()
    y= data["Attrition_rate"]
    x=data["Time_of_service"]
    ax.barh(x,y)
    ax.set_ylabel("Time of service")
    ax.set_xlabel("Attrition rate")
    st.header("Attrition rate and time of service")
    st.pyplot(fig)
    st.markdown("_")

@st.cache
def load_data_byid(id):
    filtered_data_byid=data[data["Employee_ID"].str.upper().str.contains(id.upper())]
    
    return filtered_data_byid

myid= st.sidebar.text_input("ID de empleado")
btnid=st.sidebar.button("Search by ID")

if(btnid):
    filterbyid= load_data_byid(myid)
    count_row= filterbyid.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyid)

@st.cache
def load_data_byht(ht):
    filtered_data_byht=data[data["Hometown"].str.upper().str.contains(ht.upper())]
    
    return filtered_data_byht

myht= st.sidebar.text_input("Employee's Hometown")
btnht=st.sidebar.button("Search by hometown")

if(btnht):
    filterbyht= load_data_byht(myht)
    count_row= filterbyht.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filterbyht)

@st.cache
def load_data_byunit(unit):
    filtered_data_byunit=data[data["Unit"].str.upper().str.contains(unit.upper())]
    
    return filtered_data_byunit

myunit= st.sidebar.text_input(" unit by employee")
btnunit=st.sidebar.button("search by unit")

if(btnunit):
    filterbyunit= load_data_byunit(myunit)
    count_row= filterbyunit.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filterbyunit)

@st.cache
def load_data_byeducation(education):
    filtered_data_byedu=data[data["Education_Level"]==education]
    
    return filtered_data_byedu

myedu= st.sidebar.selectbox("Select education level", data['Education_Level'].unique())
btnedu=st.sidebar.button("Search by education level")

if(btnedu):
    filterbyedu= load_data_byeducation(myedu)
    count_row= filterbyedu.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filterbyedu)

@st.cache
def load_data_byhtw(htw):
    filtered_data_byhtw=data[data["Hometown"]==htw]
    
    return filtered_data_byhtw

myhtw= st.sidebar.selectbox("Select city", data['Hometown'].unique())
btnhtw=st.sidebar.button("search by city")

if(btnhtw):
    filterbyhtw= load_data_byhtw(myhtw)
    count_row= filterbyhtw.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filterbyhtw)

@st.cache
def load_data_byun(un):
    filtered_data_byun=data[data["Unit"]==un]
    
    return filtered_data_byun

myun= st.sidebar.selectbox("Select a unit in box", data['Unit'].unique())
btnun=st.sidebar.button("Search by unit in box")

if(btnun):
    filterbyun= load_data_byun(myun)
    count_row= filterbyun.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filterbyun)