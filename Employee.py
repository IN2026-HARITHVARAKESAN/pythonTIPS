class Employee:
    def __init__(self, employee_id, name, hours, skills, availability="All"):
        self.id = employee_id
        self.name = name
        self.hours = float(hours)
        self.skills = [skill.strip().lower() for skill in skills]
        self.availability = availability

    def is_available(self, day):
        if self.availability == "All" or (
            isinstance(self.availability, str)
            and self.availability.lower() == "all"
        ):
            return True
        return day.strftime("%A").lower() in [
            item.strip().lower() for item in self.availability
        ]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "hours": self.hours,
            "skills": self.skills,
            "availability": self.availability,
        }
