import re


RENTAL_KEYWORDS = [
    "租房", "转租", "出租", "找室友", "合租",
    "sublet", "lease", "rent", "rental",
    "studio", "1b1b", "2b2b", "3b2b",
    "主卧", "次卧", "单间"
]

LOCATIONS = [
    "UBC", "Vancouver", "温哥华", "Downtown", "Richmond",
    "Burnaby", "Metrotown", "Surrey", "Coquitlam",
    "Kitsilano", "Kerrisdale", "Yaletown", "West End"
]

ROOM_TYPES = [
    "studio", "1b1b", "2b2b", "3b2b",
    "主卧", "次卧", "单间", "合租", "客厅",
    "独立卫浴", "shared room"
]


def is_rental_post(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in RENTAL_KEYWORDS)


def extract_price(text: str):
    patterns = [
        r"\$\s?(\d{3,5})",
        r"(\d{3,5})\s?(刀|cad|CAD|加币|/月|每月|monthly|per month)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    return None


def extract_location(text: str):
    text_lower = text.lower()

    for location in LOCATIONS:
        if location.lower() in text_lower:
            return location

    return None


def extract_room_type(text: str):
    text_lower = text.lower()

    for room_type in ROOM_TYPES:
        if room_type.lower() in text_lower:
            return room_type

    return None


def extract_move_in_date(text: str):
    patterns = [
        r"(\d{1,2})月(\d{1,2})日?",
        r"(\d{1,2})月入住",
        r"(May|June|July|August|September|October|November|December)\s?\d{0,2}",
        r"available now",
        r"随时入住"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)

    return None


def extract_contact(text: str):
    patterns = [
        r"微信[:：]?\s?([a-zA-Z0-9_-]+)",
        r"vx[:：]?\s?([a-zA-Z0-9_-]+)",
        r"WeChat[:：]?\s?([a-zA-Z0-9_-]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)

    return None


def extract_rental_info(text: str, url: str = "", title: str = "") -> dict:
    return {
        "title": title,
        "url": url,
        "is_rental": is_rental_post(text),
        "price": extract_price(text),
        "location": extract_location(text),
        "room_type": extract_room_type(text),
        "move_in_date": extract_move_in_date(text),
        "contact": extract_contact(text),
        "raw_text": text
    }


if __name__ == "__main__":
    sample_text = """
    UBC附近1b1b转租，$1850/月，6月1日入住。
    包家具水电，近公交，微信 abc123。
    """

    result = extract_rental_info(sample_text)
    print(result)