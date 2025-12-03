from utils.file_reader import read_log_file
from analytics.log_analyzer import analyze_logs
from analytics.brute_force_detector import BruteForceDetector
import os
import csv

def save_report_csv(analysis, suspicious_ips, suspicious_users, path="reports/reporte.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Eventos generales
        writer.writerow(["TIPO", "IP/USUARIO", "INTENTOS"])
        for ip, count in analysis["failed_by_ip"].items():
            writer.writerow(["Fallo por IP", ip, count])
        
        # Separador
        writer.writerow([])
        writer.writerow(["----- DETECCIÓN DE FUERZA BRUTA -----"])
        writer.writerow(["TIPO", "IP/USUARIO", "INTENTOS"])
        
        # IPs sospechosas
        for ip, count in suspicious_ips.items():
            writer.writerow(["IP sospechosa", ip, count])
        
        # Usuarios sospechosos
        for user, count in suspicious_users.items():
            writer.writerow(["Usuario sospechoso", user, count])
    
    print(f"\nReporte CSV guardado en: {path}")

def main():
    log_path = "data/logs.csv"

    logs = read_log_file(log_path)
    print("Archivo leído correctamente.")
    print(f"Eventos totales: {len(logs)}")

    # Análisis general
    analysis = analyze_logs(logs)
    print("\n----- RESULTADOS GENERALES -----")
    print(f"Total de eventos: {analysis['total_events']}")
    print(f"Intentos fallidos: {analysis['total_failed']}")
    print("Fallos por IP:")
    for ip, count in analysis["failed_by_ip"].items():
        print(f"  {ip}: {count}")

    # Detección de fuerza bruta
    detector = BruteForceDetector(max_attempts=5)
    suspicious_ips, suspicious_users = detector.detect(logs)

    print("\n----- DETECCIÓN DE FUERZA BRUTA -----")
    print("IPs sospechosas:")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            print(f"  {ip} → {count} intentos")
    else:
        print("  Ninguna")

    print("\nUsuarios sospechosos:")
    if suspicious_users:
        for user, count in suspicious_users.items():
            print(f"  {user} → {count} intentos")
    else:
        print("  Ninguno")

    # Guardar reporte CSV
    save_report_csv(analysis, suspicious_ips, suspicious_users)

if __name__ == "__main__":
    main()
