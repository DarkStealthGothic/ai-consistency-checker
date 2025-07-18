import os
import csv
from datetime import datetime
from parameter_extraction import extract_parameters

REPORTS_FOLDER = "reports"

def load_text_from_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def compare_parameters_across_docs(folder_path):
    results = {}  # {filename: {param: value, ...}}
    all_params = set()

    for fname in os.listdir(folder_path):
        if fname.endswith(".txt"):
            fpath = os.path.join(folder_path, fname)
            text = load_text_from_file(fpath)
            params = extract_parameters(text, method="rule")
            results[fname] = params
            all_params.update(params.keys())

    if not results:
        print("No .txt files found in folder. Make sure you have files ending with .txt!")
        return {}, {}

    param_table = {param: {} for param in all_params}
    for fname, params in results.items():
        for param in all_params:
            param_table[param][fname] = params.get(param)

    inconsistencies = {}
    for param, values in param_table.items():
        found_values = set([v for v in values.values() if v])
        if len(found_values) > 1:
            inconsistencies[param] = values

    return param_table, inconsistencies

def print_comparison_table(param_table, inconsistencies):
    print("\nComparison Table:\n")
    if not param_table:
        print("No data to display.")
        return
    files = sorted(next(iter(param_table.values())).keys())
    print("{:25}".format("Parameter"), end="")
    for fname in files:
        print("{:20}".format(fname), end="")
    print()
    print("-" * (25 + 20 * len(files)))
    for param, values in param_table.items():
        print("{:25}".format(param), end="")
        for fname in files:
            val = values.get(fname, "")
            mark = " ❗" if param in inconsistencies and inconsistencies[param].get(fname) else ""
            print("{:20}".format((val or "") + mark), end="")
        print()

    if inconsistencies:
        print("\n❗ Inconsistencies found in:")
        for param in inconsistencies:
            print(f"- {param}")
    else:
        print("\nAll parameters are consistent across documents.")

def write_comparison_csv(param_table, output_csv="consistency_report.csv"):
    if not param_table:
        print("No data to write to CSV.")
        return
    files = sorted(next(iter(param_table.values())).keys())
    # Ensure reports folder exists
    if not os.path.exists(REPORTS_FOLDER):
        os.makedirs(REPORTS_FOLDER)
    output_path = os.path.join(REPORTS_FOLDER, output_csv)
    with open(output_path, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Parameter"] + files)
        for param, values in param_table.items():
            row = [param]
            for fname in files:
                row.append(values.get(fname, ""))
            writer.writerow(row)
    print(f"\nCSV report saved as: {output_path}")

if __name__ == "__main__":
    folder_path = "extracted_txts"
    print(f"Comparing parameters for all .txt files in '{folder_path}' ...")
    param_table, inconsistencies = compare_parameters_across_docs(folder_path)
    print_comparison_table(param_table, inconsistencies)
    if param_table:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"consistency_report_{timestamp}.csv"
        write_comparison_csv(param_table, output_csv=report_filename)
