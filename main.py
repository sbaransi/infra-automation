import json
import os
import subprocess
from pathlib import Path
from src.machine import Machine
from src.logger import logger

def get_user_input():
    machines = []
    while True:
        name = input("\nEnter machine name (or 'done' to finish): ")
        if name.lower() == 'done': break
        
        os_type = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
            
        machine = Machine(name, os_type, cpu, ram)
        machine.log_creation()
        machines.append(machine.to_dict())
        
    return machines

def run_setup_script():
    print("\n--- Starting Service Configuration ---")
    try:
        # Using pathlib exactly like the instructor's whiteboard
        script_dir = Path(__file__).parent
        install_script = script_dir / "scripts" / "install.sh"
        
        subprocess.run(["bash", str(install_script)], check=True)
        logger.info("Nginx installation script completed successfully.")
        print("[SUCCESS] Nginx installation completed.")
    except Exception as e:
        logger.error(f"Failed to run bash script: {e}")
        print(f"[ERROR] Failed to run bash script.")

if __name__ == "__main__":
    os.makedirs("configs", exist_ok=True)
    print("--- DevOps Infrastructure Simulator ---")
    
    instances = get_user_input()
    
    if instances:
        with open("configs/instances.json", "w") as file:
            json.dump(instances, file, indent=4)
        logger.info("Saved instance configurations to JSON.")
        
        run_setup_script()
    
    print("\n[DONE] Provisioning process finished.")