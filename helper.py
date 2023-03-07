import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
# def fetch_stats(selected_user, df):
#     if selected_user!='Overall':
#         df = df[df['user'] == selected_user]
#     if selected_user == 'Overall':
#         num_messages = df.shape[0]
#         words = []
#         for message in df['message']:
#             if message != None:
#                 words.extend(message.split())
#         return num_messages, len(words)
#     else:
#         new_df = df[df['user'] == selected_user]
#         num_messages = new_df.shape[0]
#         words = []
#         for message in new_df['message']:
#             if message != None:
#                 words.extend(message.split())
#             return num_messages, len(words)


def fetch_stats(selected_user, df):
    df.dropna(inplace=True)
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    df = df.drop(df.loc[df['message'] == '<Media omitted>\n'].index)

    user_messages = df['message'].tolist()
    # st.write(df)

    words = 0
    for message in user_messages:
        words += (message.count(" ")+1)
    return len(user_messages),words


def user_vs_total_messages_bar(df):
    new_df = df[['user','message']]
    group_by_user_message_df = new_df.groupby('user').count().reset_index()

    fig = px.bar(x=group_by_user_message_df['user'], y=group_by_user_message_df['message'],color=group_by_user_message_df['user'])
    fig.update_xaxes(title='User Name')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>User vs. Total Messages Bar Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)







def month_vs_total_messages_bar(df):
    new_df = df[['month','message']]
    group_by_user_message_df = new_df.groupby('month').count().reset_index()

    fig = px.bar(x=group_by_user_message_df['month'], y=group_by_user_message_df['message'],color=group_by_user_message_df['month'])
    fig.update_xaxes(title='Month')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>Month vs. Total Messages Bar Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)





def user_vs_total_messages_pie(df):
    new_df = df[['user', 'message']]
    group_by_user_message_df = new_df.groupby('user').count().reset_index()

    fig = px.pie(group_by_user_message_df, values='message', names='user')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>User vs. Total Messages Pie Chart</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.95,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)






def month_vs_total_messages_pie(df):
    new_df = df[['month', 'message']]
    group_by_user_message_df = new_df.groupby('month').count().reset_index()

    fig = px.pie(group_by_user_message_df, values='message', names='month')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>Month vs. Total Messages Pie Chart</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.95,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)





def user_vs_total_messages_scatter(df):
    new_df = df[['user','message']]
    group_by_user_message_df = new_df.groupby('user').count().reset_index()

    fig = px.scatter(x=group_by_user_message_df['user'], y=group_by_user_message_df['message'],color=group_by_user_message_df['user'])
    fig.update_xaxes(title='User Name')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>User vs. Total Messages Scatter Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)




def month_vs_total_messages_scatter(df):
    new_df = df[['month','message']]
    group_by_user_message_df = new_df.groupby('month').count().reset_index()

    fig = px.scatter(x=group_by_user_message_df['month'], y=group_by_user_message_df['message'],color=group_by_user_message_df['month'])
    fig.update_xaxes(title='Month')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>Month vs. Total Messages Scatter Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)




def user_vs_total_messages_area(df):
    new_df = df[['user','message']]
    group_by_user_message_df = new_df.groupby('user').count().reset_index()

    # fig = px.area(x=group_by_user_message_df['user'], y=group_by_user_message_df['message'], color=group_by_user_message_df['user'])
    fig = px.area(group_by_user_message_df, x="user", y="message", color="user")
    fig.update_xaxes(title='User Name')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>User vs. Total Messages Area Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    fig.update_traces(
    marker_coloraxis=None
    )
    st.plotly_chart(fig)


def month_vs_total_messages_area(df):
    new_df = df[['month', 'message']]
    group_by_user_message_df = new_df.groupby('month').count().reset_index()

    # fig = px.area(x=group_by_user_message_df['user'], y=group_by_user_message_df['message'], color=group_by_user_message_df['user'])
    fig = px.area(group_by_user_message_df, x="month", y="message", color="month")
    fig.update_xaxes(title='Month')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>Month vs. Total Messages Area Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    fig.update_traces(
        marker_coloraxis=None
    )
    st.plotly_chart(fig)


def user_vs_total_messages_bubble(df):
    new_df = df[['user','message']]
    group_by_user_message_df = new_df.groupby('user').count().reset_index()

    # fig = px.scatter(x=group_by_user_message_df['user'], y=group_by_user_message_df['message'],color=group_by_user_message_df['user'])

    fig = px.scatter(group_by_user_message_df, x="user", y="message",
	         size=group_by_user_message_df['message'], color="user")


    fig.update_xaxes(title='User Name')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color:#fff;'>User vs. Total Messages Scatter Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)





def month_vs_total_messages_bubble(df):
    new_df = df[['month','message']]
    group_by_user_message_df = new_df.groupby('month').count().reset_index()

    # fig = px.scatter(x=group_by_user_message_df['user'], y=group_by_user_message_df['message'],color=group_by_user_message_df['user'])

    fig = px.scatter(group_by_user_message_df, x="month", y="message",
	         size=group_by_user_message_df['message'], color="month")


    fig.update_xaxes(title='Month')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color:#fff;'>Month vs. Total Messages Bubble Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )
    st.plotly_chart(fig)


def user_vs_total_messages_line(df):
    new_df = df[['user','message']]
    group_by_user_message_df = new_df.groupby('user').count().reset_index()

    fig = px.line(group_by_user_message_df, x="user", y="message",)


    fig.update_xaxes(title='User Name')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>User vs. Total Messages Scatter Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )

    st.plotly_chart(fig)





def month_vs_total_messages_line(df):
    new_df = df[['month','message']]
    group_by_user_message_df = new_df.groupby('month').count().reset_index()

    fig = px.line(group_by_user_message_df, x="month", y="message",)


    fig.update_xaxes(title='Month')
    fig.update_yaxes(title='Total Messages')
    # set the background color to transparent
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>Month vs. Total Messages Scatter Plot</span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.9,
            'pad': {'b': 10}
        }
    )

    st.plotly_chart(fig)


def year_month_weekday_user_totalMessage_Sunburst(df):
    df['weekday'] = df['date'].dt.strftime('%A')
    # Group by year, month, weekday, and user
    grouped_df = df.groupby(['year', 'month', 'weekday','user']).count().reset_index()

    # Create sunburst chart
    fig = px.sunburst(grouped_df, path=['year', 'month', 'weekday', 'user'], values='message', color='message',
                    color_continuous_scale='RdYlBu_r', hover_data=['message'])
    # fig.update_layout(title='Year vs. Month vs. Total Messages Sunburst Chart')

    fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title={
                'text': "<b><span style='color: #fff;'>Year ➡ Month ➡ WeekDay ➡ User ➡ Total Messages Sunburst Chart</span></b>",
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': {'size': 20},
                'y': 0.95,
                'pad': {'b': 10}
            }
        )

    st.plotly_chart(fig)






def stack_bar_month_user_messages(df):
    new_df = df[['user','month','message']]
    new_df = new_df.groupby(['month','user']).count().reset_index()
    fig = px.bar(new_df, x="month", y="user", color="user",text='user')

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "<b><span style='color: #fff;'>User Vs Month Vs Total Message   Stack Bar Chart </span></b>",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20},
            'y': 0.95,
            'pad': {'b': 10}
        }
    )

    fig.update_traces(textposition='auto')  # adjust text position

    st.plotly_chart(fig)



def heatmap_user_hour_total_messages(df):
    total_user = len(set(df['user'].tolist()))
    new_df = df[['user','message','hour']].groupby(['user','hour']).count().reset_index()

    fig = go.Figure(data=go.Heatmap(
        y=new_df['user'],
        x=new_df['hour'],
        z=new_df['message'],
        colorscale='Viridis'))

    fig.update_layout(
        title='User vs. Hour vs. Total Messages',
        xaxis_nticks=36,
        height=100+(total_user*40)  # increase the height of the plot to 800 pixels
    )

    st.plotly_chart(fig)


def heatmap_weekday_hour(df):
    df['weekday'] = df['date'].dt.strftime('%A')
    new_df = df[['weekday','hour','message']]
    new_df = new_df.groupby(['weekday','hour']).count().reset_index()
    fig = go.Figure(data=go.Heatmap(
        y=new_df['weekday'],
        x=new_df['hour'],
        z=new_df['message'],
        colorscale='Viridis'))

    fig.update_layout(
        title='User vs. Weekday vs. Total Messages',
        xaxis_nticks=36)

    st.plotly_chart(fig)






