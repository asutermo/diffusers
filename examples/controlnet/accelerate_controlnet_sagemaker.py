import os
import subprocess
import sys

if __name__ == "__main__":
    print(__file__)
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    print(current_script_directory)
    with os.scandir(current_script_directory) as entries:
        for entry in entries:
            print(entry.name, entry.path)
    args = ["accelerate", "launch", "--num_processes=8", "--multi_gpu", f"{current_script_directory}/train_controlnet_sdxl.py"] +  sys.argv[1:]
    try:
        print(args)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        print("Output from other_script.py:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running other_script.py with accelerate:\n", e.stderr)
        