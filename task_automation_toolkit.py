"""
CodeAlpha_TaskAutomationToolkit
--------------------------------
A 3-in-1 Python Automation Toolkit (covers all 3 suggested ideas in one project,
instead of picking just one — makes it stand out).

Tools included:
1. File Organizer  -> Moves files of a chosen extension (e.g. .jpg) into a
                       new destination folder automatically.
2. Email Extractor -> Scans a .txt file, extracts all valid email addresses
                       using regex, and saves them to a new file.
3. Webpage Title Scraper -> Fetches a webpage and extracts its <title> tag.

Key Concepts Used: os, shutil, re, requests, file handling
Author: Aryan
"""

import os
import re
import shutil

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


def show_banner():
    print("=" * 55)
    print("        🤖  PYTHON TASK AUTOMATION TOOLKIT  🤖")
    print("=" * 55)


# ---------------- TOOL 1: File Organizer ----------------
def organize_files():
    print("\n--- 📂 File Organizer ---")
    source = input("Enter source folder path: ").strip()
    if not os.path.isdir(source):
        print("❌ That folder doesn't exist.")
        return

    ext = input("Enter file extension to move (e.g. jpg, pdf, txt): ").strip().lower()
    ext = ext if ext.startswith(".") else "." + ext

    dest = input("Enter destination folder name (will be created if missing): ").strip()
    dest_path = os.path.join(source, dest)
    os.makedirs(dest_path, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(source):
        full_path = os.path.join(source, filename)
        if os.path.isfile(full_path) and filename.lower().endswith(ext):
            shutil.move(full_path, os.path.join(dest_path, filename))
            moved_count += 1
            print(f"   moved: {filename}")

    if moved_count == 0:
        print(f"⚠️ No '{ext}' files found in {source}.")
    else:
        print(f"✅ Moved {moved_count} file(s) to '{dest_path}'.")


# ---------------- TOOL 2: Email Extractor ----------------
def extract_emails():
    print("\n--- 📧 Email Extractor ---")
    filepath = input("Enter path of .txt file to scan: ").strip()

    if not os.path.isfile(filepath):
        print("❌ File not found.")
        return

    with open(filepath, "r", errors="ignore") as f:
        content = f.read()

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = sorted(set(re.findall(pattern, content)))

    if not emails:
        print("⚠️ No email addresses found.")
        return

    output_file = "extracted_emails.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(emails))

    print(f"✅ Found {len(emails)} unique email(s). Saved to '{output_file}'.")
    for e in emails:
        print(f"   {e}")


# ---------------- TOOL 3: Webpage Title Scraper ----------------
def scrape_title():
    print("\n--- 🌐 Webpage Title Scraper ---")
    if not REQUESTS_AVAILABLE:
        print("❌ 'requests' library not installed. Run: pip install requests")
        return

    url = input("Enter webpage URL (include https://): ").strip()

    try:
        response = requests.get(url, timeout=10)
        match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            print(f"✅ Page Title: {title}")

            with open("scraped_titles.txt", "a") as f:
                f.write(f"{url} -> {title}\n")
            print("📁 Saved to 'scraped_titles.txt'")
        else:
            print("⚠️ No <title> tag found on this page.")
    except Exception as e:
        print(f"❌ Error fetching page: {e}")


def main():
    show_banner()
    while True:
        print("\n1. Organize Files by Extension")
        print("2. Extract Emails from a .txt File")
        print("3. Scrape Webpage Title")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            organize_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("\n👋 Automation session ended. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1-4.")


if __name__ == "__main__":
    main()