import os

# Check logs folder exists
if not os.path.exists('logs'):
    os.makedirs('logs')

with open("sound_sequences.txt", "r") as f:
    data = f.readlines()

seq1 = data[0].split("[")[1].split("]")[0].split(",")
seq1 = [int(v) for v in seq1]
seq2 = data[1].split("[")[1].split("]")[0].split(",")
seq2 = [int(v) for v in seq2]

def get_sound_sequences(n):
    if n == 1:
        return seq1
    elif n == 2:
        return seq2

# SET1 = [4, 9, 3, 3, 8]
# SET1 = [4, 9, 3, 3, 8, 8, 6, 5, 5, 2, 2, 3, 4, 8, 8, 2, 7, 8, 9, 4, 4, 7, 4, 8, 5, 1, 6, 5, 5, 1]
# SET2 = [2, 6, 4, 6, 9]
# SET2 = [2, 6, 4, 6, 9, 7, 9, 7, 8, 5, 8, 6, 5, 3, 8, 6, 6, 4, 3, 8, 4, 1, 6, 8, 3, 8, 3, 1, 2, 9]
# 1-back task, rate = 6 times per minute
# SET1=[6, 7, 5, 6, 8, 7, 3, 8, 7, 6, 5, 7, 9, 9, 5, 5, 4, 3, 3, 1, 3, 5, 1, 9, 9, 9, 3, 1, 6, 6, 8, 2, 6, 5, 1, 2, 3, 8, 8, 7, 2, 9, 1, 6, 8, 6, 6, 8, 3, 9, 2, 5, 5, 7, 2, 4, 4, 4, 2, 2, 4, 4, 5, 1, 3, 7, 7, 7, 5, 4, 3, 8, 4, 4, 6, 2, 5, 1, 1, 3, 3, 6, 7, 3, 4, 3, 5, 8, 1, 8, 1, 2, 3, 4, 2, 5, 8, 1, 4, 1, 6, 6, 3, 8, 4, 4, 4, 2, 2, 1, 1, 6, 6, 5, 4, 8, 9, 6, 6, 3, 7, 9, 5, 5, 5, 2, 2, 9, 4, 7, 7, 2, 7, 8, 3, 7, 9, 4, 3, 8, 8, 9, 9, 5, 5, 5, 9, 9, 3, 7, 8, 7, 8, 7, 1, 1, 1, 7, 5, 9, 5, 1, 7, 8, 5, 7, 9, 4, 6, 3, 3, 9, 7, 7, 1, 2, 4, 7, 5, 6, 3, 6, 4, 9, 8, 8, 6, 4, 7, 2, 9, 8, 8, 1, 8, 4, 3, 4, 4, 9, 6, 6, 2, 2, 2, 4, 4, 4, 8, 1, 3, 4, 6, 2, 8, 3, 1, 6, 6, 2, 2, 2, 2, 1, 5, 3, 1, 2, 5, 3, 8, 2, 5, 9, 1, 2, 1, 5, 5, 3, 3, 8, 8, 1, 2, 3, 5, 1, 5, 9, 7, 3, 7, 8, 8, 7, 7, 8, 7, 7, 7, 4, 6, 7, 6, 9, 8, 1, 6, 4, 2, 7, 6, 8, 4, 7, 8, 9, 5, 7, 4, 8, 1, 2, 7, 3, 3, 9, 8, 4, 8, 1, 4, 9, 2, 7, 6, 6, 8, 8]
# 2-back task, rate = 5.7 times per minute
# SET2=[2, 4, 9, 4, 8, 4, 1, 3, 8, 3, 1, 8, 6, 8, 6, 8, 8, 5, 7, 9, 5, 1, 1, 1, 7, 2, 1, 6, 9, 6, 8, 1, 4, 4, 4, 6, 9, 9, 1, 9, 3, 5, 3, 5, 9, 8, 6, 9, 3, 3, 8, 6, 7, 6, 2, 6, 3, 3, 1, 5, 5, 7, 6, 6, 2, 5, 2, 9, 6, 2, 5, 5, 1, 6, 4, 1, 4, 4, 9, 3, 8, 3, 2, 1, 5, 5, 2, 7, 3, 9, 7, 2, 3, 8, 1, 8, 4, 7, 8, 3, 9, 8, 5, 3, 5, 1, 3, 3, 3, 3, 6, 7, 6, 2, 5, 2, 9, 9, 2, 3, 4, 3, 8, 5, 5, 8, 5, 6, 6, 5, 7, 9, 1, 4, 6, 1, 4, 4, 4, 6, 9, 8, 3, 6, 9, 8, 6, 4, 6, 7, 7, 7, 7, 6, 7, 2, 3, 2, 8, 8, 1, 3, 2, 8, 5, 6, 8, 8, 5, 9, 2, 1, 6, 7, 8, 6, 2, 4, 6, 2, 9, 6, 9, 8, 4, 3, 3, 5, 2, 7, 2, 5, 2, 2, 1, 6, 1, 6, 2, 4, 9, 5, 5, 2, 5, 6, 7, 6, 7, 2, 1, 2, 3, 2, 6, 5, 9, 6, 1, 4, 8, 1, 4, 2, 1, 5, 9, 5, 9, 3, 8, 2, 2, 6, 3, 2, 6, 2, 6, 5, 6, 7, 2, 3, 4, 3, 6, 2, 4, 5, 7, 5, 7, 3, 5, 3, 5, 3, 3, 6, 4, 4, 5, 5, 2, 6, 1, 9, 9, 4, 9, 4, 6, 9, 1, 2, 5, 2, 6, 8, 6, 9, 1, 7, 9, 7, 5, 1, 3, 9, 6, 4, 8, 3, 2, 5, 5, 2, 8, 6]
import pandas as pd
import numpy as np
def get_summary(n, data_path):
    df = pd.read_csv(data_path)
    gt_correct_idx = get_correct_idx(n)

    # df_seq = df[df['event'].isin([1,2,3,4,5,6,7,8,9])]
    # seq = df_seq['event'].values
    event_arr = df["event"]
    correct_idx = []
    wrong_idx = []
    start = False
    num_pressed = 0
    seq_idx = 0
    for i, event in enumerate(event_arr):
        print(i, event, type(event))
        if event == "Start":
            start = True
            continue
        if start == False:
            continue
        if i < n:
            continue
        if event in list("123456789"):
            seq_idx += 1
            continue
        if event == "pressed":
            # print(event, event_arr[i-1], event_arr[i-1-n])
            num_pressed += 1 
            if event_arr[i-1] == "pressed":
                print("double pressed")
            elif event_arr[i-1] == event_arr[i-1-n] and event_arr[i-1]!="pressed":
                print("correct pressed")
                correct_idx.append(seq_idx)
            else:
                print("wrong pressed")
                wrong_idx.append(seq_idx)

    recall = len(correct_idx) / len(gt_correct_idx)
    precision = len(correct_idx) / num_pressed

    print(f"correct presses: {len(correct_idx)} at positions {correct_idx}")
    print(f"wrong presses: {len(wrong_idx)} at positions {wrong_idx}")
    print(f"precision: {precision}")
    print(f"recall: {recall}")

    return correct_idx, wrong_idx

def get_correct_idx(n):
    seq = get_sound_sequences(n)
    correct_idx = []
    for i, num in enumerate(seq):
        if i < n:
            continue
        if num == seq[i-n]:
            correct_idx.append(i)

    return correct_idx

import glob
def get_latest_id():
    """
    return the max id in csv files
    """
    files = glob.glob("logs/*.csv")
    if len(files)>0:
        ids = [int(f.split("_")[-1]) for f in files]
        max_id = max(ids)
    else:
        max_id = 0

    return max_id

import datetime
def get_file_path(id):
    """
    return the logs csv file matches the id
    id: string after zfill
    """
    files = glob.glob("tcp_logs/*.csv")
    ret_files = ""
    if len(files) == 0:
        ret_files = f"tcp_logs/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{id}.csv"

    for f in files:
        print(f.split("_")[-1][:-4], type(f.split("_")[-1][:-4]))
        if f.split("_")[-1][:-4] == id:
            ret_files = f
            break
        else:
            ret_files = f"tcp_logs/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{id}.csv"

    return ret_files
