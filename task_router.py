import psutil
import os

class TaskRouter:
    def __init__(self):
        self.processes = self._get_all_processes()

    def _get_all_processes(self):
        """Retrieve all active processes."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return processes

    def display_processes(self):
        """Display all active processes with their resource usage."""
        print(f"{'PID':<10}{'Name':<25}{'CPU%':<10}{'Memory%':<10}")
        for proc in self.processes:
            print(f"{proc['pid']:<10}{proc['name']:<25}{proc['cpu_percent']:<10}{proc['memory_percent']:<10}")

    def optimize_resources(self, cpu_threshold=10.0, memory_threshold=10.0):
        """Optimize system resources by lowering priority of processes exceeding thresholds."""
        for proc in self.processes:
            if proc['cpu_percent'] > cpu_threshold or proc['memory_percent'] > memory_threshold:
                try:
                    p = psutil.Process(proc['pid'])
                    p.nice(psutil.IDLE_PRIORITY_CLASS)
                    print(f"Lowered priority of {proc['name']} (PID: {proc['pid']})")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    print(f"Failed to lower priority of {proc['name']} (PID: {proc['pid']})")

if __name__ == "__main__":
    router = TaskRouter()
    print("Active Processes:")
    router.display_processes()
    print("\nOptimizing Resources:")
    router.optimize_resources(cpu_threshold=20.0, memory_threshold=20.0)