def grade(score):
    if score >= 90:
        result = 'A'
        return result

    elif score < 90 and score >=  80:
        result = 'B'
        return result

    elif score < 80 and score >= 70:
        result = 'C'
        return result

    elif score < 70 and score >= 60:
        result = 'D'
        return result

    elif score < 60:
        result = 'F'
        return result
