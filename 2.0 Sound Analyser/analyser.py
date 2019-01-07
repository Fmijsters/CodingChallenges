import numpy as np

# matplotlib for displaying the output
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
import sys
# and IPython.display for audio output
import IPython.display

# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display


def generateMegSpectogram(y,sr):
	# Let's make and display a mel-scaled power (energy-squared) spectrogram
	S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

	# Convert to log scale (dB). We'll use the peak power (max) as reference.
	log_S = librosa.power_to_db(S, ref=np.max)

	# Make a new figure
	plt.figure(figsize=(12,4))

	# Display the spectrogram on a mel scale
	# sample rate and hop length parameters are used to render the time axis
	librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

	# Put a descriptive title on the plot
	plt.title('mel power spectrogram')

	# draw a color bar
	plt.colorbar(format='%+02.0f dB')

	# Make the figure layout compact
	# plt.tight_layout()

	plt.show()

def generateHarmonicPercussiveSourceSeperation(y,sr):
	y_harmonic, y_percussive = librosa.effects.hpss(y)
	# What do the spectrograms look like?
	# Let's make and display a mel-scaled power (energy-squared) spectrogram
	S_harmonic   = librosa.feature.melspectrogram(y_harmonic, sr=sr)
	S_percussive = librosa.feature.melspectrogram(y_percussive, sr=sr)

	# Convert to log scale (dB). We'll use the peak power as reference.
	log_Sh = librosa.power_to_db(S_harmonic, ref=np.max)
	log_Sp = librosa.power_to_db(S_percussive, ref=np.max)

	# Make a new figure
	plt.figure(figsize=(12,6))

	plt.subplot(2,1,1)
	# Display the spectrogram on a mel scale
	librosa.display.specshow(log_Sh, sr=sr, y_axis='mel')

	# Put a descriptive title on the plot
	plt.title('mel power spectrogram (Harmonic)')

	# draw a color bar
	plt.colorbar(format='%+02.0f dB')

	plt.subplot(2,1,2)
	librosa.display.specshow(log_Sp, sr=sr, x_axis='time', y_axis='mel')

	# Put a descriptive title on the plot
	plt.title('mel power spectrogram (Percussive)')

	# draw a color bar
	plt.colorbar(format='%+02.0f dB')

	# Make the figure layout compact
	plt.tight_layout()
	plt.show()

def generateChromagram(y,sr):
	y_harmonic, y_percussive = librosa.effects.hpss(y)
	# We'll use a CQT-based chromagram here.  An STFT-based implementation also exists in chroma_cqt()
	# We'll use the harmonic component to avoid pollution from transients
	C = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

	# Make a new figure
	plt.figure(figsize=(12,4))

	# Display the chromagram: the energy in each chromatic pitch class as a function of time
	# To make sure that the colors span the full range of chroma values, set vmin and vmax
	librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)

	plt.title('Chromagram')
	plt.colorbar()

	plt.tight_layout()
	plt.show()

def generateMFCC(y,sr):
	# Let's make and display a mel-scaled power (energy-squared) spectrogram
	S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

	# Convert to log scale (dB). We'll use the peak power (max) as reference.
	log_S = librosa.power_to_db(S, ref=np.max)
	# Next, we'll extract the top 13 Mel-frequency cepstral coefficients (MFCCs)
	mfcc        = librosa.feature.mfcc(S=log_S, n_mfcc=13)

	# Let's pad on the first and second deltas while we're at it
	delta_mfcc  = librosa.feature.delta(mfcc)
	delta2_mfcc = librosa.feature.delta(mfcc, order=2)

	# How do they look?  We'll show each in its own subplot
	plt.figure(figsize=(12, 6))

	plt.subplot(3,1,1)
	librosa.display.specshow(mfcc)
	plt.ylabel('MFCC')
	plt.colorbar()

	plt.subplot(3,1,2)
	librosa.display.specshow(delta_mfcc)
	plt.ylabel('MFCC-$\Delta$')
	plt.colorbar()

	plt.subplot(3,1,3)
	librosa.display.specshow(delta2_mfcc, sr=sr, x_axis='time')
	plt.ylabel('MFCC-$\Delta^2$')
	plt.colorbar()

	plt.tight_layout()
	plt.show()

	# For future use, we'll stack these together into one matrix
	M = np.vstack([mfcc, delta_mfcc, delta2_mfcc])

def generateBeatTracker(y,sr):
	# Let's make and display a mel-scaled power (energy-squared) spectrogram
	S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

	# Convert to log scale (dB). We'll use the peak power (max) as reference.
	log_S = librosa.power_to_db(S, ref=np.max)

	y_harmonic, y_percussive = librosa.effects.hpss(y)

	# Now, let's run the beat tracker.
	# We'll use the percussive component for this part
	plt.figure(figsize=(12, 6))
	tempo, beats = librosa.beat.beat_track(y=y_percussive, sr=sr)

	# Let's re-draw the spectrogram, but this time, overlay the detected beats
	plt.figure(figsize=(12,4))
	librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

	# Let's draw transparent lines over the beat frames
	plt.vlines(librosa.frames_to_time(beats),
	           1, 0.5 * sr,
	           colors='w', linestyles='-', linewidth=2, alpha=0.5)

	plt.axis('tight')

	plt.colorbar(format='%+02.0f dB')
	print('Estimat	ed tempo:        %.2f BPM' % tempo)

	print('First 5 beat frames:   ', beats[:5])

	# Frame numbers are great and all, but when do those beats occur?
	print('First 5 beat times:    ', librosa.frames_to_time(beats[:5], sr=sr))
	plt.tight_layout()
	plt.show()


def analyse(audio_path):
	y, sr = librosa.load(audio_path)
	print("Succes")
	# generateMegSpectogram(y,sr)
	# generateHarmonicPercussiveSourceSeperation(y,sr)
	generateChromagram(y,sr)
	# generateMFCC(y,sr)
	# generateBeatTracker(y,sr)







if __name__ == "__main__":
   if len(sys.argv) < 3:
   		print("please give a song path and an analyse method")
   		exit()
   analyse(sys.argv[1])
