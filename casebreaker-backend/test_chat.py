import requests
import json
import sseclient

def with_urllib3(url, headers):
    """Get a streaming response for a given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False, headers=headers)

def main():
    # Create a message
    message = {
        "role": "user",
        "content": "Looking at the vitals (BP 90/60, HR 120, RR 24), what should be my immediate concerns?",
        "checkpoint_id": "initial"
    }

    # Post the message
    response = requests.post(
        "http://localhost:8000/api/v1/sessions/2/messages",
        json=message,
        stream=True,
        headers={"Accept": "text/event-stream"}
    )

    # Create SSE client
    client = sseclient.SSEClient(response)

    response_started = False
    
    # Process events
    for event in client.events():
        data = json.loads(event.data)
        
        if event.event == "status":
            state = data["data"]["state"]
            message = data["data"]["message"]
            
            if state == "thinking":
                print(f"\n{message}")
            elif state == "complete":
                print(f"\n\n{message}")
                
        elif event.event == "chunk":
            if not response_started:
                print("\nClaude's Response:\n")
                response_started = True
            print(data["data"], end="", flush=True)
            
        elif event.event == "error":
            print(f"\nError: {data['data']}")
            break

if __name__ == "__main__":
    main()
