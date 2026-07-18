import os
import sys

# Storage data arrays
workouts_log = []
daily_metrics = {"steps": 0, "water_ml": 0, "active_minutes": 0, "weight_kg": 0.0}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=" * 45)
    print("    🏋️‍♂️ PURE PYTHON HEALTH & WORKOUT CLI 🏋️‍♂️    ")
    print("=" * 45)
    print(" 1. Update Daily Health Metrics (Steps, Water)")
    print(" 2. Log a New Workout Session")
    print(" 3. View Today's Health Dashboard Summary")
    print(" 4. Reset Daily Progress Tracker")
    print(" 5. Close Application Routine")
    print("=" * 45)

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Select tracking function [1-5]: ").strip()
        
        if choice == '1':
            clear_screen()
            print("--- UPDATE DAILY METRICS ---")
            try:
                daily_metrics["steps"] = int(input("Enter total daily steps: ") or daily_metrics["steps"])
                daily_metrics["water_ml"] = int(input("Enter water consumption (ml): ") or daily_metrics["water_ml"])
                daily_metrics["active_minutes"] = int(input("Enter active movement minutes: ") or daily_metrics["active_minutes"])
                daily_metrics["weight_kg"] = float(input("Enter current weight (kg): ") or daily_metrics["weight_kg"])
                print("\n✅ Daily health vectors updated successfully!")
            except ValueError:
                print("\n❌ Invalid numerical input format. Metrics skipped.")
            input("\nPress Enter to return...")
            
        elif choice == '2':
            clear_screen()
            print("--- LOG NEW WORKOUT ---")
            exercise = input("Enter exercise type (e.g., Running, Weightlifting): ").strip()
            if not exercise:
                print("❌ Exercise type field cannot remain empty.")
                input("\nPress Enter to return...")
                continue
            try:
                duration = int(input("Enter duration (minutes): "))
                calories = int(input("Enter estimated active calories burned: "))
            except ValueError:
                print("❌ Invalid entry bounds. Numbers required.")
                input("\nPress Enter to retry...")
                continue
                
            workouts_log.append({"exercise": exercise, "duration": duration, "calories": calories})
            daily_metrics["active_minutes"] += duration
            print(f"\n✅ Session registered: {exercise} for {duration} mins.")
            input("\nPress Enter to return...")
            
        elif choice == '3':
            clear_screen()
            print("--- TODAY'S HEALTH DASHBOARD SUMMARY ---")
            print("=" * 45)
            print(f" Daily Steps Walked:     {daily_metrics['steps']:,} steps")
            print(f" Hydration Logged:       {daily_metrics['water_ml']} ml")
            print(f" Total Active Minutes:   {daily_metrics['active_minutes']} minutes")
            print(f" Recorded Body Weight:   {daily_metrics['weight_kg'] if daily_metrics['weight_kg'] > 0 else 'N/A'} kg")
            print("=" * 45)
            print(f" Completed Workouts Today: {len(workouts_log)}")
            print("-" * 45)
            if not workouts_log:
                print(" No exercise log sheets recorded for this track window.")
            else:
                total_burn = 0
                for i, w in enumerate(workouts_log, 1):
                    print(f"  {i}. {w['exercise']} | {w['duration']} min | -{w['calories']} kcal")
                    total_burn += w['calories']
                print("-" * 45)
                print(f" Total Active Calorie Expenditure: {total_burn} kcal")
            print("=" * 45)
            input("\nPress Enter to return to menu...")
            
        elif choice == '4':
            clear_screen()
            confirm = input("Are you sure you want to clear daily matrices? (y/n): ").strip().lower()
            if confirm == 'y':
                workouts_log.clear()
                daily_metrics.update({"steps": 0, "water_ml": 0, "active_minutes": 0, "weight_kg": 0.0})
                print("\n✅ Dashboard state reset to baseline parameters.")
            else:
                print("\nReset aborted.")
            input("\nPress Enter to return...")
            
        elif choice == '5':
            clear_screen()
            print("Exiting health dashboard interface. Keep moving!")
            sys.exit()
        else:
            print("❌ Parsing fault. Choose menu numbers [1-5].")
            input("\nPress Enter to reload menu configuration...")

if __name__ == "__main__":
    main()
