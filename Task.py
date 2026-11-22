class Task:
    def __init__(self, task_id, description, hours, deadline, skills):
        self.id = task_id
        self.description = description
        self.hours = float(hours)
        self.deadline = deadline
        self.skills = [skill.strip().lower() for skill in skills]
        self.status = "Pending"
        self.reason = ""

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "hours": self.hours,
            "deadline": self.deadline,
            "skills": self.skills,
            "status": self.status,
            "reason": self.reason,
        }
