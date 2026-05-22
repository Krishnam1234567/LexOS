"""
LexOS — SQLite Local Database Engine
Zero-dependency persistent storage using Python's built-in sqlite3.
Auto-creates tables and seeds demo data on first run.
"""
import os
import sqlite3
import json
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "lexos.db")


def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS settings (
        section TEXT PRIMARY KEY, data TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS contracts (
        id TEXT PRIMARY KEY, name TEXT, counterparty TEXT, type TEXT,
        value TEXT, endDate TEXT, status TEXT, risk TEXT, analysis TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS compliance_scores (
        category TEXT PRIMARY KEY, score INTEGER)""")

    c.execute("""CREATE TABLE IF NOT EXISTS compliance_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, due TEXT,
        priority TEXT, status TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS upcoming_filings (
        id INTEGER PRIMARY KEY AUTOINCREMENT, filing TEXT, framework TEXT,
        jurisdiction TEXT, deadline TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS regulatory_updates (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT,
        severity TEXT, action_text TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS audit_logs (
        id TEXT PRIMARY KEY, user TEXT, action TEXT, severity TEXT,
        resource TEXT, time TEXT, ip TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS agents (
        id INTEGER PRIMARY KEY, name TEXT, description TEXT, status TEXT,
        tasksCompleted INTEGER, lastAction TEXT, confidence INTEGER)""")

    c.execute("""CREATE TABLE IF NOT EXISTS approval_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT, agent TEXT, task TEXT,
        reasoning TEXT, confidence INTEGER, impact TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS recent_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT, agent TEXT, action TEXT,
        timestamp TEXT, type TEXT)""")

    conn.commit()

    # Seed only if empty
    if c.execute("SELECT COUNT(*) FROM agents").fetchone()[0] == 0:
        _seed(c)
        conn.commit()

    conn.close()


def _seed(c):
    # Settings
    for section, data in [
        ("org", {"name":"Nexus Technologies Inc.","domain":"nexustech.com","industry":"Technology / SaaS","size":"201-500 employees","hq":"San Francisco, CA, USA","gcName":"Sarah Chen","gcEmail":"sarah.chen@nexustech.com"}),
        ("notifications", {"deadline":True,"risk":True,"agent":True,"compliance":False,"report":True,"billing":True}),
        ("appearance", {"theme":"dark","sidebarCompact":False,"aiCopilotAutoOpen":True,"denseTableView":False,"animatedTransitions":True}),
    ]:
        c.execute("INSERT INTO settings VALUES (?,?)", (section, json.dumps(data)))

    # Contracts
    for row in [
        ("CTR-2024-001","Master SaaS Agreement","Acme Corporation","Sales Contract","$1,200,000","2027-06-15","active","medium",None),
        ("CTR-2024-002","Vendor NDA","NovaTech Solutions","NDA","$0","2025-11-22","active","low",None),
        ("CTR-2024-003","Commercial Lease Agreement","Summit Properties","Real Estate Lease","$450,000","2029-12-31","active","high",None),
        ("CTR-2024-004","Independent Contractor Agreement","John Doe Consulting","Service Agreement","$75,000","2024-12-31","expired","low",None),
        ("CTR-2024-005","DPA Addendum","CloudHost Inc.","Data Processing","$0","2027-06-15","active","high",None),
        ("CTR-2024-006","Enterprise License Agreement","AWS","Cloud Services","$2,400,000","2028-03-01","active","low",None),
        ("CTR-2024-007","IP Assignment Agreement","FounderTech Labs","IP Transfer","$500,000","2030-01-01","active","medium",None),
        ("CTR-2024-008","Marketing Services Agreement","BrandWave Agency","Marketing","$180,000","2026-12-31","active","low",None),
    ]:
        c.execute("INSERT INTO contracts VALUES (?,?,?,?,?,?,?,?,?)", row)

    # Compliance
    for row in [("GDPR",92),("SOC 2",95),("CCPA",88),("HIPAA",84),("ISO 27001",90),("DORA",78),("PCI DSS",91)]:
        c.execute("INSERT INTO compliance_scores VALUES (?,?)", row)

    for row in [
        ("Perform Q2 GDPR Data Mapping Review","2026-06-30","high","pending"),
        ("Review SOC 2 Trust Services Criteria","2026-07-15","medium","in_progress"),
        ("Update CCPA Privacy Notice Policy","2026-06-15","high","completed"),
        ("Conduct HIPAA Access Log Audit","2026-08-01","low","pending"),
        ("ISO 27001 ISMS Internal Audit","2026-09-01","high","pending"),
        ("DORA ICT Risk Assessment","2026-07-01","medium","pending"),
    ]:
        c.execute("INSERT INTO compliance_tasks (title,due,priority,status) VALUES (?,?,?,?)", row)

    for row in [
        ("Q2 CCPA Privacy Protection Filing","CCPA","California, USA","2026-07-15"),
        ("GDPR Data Processing Record Update","GDPR","European Union","2026-06-30"),
        ("Delaware Corporate Franchise Tax","Corporate Law","Delaware, USA","2026-09-01"),
        ("UK Companies House Annual Return","UK Companies Act","United Kingdom","2026-08-15"),
    ]:
        c.execute("INSERT INTO upcoming_filings (filing,framework,jurisdiction,deadline) VALUES (?,?,?,?)", row)

    for row in [
        ("EU AI Act Framework Approved","EU AI Act enforces new compliance guidelines on high-risk AI models starting August 2026. All enterprises deploying AI must register systems.","destructive","Review AI Systems Compliance"),
        ("FTC Non-Compete Ban Blocked","Federal court grants nationwide injunction on FTC non-compete ban. Existing policies remain valid.","warning","Track Litigation Updates"),
        ("Delaware Corp Law Amendments","New statutory updates permit board approvals via modern electronic workflows effective July 2026.","primary","Update Board Policies"),
    ]:
        c.execute("INSERT INTO regulatory_updates (title,description,severity,action_text) VALUES (?,?,?,?)", row)

    # Audit Logs
    for row in [
        ("LOG-001","sarah.chen@nexustech.com","User role upgraded: Observer -> Senior Legal Counsel for Marcus Okafor","medium","User Management","2026-05-22 14:32:11","192.168.1.112"),
        ("LOG-002","system-auth","SSO integration validated: Okta authentication successful for 18 users","low","API Gateway","2026-05-22 14:00:05","10.0.4.5"),
        ("LOG-003","sarah.chen@nexustech.com","Contract obligation deleted: OB-741 in Master Lease CTR-2024-003","high","Contract: CTR-2024-003","2026-05-22 13:45:00","192.168.1.112"),
        ("LOG-004","admin@nexustech.com","Prompt injection defense triggered: Blocked query matching threat pattern #9","high","AI Security Layer","2026-05-22 12:20:14","192.168.1.2"),
        ("LOG-005","marcus.okafor@nexustech.com","Downloaded compliance report: SOC 2 Type II Readiness Assessment","low","Compliance Module","2026-05-22 11:15:30","192.168.1.118"),
    ]:
        c.execute("INSERT INTO audit_logs VALUES (?,?,?,?,?,?,?)", row)

    # Agents
    for row in [
        (1,"Compliance Agent","Continuously monitors 12 regulatory frameworks (GDPR, CCPA, SOC 2, HIPAA, ISO 27001, PCI DSS, DORA) and generates compliance gap reports.","active",2341,"1 min ago",98),
        (2,"Contract Agent","Reviews incoming contracts using NLP clause extraction. Flags jurisdiction conflicts, risky indemnity clauses, and auto-renewal traps.","active",3127,"3 mins ago",97),
        (3,"Filing Agent","Automates legal filings across Delaware, California, UK Companies House, MAS Singapore, and EU jurisdictions.","active",812,"22 mins ago",95),
        (4,"Litigation Risk Agent","Predicts litigation probability using historical case data, clause patterns, and jurisdictional precedents. Monitors 28 active disputes.","active",634,"45 mins ago",93),
        (5,"Governance Agent","Manages board resolutions, director conflict-of-interest checks, equity cap-table events, and corporate governance workflows.","active",189,"1 hour ago",91),
        (6,"Global Expansion Agent","Analyses market-entry legal requirements, entity structuring options, and tax treaty implications for new geographies.","idle",97,"3 hours ago",89),
        (7,"IP & Trademark Agent","Manages IP portfolio across 7 jurisdictions. Tracks filing deadlines and conducts freedom-to-operate searches.","idle",43,"5 hours ago",90),
        (8,"Due Diligence Agent","Performs automated M&A and vendor due diligence. Scans corporate structure, UCC filings, sanctions lists.","idle",41,"8 hours ago",94),
    ]:
        c.execute("INSERT INTO agents VALUES (?,?,?,?,?,?,?)", row)

    # Approval Queue
    for row in [
        ("Contract Agent","Auto-renew AWS Enterprise License Agreement (CTR-2024-006) for 3-year term at locked pricing","Contract terms highly favourable. AWS guaranteed pricing through 2027. Usage at 93% capacity. Renewal strongly recommended.",98,"High"),
        ("Filing Agent","Submit CCPA Annual Privacy Report to California Attorney General (Deadline: Jul 1, 2026)","All documentation collected and verified. Consumer request logs reconciled. Compliance score 96%. Ready for submission.",96,"High"),
        ("Litigation Risk Agent","Initiate pre-trial settlement for Case #LIT-2026-007 (Jane Roe v. Acme Corp) — recommended: $85,000","Risk score elevated to 74/100. Estimated trial cost: $320K+ over 18 months. Settlement achieves 73% cost saving.",87,"High"),
        ("Governance Agent","Execute FY2026 Equity Grant — 450,000 stock options to 23 employees at $4.20 strike","Board pre-approved March 2026. 409A valuation completed May 1, 2026 at $4.20/share. All recipients verified.",99,"Medium"),
    ]:
        c.execute("INSERT INTO approval_queue (agent,task,reasoning,confidence,impact) VALUES (?,?,?,?,?)", row)

    # Activity
    for row in [
        ("Contract Agent","Identified 4 high-risk indemnity clauses in MSA-2026-114 (NovaTech Solutions). Flagged for legal review.","2 mins ago","alert"),
        ("Compliance Agent","Detected GDPR Article 25 amendment. 3 data-processing workflows flagged for policy update.","8 mins ago","alert"),
        ("Filing Agent","Successfully filed Q1 Delaware Annual Report. Reference: DEL-2026-AC-00341.","35 mins ago","success"),
        ("Litigation Risk Agent","Updated risk score for Case #LIT-2026-007 from Medium to High. Settlement window recommended.","1 hour ago","alert"),
        ("Contract Agent","Completed AI review of 47 vendor NDAs. 41 auto-approved, 6 escalated for human review.","2 hours ago","success"),
        ("Governance Agent","Board resolution for Q2 stock option grant prepared. 4/7 directors signed.","3 hours ago","info"),
    ]:
        c.execute("INSERT INTO recent_activity (agent,action,timestamp,type) VALUES (?,?,?,?)", row)


def add_audit_log(user: str, action: str, severity: str, resource: str):
    """Add an audit log entry. Called from route handlers."""
    conn = get_conn()
    log_id = f"LOG-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    conn.execute(
        "INSERT INTO audit_logs VALUES (?,?,?,?,?,?,?)",
        (log_id, user, action, severity, resource, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "192.168.1.1")
    )
    conn.commit()
    conn.close()


# Auto-initialize on import
init_db()
