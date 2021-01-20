data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입1
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print("".join(result))


# isalpha : 문자열이 문자인지 아닌지를 True, False로 리턴
# isdigit : 문자열이 숫자인지 아닌지를 True, False로 리턴
# isinstance(인스턴스, 클래스/데이터 타입) : 인스턴스가 특정 클래스/데이터타입과 일치할경우 True, 아니면 False

