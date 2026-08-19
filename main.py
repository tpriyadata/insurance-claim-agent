from src.graph.workflow import app

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "CLM-9001"}}
    
    initial_input = {
        "claim_id": "CLM-9001",
        "incident_description": "Scratched passenger door against a side pole while parking.",
        "photo_urls": ["https://example.com/door_scratch.jpg"],
        "damage_analysis": None,
        "policy_status": None,
        "payout_amount": 0.0,
        "status": "PENDING",
        "logs": []
    }

    print("--- Starting Agentic Workflow ---")
    for event in app.stream(initial_input, config):
        for node_name, output in event.items():
            print(f"\nCompleted Node: {node_name}")
            print(f"Logs: {output.get('logs', [])}")