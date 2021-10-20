#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import joblib


from pycaret.classification import *


tuned_cat=joblib.load('Cat.pkl')


def run():


    add_selectbox = st.sidebar.selectbox(
    "What would you like to do?",
    ("Online Prediction","Batch Prediction"))

    st.sidebar.info('This app is created to predict if the applicant should be granted a loan or not.')
    

    st.title("Loan Prediction App")
    
    if add_selectbox == 'Online Prediction':
        
        gender = st.selectbox('Gender',['Female','Male'])
        married = st.selectbox('Married',['No','Yes'])
        depend = st.selectbox('Dependents',['0','1','2','3+'])
        edu = st.selectbox('Education',['Graduate','Not Graduate'])
        self = st.selectbox('Self Employed',['No','Yes'])
        app_inc = st.number_input ('Applicant Income')
        co_inc = st.number_input ('Coapplicant Income')
        amt = st.number_input ('Loan Amount')
        term = st.number_input ('Loan Amount Term')
        credit = st.selectbox('Credit History',['0','1'])
        prop_are = st.selectbox('Property Area',['Rural','Semiurban','Urban'])

        output=""

        test_df = pd.DataFrame()
        test_df['Gender']= [gender]
        test_df['Married']=[married]
        test_df['Dependents']=[depend] 
        test_df['Education']=[edu]
        test_df['Self_Employed']=[self] 
        test_df['ApplicantIncome']=[app_inc] 
        test_df['CoapplicantIncome']=[co_inc] 
        test_df['LoanAmount']=[amt] 
        test_df['Loan_Amount_Term']=[term] 
        test_df['Credit_History']=[credit] 
        test_df['Property_Area']=[prop_are]      
        

        if st.button("Predict"):
            Cat_pred=predict_model(tuned_cat,data=test_df)['Label']
            
            output = Cat_pred.values
            
            if(output==0):
                text="Rejected"
                st.error(text)
                
            elif(output==1):
                text="Approved"
                st.success(text)
 
    
    if add_selectbox == 'Batch Prediction':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            
            st.success('File uploaded successfully!')
            
            Cat_pred=predict_model(tuned_cat,data=data)['Label']
            
            data['Prediction']=Cat_pred

            st.write(data)
            st.markdown(get_table_download_link(data), unsafe_allow_html=True)
            


import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="Load_Predictions.csv">Download csv file</a>'



if __name__ == '__main__':
    run()





