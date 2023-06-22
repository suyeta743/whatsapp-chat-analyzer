import re
import pandas as pd
import streamlit as st




"""
def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s-\s'

    messages = re.split(pattern, data)[1:]

    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
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
"""


def f24(data, date_format=""):
    first = 0
    second = 1
    message_list = []
    pattern = '((\d{1,4}\/\d{1,4}\/\d{1,4}), (\d{1,2}:\d{1,2}) - ([^:]+): )'
    matches = list(re.finditer(pattern, data))
    while (second <= len(matches)):
        current_group = matches[first]
        if (second < len(matches)):
            next_group = matches[second]
        date = current_group[2]
        time = current_group[3]
        contact = current_group[4]
        if (second < len(matches)):
            message = data[current_group.end(): next_group.start()]
        else:
            message = data[current_group.end():]
        message_list.append({
            'date': date,
            'time': time,
            'user': contact,
            'message': message
        })
        first += 1
        second += 1

    df = pd.DataFrame(message_list)

    given_date_format = '%d/%m/%Y'

    if date_format == 'dd/mm/yy':
        given_date_format = '%d/%m/%y'
    elif date_format == 'dd/mm/YYYY':
        given_date_format = '%d/%m/%Y'
    elif date_format == 'mm/dd/yy':
        given_date_format = '%m/%d/%y'
    elif date_format == 'mm/dd/YYYY':
        given_date_format = '%m/%d/%Y'
    elif date_format == 'yy/mm/dd':
        given_date_format = '%y/%m/%d'
    elif date_format == 'YYYY/mm/dd':
        given_date_format = '%Y/%m/%d'
    elif date_format == 'dd-mm-yy':
        given_date_format = '%d-%m-%y'
    elif date_format == 'dd-mm-YYYY':
        given_date_format = '%d-%m-%Y'
    elif date_format == 'mm-dd-yy':
        given_date_format = '%m-%d-%y'
    elif date_format == 'mm-dd-YYYY':
        given_date_format = '%m-%d-%Y'
    elif date_format == 'yy-mm-dd':
        given_date_format = '%y-%m-%d'
    elif date_format == 'YYYY-mm-dd':
        given_date_format = '%Y-%m-%d'

    # given_date_format = '%m/%d/%y'
    df['date'] = pd.to_datetime(df['date'], format=given_date_format)
    df['time'] = df['time'].astype(str) + ':00'
    # df['time'] = df['time'].dt.strftime('%H:%M')
    df['user'] = df['user'].str.split('(').str[0].str.strip()
    df['message'] = df['message'].astype(str)
    df['day'] = df['date'].dt.day.astype(str)
    df['year'] = df['date'].dt.year.astype(str)
    df['month'] = df['date'].dt.strftime('%B')

    df['datetime'] = pd.to_datetime(df['date']) + pd.to_timedelta(
        df['time'].str.split(':').apply(lambda x: pd.Timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2]))))
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute

    df['year'] = df['year'].astype('int64')

    df['date'] = df['datetime']
    df['day'] = df['day'].astype('int64')

    # df = df[['date','time','user','message','day','year','month']]
    df = df[['date', 'user', 'message', 'year', 'month', 'day', 'hour', 'minute']]

    return df


def f12(data, date_format):
    first = 0
    second = 1
    message_list = []
    pattern = '(((\d{1,4}\/\d{1,4}\/\d{1,4}), (\d{1,2}:\d{1,2})\\u202f([ap]m)) - ([^:]+): )'
    matches = list(re.finditer(pattern, data))
    while (second <= len(matches)):
        current_group = matches[first]
        if (second < len(matches)):
            next_group = matches[second]
        date = current_group[3]
        time = current_group[4]
        am_or_pm = current_group[5]
        contact = current_group[6]
        if (second < len(matches)):
            message = data[current_group.end(): next_group.start()]
        else:
            message = data[current_group.end():]
        message_list.append({
            'date': date,
            'time': time,
            'am_or_pm': am_or_pm,
            'user': contact,
            'message': message
        })
        first += 1
        second += 1

    df = pd.DataFrame(message_list)

    given_date_format = '%d/%m/%Y'

    if date_format == 'dd/mm/yy':
        given_date_format = '%d/%m/%y'
    elif date_format == 'dd/mm/YYYY':
        given_date_format = '%d/%m/%Y'
    elif date_format == 'mm/dd/yy':
        given_date_format = '%m/%d/%y'
    elif date_format == 'mm/dd/YYYY':
        given_date_format = '%m/%d/%Y'
    elif date_format == 'yy/mm/dd':
        given_date_format = '%y/%m/%d'
    elif date_format == 'YYYY/mm/dd':
        given_date_format = '%Y/%m/%d'
    elif date_format == 'dd-mm-yy':
        given_date_format = '%d-%m-%y'
    elif date_format == 'dd-mm-YYYY':
        given_date_format = '%d-%m-%Y'
    elif date_format == 'mm-dd-yy':
        given_date_format = '%m-%d-%y'
    elif date_format == 'mm-dd-YYYY':
        given_date_format = '%m-%d-%Y'
    elif date_format == 'yy-mm-dd':
        given_date_format = '%y-%m-%d'
    elif date_format == 'YYYY-mm-dd':
        given_date_format = '%Y-%m-%d'

    df['time'] = pd.to_datetime(df['time'] + ' ' + df['am_or_pm'], format='%I:%M %p').dt.strftime('%H:%M:%S')
    # Convert date to datetime format
    df['date'] = pd.to_datetime(df['date'], format=given_date_format)

    df['day'] = df['date'].dt.day.astype(str)
    df['year'] = df['date'].dt.year.astype(str)
    df['month'] = df['date'].dt.strftime('%B')

    df['datetime'] = pd.to_datetime(df['date']) + pd.to_timedelta(
        df['time'].str.split(':').apply(lambda x: pd.Timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2]))))
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute

    df['year'] = df['year'].astype('int64')

    df['date'] = df['datetime']
    df['day'] = df['day'].astype('int64')

    # df = df[['date','time','user','message','day','year','month']]
    df = df[['date', 'user', 'message', 'year', 'month', 'day', 'hour', 'minute']]

    # df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    return df