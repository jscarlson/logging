import sys
import re
import os
import csv

model = sys.argv[1]
log_update = sys.argv[2]
save_path = "../logging/train/log.csv"

if model == "CUT":

    if log_update.startswith("(epoch:"):

        log_update = re.sub('[,():]', '', log_update)
        log_update = log_update.split()

        log_variables = []
        log_values = []
        for i in range(0, len(log_update), 2):
            variable = log_update[i]
            value = float(log_update[i+1])
            log_variables.append(variable)
            log_values.append(value)

        with open(save_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if os.stat(save_path).st_size == 0:
                writer.writerow(log_variables)
            writer.writerow(log_values)

elif model == "zi2zi":

     if log_update.strip().startswith("Epoch:"):

        log_update = re.sub('\[|\]|[,():/]', ' ', log_update)
        print(log_update)
        log_update = log_update.split()

        log_variables = []
        log_values = []
        for i in range(0, len(log_update), 2):
            variable = log_update[i]
            value = float(log_update[i+1])
            log_variables.append(variable)
            log_values.append(value)

        with open(save_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if os.stat(save_path).st_size == 0:
                writer.writerow(log_variables)
            writer.writerow(log_values)    
            


