def apply_discount(price, percent):
    if percent > 100:
        percent = 100
    discounted = price - price * percent / 100
    return round(discounted, 2)


def parse_amount(text):
    try:
        return float(text)
    except Exception:
        return None
