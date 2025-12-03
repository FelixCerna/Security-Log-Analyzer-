def analyze_logs(log_entries):
    total = len(log_entries)

    failed = [e for e in log_entries if e["status"] == "FAIL"]

    failed_by_ip = {}
    for entry in failed:
        ip = entry["ip"]
        failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1

    return {
        "total_events": total,
        "total_failed": len(failed),
        "failed_by_ip": failed_by_ip
    }
