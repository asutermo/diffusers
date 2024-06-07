import os
import subprocess
import sys

def main(args):
    try:
        #a_args.extend(args)
        print(a_args)
        result = subprocess.run(a_args, capture_output=True, text=True, check=True)
        print("Output from other_script.py:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running other_script.py with accelerate:\n", e.stderr)

if __name__ == "__main__":
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    a_args = ["accelerate", "launch", "--num_processes=8", "--multi_gpu", f"{current_script_directory}/train_controlnet_sdxl.py"] +  sys.argv[1:]
    try:
        #a_args.extend(args)
        print(a_args)
        result = subprocess.run(a_args, capture_output=True, text=True, check=True)
        print("Output from other_script.py:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running other_script.py with accelerate:\n", e.stderr)
        