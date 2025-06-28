# Simple Wake-Word Listener

A Python-based wake-word detection system that continuously listens for specific phrases like "hey omni" or "hey computer" and triggers customizable actions when detected.

## Overview

This wake-word listener provides a hands-free way to activate voice assistants or trigger automated actions. Unlike dedicated wake-word engines, this implementation uses Google's Speech Recognition API for simplicity and ease of understanding, making it perfect for prototyping and educational purposes.

## Features

- **Continuous Listening**: Runs in the background, monitoring microphone input
- **Customizable Wake Phrases**: Easily add or modify trigger words/phrases
- **Flexible Callbacks**: Execute any Python function when wake-words are detected
- **Automatic Calibration**: Adjusts to ambient noise levels automatically
- **Verbose Mode**: Debug mode to see all recognized speech
- **Session Statistics**: Track detection counts and runtime metrics

## Requirements

- Python 3.6+
- Active internet connection (uses Google Speech Recognition API)
- Working microphone
- Required Python packages:
  - `SpeechRecognition`
  - `pyaudio`

## Installation

1. **Clone or download the script**:
   ```bash
   # Save the code as wake_word_listener.py
   ```

2. **Install dependencies**:
   ```bash
   pip install SpeechRecognition pyaudio
   ```


##  Usage

### Basic Usage

Run with default wake phrases ("hey omni", "hey computer"):
```bash
python wake_word_listener.py
```

### Custom Wake Phrases

Specify your own trigger words:
```bash
python wake_word_listener.py --wake-phrases "activate assistant" "hello system" "wake up jarvis"
```

### Debug Mode

See all recognized speech (useful for troubleshooting):
```bash
python wake_word_listener.py --verbose
```

### Combined Options

```bash
python wake_word_listener.py --wake-phrases "ok computer" "hey assistant" --verbose
```

### Using in Jupyter Notebooks

```python
# Install dependencies
!pip install SpeechRecognition pyaudio

# Run the script
%run wake_word_listener.py --verbose
```

##  Configuration

### Wake Phrases

Modify the default wake phrases by editing the code:
```python
self.wake_phrases = wake_phrases or [
    "hey omni",           # ← Add your phrases here
    "hey computer",
    "wake up",
    "activate system"     # ← New phrase example
]
```

### Audio Settings

Adjust recognition sensitivity in `_configure_recognizer()`:
```python
self.recognizer.energy_threshold = 300      # Lower = more sensitive
self.recognizer.pause_threshold = 0.8       # Silence before phrase ends
self.recognizer.phrase_threshold = 0.3      # Minimum phrase length
```

### Callback Customization

Replace the callback function to trigger your own actions:
```python
def create_callback_with_action():
    def callback(wake_phrase, confidence, timestamp):
        print(f"Wake word detected: {wake_phrase}")
        
        # Your custom action here:
        # subprocess.run(["python", "my_voice_assistant.py"])
        # send_http_request("http://localhost:8080/wake")
        # trigger_home_automation()
        
    return callback
```

## Integration Examples

### STT Pipeline Integration

```python
def stt_integration_callback(wake_phrase, confidence, timestamp):
    print(f"🎯 Wake-word '{wake_phrase}' detected!")
    
    # Start recording for command
    audio_data = record_user_command()
    command_text = transcribe_audio(audio_data)
    execute_command(command_text)
    
    print("✓ Ready for next wake-word")
```


### Subprocess Execution

```python
def launch_program_callback(wake_phrase, confidence, timestamp):
    import subprocess
    subprocess.Popen(["python", "voice_assistant.py"])
```

##  Output Example

```
 Calibrating microphone for ambient noise (2 s)…
✓ Microphone calibrated
   Starting Simple Wake-Word Listener…
   Wake-phrases : ['hey omni', 'hey computer']
   Engine       : Google Speech Recognition
✓ Listening…  (Ctrl-C to stop)

 "hey omni" detected at 14:32:15
 Simulating STT activation…
   Recording in 3
   Recording in 2
   Recording in 1
 Recording started!  (Integrate STT here)
✓ Ready for next wake-word

   Session Statistics
   Runtime        : 45.2s
   Total detections: 3
✓ Listener stopped
```

##  Troubleshooting

### Common Issues

**Microphone not detected**:
- Check system audio permissions
- Verify microphone is not muted
- Test with other audio applications

**No wake-word detection**:
- Enable `--verbose` mode to see recognized text
- Speak clearly and closer to microphone
- Lower `energy_threshold` in configuration
- Check internet connection (requires Google API)

**High false positives**:
- Raise `energy_threshold` value
- Increase `pause_threshold`
- Use more specific wake phrases

**Installation errors**:
- Update pip: `pip install --upgrade pip`
- Try: `pip install --upgrade pyaudio`
- Use virtual environment to avoid conflicts

### Performance Notes

- **Latency**: 1-2 seconds (higher than dedicated engines)
- **Internet**: Required for Google Speech API
- **Accuracy**: Good for clear speech in quiet environments

## License

This project is provided as-is for educational and prototyping purposes.

