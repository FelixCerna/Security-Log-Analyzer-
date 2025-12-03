class BruteForceDetector:
    def __init__(self, max_attempts=5):
        self.max_attempts = max_attempts

    def detect(self, log_entries):
        suspicious_ips = {}
        suspicious_users = {}

        ip_attempts = {}
        user_attempts = {}

        for entry in log_entries:
            if entry["status"] != "FAIL":
                continue

            ip = entry["ip"]
            user = entry["username"]

            ip_attempts[ip] = ip_attempts.get(ip, 0) + 1
            user_attempts[user] = user_attempts.get(user, 0) + 1

            if ip_attempts[ip] >= self.max_attempts:
                suspicious_ips[ip] = ip_attempts[ip]

            if user_attempts[user] >= self.max_attempts:
                suspicious_users[user] = user_attempts[user]

        return suspicious_ips, suspicious_users
