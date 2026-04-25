"""
Voice Signal Analysis Toolkit

Usage:
    python analyze_voice.py path/to/audio.wav

This script:
- Loads a mono or stereo WAV file
- Converts stereo to mono for analysis
- Plots waveform
- Plots frequency spectrum using FFT
- Creates a spectrogram
- Applies a basic high-pass filter for voice cleanup
- Exports a processed WAV file

Author: Eduardo Acosta
"""

import sys
from pathlib import Path

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, spectrogram


def load_audio(file_path: Path):
    audio, sample_rate = sf.read(file_path)

    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    return audio, sample_rate


def normalize_audio(audio: np.ndarray):
    peak = np.max(np.abs(audio))
    if peak == 0:
        return audio
    return audio / peak


def high_pass_filter(audio: np.ndarray, sample_rate: int, cutoff_hz: float = 80.0, order: int = 4):
    nyquist = 0.5 * sample_rate
    normalized_cutoff = cutoff_hz / nyquist
    b, a = butter(order, normalized_cutoff, btype="highpass")
    return filtfilt(b, a, audio)


def plot_waveform(audio: np.ndarray, sample_rate: int, output_folder: Path):
    time = np.arange(len(audio)) / sample_rate

    plt.figure(figsize=(12, 4))
    plt.plot(time, audio)
    plt.title("Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig(output_folder / "waveform.png", dpi=200)
    plt.close()


def plot_frequency_spectrum(audio: np.ndarray, sample_rate: int, output_folder: Path):
    n = len(audio)
    fft_values = np.fft.rfft(audio)
    fft_freqs = np.fft.rfftfreq(n, 1 / sample_rate)

    magnitude = np.abs(fft_values)

    plt.figure(figsize=(12, 4))
    plt.plot(fft_freqs, magnitude)
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, 10000)
    plt.tight_layout()
    plt.savefig(output_folder / "frequency_spectrum.png", dpi=200)
    plt.close()


def plot_spectrogram(audio: np.ndarray, sample_rate: int, output_folder: Path):
    frequencies, times, spec = spectrogram(audio, fs=sample_rate)

    plt.figure(figsize=(12, 5))
    plt.pcolormesh(times, frequencies, 10 * np.log10(spec + 1e-12), shading="gouraud")
    plt.title("Spectrogram")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency (Hz)")
    plt.ylim(0, 10000)
    plt.colorbar(label="Intensity (dB)")
    plt.tight_layout()
    plt.savefig(output_folder / "spectrogram.png", dpi=200)
    plt.close()


def write_report(file_path: Path, audio: np.ndarray, sample_rate: int, output_folder: Path):
    duration = len(audio) / sample_rate
    peak = np.max(np.abs(audio))
    rms = np.sqrt(np.mean(audio ** 2))

    report = f"""# Voice Analysis Report

## File
{file_path.name}

## Technical Summary
- Sample rate: {sample_rate} Hz
- Duration: {duration:.2f} seconds
- Peak amplitude: {peak:.4f}
- RMS level: {rms:.4f}

## Listening Notes
Add your own notes here:
- Is the voice clear?
- Is there background noise?
- Is there low-end rumble?
- Are there mouth clicks or harsh consonants?
- Does the recording feel consistent?

## Processing Applied
- Converted stereo to mono if needed
- Normalized audio for analysis
- Applied high-pass filter at 80 Hz

## Relevance
This analysis supports voice cleanup, ADR review, podcast production, and preparation of clean voice recordings for modern audio workflows.
"""
    (output_folder / "voice_analysis_report.md").write_text(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_voice.py path/to/audio.wav")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    output_folder = Path("output") / file_path.stem
    output_folder.mkdir(parents=True, exist_ok=True)

    audio, sample_rate = load_audio(file_path)
    audio = normalize_audio(audio)

    processed_audio = high_pass_filter(audio, sample_rate, cutoff_hz=80.0)

    plot_waveform(audio, sample_rate, output_folder)
    plot_frequency_spectrum(audio, sample_rate, output_folder)
    plot_spectrogram(audio, sample_rate, output_folder)

    sf.write(output_folder / "processed_high_pass_voice.wav", processed_audio, sample_rate)
    write_report(file_path, audio, sample_rate, output_folder)

    print(f"Analysis complete. Files saved to: {output_folder}")


if __name__ == "__main__":
    main()
