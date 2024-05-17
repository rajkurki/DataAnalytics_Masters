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

    housing = st.number_input('housing',min_value=0,max_value=1,step=1)


    duration = st.number_input('duration',min_value=0, step=1)
    #poutcome variable defined here .
    lst_poutcome=selected_lst('poutcome', ['failure', 'success'])

    result=''
    if st.button('predict'):

        features_lst.append(housing)
        features_lst.append(duration)

        features_lst.extend(lst_poutcome)


        print(features_lst)
        prediction=classifier.predict([features_lst])
        print('prediction is : ',prediction[0])
        st.success(' The output of response variable is {0}'.format(prediction[0]))



if __name__=='__main__':
    main()

