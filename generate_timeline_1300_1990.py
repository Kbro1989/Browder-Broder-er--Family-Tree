import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "c:/Users/krist/Desktop/Family-Tree-Research"
json_model = os.path.join(workspace_dir, "browder_broderers_lineage.json")
paper_file = os.path.join(workspace_dir, "john_mark_browder_origins_paper.txt")

# Master list of chronologically ordered events from 1300 to 1990
timeline_events = [
    {
        "year": 1327,
        "era": "14th Century (1300-1399)",
        "event_title": "Flemish Weavers Invited to England & John Browderer Earliest Record",
        "location": "London & St. Hilary Parish, Cornwall",
        "persons_involved": ["John Browderer", "Roger Trewynnarde", "Sir Walter Sancre", "King Edward III"],
        "source": "St. Hilary Parish Website, J.M. Browder Paper, Llewellyn (1936)",
        "details": "King Edward III encourages Flemish weavers to settle in England. John Browderer (King's Sergeant at Arms) involved in St. Hilary Parish incident; beheaded priest Sir Walter Sancre."
    },
    {
        "year": 1348,
        "era": "14th Century (1300-1399)",
        "event_title": "The Black Death Sweeps London Weavers",
        "location": "London, England",
        "persons_involved": ["Flemish Weavers Community"],
        "source": "Worshipful Company of Weavers History",
        "details": "Black Plague devastating London population. Weavers quarter heavily affected; guild structures survive under Crown protection."
    },
    {
        "year": 1394,
        "era": "14th Century (1300-1399)",
        "event_title": "John Browderer Documented as Citizen of London",
        "location": "London, England",
        "persons_involved": ["John Browderer"],
        "source": "Entries in Papal Registers (Papal Letters Vol. IV p. 488; Lateran Regesta Vol. XXXIV)",
        "details": "Notation on 4 Kal. May (May 4, 1394) recording 'John Browderer, citizen of London'. Earliest recorded usage of Browderer as a formal surname."
    },
    {
        "year": 1406,
        "era": "15th Century (1400-1499)",
        "event_title": "Thome Browderer Recorded in Suffolk Accounts",
        "location": "Mettingham College, Suffolk, England",
        "persons_involved": ["Thome Browderer"],
        "source": "Ancient Accounts of Mettingham College, Suffolk (Rev. C.R. Manning)",
        "details": "Mettingham College accounts for 1406-07 record payment to Thome Browderer."
    },
    {
        "year": 1412,
        "era": "15th Century (1400-1499)",
        "event_title": "Joh Browdere Recorded in Mettingham Accounts (Dropping 'r')",
        "location": "Suffolk, England",
        "persons_involved": ["Joh Browdere"],
        "source": "Mettingham College Accounts, J.M. Browder Paper",
        "details": "Record for 1412-13 listing 'Joh Browdere'. Earliest recorded spelling variant dropping the final 'r'."
    },
    {
        "year": 1439,
        "era": "15th Century (1400-1499)",
        "event_title": "William Browderer Recorded in Yorkshire Accounts for London Clothing Purchase",
        "location": "East Riding, Yorkshire / London",
        "persons_involved": ["William Browderer"],
        "source": "Transactions of the East Riding Antiquarian Society (Vol 3, p. 99)",
        "details": "Payment recorded for 1439-40: 'And paid to William Browderer for the expense incurred by him at London for the purchase of said clothing'."
    },
    {
        "year": 1459,
        "era": "15th Century (1400-1499)",
        "event_title": "Baron Robert Hungerford Bequeaths Will Legacy to William Browderer",
        "location": "London / Wiltshire, England",
        "persons_involved": ["William Browderer", "Baron Robert Hungerford", "Sir Edmund Hungerford"],
        "source": "Last Will and Testament of Sir Robert Hungerford (2nd Baron Hungerford, April 22, 1459)",
        "details": "Will executed April 22, 1459 bequeaths 'To William Browderer 53s, 4d'. Proves high-status association with nobility."
    },
    {
        "year": 1466,
        "era": "15th Century (1400-1499)",
        "event_title": "Richard Browderer at Coldharbour, Cornwall",
        "location": "Coldharbour, Cornwall, England",
        "persons_involved": ["Richard Browderer"],
        "source": "Cornwall Manorial & Port Records (1502 record)",
        "details": "Richard Browderer (b. c. 1466) recorded at Coldharbour port in 1502."
    },
    {
        "year": 1497,
        "era": "15th Century (1400-1499)",
        "event_title": "Pact Between Native & Alien Weavers Guilds",
        "location": "London, England",
        "persons_involved": ["Flemish & Native Weavers Guilds"],
        "source": "Worshipful Company of Weavers History",
        "details": "Pact signed absorbing alien Flemish weavers into London Weavers Guild, ending 170 years of trade friction."
    },
    {
        "year": 1517,
        "era": "16th Century (1500-1599)",
        "event_title": "Evil May Day Riots Targeting Foreign Weavers",
        "location": "London, England",
        "persons_involved": ["Foreign Weavers Community"],
        "source": "Tudor London History",
        "details": "Apprentices and journeymen riot against alien craft competitors in London."
    },
    {
        "year": 1541,
        "era": "16th Century (1500-1599)",
        "event_title": "Gilliam [William] Browderer Assessed in Tudor Subsidy Roll",
        "location": "St. Peter's Somerset Parish, Queenhithe Ward, London",
        "persons_involved": ["Gilliam Browderer"],
        "source": "Tudor Subsidy Roll 1541 (London Record Society Vol 29, p. 102; BHO)",
        "details": "Listed under 'Strangers in Saynt Peters Somersettes Parysshe': 'Gyllam Browderer (£250) £12 s10'. Shows substantial wealth."
    },
    {
        "year": 1561,
        "era": "16th Century (1500-1599)",
        "event_title": "Royal Charter Granted to Worshipful Company of Broderers",
        "location": "London (36 Gutter Lane, Cheapside)",
        "persons_involved": ["Queen Elizabeth I", "Broderers Liverymen"],
        "source": "Worshipful Company of Broderers Official History",
        "details": "Queen Elizabeth I grants Royal Charter to Broderers Company (Coat of Arms granted 1558, motto: 'Omnia desuper')."
    },
    {
        "year": 1575,
        "era": "16th Century (1500-1599)",
        "event_title": "Thomas Browder Baptized at Saffron Walden (First Contracted Surname)",
        "location": "Saffron Walden, St. Mary The Virgin Parish, Essex",
        "persons_involved": ["Thomas Browder", "Katherine Browder"],
        "source": "Saffron Walden Parish Register (Nov 25, 1575), J.M. Browder Paper",
        "details": "Baptism on Nov 25, 1575 of Thomas Browder, son of Katherine Browder. Earliest recorded baptism with contracted 'Browder' spelling."
    },
    {
        "year": 1601,
        "era": "17th Century (1600-1699)",
        "event_title": "Marye Hulme Christened at Manchester Cathedral",
        "location": "Manchester Cathedral, Lancashire",
        "persons_involved": ["Marye Hulme", "Adam Hulme"],
        "source": "Manchester Cathedral Registers (LPRS Vol 31, Roll 745)",
        "details": "Christening on Feb 4, 1601 (baptized June 17, 1609) of Marye Hulme, daughter of Adam Hulme."
    },
    {
        "year": 1606,
        "era": "17th Century (1600-1699)",
        "event_title": "Master John Parr Serves as Master Broderer",
        "location": "London, Broderers Hall",
        "persons_involved": ["John Parr", "King James I"],
        "source": "Broderers Company History / 20 Questions",
        "details": "Master John Parr serves as Master of the Broderers Company; royal embroiderer to King James I."
    },
    {
        "year": 1610,
        "era": "17th Century (1600-1699)",
        "event_title": "Alphonse Browder Baptized in Warwickshire",
        "location": "Stoke Parish, Warwickshire, England",
        "persons_involved": ["Alphonse Browder", "Thomas Browder"],
        "source": "Stoke Parish Registers, J.M. Browder Paper",
        "details": "Baptism in 1610 of Alphonse Browder, son of Thomas Browder."
    },
    {
        "year": 1611,
        "era": "17th Century (1600-1699)",
        "event_title": "Broderers Company Precept for Ulster Plantation Allotment",
        "location": "London / Ulster, Ireland",
        "persons_involved": ["Broderers Company", "Irish Society", "Lord Mayor of London"],
        "source": "Gutenberg #20990 (London and the Kingdom Vol 3, p. 40, Jan 31, 1611)",
        "details": "Precept issued 31 Jan 1611 requiring Broderers Company to signify willingness to accept Ulster Plantation allotment."
    },
    {
        "year": 1623,
        "era": "17th Century (1600-1699)",
        "event_title": "Marriage of Robert Browder & Marye Hulme at Manchester Cathedral",
        "location": "Manchester Cathedral, Lancashire",
        "persons_involved": ["Robert Browder", "Marye Hulme"],
        "source": "Manchester Cathedral Registers (LPRS Vol 31, Dec 26, 1623)",
        "details": "Marriage on Dec 26, 1623 between Robert Browder (c. 1604) and Marye Hulme (b. 1601). First recorded Browder entry in Lancashire."
    },
    {
        "year": 1628,
        "era": "17th Century (1600-1699)",
        "event_title": "Master Edmund Harrison Appointed King's Embroiderer",
        "location": "London, Broderers Hall",
        "persons_involved": ["Edmund Harrison", "King Charles I"],
        "source": "Broderers Company History / 20 Questions",
        "details": "Edmund Harrison appointed King's Embroiderer to Charles I; served as Master of Broderers Company in 1628, 1638, and 1648."
    },
    {
        "year": 1634,
        "era": "17th Century (1600-1699)",
        "event_title": "Baptisms of Thomas Browder (Norfolk) & Katherine Browder (London)",
        "location": "Brockdish, Norfolk & St. Giles Cripplegate, London",
        "persons_involved": ["Thomas Browder", "William Browder", "Katherine Browder", "Matthew Browder"],
        "source": "Brockdish Registers & St. Giles Cripplegate Registers",
        "details": "Feb 22, 1634 baptism of Thomas Browder (son of William) at Brockdish, Norfolk; Oct 26, 1634 baptism of Katherine Browder (daughter of Matthew) at St. Giles Cripplegate, London."
    },
    {
        "year": 1642,
        "era": "17th Century (1600-1699)",
        "event_title": "George Browder Documented in Dublin Chancery Court Suit",
        "location": "Dublin, Ireland",
        "persons_involved": ["George Browder"],
        "source": "Dublin Chancery Court Records, J.M. Browder Blog (Feb 2023)",
        "details": "Lawsuit in Dublin Chancery Court naming George Browder (b. c. 1624). Proves Browder family presence in Ireland prior to 1650."
    },
    {
        "year": 1664,
        "era": "17th Century (1600-1699)",
        "event_title": "Thomas Browder Assessed in Tipperary Hearth Money Roll",
        "location": "Ballynoran, Shunraghan Parish, Baronies of Iffa & Offa, Co. Tipperary, Ireland",
        "persons_involved": ["Thomas Browder"],
        "source": "1664 Hearth Money Rolls (Burke History of Clonmel, Appendix)",
        "details": "Thomas Browder (b. c. 1624) assessed for 1 hearth in Ballynoran, Tipperary. Confirms Browder residency in Ireland."
    },
    {
        "year": 1674,
        "era": "17th Century (1600-1699)",
        "event_title": "John Broadar [Browder] Headright Land Grant on Elizabeth River, VA",
        "location": "Lower Norfolk County, Virginia",
        "persons_involved": ["John Broadar", "William Havercomb", "James Jopling", "John Porter Sr.", "Isaac Hocker"],
        "source": "Virginia Land Patents Book 6, p. 526 (Sept 23, 1674)",
        "details": "William Havercomb granted 950 acres for transporting 18 persons, including John Broadar [Browder]. Land situated on South side of Eastern Branch of Elizabeth River."
    },
    {
        "year": 1682,
        "era": "17th Century (1600-1699)",
        "event_title": "Edmund Browder I Documented in Surry County VA Court Suit",
        "location": "Surry County, Virginia",
        "persons_involved": ["Edmund Browder I", "Sheriff Robert Bolling"],
        "source": "Surry County Orders, Deeds, Wills (1682, 1695)",
        "details": "Edmund Browder I (b. c. 1651) involved in court suit regarding serge suits and French fall shoes. Merchant merchant dealing in imported English cloth."
    },
    {
        "year": 1701,
        "era": "18th Century (1700-1799)",
        "event_title": "John Browder Headright Grant near Chowan / Albemarle, NC",
        "location": "Chowan County / Albemarle Sound, North Carolina",
        "persons_involved": ["John Browder Sr."],
        "source": "North Carolina Land Grants (Sides-Dye, p. 5)",
        "details": "John Browder receives headright land grant in border region between Virginia and North Carolina."
    },
    {
        "year": 1715,
        "era": "18th Century (1700-1799)",
        "event_title": "Marriage of John Browder Sr. & Elizabeth Jones",
        "location": "Prince George County, Virginia",
        "persons_involved": ["John Browder Sr.", "Elizabeth Jones", "Lt. Arthur Jones", "Susanna King"],
        "source": "Prince George County Deed Books, J.M. Browder Paper",
        "details": "John Browder Sr. marries Elizabeth Jones, daughter of Lt. Arthur Jones and Susanna King."
    },
    {
        "year": 1722,
        "era": "18th Century (1700-1799)",
        "event_title": "George Andrew Browder 264-Acre Purchase on Gravelly Run",
        "location": "Prince George County, Virginia",
        "persons_involved": ["George Andrew Browder", "Edmund Browder I", "John Browder Sr.", "Edmund W. Browder"],
        "source": "Prince George County Deed Book III (June 22, 1722)",
        "details": "George Andrew Browder purchases 264 acres on both sides of Gravelly Run, adjoining lands of Edmund I, John Sr., and Edmund W. Browder."
    },
    {
        "year": 1739,
        "era": "18th Century (1700-1799)",
        "event_title": "Will of Edmund Browder I Probated in Prince George County",
        "location": "Prince George County, Virginia",
        "persons_involved": ["Edmund Browder I", "Elizabeth Parsons", "John Browder Sr.", "Edmund W. Browder", "George Andrew Browder"],
        "source": "Prince George County Will Book (1738/39)",
        "details": "Edmund Browder I dies at ~88 years of age. Will probated in Prince George County, establishing the Tidewater Virginia patriarch line."
    },
    {
        "year": 1759,
        "era": "18th Century (1700-1799)",
        "event_title": "Virginia Act of Assembly Concerning Browder's Island Appomattox Bridge",
        "location": "Browder's Island, Appomattox River, Chesterfield County, VA",
        "persons_involved": ["Edmund W. Browder", "Virginia House of Burgesses"],
        "source": "Hening's Statutes at Large / 1759 Act of Assembly",
        "details": "Act of Assembly passed regarding bridge across Appomattox River at Browder's Island (site of old Fort Henry). Edmund W. Browder later dies impoverished in 1771."
    },
    {
        "year": 1776,
        "era": "18th Century (1700-1799)",
        "event_title": "Browder Revolutionary War Mobilization",
        "location": "Dinwiddie & Prince George Counties, Virginia",
        "persons_involved": ["Captain Isham Browder", "Lt. Joseph Browder", "Jesse Browder", "Charles Browder"],
        "source": "Virginia Revolutionary War Pension Files & Sworn Depositions",
        "details": "Capt. Isham Browder, Lt. Joseph Browder, Jesse Browder, and Charles Browder enlist in Continental Army / Virginia Militia."
    },
    {
        "year": 1780,
        "era": "18th Century (1700-1799)",
        "event_title": "Sworn Testimony of Peter Eppes Regarding Fallen Sons Jesse & Charles",
        "location": "Dinwiddie County, Virginia",
        "persons_involved": ["Peter Eppes", "Jesse Browder", "Charles Browder", "William Browder Sr."],
        "source": "Sworn Deposition of Peter Eppes, J.M. Browder Research",
        "details": "Peter Eppes provides sworn court testimony confirming that Jesse and Charles Browder (sons of William Sr. & Margaret) died in Revolutionary War service."
    },
    {
        "year": 1820,
        "era": "19th Century (1800-1899)",
        "event_title": "Browder Migration to McMinn County, Tennessee",
        "location": "McMinn County, Tennessee (Pond Creek)",
        "persons_involved": ["Darius Browder", "Jesse Browder", "Charles Browder", "Lt. Joseph Browder"],
        "source": "McMinn County Historical Society Wills & Deeds",
        "details": "Browder family moves from North Carolina and Virginia to settle in McMinn County, TN, acquiring extensive farming and milling lands."
    },
    {
        "year": 1861,
        "era": "19th Century (1800-1899)",
        "event_title": "Civil War Service of Tennessee & Virginia Browders",
        "location": "Tennessee & Virginia",
        "persons_involved": ["Albert Browder", "George Thomas Browder", "Joseph Browder (b. 1789)"],
        "source": "Civil War Confederate & Union Service Records",
        "details": "Browder family members serve in Tennessee and Virginia regiments during the American Civil War."
    },
    {
        "year": 1890,
        "era": "19th Century (1800-1899)",
        "event_title": "Albert Edgar Browder Born in Tennessee",
        "location": "McMinn County, Tennessee",
        "persons_involved": ["Albert Edgar Browder", "George Thomas Browder", "Albert D. Browder"],
        "source": "Tennessee Census & Cemetery Records",
        "details": "Albert Edgar Browder (1890–1965) born into McMinn County farming lineage."
    },
    {
        "year": 1920,
        "era": "20th Century (1900-1990)",
        "event_title": "Paul Eugene Browder Born in Tennessee",
        "location": "McMinn County, Tennessee",
        "persons_involved": ["Paul Eugene Browder", "Albert Edgar Browder"],
        "source": "Tennessee Vital Records / Social Security Death Index",
        "details": "Paul Eugene Browder (1920–1995) born; serves in U.S. Armed Forces during World War II."
    },
    {
        "year": 1955,
        "era": "20th Century (1900-1990)",
        "event_title": "Herman Edward Browder Compiles Family Research & Papers",
        "location": "Texas & Tennessee",
        "persons_involved": ["Herman Edward Browder", "Frank Browder", "Esther Browder", "John Mark Browder"],
        "source": "John Mark Browder Origins Paper (p. 13, 33)",
        "details": "Herman Edward Browder compiles extensive historical notes asserting Flemish/Germanic occupational origin of Browder surname; papers inherited by grand-nephew John Mark Browder."
    },
    {
        "year": 1985,
        "era": "20th Century (1900-1990)",
        "event_title": "Modern Lineage Documentation by Kevin Browder I",
        "location": "United States",
        "persons_involved": ["Kevin Browder I", "Kevin Browder II"],
        "source": "Family Tree Research Corpus / Modern Generation",
        "details": "Contemporary lineage link connecting 20th-century Browder family directly back to 1327 London/Flemish Broderers roots."
    }
]

print(f"=== GENERATING TIMELINED EVENTS MATRIX (1300-1990) WITH {len(timeline_events)} KEY MILESTONES ===")

# Save JSON matrix
json_out = os.path.join(workspace_dir, "TIMELINED_EVENTS_1300_1990_MATRIX.json")
with open(json_out, "w", encoding="utf-8") as jout:
    json.dump(timeline_events, jout, indent=2, ensure_ascii=False)

# Build Markdown Report
md_out = os.path.join(workspace_dir, "TIMELINED_EVENTS_1300_1990_MATRIX.md")
with open(md_out, "w", encoding="utf-8") as mout:
    mout.write("# ⏳ TIMELINED EVENTS MATRIX (1300 – 1990)\n\n")
    mout.write("Comprehensive chronological cross-reference matrix of all primary evidence, parish registers, land grants, wills, battles, and person milestones across **690 years (1300–1990)**.\n\n")
    
    current_era = ""
    for ev in timeline_events:
        if ev["era"] != current_era:
            current_era = ev["era"]
            mout.write(f"\n---\n\n## 📅 {current_era}\n\n")
            
        persons_str = ", ".join(ev["persons_involved"])
        mout.write(f"### 📍 **{ev['year']}** — {ev['event_title']}\n")
        mout.write(f"• **Location:** `{ev['location']}`  \n")
        mout.write(f"• **Persons Involved:** *{persons_str}*  \n")
        mout.write(f"• **Primary Source:** `{ev['source']}`  \n")
        mout.write(f"• **Historical Details:** {ev['details']}  \n\n")

print(f"✓ Timelined matrix saved to '{json_out}' and '{md_out}'!")

