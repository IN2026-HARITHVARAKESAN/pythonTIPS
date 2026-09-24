"""This file contains date_analytics() which takes a list of dates in the format 'YYYY-MM-DD' and returns a dictionary containing the earliest date, latest date, and a sorted list of all unique dates."""

def date_analytics(dates: list[str]) -> dict:
    """Takes a list of dates in the format 'YYYY-MM-DD' and returns a dictionary containing the earliest date, latest date, and a sorted list of all unique dates."""
    unique_dates = sorted(set(dates))
    earliest_date = unique_dates[0]
    latest_date = unique_dates[-1]
    return {
        "earliest_date": earliest_date,
        "latest_date": latest_date,
        "unique_dates": unique_dates
    }  

if __name__ == "__main__":
    given_input = input("enter dates in the format 'YYYY-MM-DD' separated by spaces: ")
    dates = given_input.split()
    analytics = date_analytics(dates)
    print(f"The earliest date is {analytics['earliest_date']}")
    print(f"The latest date is {analytics['latest_date']}")
    print(f"The sorted list of unique dates is {analytics['unique_dates']}")