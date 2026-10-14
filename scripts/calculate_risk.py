import os

def run_risk_calculator():
    threats = [
        {"Asset": "Customer PII Database", "Threat": "SQL Injection Attack", "L": 3, "I": 3},
        {"Asset": "Payment Gateway API", "Threat": "Man-in-the-Middle Sniffing", "L": 2, "I": 3},
        {"Asset": "Source Code Repo", "Threat": "Unauthorized Code Leakage", "L": 2, "I": 2},
        {"Asset": "AWS Cloud Console", "Threat": "Credential Stuffing Admin Login", "L": 3, "I": 3},
        {"Asset": "Corporate Email", "Threat": "Spear Phishing Campaigns", "L": 3, "I": 2}
    ]
    
    csv_path = os.path.join('matrix', 'threat_vulnerability_matrix.csv')
    with open(csv_path, 'w') as f:
        f.write("Asset,Threat,Likelihood,Impact,Risk Score,Risk Level\n")
        for t in threats:
            score = t["L"] * t["I"]
            level = "High" if score >= 7 else ("Medium" if score >= 4 else "Low")
            f.write(f'"{t["Asset"]}","{t["Threat"]}",{t["L"]},{t["I"]},{score},{level}\n')
    print("[SUCCESS] Threat Vulnerability Matrix generated successfully!")

if __name__ == "__main__":
    run_risk_calculator()
