import re
import csv
from collections import Counter, defaultdict

LOG_FILE = "sample.log"  # Input log file path
OUTPUT_FILE = "log_analysis_results.csv"  # Output CSV file path

FAILED_LOGIN_THRESHOLD = 5  # Threshold for failed login attempts to flag suspicious activity

def parse_log_file(log_file):
    """Parse the log file and return data in a structured format."""

    with open(log_file, 'r') as file:
        logs = file.readlines()
    
    parsed_logs = []
    for line in logs:
        match = re.match(
            r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*\] "(?P<method>GET|POST) (?P<endpoint>.+?) HTTP.*" (?P<status>\d+) .*',
            line,
        )
        if match:
            parsed_logs.append(match.groupdict())
    return parsed_logs

def count_requests_per_ip(parsed_logs):
    """Count the number of requests made by each IP address."""

    ip_counts = Counter(log['ip'] for log in parsed_logs)
    return ip_counts.most_common()

def find_most_frequent_endpoint(parsed_logs):
    """Find the most frequently accessed endpoint."""

    endpoint_counts = Counter(log['endpoint'] for log in parsed_logs)
    most_common = endpoint_counts.most_common(1)
    return most_common[0] if most_common else None

def detect_suspicious_activity(parsed_logs, threshold):
    """Detect IP addresses with failed login attempts exceeding the threshold."""

    failed_attempts = defaultdict(int)
    for log in parsed_logs:
        if log['status'] == '401':
            failed_attempts[log['ip']] += 1
    return {ip: count for ip, count in failed_attempts.items() if count > threshold}

def save_results_to_csv(ip_counts, most_frequent_endpoint, suspicious_activity, output_file):
    """Save analysis results to a CSV file."""

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write IP Request Counts
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_counts)
        writer.writerow([])

        # Write Most Frequent Endpoint
        writer.writerow(["Most Accessed Endpoint"])
        if most_frequent_endpoint:
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow([most_frequent_endpoint[0], most_frequent_endpoint[1]])
        writer.writerow([])

        # Write Suspicious Activity
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in suspicious_activity.items():
            writer.writerow([ip, count])

def main():
    """Main function that runs the log analysis."""
    # Parse log file
    parsed_logs = parse_log_file(LOG_FILE)

    # Analyze data
    ip_counts = count_requests_per_ip(parsed_logs)
    most_frequent_endpoint = find_most_frequent_endpoint(parsed_logs)
    suspicious_activity = detect_suspicious_activity(parsed_logs, FAILED_LOGIN_THRESHOLD)

    # Print results to terminal
    print("IP Address           Request Count")
    for ip, count in ip_counts:
        print(f"{ip:20} {count}")
    
    print("\nMost Frequently Accessed Endpoint:")
    if most_frequent_endpoint:
        print(f"{most_frequent_endpoint[0]} (Accessed {most_frequent_endpoint[1]} times)")

    print("\nSuspicious Activity Detected:")
    if suspicious_activity:
        print("IP Address           Failed Login Attempts")
        for ip, count in suspicious_activity.items():
            print(f"{ip:20} {count}")
    else:
        print("No suspicious activity detected.")

    # Save results to CSV
    save_results_to_csv(ip_counts, most_frequent_endpoint, suspicious_activity, OUTPUT_FILE)
    print(f"\nResults saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
