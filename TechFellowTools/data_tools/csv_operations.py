import csv

def read_csv(file_path):
    """Read a CSV file and return its rows as dictionaries."""
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def write_csv(file_path, data, fieldnames):
    """Write dictionary records into a CSV file."""
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)  

def filter_rows(data, column, value):
    """Return rows where a column matches the given value."""
    return [
        row for row in data
        if row.get(column) == value
    ]

def sort_rows(data, column):
    """Sort rows based on the selected column."""
    return sorted(
        data,
        key=lambda row: row.get(column, "")
    )

def merge_csv_files(first_file, second_file, output_file):
    """Merge two CSV files into one CSV file."""
    first_data = read_csv(first_file)
    second_data = read_csv(second_file)

    if not first_data and not second_data:
        write_csv(output_file, [], [])
        return

    fieldnames = list(first_data[0].keys() if first_data else second_data[0].keys())

    merged_data = first_data + second_data

    write_csv(output_file, merged_data, fieldnames)