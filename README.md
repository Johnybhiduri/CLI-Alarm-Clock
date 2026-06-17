# Alarm Clock CLI

A simple command-line Alarm Clock application built with Python.

## Features

- Add alarms
- List alarms
- Delete alarms
- Persist alarms using JSON
- Background alarm monitoring
- Object-oriented design using a single class

---

## Requirements

- Python 3.8+

---

## Run

```bash
python main.py
```

---

## Menu

```text
===== Alarm Clock =====

1. Add Alarm
2. List Alarms
3. Delete Alarm
4. Start Alarm Service
5. Exit
```

---

## Add Alarm

Enter time in 24-hour format.

Example:

```text
14:30
```

---

## List Alarms

Displays all alarms:

```text
ID: 1712345678 | Time: 14:30 | Status: Active
```

---

## Delete Alarm

Provide the alarm ID shown in the list.

Example:

```text
Enter alarm ID: 1712345678
```

---

## Data Storage

Alarms are stored locally in:

```text
alarms.json
```

Example:

```json
[
  {
    "id": 1712345678,
    "time": "14:30",
    "active": true
  }
]
```

---

## Design

The application uses a single class:

```python
AlarmClock
```

Responsibilities:

- Load alarms
- Save alarms
- Add alarms
- Delete alarms
- List alarms
- Check alarms
- Run CLI menu

This keeps the implementation simple, maintainable, and easy to extend.

---

## Future Improvements

- Recurring alarms
- Alarm labels
- Snooze functionality
- Sound notifications
- Multiple alarm schedules
- Unit tests