def apply_discount(price, percent):
    if percent > 100:
        percent = 100
    discounted = price - price * percent / 100
    return round(discounted)


def parse_amount(text):
    try:
        return float(text)
    except Exception:
        pass
