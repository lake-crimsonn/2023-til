# subplot

```python
cnt = 0
plt.figure(figsize=(10,3))
for x, y in zip(first_batch[0][:5],first_batch[1][:5]):
    print(y, x.shape)
    cnt+=1
    plt.subplot(1,len(first_batch[0][:5]),cnt)
    plt.title('label : '+str(y.numpy())) # 'label: %s' %y.numpy()
    plt.xticks(ticks=[])
    plt.yticks(ticks=[])
    plt.imshow(x.squeeze().numpy(), cmap = 'gray')

# plt.subplot 그리는 방법
# 1. 피그사이즈
# 2. 피그 서브플랏 정해주기 (시작숫자,마지막숫자,1번부터)
# 3. 타이틀, 틱 디테일 등 잡다한 거 넣어주기
# 3. 이미지쇼는 항상 마지막에 표기
```
