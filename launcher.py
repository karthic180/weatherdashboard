import os
import sys
import subprocess

# -------------------- DELETE WEATHER DB --------------------
def delete_weather_db():
    db_path = "weather.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print("🗑️ Deleted old weather.db cache.")

# -------------------- RUN TERMINAL APP --------------------
def run_terminal():
    os.system(f'"{sys.executable}" terminal_app.py')

# -------------------- RUN WEB APP --------------------
def run_web():
    # Auto-delete cache before launching web UI
    delete_weather_db()

    # Launch Streamlit in background, no logs, no blocking
    subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "web_app.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    )

    print("\n🌐 Web UI launched in your browser.")
    print("Returning to menu...\n")

# -------------------- MAIN MENU --------------------
def main():
    while True:
        print("""
==============================
      Weather Dashboard
==============================
1) Run Terminal App
2) Run Web Dashboard
0) Exit
==============================
""")
        choice = input("Choose: ").strip()

        if choice == "1":
            run_terminal()
        elif choice == "2":
            run_web()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
