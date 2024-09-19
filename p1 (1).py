import csv
from collections import defaultdict

class LogEvent:
    def __init__(self, timestamp, level, message, correlation_id):
        self.timestamp = timestamp
        self.level = level
        self.message = message
        self.correlation_id = correlation_id

    def __str__(self):
        return f"[{self.timestamp}] {self.level}: {self.message} (Correlation ID: {self.correlation_id})"

class LogCapturer:
    def __init__(self):
        self.log_events = []

    def capture_logs(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row) >= 4:
                    log_event = LogEvent(row[0], row[1], row[2], row[3])
                    self.log_events.append(log_event)

    def get_all_logs(self):
        return self.log_events

class EventCorrelation:
    def __init__(self, log_capturer):
        self.log_capturer = log_capturer

    def correlate_events(self):
        correlation_map = defaultdict(list)
        for event in self.log_capturer.get_all_logs():
            correlation_map[event.correlation_id].append(event)
        return correlation_map

def main():
    log_capturer = LogCapturer()
    log_capturer.capture_logs('logs.txt')  # Path to your log file

    event_correlation = EventCorrelation(log_capturer)
    correlated_events = event_correlation.correlate_events()

    # Displaying correlated events
    for correlation_id, events in correlated_events.items():
        print(f"Correlation ID: {correlation_id}")
        for event in events:
            print(event)
        print()

if __name__ == "__main__":
    main()
