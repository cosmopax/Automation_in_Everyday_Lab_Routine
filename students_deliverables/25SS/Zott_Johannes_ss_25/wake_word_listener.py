"""
Simple Wake-Word Listener
=========================

A simplified implementation that uses the SpeechRecognition package and Google’s
online speech-to-text service to detect a spoken wake-phrase such as
“hey computer”.  Once the phrase is heard it calls a user-supplied callback
function (default prints to console) and then continues listening.

"""

import sys
import time
from datetime import datetime

# ---------------------------------------------------------------------------
# Dependency Import
# ---------------------------------------------------------------------------
try:
    import speech_recognition as sr         # High-level speech-to-text wrapper
    import pyaudio                          # Low-level microphone access
except ImportError as e:
    # If either library is missing, print instructions and exit gracefully.
    print(f"ERROR: Required dependency missing: {e}")
    print("Install with:  pip install SpeechRecognition pyaudio")
    sys.exit(1)


class SimpleWakeWordListener:
    """
    Continuously captures microphone audio and checks each recognized
    phrase for one of the configured wake-phrases.

    • wake_phrases : list of strings that should trigger the callback.
                     Modify/extend this list to add new trigger words.
    • callback     : function executed when a wake-phrase is detected.
                     Replace with your own function to launch other programs
                     or kick off an STT pipeline.
    """

    def __init__(self, wake_phrases=None, callback=None):
        # -------------------------------------------------------------------
        # Configure wake-phrases and callback
        # -------------------------------------------------------------------
        self.wake_phrases = wake_phrases or [
            "hey omni",
            "hey computer",
            "wake up"
        ]                                   # ←--- Add/remove phrases here
        self.callback = callback or self._default_callback

        # -------------------------------------------------------------------
        # SpeechRecognition setup
        # -------------------------------------------------------------------
        self.recognizer = sr.Recognizer()   # Performs STT
        self.microphone = sr.Microphone()   # Interface to system mic

        # Runtime state
        self.running = False
        self.total_detections = 0
        self.start_time = None

        # Fine-tune recognizer thresholds for ambient noise and silence gaps
        self._configure_recognizer()

    # -----------------------------------------------------------------------
    # Recognizer configuration
    # -----------------------------------------------------------------------
    def _configure_recognizer(self):
        """One-time mic calibration and threshold tuning."""

        print(" Calibrating microphone for ambient noise (2 s)…")
        with self.microphone as source:
            # Listen to background noise for 2 s to set energy threshold
            self.recognizer.adjust_for_ambient_noise(source, duration=2)

        # Optional manual tweaks (raise/lower if false positives occur)
        self.recognizer.energy_threshold = 300          # Minimum volume
        self.recognizer.dynamic_energy_threshold = True # Auto-adapt
        self.recognizer.pause_threshold = 0.8           # Silence = phrase end
        self.recognizer.phrase_threshold = 0.3          # Min length (s)
        self.recognizer.non_speaking_duration = 0.5     # Silence padding
        print("✓ Microphone calibrated")

    # -----------------------------------------------------------------------
    # Default callback (prints info).  Replace with your own logic.
    # -----------------------------------------------------------------------
    def _default_callback(self, wake_phrase, confidence, timestamp):
        """
        Runs when a wake-phrase is detected.  
        """
        print("\n Wake-word detected!")
        print(f"   Phrase      : {wake_phrase}")
        print(f"   Confidence  : {confidence:.2f}")
        print(f"   Time        : {timestamp.strftime('%H:%M:%S.%f')[:-3]}")
        print(f"   Detections  : {self.total_detections}\n")

    # -----------------------------------------------------------------------
    # Background audio handler
    # -----------------------------------------------------------------------
    def _process_audio(self, recognizer, audio):
        """
        Executed in a background thread for every 5-second chunk (see
        phrase_time_limit).  Converts audio to text via Google STT and looks
        for any wake-phrase substring.
        """
        try:
            text = recognizer.recognize_google(audio, language="en-US").lower()

            # DEBUG: show everything Google heard when --verbose flag enabled
            if getattr(self, "verbose", False):
                print(f"Recognized: “{text}”")

            # Check each configured phrase
            for wake_phrase in self.wake_phrases:
                if wake_phrase in text:
                    self.total_detections += 1
                    timestamp = datetime.now()

                    # Naïve “confidence” estimation (length ratio)
                    confidence = min(len(text) / len(wake_phrase), 1.0)

                    # Trigger the user callback
                    self.callback(wake_phrase, confidence, timestamp)
                    break

        except sr.UnknownValueError:
            # Normal when Google cannot understand the audio
            pass
        except sr.RequestError as e:
            print(f"Google STT request failed: {e}")

    # -----------------------------------------------------------------------
    # Public control methods
    # -----------------------------------------------------------------------
    def start(self):
        """Initializes mic stream and spawns background STT thread."""
        print(" Starting Simple Wake-Word Listener…")
        print(f"   Wake-phrases : {self.wake_phrases}")
        print("   Engine       : Google Speech Recognition")

        # Verify microphone availability early
        try:
            with self.microphone as _:
                pass
        except Exception as e:
            print(f" Microphone error: {e}")
            return False

        self.running = True
        self.start_time = time.time()

        # Non-blocking background listener; returns a stopper function
        self.stop_listening = self.recognizer.listen_in_background(
            self.microphone,
            self._process_audio,
            phrase_time_limit=5   # ←--- Increase if phrases are cut off
        )

        print("✓ Listening…  (Ctrl-C to stop)\n")
        return True

    def run(self):
        """
        Convenience wrapper: call .start() then keep the main thread alive.
        Use in scripts.  For notebooks, you might call .start() only.
        """
        if not self.start():
            return False

        try:
            while self.running:
                time.sleep(0.1)  # Idle loop
        except KeyboardInterrupt:
            print("\n Keyboard interrupt received – shutting down")

        self.stop()
        return True

    def stop(self):
        """Gracefully terminate background thread and print session stats."""
        self.running = False
        if hasattr(self, "stop_listening"):
            self.stop_listening(wait_for_stop=False)

        if self.start_time:
            runtime = time.time() - self.start_time
            print("\n Session Statistics")
            print(f"   Runtime        : {runtime:.1f}s")
            print(f"   Total detections: {self.total_detections}")

        print(" Listener stopped")


# ---------------------------------------------------------------------------
# Example callback that pretends to launch an STT module
# ---------------------------------------------------------------------------
def create_callback_with_action():
    """
    Builds and returns a custom callback.  Replace the body of the inner
    function to launch your code (e.g., speech-to-text pipeline, shell
    command, home-automation action). 
    """
    def callback(wake_phrase, confidence, timestamp):
        print(f"\n “{wake_phrase}” detected at {timestamp:%H:%M:%S}")
        print(" Simulating STT activation…")

        # Placeholder countdown before recording starts
        for i in range(3, 0, -1):
            print(f"   Recording in {i}")
            time.sleep(1)

        # >>>>>>  INSERT YOUR REAL STT / COMMAND HERE  <<<<<<
        print("    Recording started!  (Integrate STT here)")
        # e.g.  subprocess.Popen(["python", "my_stt_script.py"])

        print(" Ready for next wake-word\n")

    return callback


# ---------------------------------------------------------------------------
# Command-line entry point
# ---------------------------------------------------------------------------
def main():
    """
    Parses CLI arguments, constructs SimpleWakeWordListener, and runs it.

    Modifiable options:
        • --wake-phrases : add any number of trigger words/phrases.
        • --verbose      : print every recognized phrase for debugging.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Simple Wake-Word Listener")
    parser.add_argument(
        "--wake-phrases",
        nargs="+",
        default=["hey omni", "hey computer"],
        help="Wake phrases to detect (case-insensitive)."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show all recognized text (useful for tuning thresholds)."
    )
    args = parser.parse_args()

    # Build custom callback (replace with your own if desired)
    callback = create_callback_with_action()

    # Instantiate listener with user-supplied phrases
    listener = SimpleWakeWordListener(args.wake_phrases, callback)
    listener.verbose = args.verbose

    # Blocking run loop
    success = listener.run()
    return 0 if success else 1


# ---------------------------------------------------------------------------
# Run when the file is executed directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
