# main.py
import tkinter as tk
from modules.system_monitor import get_system_info, get_process_info
from modules.data_handler import save_data, export_data
from modules.ui_components import create_labels, create_process_table, create_buttons
import threading
import time