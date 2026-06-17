import json
import os
import time
from datetime import datetime


class AlarmClock:
    def __init__(self, file_name="alarms.json"):
        self.file_name = file_name
        self.alarms = []
        self.load_alarms()

    def load_alarms(self):
        """Load alarms from JSON file."""
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    self.alarms = json.load(file)
            except Exception:
                self.alarms = []
        else:
            self.save_alarms()

    def save_alarms(self):
        """Persist alarms to JSON file."""
        with open(self.file_name, "w") as file:
            json.dump(self.alarms, file, indent=4)

    def add_alarm(self, alarm_time):
        """
        Add a new alarm.

        Expected format: HH:MM (24-hour)
        Example: 14:30
        """
        try:
            datetime.strptime(alarm_time, "%H:%M")
        except ValueError:
            print("❌ Invalid time format. Use HH:MM")
            return

        alarm = {
            "id": int(time.time()),
            "time": alarm_time,
            "active": True
        }

        self.alarms.append(alarm)
        self.save_alarms()

        print(f"✅ Alarm added for {alarm_time}")

    def list_alarms(self):
        """Display all alarms."""
        if not self.alarms:
            print("No alarms found.")
            return

        print("\n=== Alarms ===")
        for alarm in self.alarms:
            status = "Active" if alarm["active"] else "Disabled"

            print(
                f"ID: {alarm['id']} | "
                f"Time: {alarm['time']} | "
                f"Status: {status}"
            )

    def delete_alarm(self, alarm_id):
        """Delete alarm by ID."""
        original_count = len(self.alarms)

        self.alarms = [
            alarm for alarm in self.alarms
            if alarm["id"] != alarm_id
        ]

        if len(self.alarms) < original_count:
            self.save_alarms()
            print("✅ Alarm deleted")
        else:
            print("❌ Alarm not found")

    def check_alarms(self):
        """Check whether any alarm should fire."""
        current_time = datetime.now().strftime("%H:%M")

        for alarm in self.alarms:
            if alarm["active"] and alarm["time"] == current_time:
                print("\n" + "=" * 40)
                print(f"⏰ ALARM! Time: {alarm['time']}")
                print("=" * 40)

                # Prevent repeated triggering
                alarm["active"] = False

        self.save_alarms()

    def run(self):
        """CLI menu."""
        while True:
            print("\n===== Alarm Clock =====")
            print("1. Add Alarm")
            print("2. List Alarms")
            print("3. Delete Alarm")
            print("4. Start Alarm Service")
            print("5. Exit")

            choice = input("Choose option: ").strip()

            if choice == "1":
                alarm_time = input(
                    "Enter time (HH:MM): "
                ).strip()
                self.add_alarm(alarm_time)

            elif choice == "2":
                self.list_alarms()

            elif choice == "3":
                try:
                    alarm_id = int(
                        input("Enter alarm ID: ")
                    )
                    self.delete_alarm(alarm_id)
                except ValueError:
                    print("Invalid ID")

            elif choice == "4":
                print("🚀 Alarm service started...")
                print("Press Ctrl+C to stop.")

                try:
                    while True:
                        self.check_alarms()
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\nAlarm service stopped.")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid option")


if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()