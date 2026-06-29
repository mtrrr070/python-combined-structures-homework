reviews = [
    "Товар отличный, доставка быстрая",
    "Ужасный сервис, очень долго",
    "В целом нормально",
    "Хороший продукт, мне нравится",
    "Товар сломанный и плохой",
    "Классный товар, качество отличное",
    "Очень удобный и надежный продукт",
    "Отвратительная упаковка и плохое качество",
    "Доставка пришла быстро, я доволен",
    "Сервис ужасный и товар сломанный",
    "Прекрасная вещь, всем рекомендую",
    "Нормальный товар за свои деньги",
    "Качество ужасное, деньги потрачены зря"
]

positive_words = [
    "отличный",
    "хороший",
    "быстрая",
    "нравится",
    "классный",
    "удобный",
    "надежный",
    "доволен",
    "прекрасная",
    "рекомендую"
]

negative_words = [
    "плохой",
    "ужасный",
    "долго",
    "сломанный",
    "отвратительная",
    "ужасное",
    "зря",
    "проблема",
    "дорогой",
    "некачественный"
]

results = []
positive_count = 0
negative_count = 0
neutral_count = 0
total_score = 0

for review in reviews:
    review_lower = review.lower()
    score = 0

    for word in positive_words:
        if word in review_lower:
            score += 1

    for word in negative_words:
        if word in review_lower:
            score -= 1

    if score > 0:
        sentiment = "positive"
        positive_count += 1
    elif score < 0:
        sentiment = "negative"
        negative_count += 1
    else:
        sentiment = "neutral"
        neutral_count += 1

    total_score += score
    results.append([review, score, sentiment])

for review, score, sentiment in results:
    print(f"Отзыв: {review}")
    print(f"Балл: {score}")
    print(f"Настроение: {sentiment}")
    print("-" * 40)

average_score = total_score / len(reviews)

print(f"Количество положительных отзывов: {positive_count}")
print(f"Количество отрицательных отзывов: {negative_count}")
print(f"Количество нейтральных отзывов: {neutral_count}")
print(f"Средний балл: {average_score:.2f}")

user_review = input("Введите свой отзыв: ").lower()

user_score = 0

for word in positive_words:
    if word in user_review:
        user_score += 1

for word in negative_words:
    if word in user_review:
        user_score -= 1

if user_score > 0:
    user_sentiment = "positive"
elif user_score < 0:
    user_sentiment = "negative"
else:
    user_sentiment = "neutral"

print(f"Ваш отзыв: {user_review}")
print(f"Балл: {user_score}")
print(f"Настроение: {user_sentiment}")