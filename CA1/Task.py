"""Define the task model used by the scheduler."""

class Task:
    """Represent work that must be completed before a deadline."""

    def __init__(self, task_id, description, hours, deadline, skills):
        """Create a task with its hours, deadline, and required skills."""
        self.id = task_id
        self.description = description
        self.hours = float(hours)
        self.deadline = deadline
        self.skills = [skill.strip().lower() for skill in skills]
        self.status = "Pending"
        self.reason = ""

    def to_dict(self):
        """Return the task as a dictionary for JSON export."""
        return {
            "id": self.id,
            "description": self.description,
            "hours": self.hours,
            "deadline": self.deadline,
            "skills": self.skills,
            "status": self.status,
            "reason": self.reason,
        }
