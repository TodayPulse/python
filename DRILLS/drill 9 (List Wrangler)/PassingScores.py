# Implement passing_scores(scores, minimum). 
# Return a new list containing only the scores that are greater than or 
# to minimum. Preserve the original order. 
# Do not modify the original list.

def passing_scores(scores, minimum):
    score_list = []

    for score in scores:
        if score >= minimum:
            score_list.append(score)

    return score_list

print(passing_scores([40,70,90,55],70))