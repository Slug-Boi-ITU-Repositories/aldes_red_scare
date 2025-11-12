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

    output = [header, separator]

    for test, outputs in results_by_test.items():
        row = f"| {test} | " + " | ".join(outputs.get(problem, "") for problem in solutions) + " |"
        output.append(row)

    if args.markdown != "stdout":
        with open(args.markdown, "w") as f:
            f.write("\n".join(output))
    else:
        print("\n".join(output))

def print_results_latex(results_by_test):
    col_format = "|l|" + "c|" * len(solutions)

    output = [
        "\\begin{table}[h!]", 
        "\\centering", 
        f"\\begin{{tabular}}{{{col_format}}}", 
        "\\hline"
    ]

    header = "Test File & " + " & ".join(solutions) + " \\\\"
    output.extend([header, "\\hline"])

    for test, outputs in results_by_test.items():
        row_values = " & ".join(outputs.get(problem, "") for problem in solutions)
        output.append(f"{test} & {row_values} \\\\")
    output.append("\\hline")

    output.extend([
        "\\end{tabular}", 
        "\\caption{Test results for all problem solutions}", 
        "\\label{tab:test_results}", 
        "\\end{table}"
    ])

    if args.latex != "stdout":
        with open(args.latex, "w") as f:
            f.write("\n".join(output))
    else:
        print("\n".join(output))

def print_results_json(results_by_test):
    output = json.dumps(results_by_test)
    if args.json != "stdout":
        with open(args.json, "w") as f:
            f.write(output)
    else:
        print(output)


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

p.add_argument(
    "-m",
    "--markdown",
    nargs="?",
    const='stdout',
    help="Prints the output as markdown"
)

p.add_argument(
    "-l",
    "--latex",
    nargs='?',
    const='stdout',
    help="Prints the output as a latex table"
)

p.add_argument(
    "-j",
    "--json",
    nargs='?',
    const="stdout",
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
    print_results_json(all)
