# for문은 반복횟수가 정해진 상태에 적합하다.

# 물 10잔 떠오기
#for [하나씩 가져올 변수] in[범위]:


    # 만약 커피를 타는데 한잔의 물에 믹스 2개씩을 넣어야 한다면?
    # 반복안에 반복이 발생된다.
for cup in range(1, 11):
    print(f'물 {cup} 번째 잔에 물을 떠왔습니다.')

    for coffeemix in range(2, 3):
        print(f'커피믹스{coffeemix}개를 넣었습니다.')

        for spoon in range(3, 4):
            print(f'{spoon} 번 수픈으로 젖는다.')

