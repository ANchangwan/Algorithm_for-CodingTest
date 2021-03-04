
def solution(N, stages):
    answer = []

    clear_stage = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)
        if clear_stage == 0:
            fail = 0
        else:
            fail = count / clear_stage

        answer.append((i, fail))
        clear_stage -= count
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

