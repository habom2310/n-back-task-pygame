import os

# Check logs folder exists
if not os.path.exists('logs'):
    os.makedirs('logs')

with open("sound_sequences.txt", "r") as f:
    data = f.read()

seq = data.split(",")
seq = [int(v) for v in seq]

def get_sound_sequences():
    return seq

# import pandas as pd
# import numpy as np
# def get_summary(n, data_path):
#     df = pd.read_csv(data_path)
#     gt_correct_idx = get_correct_idx(n)

#     # df_seq = df[df['event'].isin([1,2,3,4,5,6,7,8,9])]
#     # seq = df_seq['event'].values
#     event_arr = df["event"]
#     correct_idx = []
#     wrong_idx = []
#     start = False
#     num_pressed = 0
#     seq_idx = 0
#     for i, event in enumerate(event_arr):
#         print(i, event, type(event))
#         if event == "Start":
#             start = True
#             continue
#         if start == False:
#             continue
#         if i < n:
#             continue
#         if event in list("123456789"):
#             seq_idx += 1
#             continue
#         if event == "pressed":
#             # print(event, event_arr[i-1], event_arr[i-1-n])
#             num_pressed += 1 
#             if event_arr[i-1] == "pressed":
#                 print("double pressed")
#             elif event_arr[i-1] == event_arr[i-1-n] and event_arr[i-1]!="pressed":
#                 print("correct pressed")
#                 correct_idx.append(seq_idx)
#             else:
#                 print("wrong pressed")
#                 wrong_idx.append(seq_idx)

#     recall = len(correct_idx) / len(gt_correct_idx)
#     precision = len(correct_idx) / num_pressed

#     print(f"correct presses: {len(correct_idx)} at positions {correct_idx}")
#     print(f"wrong presses: {len(wrong_idx)} at positions {wrong_idx}")
#     print(f"precision: {precision}")
#     print(f"recall: {recall}")

#     return correct_idx, wrong_idx

def get_correct_idx(seq):
    correct_idx = []
    for i, num in enumerate(seq):
        if i < 2:
            continue
        if num == seq[i-2]:
            correct_idx.append(i)

    return correct_idx

import glob
def get_latest_id():
    """
    return the max id in csv files
    """
    files = glob.glob("logs/*.csv")
    if len(files)>0:
        ids = [int(f.split("_")[-1][:-4]) for f in files]
        max_id = max(ids)
    else:
        max_id = 0

    return max_id
