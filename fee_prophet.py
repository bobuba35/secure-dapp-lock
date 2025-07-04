"""
Fee Prophet — утилита для предсказания оптимальной комиссии в зависимости от времени суток.
"""

import requests
import datetime

def fetch_fee_estimates():
    url = "https://mempool.space/api/v1/fees/recommended"
    r = requests.get(url)
    return r.json()

def analyze_fees_by_time():
    now = datetime.datetime.utcnow()
    hour = now.hour

    print(f"🕒 Текущее UTC-время: {now.strftime('%Y-%m-%d %H:%M:%S')} (Час: {hour})")

    print("📡 Получаем данные о комиссиях с mempool.space...")
    fees = fetch_fee_estimates()

    print("🚀 Рекомендуемые комиссии:")
    print(f"🌪️ Экстренная (fastestFee): {fees['fastestFee']} sat/vByte")
    print(f"⚡ Срочная (halfHourFee): {fees['halfHourFee']} sat/vByte")
    print(f"🕰️ Стандарт (hourFee): {fees['hourFee']} sat/vByte")
    print(f"🛸 Медленная (economyFee): {fees['economyFee']} sat/vByte")

    if 0 <= hour <= 6 or 21 <= hour <= 23:
        print("📉 Сейчас низкая активность сети — можно ставить низкую комиссию.")
    elif 7 <= hour <= 16:
        print("📈 Сейчас высокая активность сети — лучше поставить повыше.")
    else:
        print("⚖️ Активность умеренная — стандартная комиссия подойдёт.")

if __name__ == "__main__":
    analyze_fees_by_time()
