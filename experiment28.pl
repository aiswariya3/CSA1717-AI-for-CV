symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

disease(john, flu) :- 
    symptom(john, fever), 
    symptom(john, cough), 
    symptom(john, headache).