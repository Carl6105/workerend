import os
import sys
import ray
import torch

# Ensure the script runs from the correct directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import the required functions
from utils.communication import send_result_to_server
from config.settings import MAIN_SERVER_IP

# ✅ Connect to Main Server's Ray Cluster
RAY_ADDRESS = f"ray://{MAIN_SERVER_IP}:10001"

if not ray.is_initialized():
    ray.init(address=RAY_ADDRESS, ignore_reinit_error=True)

@ray.remote
def worker_task(task_id: str, prompt: str):
    """
    Process AI inference tasks assigned by the main server.
    
    Args:
        task_id (str): Unique task identifier.
        prompt (str): The user input prompt.

    Returns:
        dict: Task result containing task_id and AI-generated response.
    """
    print(f"📩 Received task: {task_id} | Processing prompt: {prompt[:50]}...")

    try:
        # Simulate AI processing (replace with real AI inference if needed)
        response = f"Generated response for: {prompt}"
        
        # Send result back to server
        send_result_to_server(task_id, response)
        
        print(f"✅ Task {task_id} completed successfully!")
        return {"task_id": task_id, "response": response}
    
    except Exception as e:
        print(f"❌ Error in worker_task {task_id}: {e}")
        return {"task_id": task_id, "error": str(e)}

if __name__ == "__main__":
    print(f"✅ Worker node connected to {RAY_ADDRESS} and ready for tasks...")