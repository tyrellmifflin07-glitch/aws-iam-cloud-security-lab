# apply_branding.py
# Purpose: Automatically apply MiffTech branding to the AWS lab dashboard.py
# Run from inside the aws-iam-cloud-security-lab folder:  python3 apply_branding.py

import os
import sys

FILE = "dashboard.py"

if not os.path.exists(FILE):
    print("[!] dashboard.py not found. Run this from inside aws-iam-cloud-security-lab.")
    sys.exit(1)

with open(FILE, "r") as f:
    content = f.read()

original = content
edits_applied = []

# ── EDIT 1: Page title ──
old = 'page_title="AWS IAM & Cloud Security Lab",'
new = 'page_title="MiffTech · AWS IAM & Cloud Security Lab",'
if old in content:
    content = content.replace(old, new)
    edits_applied.append("1. Page title branded")
elif new in content:
    edits_applied.append("1. Page title (already branded)")
else:
    print("[!] Edit 1 target not found — aborting, no changes made.")
    sys.exit(1)

# ── EDIT 2: Logo in sidebar ──
old = '''# Sidebar navigation
st.sidebar.title("🛡️ Lab Navigation")'''
new = '''# Sidebar navigation
import os as _os
if _os.path.exists("assets/logo.png"):
    st.sidebar.image("assets/logo.png", use_container_width=True)
st.sidebar.title("🛡️ Lab Navigation")'''
if old in content:
    content = content.replace(old, new)
    edits_applied.append("2. Logo added to sidebar")
elif 'st.sidebar.image("assets/logo.png"' in content:
    edits_applied.append("2. Logo (already present)")
else:
    print("[!] Edit 2 target not found — aborting, no changes made.")
    sys.exit(1)

# ── EDIT 3: Consultant line -> MiffTech ──
old = 'st.sidebar.markdown("IAM/GRC Consultant · CEH · CSM")'
new = 'st.sidebar.markdown("MiffTech Risk AI & Consulting · CEH · CSM")'
if old in content:
    content = content.replace(old, new)
    edits_applied.append("3. Sidebar brand line updated")
elif new in content:
    edits_applied.append("3. Sidebar brand line (already updated)")
else:
    print("[!] Edit 3 target not found — aborting, no changes made.")
    sys.exit(1)

# ── EDIT 4: Gold accent border ──
old = "border-right: 2px solid #00B4D8;"
new = "border-right: 3px solid #E8B830;"
if old in content:
    content = content.replace(old, new)
    edits_applied.append("4. Gold accent border applied")
elif new in content:
    edits_applied.append("4. Gold border (already applied)")
else:
    print("[!] Edit 4 target not found — aborting, no changes made.")
    sys.exit(1)

# ── EDIT 5: MiffTech footer ──
footer = '''

# ── MIFFTECH FOOTER ──
st.markdown("""
<div style="margin-top: 3rem; padding-top: 1rem; border-top: 2px solid #E8B830; color: #666; font-size: 0.85rem; text-align: center;">
    <strong>MiffTech Risk AI & Consulting</strong> · Tyrell Mifflin, CEH · CSM · CCSP (Expected 2026)<br>
    IAM Governance · GRC Engineering · AI Risk Advisory · New Castle, DE<br>
    <a href="https://iam-grc-assistant.streamlit.app">AI GRC Platform</a> ·
    <a href="https://github.com/tyrellmifflin07-glitch">GitHub</a> ·
    <a href="https://linkedin.com/in/tyrell-mifflin-ceh-csm-85a27583">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
'''
if "MIFFTECH FOOTER" not in content:
    content = content + footer
    edits_applied.append("5. MiffTech footer added")
else:
    edits_applied.append("5. Footer (already present)")

# ── Save a backup, write the new file, validate syntax ──
with open(FILE + ".backup", "w") as f:
    f.write(original)

with open(FILE, "w") as f:
    f.write(content)

# Syntax validation
import py_compile
try:
    py_compile.compile(FILE, doraise=True)
    print("\n===== MIFFTECH BRANDING APPLIED =====")
    for e in edits_applied:
        print(f"  [+] {e}")
    print(f"\n  [+] Syntax check: PASSED")
    print(f"  [+] Backup saved: {FILE}.backup")
    print("\nNext: streamlit run dashboard.py")
except py_compile.PyCompileError as err:
    # Restore the backup if something went wrong
    with open(FILE + ".backup") as f:
        restore = f.read()
    with open(FILE, "w") as f:
        f.write(restore)
    print("[!] Syntax check FAILED — original file restored automatically.")
    print(err)
    sys.exit(1)