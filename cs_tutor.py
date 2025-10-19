# cs_tutor.py: CS Tutor Minimum Viable Product (MVP)

# This module provides quick, context-aware, scaffolded lessons
# based on the user's current cognitive state and learning preferences.

# 1. LEARNING PREFERENCE (Define your "teaching style" here)
# Options: 'Haiku', 'Absurdist Metaphor', 'Cop Drama', 'Ziggurat Scaffolding'
teaching_style = "Ziggurat Scaffolding" 

# 2. THE TUTOR FUNCTION
def teach_concept(topic, style=teaching_style):
    """Generates a highly compressed, focused lesson."""

    # This is the placeholder for the main teaching logic
    # The real model (Gemini/Claude) would generate the response here.
    
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

    # Example of a concept-check printout:
    from core import HANDOFF_JSON
    print(f"\nConnected to Handoff: Current focus is {HANDOFF_JSON['current_focus']}")
