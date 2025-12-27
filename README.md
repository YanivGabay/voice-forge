# easy-edge-tts

> High-level TTS with voice rotation and mood selection for content creators

[![PyPI version](https://badge.fury.io/py/easy-edge-tts.svg)](https://badge.fury.io/py/easy-edge-tts)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**easy-edge-tts** makes text-to-speech dead simple. Built on top of Edge TTS (free, high-quality Microsoft voices), it adds voice rotation, mood-based selection, and word-level timestamps - everything content creators need.

## Features

- **Free** - Uses Microsoft Edge TTS (no API key needed)
- **20+ voices** - Male, female, US, UK, Australian accents
- **Mood-based selection** - Pick voices that match your content
- **Voice rotation** - Automatic variety across multiple generations
- **Word timestamps** - Perfect for synchronized subtitles
- **Async-first** - Built for modern Python

## Installation

```bash
pip install easy-edge-tts
```

For ElevenLabs support (premium voices):
```bash
pip install easy-edge-tts[elevenlabs]
```

## Quick Start

### Simple One-Liner

```python
from easy_edge_tts import speak

await speak("Hello world!", "output.mp3")
```

### Choose a Voice

```python
from easy_edge_tts import EdgeTTS

# Use a specific voice
tts = EdgeTTS(voice="aria")  # Expressive, dramatic female
result = await tts.generate("The tension was unbearable...", "drama.mp3")

print(f"Generated {result.duration:.1f}s of audio")
```

### Mood-Based Selection

```python
from easy_edge_tts import VoiceRotator

rotator = VoiceRotator()

# Get a voice that matches the mood
tts = rotator.get_tts_for_mood("dramatic")
await tts.generate("And then... everything changed.", "scene.mp3")

# Available moods: dramatic, suspense, scary, happy, sad, news, tutorial, podcast, aita, revenge, heartwarming, shocking
```

### Voice Rotation for Variety

```python
from easy_edge_tts import VoiceRotator

rotator = VoiceRotator()

stories = ["Story one...", "Story two...", "Story three..."]

for i, story in enumerate(stories):
    # Each story gets a different voice
    tts = rotator.get_next_tts()
    await tts.generate(story, f"story_{i}.mp3")
```

### Word-Level Timestamps (for subtitles)

```python
from easy_edge_tts import EdgeTTS

tts = EdgeTTS(voice="guy")
result, timestamps = await tts.generate_with_timestamps(
    "This is perfect for creating synchronized subtitles.",
    "output.mp3"
)

for word in timestamps:
    print(f"{word['start']:.2f}s - {word['end']:.2f}s: {word['text']}")
```

## Available Voices

| Name | Gender | Accent | Best For |
|------|--------|--------|----------|
| `guy` | Male | US | Storytelling, warm narratives |
| `jenny` | Female | US | Friendly, versatile content |
| `aria` | Female | US | Dramatic, emotional content |
| `davis` | Male | US | Professional, authoritative |
| `ryan` | Male | UK | British, formal content |
| `sonia` | Female | UK | British, warm professional |
| `thomas` | Male | UK | Deep, serious, dramatic |

[See all 20+ voices →](easy_edge_tts/voices.py)

## Mood Categories

Perfect for content creators who need the right voice for their content:

| Mood | Best Voices | Use Case |
|------|-------------|----------|
| `dramatic` | aria, guy, ryan | Reddit stories, drama |
| `suspense` | aria, thomas, davis | Thriller content |
| `happy` | jenny, sara, tony | Upbeat content |
| `news` | davis, nancy, ryan | News, reports |
| `aita` | guy, aria, jenny | "Am I The A-hole" stories |
| `tutorial` | jenny, guy, sara | How-to videos |

## Adjust Speed and Pitch

```python
from easy_edge_tts import EdgeTTS

tts = EdgeTTS(voice="guy")

# Faster for short-form content
await tts.generate("Quick update!", "fast.mp3", rate="+20%")

# Slower for dramatic effect
await tts.generate("And then...", "slow.mp3", rate="-30%")

# Higher pitch
await tts.generate("Exciting news!", "high.mp3", pitch="+10Hz")
```

## ElevenLabs (Premium)

For the most natural-sounding voices:

```python
from easy_edge_tts import ElevenLabsTTS

tts = ElevenLabsTTS(
    api_key="your-api-key",
    voice_id="your-voice-id"
)

result = await tts.generate("Premium quality voice.", "premium.mp3")
```

## Requirements

- Python 3.10+
- `ffprobe` (optional, for accurate duration detection)

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use in your projects!

---

Made for content creators
