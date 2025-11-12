import asyncio
import signal
import subprocess
import os
import argparse
import json
from time import time

solutions = [
    "ProblemAlternate",
    "ProblemFew",
    "ProblemNone",
    "ProblemMany",
    "ProblemSome"
]

accuracies = []
accuracies = []
all = {}


def current_milli_time():
    return round(time() * 1000)

def run_tests(tests = os.listdir("./data")):
    tests = sorted(tests)
    if "README.md" in tests:
        tests.remove("README.md") 

    for test in tests:
        results = {}
        for problem in solutions:
            if args.debug:
                start_time = current_milli_time()
                print(f"[DEBUG]: running '{test}' for '{problem}'")
            process = subprocess.Popen(f"cd problems && python3 -m {problem}.solution < ../data/{test}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
            try:
                stdout, stderr = process.communicate(timeout=args.timeout)
                if process.returncode != 0:
                    if "RecursionError" in stderr:
                        results[problem] = "REC LIMIT REACHED"
                    else:
                        results[problem] = "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK"
                else:
                    results[problem] = stdout.strip()
                
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.kill()
                stdout, stderr = process.communicate()
                results[problem] = "TIMEOUT"
            

            process = None

            if args.debug:
                end_time = current_milli_time()
                print(f"[DEBUG]: '{test}' finished for {problem} with result '{results[problem]}' | finished in {end_time-start_time} ms")
        all[test] = results


def print_results_markdown(results_by_test):
    header = "| Test File | " + " | ".join(solutions) + " |"
    separator = "|:------------|:" + ":|:".join(["------------" for _ in solutions]) + ":|"

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
    print(json.dumps(results_by_test))


def parse_file_list(value):
    """Parse file input that can be either a string or list format"""
    if not value:
        return []
    
    if value.startswith('[') and value.endswith(']'):
        content = value[1:-1].strip()
        if not content:
            return []
        return [item.strip() for item in content.split(',')]
    else:
        return [value]


p = argparse.ArgumentParser(
    description="Testing program for the red scare algorithm solutions"
)

parser = p.add_mutually_exclusive_group()

p.add_argument(
    "-d",
    "--debug",
    action="store_true",
    help="Prints debug information"
)

p.add_argument(
    "-f",
    "--file",
    type=parse_file_list,
    default=[],
    help="Runs a single test on a list of file"
)

p.add_argument(
    "-t",
    "--timeout",
    type=int,
    default=1,
    help="Sets the timeout timer on problems",
)

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


args = p.parse_args()

if args.file:
    run_tests(args.file)
else:
    run_tests()
if args.markdown:
    print_results_markdown(all)

if args.latex: 
    print_results_latex(all)

if args.json:
    print("Not implemented yet. Get fucked idiot")

