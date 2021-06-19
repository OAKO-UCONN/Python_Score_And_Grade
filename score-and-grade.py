def compute_grade(score):
    if score > 1:
        return 'It is not possible.'
    if score>0.9:
        grade = 'A'
    elif score > 0.8:
        grade = 'B'
    else:
        grade = 'F'
    return grade
    
res = compute_grade(0.5)
    