# cs_tutor.py: CS Tutor Minimum Viable Product (MVP)

# NEW: Import Handoff data from the core architecture
from core import HANDOFF_JSON # <--- THIS IS THE KEY LINE

# This module provides quick, context-aware, scaffolded lessons
# based on the user's current cognitive state and learning preferences.

# 1. LEARNING PREFERENCE (Define your "teaching style" here)
# Options: 'Haiku', 'Absurdist Metaphor', 'Cop Drama', 'Ziggurat Scaffolding'
# We can use the Handoff status to dynamically adjust the style.
teaching_style = "Ziggurat Scaffolding" 

# 2. THE TUTOR FUNCTION
def teach_concept(topic, style=teaching_style):
    """Generates a highly compressed, focused lesson."""

    # This is the placeholder for the main teaching logic
    
    # We can now use HANDOFF_JSON data inside this function if needed!
    
    if topic.lower() == "git" and style == "Ziggurat Scaffolding":
        return "Git is the **History Engine**. Commit is saving. Branch is a **side quest**. Merge is bringing the loot back to the **main timeline**."
    
    elif topic.lower() == "git" and style == "Absurdist Metaphor":
        return "Git is a library where every single book has its own clone, and the main book is a sentient blob of butter."
    
    else:
        return f"Tutor is active. Topic: {topic}, Style: {style}. Ready for a full lesson."

# --- MAIN EXECUTION EXAMPLE ---
if __name__ == "__main__":
    lesson = teach_concept("Git")
    print(f"CS Tutor Active (Style: {teaching_style}):")
    print(lesson)

    # The Handoff status check is now built-in:
    print(f"\nConnected to Handoff: Current focus is {HANDOFF_JSON['current_focus']}")
