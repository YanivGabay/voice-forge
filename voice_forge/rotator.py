"""
Voice Forge - Voice Rotator

Automatic voice rotation for variety in content creation.
"""

import random
import logging
from typing import Optional

from .tts import EdgeTTS
from .voices import EDGE_VOICES, VOICE_MOODS, get_voice_id

logger = logging.getLogger(__name__)


class VoiceRotator:
    """
    Rotate through voices for variety in content.

    Perfect for creating multiple videos/podcasts with different voices
    to keep content fresh and engaging.

    Example:
        >>> rotator = VoiceRotator()

        >>> # Random voice each time
        >>> tts = rotator.get_random_tts()
        >>> await tts.generate("Story 1...", "story1.mp3")

        >>> # Mood-based selection
        >>> tts = rotator.get_tts_for_mood("dramatic")
        >>> await tts.generate("The tension built...", "drama.mp3")

        >>> # Sequential rotation (deterministic)
        >>> for i, story in enumerate(stories):
        ...     tts = rotator.get_next_tts()
        ...     await tts.generate(story, f"story_{i}.mp3")
    """

    def __init__(
        self,
        voices: list[str] = None,
        mood_mapping: dict[str, list[str]] = None,
    ):
        """
        Initialize the voice rotator.

        Args:
            voices: List of voice names to rotate through.
                    Defaults to ["guy", "jenny", "aria", "ryan"]
            mood_mapping: Custom mood-to-voices mapping.
                         Defaults to VOICE_MOODS
        """
        self.voices = voices or ["guy", "jenny", "aria", "ryan"]
        self.mood_mapping = mood_mapping or VOICE_MOODS
        self._rotation_index = 0

    def get_random_voice(self) -> str:
        """
        Get a random voice from the rotation pool.

        Returns:
            Voice short name (e.g., "guy", "aria")
        """
        return random.choice(self.voices)

    def get_random_tts(self) -> EdgeTTS:
        """
        Get an EdgeTTS instance with a random voice.

        Returns:
            EdgeTTS configured with a random voice
        """
        voice = self.get_random_voice()
        return EdgeTTS(voice=voice)

    def get_voice_for_mood(self, mood: str) -> str:
        """
        Get an appropriate voice for the given mood/content type.

        Args:
            mood: Mood name (dramatic, happy, news, aita, etc.)
                  See VOICE_MOODS for all options.

        Returns:
            Voice short name appropriate for the mood
        """
        mood_lower = mood.lower()
        voice_options = self.mood_mapping.get(mood_lower, self.voices)
        return random.choice(voice_options)

    def get_tts_for_mood(self, mood: str) -> EdgeTTS:
        """
        Get an EdgeTTS instance with a mood-appropriate voice.

        Args:
            mood: Mood name (dramatic, happy, scary, news, etc.)

        Returns:
            EdgeTTS configured with an appropriate voice
        """
        voice = self.get_voice_for_mood(mood)
        return EdgeTTS(voice=voice)

    def get_next_voice(self) -> str:
        """
        Get the next voice in sequential rotation.

        This is deterministic - calling repeatedly cycles through
        all voices in order.

        Returns:
            Voice short name
        """
        voice = self.voices[self._rotation_index % len(self.voices)]
        self._rotation_index += 1
        return voice

    def get_next_tts(self) -> EdgeTTS:
        """
        Get an EdgeTTS instance with the next voice in rotation.

        Returns:
            EdgeTTS configured with the next voice
        """
        voice = self.get_next_voice()
        return EdgeTTS(voice=voice)

    def reset_rotation(self) -> None:
        """Reset the sequential rotation to the beginning."""
        self._rotation_index = 0

    def get_voice_id(self, name: str) -> str:
        """
        Get the full voice ID from a short name.

        Args:
            name: Short name (e.g., "guy") or full ID

        Returns:
            Full Edge TTS voice ID
        """
        return get_voice_id(name)

    def list_voices(self) -> list[str]:
        """List all voices in the rotation pool."""
        return list(self.voices)

    def list_all_voices(self) -> list[str]:
        """List all available Edge TTS voices."""
        return list(EDGE_VOICES.keys())

    def list_moods(self) -> list[str]:
        """List all available mood categories."""
        return list(self.mood_mapping.keys())

    def __repr__(self) -> str:
        return f"VoiceRotator(voices={self.voices})"


# Global singleton instance
_voice_rotator: Optional[VoiceRotator] = None


def get_voice_rotator() -> VoiceRotator:
    """
    Get the global voice rotator instance.

    Returns:
        Shared VoiceRotator instance
    """
    global _voice_rotator
    if _voice_rotator is None:
        _voice_rotator = VoiceRotator()
    return _voice_rotator


def reset_voice_rotator() -> None:
    """Reset the global voice rotator instance."""
    global _voice_rotator
    _voice_rotator = None
