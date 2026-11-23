"""Define the employee model used by the scheduler."""

class Employee:
    """Represent an employee and their available work capacity."""

    def __init__(self, employee_id, name, hours, skills, availability="All"):
        """Create an employee with hours, skills, and available days."""
        self.id = employee_id
        self.name = name
        self.hours = float(hours)
        self.skills = [skill.strip().lower() for skill in skills]
        self.availability = availability

    def is_available(self, day):
        """Return whether the employee can work on the given day."""
        if self.availability == "All" or (
            isinstance(self.availability, str)
            and self.availability.lower() == "all"
        ):
            return True
        return day.strftime("%A").lower() in [
            item.strip().lower() for item in self.availability
        ]

    def to_dict(self):
        """Return the employee as a dictionary for JSON export."""
        return {
            "id": self.id,
            "name": self.name,
            "hours": self.hours,
            "skills": self.skills,
            "availability": self.availability,
        }
