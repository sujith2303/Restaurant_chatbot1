import streamlit as st

st.set_page_config(page_title='Restaurant_chatbot',page_icon='icon.jpg',layout='wide')

st.markdown("<h1 style='text-align: center; '> Restaurant Chatbot</h1>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '></h1>",unsafe_allow_html=True)
col1,col2 = st.columns(2)



with col1:
    st.markdown("<h3 style='text-align: center; '> Veg Items</h3>",unsafe_allow_html=True)
    with st.expander('Veg Items'):
        c1,c2,c3 = st.columns(3)
        with c1:
            st.text_input("Enter item name",key='Veg dish')
        with c2:
            st.selectbox('Items',options=['Soups and Salads','Appetizers','Staters','Biryanis','Fried Rice','Curries','Pasta Dishes','Other'],key='Veg Select box')
        with c3:
            st.number_input("Enter the cost :+1:", value=100,format= '%d' , placeholder="Cost",key='Veg Cost')
        if st.button('submit',key='Veg Submit'):
            st.success('Done Successfully updated the Menu')
            with open('file_veg.txt','w') as f:
                f.write(st.session_state['Veg Select box'] + ':  ' + st.session_state['Veg dish']+'  ,cost :' + st.session_state['Veg Select box'])
            f.close()




with col2:
    st.markdown("<h3 style='text-align: center; '>Non Veg Items</h3>",unsafe_allow_html=True)
    with st.expander('Non Veg Items'):
        c1,c2,c3 = st.columns(3)
        with c1:
            st.text_input("Enter item name",key='Non Veg dish')
        with c2:
            st.selectbox('Items',options=['Soups and Salads','Appetizers','Staters','Biryanis','Fried Rice','Curries','Pasta Dishes','Other'],key='Non Veg selectbox')
        with c3:
            st.number_input("Enter the cost :+1:", value=100,format= '%d' , placeholder="Cost",key='Non  Veg Cost')
        if st.button('submit',key='Non Veg Submit'):
            st.success('Done Successfully updated the Menu')
            with open('file_non_veg.txt','w') as f:
                f.write(st.session_state['Non Veg selectbox'] + ':  ' + st.session_state['Non Veg dish']+'  ,cost :' + st.session_state['Non  Veg Cost'])
            f.close()



 


st.markdown("<h1 style='text-align: center; '></h1>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '></h1>",unsafe_allow_html=True)
col3,col4,col5  =st.columns(3)
with col3:
    st.markdown("<h3 style='text-align: center; '>Desserts</h3>",unsafe_allow_html=True)
    with st.container(border=True):
        c31,c32 = st.columns(2)
        with c31:
            st.text_input('Item name',key ='Dessert_name')
        
        with c32:
            st.number_input('Cost',key='Dessert Cost',value=100,placeholder='Cost',format= '%d')

        st.button('Submit',key = 'Dessert Submit')





with col4:
    st.markdown("<h3 style='text-align: center; '>Today's Special</h3>",unsafe_allow_html=True)
    with st.container(border=True):
        c41,c42,c43 = st.columns(3)
        with c41:
            st.selectbox('Item Type',options=['Soups and Salads','Appetizers','Staters','Biryanis','Fried Rice','Curries','Pasta Dishes','Other'],key='Todays special item')
        with c42:
            st.text_input("Enter item name",key='Special Dish')
        with c43:
            st.number_input("Enter the cost :+1:", value=100,format= '%d' , placeholder="Cost",key='Special item cost')
        st.button('Submit', key ='special items submit')




with col5:
    st.markdown("<h3 style='text-align: center; '>Offers and coupons</h3>",unsafe_allow_html=True)
    with st.container(border=True):
        c51,c52,c53 = st.columns(3)
        with c51:
            st.selectbox('Card type', options=['Debit','Credit','UPI','Paytm Postpaid'],key = 'card_offers')
        with c52:
            st.selectbox('Bank',['Icici','HDFC','Kotak','Swiggy','Other'],key='Bank name')
        with c53:
            st.slider('Offer percentage',value=None,min_value=10,max_value=60,key = 'offer percentage')
        
        if st.button('Submit',key ='offer Button'):
            st.success('Done!! Updated Successfully',icon='✅')
        
