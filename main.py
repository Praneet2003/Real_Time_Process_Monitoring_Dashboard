import tkinter as tk
from modules.system_monitor import get_system_info, get_process_info

from modules.data_handler import save_data, export_data
from modules.ui_components import create_labels, create_process_table, create_buttons
import threading
import time

monitoring = False
previous_process_data = {}


def update_process_table(process_list):
    """Update process table dynamically."""
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
    """Continuously monitor system data in the background."""
    global monitoring
    while monitoring:
        cpusg, memusg = get_system_info()

        # Highlight if above threshold
        cpu_label.config(text=f"CPU Usage: {cpusg:.2f}%", fg="red" if cpusg > 85 else "white")
        memory_label.config(text=f"Memory Usage: {memusg:.2f}%", fg="red" if memusg > 85 else "white")

        process_list = get_process_info()
        update_process_table(process_list)

        save_data(cpusg, memusg, process_list)
        time.sleep(1)

def start_monitoring():
    global monitoring
    if not monitoring:
        monitoring = True
        thread = threading.Thread(target=monitor_system, daemon=True)
        thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        export_button.config(state=tk.NORMAL)


def stop_monitoring():
    global monitoring
    monitoring = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)


def export_monitor_data():
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
    start_monitoring,
    stop_monitoring,
    export_monitor_data
)

root.mainloop()