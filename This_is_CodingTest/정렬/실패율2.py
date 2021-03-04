def count_function(x, stage):
    count = 0
    for i in range(len(stage)):
        if x == stage[i]:
            count += 1

    return count


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

print(solution(5,[3,4,2,1,5]))