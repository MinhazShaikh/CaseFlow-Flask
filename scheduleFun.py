import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def judgeSchedule():
    schedule = pd.read_csv("scheduler.csv")
    judges_dict = {"Judge1":[],"Judge2":[],"Judge3":[],"Judge4":[],"Judge5":[]}
    for i in range(len(schedule)):
    # Determine the judge's key based on the index (1 to 5)
        judge_key = f'Judge{i % 5 + 1}'
    # Append the row to the judge's list
        row_data = schedule.loc[i]
        # print(row_data)
        temp = row_data.to_dict()
        judges_dict[judge_key].append(temp)
        # print(temp)
    
    return judges_dict

def scheduler():
    data = pd.read_csv('newdatacase.csv') 

    # Create a DataFrame from the dataset
    df = pd.DataFrame(data)
    priority_values = {6: 10, 1: 10, 2: 9, 5: 9, 4: 2, 3: 1}
    df[' Past Hearing'] = df['Number of Past Hearing'].map(priority_values)
    df=df.sort_values(by='Priority')
    df=df.sort_values(by=['Confession',' Past Hearing'],ascending=False)

    dd=df.head(125)

    num_days = 5

    num_cases_per_day = len(dd) / num_days
    current_date = datetime.now().date()
    date_range = [current_date + timedelta(days=i) for i in range(num_days)]

    # Initialize an empty schedule DataFrame
    schedule = pd.DataFrame(columns=['CaseID', 'Priority', 'NoOfHearings', 'ScheduledDate'])

    for i, date in enumerate(date_range):
        start_idx = int(i * num_cases_per_day)
        end_idx = int((i + 1) * num_cases_per_day)
        cases_to_schedule = dd.iloc[start_idx:end_idx]
        cases_to_schedule['ScheduledDate'] = date
        schedule = pd.concat([schedule, cases_to_schedule], ignore_index=True)
    print(schedule)

def call():
    scheduler()
    df = judgeSchedule()
    # print(df)
    return df

# call()