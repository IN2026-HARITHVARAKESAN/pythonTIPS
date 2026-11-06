def find_missing_values(data):
    """Find missing or empty values in each column."""
    missing = {}

    for column in data[0]:
        missing[column] = sum(
            1 for row in data
            if row.get(column) is None or row.get(column) == ""
        )

    return missing


def group_by_column(data, column):
    """Group records based on a column value."""
    groups = {}

    for row in data:
        value = row.get(column)
        groups.setdefault(value, []).append(row)

    return groups


def aggregate_column(data, column):
    """Calculate the total of numeric values in a column."""
    values = [
        float(row[column])
        for row in data
        if row.get(column) not in (None, "")
    ]

    return sum(values)


def find_duplicates(data):
    """Find duplicate records."""
    seen = set()
    duplicates = []

    for row in data:
        record = tuple(sorted(row.items()))

        if record in seen:
            duplicates.append(row)
        else:
            seen.add(record)

    return duplicates


def column_statistics(data, column):
    """Calculate basic statistics for a numeric column."""
    values = [
        float(row[column])
        for row in data
        if row.get(column) not in (None, "")
    ]

    if not values:
        return {}

    return {
        "count": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "average": sum(values) / len(values),
        "total": sum(values)
    }