# set

- 차집합을 이용하면 중복되는 내용을 완전히 제거 가능

  ```python
  # 사건에 언급이 안되는 당사자들 빼기

  def deleteParty(first=False, second=False, both=True):
      """
          제외시킬 사람들. 양측 제거는 디폴트
      """
      # 양측 모두 제거
      deleted_df = df.copy()
      print('원래 데이터셋 행의 갯수 :',len(df))
      if both == True:
          deleted_df = deleted_df.drop(index=name_both_nofacts)
          print('양측 제거 후 행의 갯수 :',len(deleted_df))
      # 퍼스트 제거
      if first == True:
          left_name_list = set(name_first_nofacts) - set(name_both_nofacts) # 차집합 # 0619
          deleted_df = deleted_df.drop(index=left_name_list)
          print('퍼스트파티 제거 후 갯수 :',len(deleted_df))
      # 세컨드 제거
      if second == True:
          left_name_list = set(name_second_nofacts) - set(name_both_nofacts)
          deleted_df = deleted_df.drop(index=left_name_list)
          print('세컨드파티 후 갯수 :',len(deleted_df))

      return deleted_df

  name_deleted_df = deleteParty(first=False, second=False, both=True)
  name_deleted_df
  ```

- 교집합은 &를 이용하자
  ```python
  intersection_label = set(f_label) & set(s_label) # set으로 만들어서 중복되는 지 체크
  ```

---

> ### 중복체크

- 셋으로 만들어서 서로 중복되는 지 확인해보기

```python
intersection_label = set(f_label) & set(s_label)
```

---
