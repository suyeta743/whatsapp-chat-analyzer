import streamlit as st
import preprocessor, helper
from streamlit.components.v1 import html

st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    # st.write(df.shape)


    # fetch unique users
    user_list = df['user'].unique().tolist()
    # st.write(user_list)
    # user_list.remove(None)
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.checkbox("Show Analysis"):

        num_messages, words = helper.fetch_stats(selected_user, df)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        # helper.user_vs_total_messages(df=df)

        # user_vs_total_messages_bar_checkbox=st.button(label='Bar Chart',key='bar')
        # user_vs_total_messages_pie_checkbox = st.button(label='Pie Chart', key='pie')
        # if user_vs_total_messages_bar_checkbox:
        #     helper.user_vs_total_messages_bar(df=df)
        # if user_vs_total_messages_pie_checkbox:
        #     helper.user_vs_total_messages_pie(df=df)

        # html_code = """
        # <h1 style="color:pink;">User Vs Total Messages</h1>
        # """

        st.markdown("""
        <h1 style="color:pink;">User Vs Total Messages</h1>
        """, unsafe_allow_html=True)

        chart_type = st.radio(label='Select chart type:', options=['Bar Chart', 'Pie Chart','Scatter Chart','Area Chart','Bubble Chart','Line Chart'],key=1)
        if chart_type == 'Bar Chart':
            helper.user_vs_total_messages_bar(df=df)
        elif chart_type == 'Pie Chart':
            helper.user_vs_total_messages_pie(df=df)
        elif chart_type == 'Scatter Chart':
            helper.user_vs_total_messages_scatter(df=df)
        elif chart_type == 'Area Chart':
            helper.user_vs_total_messages_area(df=df)
        elif chart_type == 'Bubble Chart':
            helper.user_vs_total_messages_bubble(df=df)
        elif chart_type == 'Line Chart':
            helper.user_vs_total_messages_line(df=df)

        st.markdown("""
                <h1 style="color:pink;">Month Vs Total Messages</h1>
                """, unsafe_allow_html=True)



        chart_type_user_totalmessages = st.radio(label='Select chart type:',
                              options=['Bar Chart', 'Pie Chart', 'Scatter Chart', 'Area Chart', 'Bubble Chart', 'Line Chart'],key=2)
        if chart_type_user_totalmessages == 'Bar Chart':
            helper.month_vs_total_messages_bar(df=df)
        elif chart_type_user_totalmessages == 'Pie Chart':
            helper.month_vs_total_messages_pie(df=df)
        elif chart_type_user_totalmessages == 'Scatter Chart':
            helper.month_vs_total_messages_scatter(df=df)
        elif chart_type_user_totalmessages == 'Area Chart':
            helper.month_vs_total_messages_area(df=df)
        elif chart_type_user_totalmessages == 'Bubble Chart':
            helper.month_vs_total_messages_bubble(df=df)
        elif chart_type_user_totalmessages == 'Line Chart':
            helper.month_vs_total_messages_line(df=df)




        st.markdown("""
                <h1 style="color:pink;">Month Vs User Vs Total Messages</h1>
                """, unsafe_allow_html=True)

        helper.stack_bar_month_user_messages(df=df)

        st.markdown("""
                <h1 style="color:pink;">User Vs Hour   Heatmap</h1>
                """, unsafe_allow_html=True)
        helper.heatmap_user_hour_total_messages(df=df)

        st.markdown("""
                        <h1 style="color:pink;">Week Vs Hour   Heatmap</h1>
                        """, unsafe_allow_html=True)
        helper.heatmap_weekday_hour(df=df)

        st.markdown("""
                <h1 style="color:pink;">Year ➡ Month ➡ WeekDay ➡ User ➡ Total Messages</h1>
                """, unsafe_allow_html=True)
        view_option=st.radio(label='seen or unseen:',options=['Invisible','Visible'])
        if view_option=='Visible':
            helper.year_month_weekday_user_totalMessage_Sunburst(df=df)



