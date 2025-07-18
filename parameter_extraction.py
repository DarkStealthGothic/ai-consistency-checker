import re

def extract_parameters_rule_based(text):
    """
    Rule-based extraction using regex and keyword search.
    Returns a dict of parameters.
    """
    params = {}

    # Define regex patterns for each parameter (tweak as needed)
    patterns = {
        "Protocol Number": r"(Protocol Number|Protocol No\.?):?\s*([A-Za-z0-9\-\/]+)",
        "Protocol Title": r"(Protocol Title|Study Title):?\s*(.+)",
        "Protocol Version": r"(Protocol Version|Version):?\s*([A-Za-z0-9\.]+)",
        "Protocol Version Date": r"(Version Date|Dated):?\s*([0-9]{1,2}\s+\w+\s+[0-9]{4}|[0-9]{4}-[0-9]{2}-[0-9]{2})",
        "Investigational Product Name": r"(Investigational Product|Study Drug|Study Intervention):?\s*([A-Za-z0-9 \-]+)",
        "Number of Subjects": r"(Number of Subjects|Sample Size|Patients to be enrolled):?\s*([0-9]+)",
        "Study Disease": r"(Indication|Study Disease|Condition):?\s*([A-Za-z0-9 \-]+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            params[key] = match.groups()[-1].strip()
        else:
            params[key] = None

    return params

# Placeholder for AI extraction (to be implemented later)
def extract_parameters_ai(text):
    raise NotImplementedError("AI extraction not yet implemented.")

def extract_parameters(text, method="rule"):
    if method == "rule":
        return extract_parameters_rule_based(text)
    elif method == "ai":
        return extract_parameters_ai(text)
    else:
        raise ValueError("Unknown extraction method: " + method)

if __name__ == "__main__":
    # Simple test usage
    file_path = input("Enter path to text file: ")
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    params = extract_parameters(text, method="rule")
    print("\nExtracted Parameters:")
    for k, v in params.items():
        print(f"{k}: {v}")
