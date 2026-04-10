# 📬 Inbox Environment (RL)

A reinforcement learning-style environment where an AI agent processes emails, classifies them, extracts tasks, and prioritizes actions in a simulated workflow.

This project is designed to evaluate how well an agent can manage real-world inbox scenarios using structured decision-making.

---

## 🚀 Features

* 📧 Email processing simulation
* 🧠 Task extraction and prioritization
* 🏷️ Email classification (work / personal / ignore)
* 📊 Reward-based evaluation (RL-style grading)
* ⚙️ Gym-style environment (`step`, `reset`, `action_space`)
* 🧪 Ready-to-run testing and baseline scripts

---

## 📁 Project Structure

```
inbox_env/

├── env/
│   ├── __init__.py
│   ├── environment.py   # Gym-style RL environment
│   ├── models.py        # Pydantic data models (Email, Task)
│   ├── grader.py        # Scoring and reward logic
│   ├── tasks.py         # Task-related utilities
│
├── data/
│   ├── emails_easy.json
│   ├── emails_medium.json
│   ├── emails_hard.json
│
├── scripts/
│   ├── run_baseline.py  # Runs a simple agent
│   ├── test_env.py      # Test script for environment
│
├── requirements.txt
├── Dockerfile
├── openenv.yaml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd inbox_env
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate it:

* Windows:

```
venv\Scripts\activate
```

* Linux/Mac:

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Run Environment Test

```
python scripts/test_env.py
```

This will:

* Load sample emails
* Simulate random actions
* Print rewards and environment behavior

---

### 🔹 Run Baseline Agent

```
python scripts/run_baseline.py
```

This runs a simple agent over multiple steps/episodes and prints performance.

---

## 🧠 Environment Overview

### Actions

| Action | Description            |
| ------ | ---------------------- |
| 0      | Ignore email           |
| 1      | Classify as "work"     |
| 2      | Classify as "personal" |
| 3      | Complete task          |

---

### Observation Space

A simple numeric representation of the current email:

```
[task_count, first_task_priority]
```

---

### Reward System

The agent is evaluated based on:

* ✅ Correct email classification
* ✅ Accurate task extraction
* ✅ Proper task prioritization

Final reward is a combined score between **0 and 1**.

---

## 📊 Example Output

```
Email: Test, Tasks: 1
Action: 1, Reward: 1.0

Email: Hello, Tasks: 1
Action: 3, Reward: 0.66

Test completed.
```

---

## 🧪 Data

Sample datasets are included in:

```
data/
```

* `emails_easy.json`
* `emails_medium.json`
* `emails_hard.json`

These can be extended to create more complex scenarios.

---

## 🐳 Docker (Optional)

Build and run:

```
docker build -t inbox_env .
docker run -it inbox_env python scripts/test_env.py
```

---

## 🎯 Goal

To simulate a realistic inbox workflow where AI agents can:

* Understand email context
* Extract actionable tasks
* Make decisions efficiently
* Optimize behavior using reward signals

---

## 📌 Notes

* Designed for experimentation with RL agents
* Minimal and extensible architecture
* Easy to integrate with custom agents or models

---

## 👤 Author

Kishore Nath

```
```
