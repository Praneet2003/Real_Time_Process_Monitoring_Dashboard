# modules/system_monitor.py
import psutil
import numpy as np
import time


def get_cpu_usage():
    prcorusg= psutil.cpu_percent(percpu=True, interval=1)
    avgcpuusg = np.mean(prcorusg)
    return round(avgcpuusg, 2)


def get_system_info():
    cpusg = get_cpu_usage()
    meminfo = psutil.virtual_memory()
    memusg = meminfo.percent
    return cpusg, memusg


def get_process_info():
    prolist = []
    for pro in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']):
        try:
            if pro.info['pid'] == 0: 
                continue
            prolist.append(pro.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return prolist