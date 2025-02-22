import requests

iana_url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"

def get_tlds():
    try:
        # Fetch the list from IANA
        response = requests.get(iana_url)
        response.raise_for_status()  

        tlds = [line.strip() for line in response.text.splitlines() if line and not line.startswith("#")]

    except requests.RequestException as e:
        tlds = [
            "net", "me", "org", "us", "info", "la", "asia", "biz", "tv", "ws", "nyc", "okinawa", "online", "network", "ninja", "photo", "photography", "photos", "pics", "pictures", "pink", "pizza", "place", "plumbing", "press","productions", "reisen", "repair", "report", "republican", "rest", "restaurant", "reviews", "rich", "rip", "rocks", "paris", "partners", "sale", "sarl", "schule", "shiksha", "shoes", "singles", "social", "solar", "solutions", "space", "support", "surgery", "systems", "tattoo", "tax", "services", "sexy", "technology", "tips", "tires", "land", "juegos", "kaufen", "kim", "kitchen", "kiwi", "immo", "immobilien", "jetzt", "ink", "institute", "insure", "international", "investments", "guide", "guitars", "guru", "haus", "help", "hiphop", "holdings", "holiday", "host", "hosting", "house", "lawyer", "lease", "legal", "life", "lighting", "limited", "limo", "link", "loans", "london", "luxury", "maison", "management", "market", "marketing", "nagoya", "navy", "media", "memorial", "menu", "moda", "money", "mortgage", "blackfriday", "blue", "boutique", "builders", "business", "buzz", "bz", "auction", "audio", "band", "bar", "bid", "bike", "bio", "associates", "attorney", "agency", "airforce", "academy", "accountants", "coach", "codes", "coffee", "bargains", "bayern", "archi", "cab", "camera", "camp", "capital", "cards", "care", "careers", "casa", "cash", "catering", "cc", "center", "ceo", "cheap", "christmas", "church", "city", "claims", "company", "construction", "consulting", "contractors", "cool", "deals", "degree", "delivery", "democrat", "dental", "dentist", "desi"
        ]

    return tlds