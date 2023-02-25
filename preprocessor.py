import re
import pandas as pd
import streamlit as st

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s-\s'

    messages = re.split(pattern, data)[1:]

    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # users = []
    #
    #
    # messages = []
    # for message in df['user_message']:
    #     entry = re.split('([w\W]+?):\s', message)
    #     if entry[1:]:  # username
    #         users.append(entry[1])
    #         messages.append(entry[2])
    #     else:
    #         users.append('group_notification')
    #         messages.append(entry[0])
    # # df['user'] = messages.split(':')[0]
    # for message in messages:
    #     users.append(message.split(':')[0])
    # st.write(len(messages))
    # st.write(len(users))
    # df['user']=users
    # df['message'] = messages

    users = []
    message_list = []
    for message in df['user_message']:
        pos = message.find(": ")
        if (pos != -1):
            users.append(message[:pos])
            message_list.append(message[pos+2:])
        else:
            users.append(None)
            message_list.append(None)
    df['user'] = users
    df['message'] = message_list
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df.dropna(inplace=True)
    # df = df.drop(columns=['date'])
    df = df.drop(df.loc[df['message'] == '<Media omitted>\n'].index)

    return df
