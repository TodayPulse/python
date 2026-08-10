# Implement eligibility_logic(score, attendance, completed_drill). 
# Return "Eligible" only when score is greater than or equal to 70,
# attendance is greater than or equal to 80, and completed_drill is True.
# Otherwise return "Not eligible".

def eligibility_logic(score, attendance, completed_drill):

    if isinstance(completed_drill,str):
        completed_drill = completed_drill.lower()=="true"
    if score >= 70 and attendance >=80 and completed_drill:
        return "Eligible"

    return "Not Eligible"


print(eligibility_logic(80,90,True))
