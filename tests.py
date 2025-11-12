import asyncio
import subprocess
import os
import argparse
import json

solutions = [
    "ProblemAlternate",
    "ProblemFew",
    "ProblemNone"
]

accuracies = []
accuracies = []
all = {}

def run_tests():
    tests = sorted(os.listdir("./data"))
    tests.remove("README.md") 

    for test in tests:
        results = {}
        for problem in solutions:
            process = subprocess.Popen(f"cd problems && python3 -m {problem}.solution < ../data/{test}", shell=True, stdout=subprocess.PIPE, text=True)
            process.wait()
            results[problem] = process.stdout.read().strip()
        all[test] = results


run_tests()

def print_results_markdown(results_by_test):
    header = "| Test File | " + " | ".join(solutions) + " |"
    separator = "|------------|" + "|".join(["------------|" for _ in solutions])

    print(header)
    print(separator)

    for test, outputs in results_by_test.items():
        row = f"| {test} | " + " | ".join(outputs.get(problem, "") for problem in solutions) + " |"
        print(row)

def print_results_latex(results_by_test):
    col_format = "|l|" + "c|" * len(solutions)
    print("\\begin{table}[h!]")
    print("\\centering")
    print(f"\\begin{{tabular}}{{{col_format}}}")
    print("\\hline")

    header = "Test File & " + " & ".join(solutions) + " \\\\"
    print(header)
    print("\\hline")

    for test, outputs in results_by_test.items():
        row_values = " & ".join(outputs.get(problem, "") for problem in solutions)
        print(f"{test} & {row_values} \\\\")
    print("\\hline")

    print("\\end{tabular}")
    print("\\caption{Test results for all problem solutions}")
    print("\\label{tab:test_results}")
    print("\\end{table}")

def print_results_json(results_by_test):
    print(json.dumps(results_by_test)))


p = argparse.ArgumentParser(
    description="Testing program for the red scare algorithm solutions"
)

parser = p.add_mutually_exclusive_group()

parser.add_argument(
    "-m",
    "--markdown",
    action="store_true",
    help="Prints the output as markdown"
)

parser.add_argument(
    "-l",
    "--latex",
    action="store_true",
    help="Prints the output as a latex table"
)

parser.add_argument(
    "-j",
    "--json",
    action="store_true",
    help="Prints the output as a json object"
)

args = parser.parse_args()

if args.markdown:
    print("markdown")

# print_results_markdown(all)