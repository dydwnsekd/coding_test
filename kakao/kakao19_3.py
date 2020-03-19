#-*- coding: utf-8 -*-

'''
http://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/
3. 후보키
정답률: 16.09%
문제 풀러 가기
프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.

그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.



위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 “학번”을 가지고 있다. 따라서 “학번”은 릴레이션의 후보 키가 될 수 있다. 그다음 “이름”에 대해서는 같은 이름(“apeach”)을 사용하는 학생이 있기 때문에, “이름”은 후보 키가 될 수 없다. 그러나, 만약 [“이름”, “전공”]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로 후보 키가 될 수 있게 된다. 물론 [“이름”, “전공”, “학년”]을 함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만, 최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다. 따라서, 위의 학생 인적사항의 후보키는 “학번”, [“이름”, “전공”] 두 개가 된다.

릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

제한사항
relation은 2차원 문자열 배열이다.
relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)
입출력 예
relation	result
[[“100”,”ryan”,”music”,”2”],[“200”,”apeach”,”math”,”2”],[“300”,”tube”,”computer”,”3”],[“400”,”con”,”computer”,”4”],[“500”,”muzi”,”music”,”3”],[“600”,”apeach”,”music”,”2”]]	2
입출력 예 설명
입출력 예 #1 문제에 주어진 릴레이션과 같으며, 후보 키는 2개이다.
'''
import pandas as pd
import copy

def subset(list_len):
    num_list = make_list(list_len)
    result_list = list()
    result_list.append(num_list[0])
    
    for i in range(1, list_len):
        result_list = merge_list(result_list, num_list[i])

    return (result_list)

def make_list(list_len):
    result_list = list()

    for i in range(list_len):
        temp_list = list()
        temp_list.append(i)
        result_list.append(temp_list)
        
    #[[0],[1],[2],[3]]
    return result_list

def merge_list(input_list, new_num):

    merge_list = list()
    list_len = len(input_list)

    merge_list = copy.deepcopy(input_list)

    for i in range(list_len):
        input_list[i].append(new_num[0])

        temp = input_list[i]
        merge_list.append(temp)

    merge_list.append(new_num)

    return merge_list


def solution(relation):
    print (relation)
    df = pd.DataFrame(relation)

    list_len = len(relation[0])
    input_len = len(relation)
    subset_index = subset(list_len)

    candidate_key = list()

    for i in subset_index:

        temp_df = df[i]
        temp_df = temp_df.drop_duplicates()

        if len(temp_df) == input_len:
            candidate_key.append(i)

    candidate_result = list()
    candidate_key = sorted(candidate_key, key=len)

    while(candidate_key):
        temp = candidate_key.pop(0)
        del_list = list()
        for i in range(len(candidate_key)):
            cnt = 0
            for t in temp:
                if t in candidate_key[i]:
                    cnt = cnt + 1
            if cnt == len(temp):
                del_list.append(i)

        del_list.reverse()
        for i in del_list:
            del candidate_key[i]

        candidate_result.append(temp)
        
        answer = len(candidate_result)
    return answer