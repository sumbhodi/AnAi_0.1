# llm_connector.py: The Brain Stem (API Call Holder)

# 1. ARCHITECTURE IMPORTS
from core import HANDOFF_JSON # Get the system state and memory
from cs_tutor import teach_concept # Get the first functional tool

# 2. API PLACEHOLDER
def query_llm(prompt: str, function_call: str = None):
    """
    This function will eventually hold the actual API call (e.g., to Gemini, Claude, etc.)
    For now, it acts as a router based on the prompt.
    """
    
    # Check current status from the core
    current_status = HANDOFF_JSON['status_flag']
    
    # ROUTING LOGIC PLACEHOLDER
    if "teach me" in prompt.lower() or function_call == "cs_tutor":
        # Route to the functional module
        topic = prompt.split("teach me", 1)[-1].strip() or "a concept"
        return teach_concept(topic)
    
    # Default behavior for a general query
    return f"LLM Connector is ready. Status: {current_status}. Received Prompt: '{prompt}'. (API call is currently simulated.)"

# --- MAIN EXECUTION EXAMPLE ---
if __name__ == "__main__":
    print(f"LLM Connector Initialized. Model Tier: {HANDOFF_JSON['current_model_tier']}")
    
    # Test 1: Simple query
    response_general = query_llm("Tell me about today.")
    print(f"\nGeneral Query Test:\n{response_general}")
    
    # Test 2: Function call routing
    response_tutor = query_llm("Teach me Git now!")
    print(f"\nTutor Routing Test:\n{response_tutor}")
