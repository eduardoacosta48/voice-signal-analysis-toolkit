[README.md](https://github.com/user-attachments/files/27072195/README.md)
## About Me

Audio engineer specializing in voice, ADR, and post-production workflows.  
Currently pursuing Electrical Engineering with a focus on signal processing.

This project bridges real-world audio engineering with technical signal analysis.
# Voice Signal Analysis Toolkit

A beginner-friendly audio engineering and signal-processing project focused on voice analysis, cleanup, and technical listening workflows.

This project demonstrates foundational DSP skills relevant to dialogue editing, ADR, podcast production, voice cleanup, and AI voice workflows.

## Project Goals

- Load and analyze voice recordings
- Visualize waveform and frequency content
- Generate a spectrogram
- Apply basic filtering for voice cleanup
- Export processed audio
- Document technical observations like noise, frequency buildup, and intelligibility

## Why This Project Matters

For voice-focused audio roles, especially companies working with synthetic voice, dubbing, ADR, and voice quality, it is important to understand what makes a voice recording clean, consistent, and usable.

This project connects audio engineering experience with signal-processing tools.

## Tools Used

- Python
- NumPy
- SciPy
- Matplotlib
- SoundFile

## Recommended Folder Structure

```text
voice_signal_analysis_project/
│
├── README.md
├── requirements.txt
├── analyze_voice.py
├── notes_voice_quality.md
└── audio_samples/
    └── place_your_voice_file_here.wav
```

## How to Use

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add a WAV file into the `audio_samples` folder.

3. Run:

```bash
python analyze_voice.py audio_samples/your_file.wav
```

4. The script will create:
- waveform plot
- frequency spectrum plot
- spectrogram
- filtered audio export

## Audio Concepts Demonstrated

- Waveform analysis
- Frequency-domain analysis using FFT
- Spectrogram interpretation
- High-pass filtering
- Voice cleanup preparation
- Technical documentation

## Future Improvements

- Add noise reduction
- Add LUFS loudness measurement
- Add automatic silence trimming
- Add comparison between raw ADR and edited ADR
- Add voice consistency metrics across multiple takes
