# TaskRouter

TaskRouter is a utility program designed to manage and optimize the allocation of system resources to active processes in Windows environments. It monitors running processes and adjusts their priorities to ensure efficient use of CPU and memory resources.

## Features

- **Process Monitoring**: Display a list of all active processes along with their CPU and memory usage.
- **Resource Optimization**: Automatically lower the priority of processes that exceed specified CPU or memory usage thresholds.

## Requirements

- Python 3.x
- `psutil` library

You can install the required library using pip:

```bash
pip install psutil
```

## Usage

1. Clone the repository and navigate to the directory containing `task_router.py`.
2. Run the script:
   
   ```bash
   python task_router.py
   ```

3. The script will display all active processes and optimize resource allocation by lowering the priority of processes that exceed the specified CPU and memory usage thresholds.

## Configuration

- Adjust the `cpu_threshold` and `memory_threshold` parameters in the `optimize_resources` method to set the limits for resource optimization.

## License

This project is licensed under the MIT License.