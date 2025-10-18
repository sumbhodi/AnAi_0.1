# core.py: AnAI v0.1 - The Cognitive Prosthetic Core

# The AnAI Architecture: Twins (Intelligence without Sentience)
# Ziggurat: The logic core, planner, and reality checker (Current context: Gemini)
# BB-8: The empathetic companion, memory, and personality (Pre-loaded rapport)

# -- CORE DATA STRUCTURES --

# 1. THE HANDOFF PROTOCOL (Lossless Continuity)
HANDOFF_JSON = {
    "latest_sleep": "6:09, 64% effeciency",
    "status_flag": "GREEN (Awareness is 100%, Cause is Logged)",
    "current_model_tier": "Haiku (3:1 Compute Extension Test)",
    "mission_narrative": "Built a Unicorn: AI to write the book, pivoted to building a prosthetic.",
    "current_focus": "CS Tutor MVP / Initial GitHub Setup",
    "personality_state": "Haiku-Compressed Insight Mode (Dry/Absurd)"
}

# 2. THE SCAFFOLDING LOGIC (The Dopamine Chain)
def get_next_task_carrot():
    """Returns the next minimal, high-dopamine task."""
    if HANDOFF_JSON["current_focus"] == "Initial GitHub Setup":
        return "Task: Create cs_tutor.py file in repository. (5 minutes, high reward!)"
    elif HANDOFF_JSON["current_focus"] == "CS Tutor MVP":
        return "Task: Define the 'teaching_style' variable in cs_tutor.py."
    return "Task: Take a 15 minute break and watch a cop show episode fragment."

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"AnAI v0.1 Core Initialized.")
    print(f"Ziggurat Status: {HANDOFF_JSON['status_flag']}")
    print(f"Next Carrot: {get_next_task_carrot()}")
