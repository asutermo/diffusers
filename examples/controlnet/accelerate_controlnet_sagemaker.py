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
    a_args = ["accelerate", "launch", "num_processes=8", "--multi_gpu", "examples/controlnet/train_controlnet_sagemaker.py", sys.argv[1:]]
    try:
        #a_args.extend(args)
        print(a_args)
        result = subprocess.run(a_args, capture_output=True, text=True, check=True)
        print("Output from other_script.py:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running other_script.py with accelerate:\n", e.stderr)
        