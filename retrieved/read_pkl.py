# import pickle
import sys
import torch

if len(sys.argv) != 2:
    print("Usage: python read_pickle.py <path_to_pickle_file>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'rb') as file:
        data = torch.load(file)
    print(data)
except FileNotFoundError:
    print(f"File not found: {file_path}")
# except pickle.UnpicklingError:
#     print(f"Error unpickling file: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")