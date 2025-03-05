import requests
import json
from config.settings import MAIN_SERVER_IP, SERVER_PORT

def send_result_to_server(task_id, response):
    """
    Send the AI-generated response back to the main server.

    Args:
        task_id (str): Unique identifier of the task.
        response (str): The AI-generated response.
    """
    url = f"http://{MAIN_SERVER_IP}:{SERVER_PORT}/receive_result"

    payload = {
        "task_id": task_id,
        "response": response
    }

    headers = {"Content-Type": "application/json"}

    try:
        print(f"📤 Sending result for task {task_id} to {url}...")
        res = requests.post(url, data=json.dumps(payload), headers=headers)

        if res.status_code == 200:
            print(f"✅ Successfully sent result for task {task_id}!")
        else:
            print(f"⚠️ Failed to send result! Status: {res.status_code} | Response: {res.text}")

    except Exception as e:
        print(f"❌ Error sending result to server: {e}")