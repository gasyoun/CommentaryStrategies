import json
import random

class ParibokLlama:
    """
    Mockup of the Paribok-Llama model for automatic commentary classification.
    Uses the 4-axis framework established in the project.
    """
    
    AXIS_1_TOPICS = ["sanskrit_term", "myth", "philosophy", "realia", "geography", "textology", "poetics", "context", "reference"]
    AXIS_2_KAZANSKY = ["A", "V", "B", "G", "R"]
    AXIS_3_LAKSHANA = ["L1", "L2", "L3", "L4", "L5"]
    AXIS_4_PARIBOK = ["P", "K", "D"]

    def classify(self, text, translator):
        """
        Simulate LLM classification.
        """
        # Heuristics for "intelligent" mocking
        has_iast = any(c in text for c in "āīūṛṭḍṇśṣṃḥ")
        
        # Topic selection based on keywords
        topics = []
        if "бог" in text.lower() or "миф" in text.lower(): topics.append("myth")
        if "быт" in text.lower() or "одежд" in text.lower(): topics.append("realia")
        if "атман" in text.lower() or "душа" in text.lower(): topics.append("philosophy")
        if not topics: topics = [random.choice(self.AXIS_1_TOPICS)]
        
        # Strategy (Axis 2) based on translator
        strategy = "G"
        if translator == "kalyanov": strategy = "A"
        elif translator == "vassilkov": strategy = "V"
        elif translator == "erman": strategy = "B"
        
        # Paribok category (Axis 4)
        paribok = "P"
        if "философ" in text.lower() or "духов" in text.lower(): paribok = "D"
        elif has_iast and translator == "kalyanov": paribok = "K"

        return {
            "has_iast": has_iast,
            "axis_1_topic": topics,
            "axis_2_kazansky": strategy,
            "axis_3_lakshana": [random.choice(self.AXIS_3_LAKSHANA)],
            "axis_4_paribok": paribok,
            "confidence": round(random.uniform(0.85, 0.99), 2)
        }

if __name__ == "__main__":
    model = ParibokLlama()
    test_text = "Атман (ātman) — бессмертная душа в упанишадах."
    result = model.classify(test_text, "syrkin")
    print(json.dumps(result, indent=2, ensure_ascii=False))
