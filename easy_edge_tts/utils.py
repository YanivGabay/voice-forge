"""
Voice Forge - Utilities

Helper functions for audio processing.
"""

import subprocess
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def get_audio_duration(audio_path: Path | str) -> float:
    """
    Get audio file duration in seconds using ffprobe.

    Args:
        audio_path: Path to audio file

    Returns:
        Duration in seconds, or 0.0 if detection fails

    Example:
        >>> duration = get_audio_duration("speech.mp3")
        >>> print(f"Audio is {duration:.1f} seconds long")
    """
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(audio_path)
            ],
            capture_output=True,
            text=True,
            timeout=30
        )
        return float(result.stdout.strip())
    except (subprocess.TimeoutExpired, ValueError, AttributeError, FileNotFoundError) as e:
        logger.debug(f"Could not get audio duration: {e}")
        return 0.0


def estimate_duration(text: str, words_per_minute: int = 150) -> float:
    """
    Estimate speech duration from text.

    Args:
        text: Text to estimate
        words_per_minute: Speaking rate (default: 150 wpm, natural pace)

    Returns:
        Estimated duration in seconds

    Example:
        >>> estimate_duration("Hello world, this is a test.")
        2.4
    """
    word_count = len(text.split())
    return (word_count / words_per_minute) * 60


def check_ffprobe_available() -> bool:
    """Check if ffprobe is available on the system."""
    try:
        subprocess.run(
            ["ffprobe", "-version"],
            capture_output=True,
            timeout=5
        )
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False
