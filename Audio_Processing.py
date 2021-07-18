from pydub import AudioSegment
import subprocess
import os
import shutil


# for converting stereo sound into mono
def mono(audio_data):

    audio = AudioSegment.from_file(audio_data)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    mono_audio = audio.export(format="wav")
    return mono_audio


def enhance():
    # function to execute fb-denoiser

    subprocess.run([
        "python", "-m", "denoiser.enhance", "--dns48", "--noisy_dir", ".tmp", "--out_dir", ".tmp",
        "--sample_rate", "16000", "--num_workers", "1", "--device", "cpu"], shell=True)


def process(audio_data):

    os.mkdir(".tmp")

    audio = AudioSegment.from_wav(mono(audio_data))
    audio.export(".tmp/audio.wav", format="wav")
    enhance()

    enhanced_sound = AudioSegment.export(AudioSegment.from_wav(mono(".tmp/audio_enhanced.wav")), format="wav")

    shutil.rmtree(".tmp")
    return enhanced_sound

