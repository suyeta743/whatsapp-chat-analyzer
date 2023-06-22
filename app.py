import pandas as pd
import streamlit as st
import preprocessor, helper
from streamlit.components.v1 import html







st.sidebar.title("Whatsapp Chat Analyzer")
date_formats_dict = {
    'dd/mm/yy': '%d/%m/%y',
    'dd/mm/YYYY': '%d/%m/%Y',
    'mm/dd/yy': '%m/%d/%y',
    'mm/dd/YYYY': '%m/%d/%Y',
    'yy/mm/dd': '%y/%m/%d',
    'YYYY/mm/dd': '%Y/%m/%d',
    'dd-mm-yy': '%d-%m-%y',
    'dd-mm-YYYY': '%d-%m-%Y',
    'mm-dd-yy': '%m-%d-%y',
    'mm-dd-YYYY': '%m-%d-%Y',
    'yy-mm-dd': '%y-%m-%d',
    'YYYY-mm-dd': '%Y-%m-%d'
}
time_format = st.sidebar.radio(label='Select Time Format : ', options=['12 Hr.','24 Hr.'])
date_format = st.sidebar.radio(label='Select Date Format : ', options=date_formats_dict.keys())
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    # df = preprocessor.preprocess(data)
    df = pd.DataFrame()
    if time_format == '12 Hr.':
        df = preprocessor.f12(data=data, date_format=date_format)
    else:
        df = preprocessor.f24(data=data, date_format=date_format)


    # fetch unique users
    user_list = df['user'].unique().tolist()
    # st.write(user_list)
    # user_list.remove(None)
    user_list.sort()
    user_list.insert(0, "Overall")

    if st.sidebar.checkbox("Show Analysis"):

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

        st.markdown("""
                                <h1 style="color:pink;">Chat analysis by selecting year and month  weekwise chat analysis</h1>
                                """, unsafe_allow_html=True)
        selected_year = st.radio(label='Select Year',options=list(set(df.year.tolist())),horizontal=True)
        selected_month = st.radio(label='Select Month',options=list(set(df.month.tolist())),horizontal=True)

        select_chart_type = st.radio(label="Select Chart",options=["Bar","Pie"],horizontal=True)

        helper.get_week_number_vs_messgae(df=df,year=selected_year,month=selected_month,chart_type=select_chart_type)

        st.markdown(
            """
                <h1 style="color:pink;">Message Word Cloud</h2>
            """,unsafe_allow_html=True
        )
        helper.create_word_cloud(df)


