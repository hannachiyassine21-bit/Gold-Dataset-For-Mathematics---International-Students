import os
import csv

print("=" * 50)
print("DATA QUALITY CHECK")
print("=" * 50)

# 1. Check CSV file
print("\n[1] CSV FILE")

with open('master_index.csv', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)

print("Rows found:", len(lines) - 1)

header = lines[0]
print("Columns:", header)

# Check empty rows
empty_rows = 0
for line in lines[1:]:
    if not any(line):
        empty_rows += 1

if empty_rows > 0:
    print(f"⚠️ Empty rows found: {empty_rows}")
else:
    print("✅ No empty rows")

# Check empty cells
empty_cells = 0
for line in lines[1:]:
    for cell in line:
        if cell == "" or cell.strip() == "":
            empty_cells += 1

if empty_cells > 0:
    print(f"⚠️ Empty cells found: {empty_cells}")
else:
    print("✅ No empty cells")

# Check duplicate IDs
ids = []
duplicates = []
for line in lines[1:]:
    ex_id = line[0]
    if ex_id in ids:
        duplicates.append(ex_id)
    else:
        ids.append(ex_id)

if duplicates:
    print(f"⚠️ Duplicate IDs found: {duplicates}")
else:
    print("✅ All IDs are unique")

# Check difficulties
difficulties = ['Easy', 'Intermediate', 'Hard']
invalid_diff = []
for line in lines[1:]:
    ex_id = line[0]
    diff = line[3]
    if diff not in difficulties:
        invalid_diff.append(ex_id)

if invalid_diff:
    print(f"⚠️ Invalid difficulties: {invalid_diff}")
else:
    print("✅ All difficulties are valid")

# Count by difficulty
easy = 0
intermediate = 0
hard = 0
for line in lines[1:]:
    diff = line[3]
    if diff == 'Easy':
        easy += 1
    elif diff == 'Intermediate':
        intermediate += 1
    elif diff == 'Hard':
        hard += 1

print(f"\n   Statistics:")
print(f"   - Easy: {easy}")
print(f"   - Intermediate: {intermediate}")
print(f"   - Hard: {hard}")

# 2. Check exercise files
print("\n[2] EXERCISE FILES")

folders = ['Sequences', 'Limits&Continuity', 'Differentiability', 'Integration&Primitives', 'DifferentialEquations']
prefixes = ['SEQ', 'LIM', 'DIF', 'INT', 'DE']

found_ex = 0
missing_ex = []

for folder, prefix in zip(folders, prefixes):
    for i in range(1, 10):
        ex_id = f"{prefix}{i:02d}"
        filepath = f"{folder}/{ex_id}_EX.md"
        
        if os.path.exists(filepath):
            found_ex += 1
        else:
            missing_ex.append(filepath)

print(f"Exercises found: {found_ex}/45")

if missing_ex:
    print("⚠️ Missing:")
    for m in missing_ex:
        print("   ", m)
else:
    print("✅ All exercises are present")

# 3. Check correction files
print("\n[3] CORRECTION FILES")

found_cor = 0
missing_cor = []

for folder, prefix in zip(folders, prefixes):
    for i in range(1, 10):
        ex_id = f"{prefix}{i:02d}"
        filepath = f"{folder}/{ex_id}_COR.md"
        
        if os.path.exists(filepath):
            found_cor += 1
        else:
            missing_cor.append(filepath)

print(f"Corrections found: {found_cor}/45")

if missing_cor:
    print("⚠️ Missing:")
    for m in missing_cor:
        print("   ", m)
else:
    print("✅ All corrections are present")

# 4. Final summary
print("\n" + "=" * 50)
print("FINAL SUMMARY")
print("=" * 50)

if found_ex == 45 and found_cor == 45 and not duplicates and empty_cells == 0:
    print("✅ EVERYTHING IS GOOD! Your dataset is clean.")
else:
    print("⚠️ Some issues found. Check the details above.")