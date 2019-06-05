import sys

step_count = int(sys.stdin.readline())
score_list = list()
for _ in range(step_count):
     score_list.append(int(sys.stdin.readline()))

pre_step = False
score = 0

if score_list[0] >= score_list[1]:
    score += score_list[0]
    step = 0
else:
    score += score_list[1]
    step = 1


while(True):
    if step+2 == step_count:
        score += score_list[-1]
        break
    elif step+1 == step_count:
        if pre_step:
            if score_list[step-1] >= score_list[step]:
                score -= score_list[step]
                score += score_list[-1]
                break
        else:
            score += score_list[-1]
            break

    if pre_step:
        score += score_list[step+2]
        step += 2
        pre_step = False

    elif score_list[step+1] >= score_list[step+2]:
        score += score_list[step+1]
        if step != -1:
            pre_step = True
        step += 1
    
    else:
        score += score_list[step+2]
        step += 2
        pre_step = False

print (score)
