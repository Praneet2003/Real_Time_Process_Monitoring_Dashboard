

🖥️ Real-Time Process Monitoring Dashboard 🚀


A sleek and efficient real-time system and process monitoring tool built with Python and Tkinter. This dashboard provides live insights into CPU and memory usage, active processes, and lets you export monitoring data as a CSV file! 📊🧠

📂 Project Structure
graphql
Copy
Edit
📁 project/
├── main.py                 # Main GUI and controller
├── modules/
│   ├── system_monitor.py   # Collects system and process info
│   ├── data_handler.py     # Saves and exports monitoring data
│   └── ui_components.py    # UI layout components
└── data/
    └── monitor_data.csv    # Exported data (generated)
✨ Features
🔴 Live CPU & Memory Usage Monitoring

📋 Dynamic Process Table with PID, Name, Status & CPU Usage

💾 Data Logging

📤 CSV Export of Monitoring Stats

💡 User-friendly Interface with Styled Widgets

🛠️ Requirements
Python 3.x 🐍

psutil 🧰

pandas 📐

numpy 📊

tkinter (usually comes with Python)

Install dependencies:

bash
Copy
Edit
pip install psutil pandas numpy


▶️ How to Run
Clone/download the project.

Make sure you have the required dependencies installed.

Run the main script:

bash
Copy
Edit
python main.py


📤 Exporting Data
After starting and stopping monitoring, click "Export Data" to generate a CSV file saved in the data/ directory. The CSV includes:

CPU Usage

Memory Usage

Number of Active Processes

Timestamp ⏰


🙌 Acknowledgements
Special thanks to:

psutil for powerful system insights

pandas for easy data handling

You, for using this tool! ❤️

Contributed by :
1. Praneet Raj
2. Nikhil Prakash
3. Rohit Singh Yadav