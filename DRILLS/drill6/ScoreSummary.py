# Implement score_summary(name, a, b, c). Convert the three score values to numbers. 
# If conversion fails, return Invalid score. If any score is below 0 or above 100, return Invalid score. 
# Otherwise calculate the average, round it to 2 decimal places, choose a grade, and return a three-line 
# report with labels Student, Average, and Grade. Grade is A for 90 and above, B for 80 and above, C for 70 and 
# above, and F below 70.

def score_summary(name,a,b,c):
    def to_number(value):
        try:
            return float(value)
        except(ValueError,TypeError):
            return None

        
