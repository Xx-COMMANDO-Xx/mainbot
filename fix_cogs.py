#!/usr/bin/env python3
"""Fix all generated cog files that are missing the setup() function."""
import os
import re

COGS_DIR = os.path.join(os.path.dirname(__file__), "cogs")

def fix_setup_function(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if setup function already exists at module level (0 indentation)
    if re.search(r"^async def setup\(bot\):", content, re.MULTILINE):
        print(f"  ✓ Already has setup: {os.path.basename(filepath)}")
        return True

    # Extract the class name
    match = re.search(r"class (\w+)\(commands\.Cog", content)
    if not match:
        print(f"  ✗ No Cog class found in: {os.path.basename(filepath)}")
        return False

    class_name = match.group(1)

    # Remove any setup function that might be indented inside the class
    content = re.sub(r"\n\s+async def setup\(bot\):.*?(?=\n\S|\Z)", "", content, flags=re.DOTALL)

    # Add module-level setup
    content = content.rstrip() + f"\n\nasync def setup(bot):\n    await bot.add_cog({class_name}(bot))\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✓ Fixed: {os.path.basename(filepath)}")
    return True


def main():
    print("🔧 Scanning cog files for missing setup()...\n")
    fixed = 0
    failed = 0
    for filename in sorted(os.listdir(COGS_DIR)):
        if not filename.endswith(".py") or filename == "__init__.py":
            continue
        filepath = os.path.join(COGS_DIR, filename)
        if fix_setup_function(filepath):
            fixed += 1
        else:
            failed += 1

    print(f"\n✅ Fixed {fixed} files{' ❌ ' + str(failed) + ' failed' if failed else ''}")


if __name__ == "__main__":
    main()