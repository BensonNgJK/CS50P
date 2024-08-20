import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", action="store_true")
args = parser.parse_args()

if args.n:
    print("meow")
