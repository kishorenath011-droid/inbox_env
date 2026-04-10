# env/grader.py

class Grader:
    """
    Simple reward system for the environment.
    """

    @staticmethod
    def grade(task_completed: bool) -> float:
        """
        Return reward based on task completion.
        """
        return 1.0 if task_completed else -0.1