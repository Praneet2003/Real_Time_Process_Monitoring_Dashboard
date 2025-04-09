import tkinter as tk
from tkinter import messagebox
from modules.MonitoringSystem import get_system_info, get_process_info
from modules.ExportingData import save_data, export_data
from modules.userInterface import create_labels, create_process_table, create_buttons
import threading
import time

monitoring = False
previous_process_data = {}


def updateprocesstable(process_list):
    # Refresh the process list in the UI if changes are detected.
    global previous_process_data
    curprodata = {proc['pid']: proc for proc in process_list}
    if curprodata == previous_process_data:
        return
    previous_process_data = curprodata
    for row in process_tree.get_children():
        process_tree.delete(row)
    for proc in process_list:
        process_tree.insert("", "end", values=(proc['pid'], proc['name'], proc['status'], f"{proc['cpu_percent']:.2f}%"))


def monitor_system():
    # displays the real time monitored data from the PC. 
    global monitoring
    while monitoring:
        cpusg, memusg = get_system_info()
        cpu_label.config(text=f"CPU Usage: {cpusg:.2f}%", fg="red" if cpusg > 85 else "white")
        memory_label.config(text=f"Memory Usage: {memusg:.2f}%", fg="red" if memusg > 85 else "white")
        process_list = get_process_info()
        updateprocesstable(process_list)
        save_data(cpusg, memusg, process_list)
        time.sleep(1)#refreshed after 1 unit of time.

def startmonitoring():
    # button ,clicking on which the sytsem starts 
    # calling the functions of psutil and data is displayed. 
    global monitoring
    if not monitoring:
        monitoring = True
        thread = threading.Thread(target=monitor_system, daemon=True)
        thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        export_button.config(state=tk.NORMAL)


def stopmonitoring():
    # button to stop monitoring, application will staop deflecting new data.
    global monitoring
    monitoring = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)


def export_monitored_data():
    # exporting the data of the processes running in the dashboard.
    file_path, msg = export_data()
    if file_path:
        tk.messagebox.showinfo("Success", f"Data exported successfully to {file_path}")
    else:
        tk.messagebox.showwarning("No Data", msg)


root = tk.Tk()
root.title("Real-Time Process Monitoring Dashboard")
root.geometry("800x500")
root.configure(bg="#0F2027")

cpu_label, memory_label = create_labels(root)
process_tree = create_process_table(root)
start_button, stop_button, export_button = create_buttons(
    root,
    startmonitoring,
    stopmonitoring,
    export_monitored_data
)

root.mainloop()