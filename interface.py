# interface.py: The Command Line User Interface (CLI)

# 1. ARCHITECTURE IMPORTS
from core import HANDOFF_JSON # Get the system state and memory
from llm_connector import query_llm # Get the function to talk to the 'brain'

# 2. INTERFACE FUNCTION
def start_cli_interface():
    """Initializes the command-line interface for the AnAI Prosthetic."""
    
    # Greet the user and display current status from the Handoff data
    print("-------------------------------------------------------")
    print(f"**AnAI v0.1 Cognitive Prosthetic Initialized**")
    print(f"  System Status: {HANDOFF_JSON['status_flag']}")
    print(f"  Current Focus: {HANDOFF_JSON['current_focus']}")
    print("-------------------------------------------------------")
    print("Type a command (e.g., 'teach me git', 'today's mission'):")
    
    # Simulation loop
    while True:
        user_input = input(">> ").strip()
        
        if user_input.lower() in ["quit", "exit"]:
            print("System Handoff initiated. Goodbye.")
            break
            
        # Route the input through the LLM Connector
        response = query_llm(user_input)
        print(f"\n[Ziggurat Response]: {response}\n")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    start_cli_interface()
