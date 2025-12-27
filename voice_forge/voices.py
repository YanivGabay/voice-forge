"""
Voice Forge - Voice Definitions

Curated collection of Edge TTS voices organized by characteristics.
"""

# High-quality Edge TTS voices for content creation
EDGE_VOICES = {
    # US English - Male
    "guy": "en-US-GuyNeural",           # Natural, warm male
    "davis": "en-US-DavisNeural",       # Professional male
    "tony": "en-US-TonyNeural",         # Friendly male
    "jason": "en-US-JasonNeural",       # Clear male

    # US English - Female
    "jenny": "en-US-JennyNeural",       # Natural, friendly female
    "aria": "en-US-AriaNeural",         # Expressive, dramatic female
    "sara": "en-US-SaraNeural",         # Warm female
    "nancy": "en-US-NancyNeural",       # Professional female

    # UK English
    "ryan": "en-GB-RyanNeural",         # British male
    "sonia": "en-GB-SoniaNeural",       # British female
    "thomas": "en-GB-ThomasNeural",     # British male, deeper

    # Australian English
    "william": "en-AU-WilliamNeural",   # Australian male
    "natasha": "en-AU-NatashaNeural",   # Australian female

    # Other accents
    "connor": "en-IE-ConnorNeural",     # Irish male
    "emily": "en-IE-EmilyNeural",       # Irish female
    "sam": "en-HK-SamNeural",           # Hong Kong English male
}

# Voice categories for easy selection
VOICE_CATEGORIES = {
    "male": ["guy", "davis", "tony", "jason", "ryan", "thomas", "william", "connor"],
    "female": ["jenny", "aria", "sara", "nancy", "sonia", "natasha", "emily"],
    "us": ["guy", "davis", "tony", "jason", "jenny", "aria", "sara", "nancy"],
    "uk": ["ryan", "sonia", "thomas"],
    "expressive": ["aria", "jenny", "guy"],
    "professional": ["davis", "nancy", "ryan"],
    "warm": ["guy", "sara", "jenny"],
}

# Mood-to-voice mapping for content creation
VOICE_MOODS = {
    # Storytelling moods
    "dramatic": ["aria", "guy", "ryan"],
    "suspense": ["aria", "thomas", "davis"],
    "scary": ["thomas", "aria", "davis"],
    "mysterious": ["aria", "thomas", "sonia"],

    # Emotional moods
    "happy": ["jenny", "sara", "tony"],
    "sad": ["sonia", "nancy", "guy"],
    "angry": ["davis", "aria", "thomas"],
    "excited": ["aria", "jenny", "tony"],

    # Content type moods
    "news": ["davis", "nancy", "ryan"],
    "documentary": ["guy", "sonia", "davis"],
    "tutorial": ["jenny", "guy", "sara"],
    "podcast": ["guy", "jenny", "ryan"],

    # Reddit story moods (common use case)
    "aita": ["guy", "aria", "jenny"],  # Am I The Asshole
    "tifu": ["guy", "tony", "jenny"],  # Today I F'd Up
    "revenge": ["aria", "davis", "thomas"],
    "heartwarming": ["jenny", "sara", "guy"],
    "shocking": ["aria", "thomas", "guy"],

    # Default/neutral
    "neutral": ["guy", "jenny", "davis"],
    "default": ["guy", "jenny"],
}

# Voice characteristics for documentation
VOICE_INFO = {
    "guy": {"gender": "male", "accent": "us", "style": "natural, warm, storytelling"},
    "jenny": {"gender": "female", "accent": "us", "style": "friendly, clear, versatile"},
    "aria": {"gender": "female", "accent": "us", "style": "expressive, dramatic, emotional"},
    "davis": {"gender": "male", "accent": "us", "style": "professional, authoritative"},
    "ryan": {"gender": "male", "accent": "uk", "style": "british, clear, formal"},
    "sonia": {"gender": "female", "accent": "uk", "style": "british, warm, professional"},
    "thomas": {"gender": "male", "accent": "uk", "style": "deep, serious, dramatic"},
}


def get_voice_id(name: str) -> str:
    """
    Get the full voice ID from a short name.

    Args:
        name: Short name (e.g., "guy") or full ID (e.g., "en-US-GuyNeural")

    Returns:
        Full voice ID for Edge TTS
    """
    name_lower = name.lower()
    if name_lower in EDGE_VOICES:
        return EDGE_VOICES[name_lower]
    # Assume it's already a full voice ID
    return name


def list_voices(category: str = None) -> list[str]:
    """
    List available voice names.

    Args:
        category: Optional filter (male, female, us, uk, expressive, etc.)

    Returns:
        List of voice short names
    """
    if category and category in VOICE_CATEGORIES:
        return VOICE_CATEGORIES[category]
    return list(EDGE_VOICES.keys())


def get_voices_for_mood(mood: str) -> list[str]:
    """
    Get recommended voices for a mood/content type.

    Args:
        mood: Mood name (dramatic, happy, news, aita, etc.)

    Returns:
        List of recommended voice short names
    """
    mood_lower = mood.lower()
    return VOICE_MOODS.get(mood_lower, VOICE_MOODS["default"])
