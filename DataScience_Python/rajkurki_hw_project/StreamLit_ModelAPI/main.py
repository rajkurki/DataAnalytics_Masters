import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
pickle_in=open('model.pkl','rb')
classifier=pickle.load(pickle_in)

def selected_lst(colname, lst_recived):
    dict_sm = {}
    option = st.selectbox(
        colname,
        lst_recived)

    for value in lst_recived:

        if option == value:
            dict_sm[value] = 1

        else:
            dict_sm[value] = 0
    lst_return = []
    for a in lst_recived:
        lst_return.append(dict_sm[a])
    print(lst_return)
    return lst_return




def main():
    pickle_in = open('model.pkl', 'rb')
    classifier = pickle.load(pickle_in)



    st.title('Bank Direct Marketing')




    html_str = """
    <div style="background-color:#ABBAEA;padding:10px">
    <h2 style="color:white;text-align:center;">Predict if the client will subscribe a term deposit</h2>
    </div>
    """
    st.markdown(html_str, unsafe_allow_html=True)
    features_lst=[]
    age=st.number_input('age',value=18,min_value=18,max_value=80,step=1)
    default=st.number_input('default',value=0,min_value=0,max_value=1,step=1)
    balance = st.number_input('balance',value=0.0,min_value=0.0)
    housing = st.number_input('housing',min_value=0,max_value=1,step=1)
    loan = st.number_input('loan',min_value=0,max_value=1,step=1)
    contact = st.number_input('contact', min_value=0, step=1)
    day = st.number_input('day', min_value=1, max_value=31,step=1)
    duration = st.number_input('duration',min_value=0, step=1)
    campaign = st.number_input('campaign', min_value=0, step=1)
    pdays = st.number_input('pdays', min_value=0, step=1)
    previous = st.number_input('previous', min_value=0, step=1)


    #poutcome variable defined here .
    lst_poutcome=selected_lst('poutcome', ['failure', 'other', 'success'])
   #
    lst_month=selected_lst('month',['apr','aug','dec','feb','jan','jul','jun','mar','may','nov','oct','sep'])
    #
    lst_job=selected_lst('job',['admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown'])

    #
    lst_marital=selected_lst('marital',['divorced','married','single'])

    lst_education=selected_lst('education',['primary','secondary','tertiary','unknown'])
    result=''
    if st.button('predict'):
        features_lst.append(age)
        features_lst.append(default)
        features_lst.append(balance)
        features_lst.append(housing)
        features_lst.append(loan)
        features_lst.append(contact)
        features_lst.append(day)
        features_lst.append(duration)
        features_lst.append(campaign)
        features_lst.append(pdays)
        features_lst.append(previous)
        features_lst.extend(lst_poutcome)
        features_lst.extend(lst_month)
        features_lst.extend(lst_job)
        features_lst.extend(lst_marital)
        features_lst.extend(lst_education)

        print(features_lst)
        prediction=classifier.predict([features_lst])
        print('prediction is : ',prediction[0])
        st.success(' The output of response variable is {0}'.format(prediction[0]))



if __name__=='__main__':
    main()

