import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--micro")
parser.add_argument("--meta")
parser.add_argument("--clinical")
parser.add_argument("--output")
args = parser.parse_args()

micro = pd.read_csv(args.micro)
meta = pd.read_csv(args.meta)
clinical = pd.read_csv(args.clinical)

df = micro.merge(meta, on="sample_id").merge(clinical, on="sample_id")

df.to_csv(args.output, index=False)