import tkinter as tk


from modules.data_handler import save_data, export_data
from modules.ui_components import create_labels, create_process_table, create_buttons
import threading
import time

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