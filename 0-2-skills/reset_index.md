```python
won = df[df['first_party_winner'] == 1]
lost = df[df['first_party_winner'] == 0]
lost.reset_index(inplace=True, drop=True) # 리셋 인덱스, inplace 데이터 바로 적용
# boxPrint(lost['facts'][0])
# boxPrint(lost['facts'][1])
# boxPrint(lost['facts'][3])
lost_fp = lost['first_party']
lost_sp = lost['second_party']
lost_fp.reset_index(inplace=True, drop=True)
lost_sp.reset_index(inplace=True, drop=True)

print('fp: ', lost_fp[4], 'sp: ',lost_sp[4])

boxPrint(lost['facts'][4])
```

- 다른 예제
```python
# 승소와 패소 데이터 비율 5:5로 맞추기 # 0619

# 승소와 패소 개수 각각 저장
won_lost_value = name_deleted_df['first_party_winner'].value_counts()
count1 = won_lost_value[1]
count0 = won_lost_value[0]

# 승소한 리스트 인덱스 0부터 다시 지정
reindex_df1 = name_deleted_df[name_deleted_df['first_party_winner']==1]
reindex_df1.reset_index(inplace=True, drop=True)
# 패소한 리스트
reindex_df0 = name_deleted_df[name_deleted_df['first_party_winner']==0]

# 시드 정해놔서 항상 같은 숫자 나오도록 하기
import random
random.seed(0)
remove_list = random.randint(0,count0)

# 패소한 리스트의 갯수만큼 인덱스 랜덤으로 뽑기
lst_1_index = random.sample(range(0,len(reindex_df1)),count0)
lst_1_index.sort() # 정렬은 a = b.sort()처럼 사용하지 못한다
lst_1_index

# 랜덤인덱스에 맞는 승소 리스트 만들기 (패소리스트 갯수만큼)
newone = reindex_df1.loc[reindex_df1.index.isin(lst_1_index)] # 특정한 데이터 뽑을 땐 loc

# 승소리스트 패소리스트 합치기
balanced_list = pd.concat([newone, reindex_df0])
balanced_list.reset_index(inplace=True, drop=True)
print('새로운 데이터갯수 :',len(balanced_list))
balanced_list
```