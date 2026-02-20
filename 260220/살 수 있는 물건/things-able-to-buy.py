N = int(input())
items = {
    "book": 3000,
    "mask": 1000
}
max_price = -1       # 가장 비싼 가격 (아무것도 못 살 때를 대비해 -1로 시작)
expensive_item = ""  # 가장 비싼 물건 이름

# 4. 물건들을 하나씩 확인 (딕셔너리의 key, value 꺼내기)
for name, price in items.items():
    # 내 돈으로 살 수 있고(price <= N), 기존에 찾은 것보다 더 비싸다면(price > max_price)
    if price <= N and price > max_price:
        max_price = price
        expensive_item = name

# 5. 최종 출력 조건 처리
if max_price == -1:
    print("no")
else:
    print(expensive_item)