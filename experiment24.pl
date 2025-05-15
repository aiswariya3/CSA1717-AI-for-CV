diet(diabetes, low_sugar).
diet(bp, low_salt).
diet(anemia, iron_rich).

suggest_diet(Disease, Diet) :- diet(Disease, Diet).
