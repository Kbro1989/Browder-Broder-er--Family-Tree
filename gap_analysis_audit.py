import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("browder_broderers_lineage.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nodes = data.get("nodes", {})

# Chronological list of key nodes in the direct & early unproven chain
chain_keys = [
    ("john_browderer_1327", 1327, "John Browderer (King's Sergeant)"),
    ("john_browderer_1394", 1394, "John Browderer (Citizen of London)"),
    ("thome_browderer_1406", 1406, "Thome Browderer (Mettingham College)"),
    ("joh_browdere_1412", 1412, "Joh Browdere (Mettingham College)"),
    ("william_browderer_1419", 1419, "William Browderer (Baron Hungerford Will)"),
    ("richard_browderer_1466", 1466, "Richard Browderer (Coldharbour, Cornwall)"),
    ("gilliam_browderer_1521", 1521, "Gilliam Browderer (Tudor Subsidy Roll)"),
    ("thomas_browder_1575", 1575, "Thomas Browder (Saffron Walden)"),
    ("robert_browder_1604", 1604, "Robert Browder (Manchester Cathedral)"),
    ("george_browder_1624", 1624, "George Browder (Dublin Chancery)"),
    ("edmund_browder_I_1651", 1651, "Edmund Browder I (Surry Co., VA)"),
    ("john_browder_sr_1680", 1680, "John Browder, Sr. (Bristol Parish, VA)"),
    ("edmund_browder_sr_1716", 1716, "Edmund Browder, Sr. (Bristol Parish, VA)"),
    ("edmund_browder_jr_1734", 1734, "Edmund Browder, Jr. (NC Militia)"),
    ("darius_browder_1752", 1752, "Darius Browder (Roane Co., TN)"),
    ("joseph_browder_1789", 1789, "Joseph Browder (McMinn Co., TN)"),
    ("albert_browder_1825", 1825, "Albert Browder (Cherokee Nation / OK)"),
    ("george_thomas_browder_1851", 1851, "George Thomas Browder (Pittsburg Co., OK)"),
    ("albert_d_browder_1883", 1883, "Albert D. Browder (Indianola, OK)"),
    ("albert_edgar_browder_1915", 1915, "Albert Edgar Browder (Pittsburg, OK)"),
    ("paul_eugene_browder_1944", 1944, "Paul Eugene Browder (Indianola, OK)"),
    ("kevin_browder_I", 1970, "Kevin Browder I (Oklahoma)"),
    ("kevin_browder_II", 1995, "Kevin Browder II (POG Sovereign Stack)")
]

print("==========================================================================================")
print("                       BROWDER-BRODERERS LINEAGE GAP ANALYSIS AUDIT                        ")
print("==========================================================================================")
print(f"{'Step':<5} {'From Person (Year)':<35} {'To Person (Year)':<35} {'Gap':<8} {'Status'}")
print("-" * 95)

for i in range(len(chain_keys) - 1):
    k1, yr1, n1 = chain_keys[i]
    k2, yr2, n2 = chain_keys[i+1]
    gap = yr2 - yr1
    
    node1 = nodes.get(k1, {})
    node2 = nodes.get(k2, {})
    
    # Check if k1 is in k2's parents
    parents2 = node2.get("parents", [])
    if k1 in parents2 or k1.replace("_1327","").replace("_1394","") in [p.replace("_1327","") for p in parents2]:
        status = "PROVEN DIRECT"
    elif yr1 < 1604 or yr2 <= 1624:
        status = "UNPROVEN DISCRETE RECORD"
    else:
        status = "PROBABLE / PROVEN"
        
    print(f"{i+1:<5} {n1:<35} {n2:<35} {gap:<3} yrs   {status}")

print("=" * 95)

