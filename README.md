# DevOps Infrastructure Provisioning Simulator

## Overview
This is a modular Python-based automation tool that simulates infrastructure provisioning and service configuration. It is designed as Phase 1 of a rolling project that will eventually integrate AWS and Terraform. Currently, it mocks the provisioning process by collecting user input, validating it, storing it persistently, and triggering a simulated Bash configuration script.

## Objectives
* Accept and validate user inputs for dynamically defining virtual machines.
* Utilize Object-Oriented Programming (OOP) with a `Machine` class.
* Store machine configurations persistently in JSON format.
* Automate simulated service configuration (e.g., Nginx) using Bash and Python's `subprocess` module.
* Implement structured logging to both the console and a dedicated file.

## Project Structure
    infra-automation/
    ├── configs/
    │   └── instances.json      # Persistent storage for VM configurations
    ├── logs/
    │   └── provisioning.log    # Log file for provisioning events and errors
    ├── scripts/
    │   └── setup_nginx.sh      # Bash script to simulate service installation
    ├── src/
    │   ├── logger.py           # Centralized Python logging configuration
    │   └── machine.py          # OOP class blueprint for Machine objects
    ├── main.py                 # Main execution script
    └── README.md               # Project documentation

## Setup & Execution Instructions

**1. Clone the repository:**
    git clone https://github.com/sbaransi/infra-automation.git
    cd infra-automation

**2. Set up a virtual environment (Optional but recommended):**
    python3 -m venv venv
    source venv/bin/activate

**3. Run the application:**
Execute the main script to start the simulator. The script will automatically handle the Python validation, JSON saving, and Bash script execution.
    python3 main.py

**4. Usage:**
* The CLI wizard will prompt you for machine details (Name, OS, CPU, RAM).
* Type `done` when asked for a machine name to finish.
* The system will automatically save your configurations to `configs/instances.json` and trigger the `setup_nginx.sh` bash script.

## Example Expected Output

    --- DevOps Infrastructure Simulator ---

    Enter machine name (or 'done' to finish): web-server
    Enter OS (Ubuntu/CentOS): Ubuntu
    Enter CPU (e.g., 2vCPU): 2vCPU
    Enter RAM (e.g., 4GB): 4GB
    [INFO] Provisioning web-server: Ubuntu, 2vCPU, 4GB

    Enter machine name (or 'done' to finish): done
    [SUCCESS] Saved instance configurations to JSON.

    --- Starting Service Configuration ---
    [BASH] Checking if Nginx is installed...
    [BASH] Nginx not found. Proceeding with installation...
    [BASH] Downloading packages...
    [BASH] Installation complete. Nginx service started.
    [SUCCESS] Nginx installation completed.

    [DONE] Provisioning process finished.