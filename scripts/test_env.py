from env.environment import InboxEnv
from env.models import Email, Task
from datetime import datetime
import random

# Create sample emails
emails = [
    Email(
        id="1",
        subject="Test",
        body="This is a test email",
        sender="alice@example.com",
        received_at=datetime.now(),
        tasks=[Task(id="t1", description="Reply", priority=3)]
    ),
    Email(
        id="2",
        subject="Hello",
        body="Another test",
        sender="bob@example.com",
        received_at=datetime.now(),
        tasks=[Task(id="t2", description="Summarize", priority=2)]
    )
]

# ✅ Create environment FIRST
env = InboxEnv(emails)

# ✅ THEN reset
obs = env.reset()
print("Initial Observation:", obs)

done = False
step_count = 0

while not done:
    action = random.randint(0, 3)
    obs, reward, done, info = env.step(action)

    print(f"Step {step_count} | Action: {action}, Reward: {reward}, Done: {done}")
    step_count += 1

print("Test completed.")