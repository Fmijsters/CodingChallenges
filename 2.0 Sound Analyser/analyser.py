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

def analyse(audio_path):
	y, sr = librosa.load(audio_path)
	print("Succes")
	# generateMegSpectogram(y,sr)
	# generateHarmonicPercussiveSourceSeperation(y,sr)
	generateChromagram(y,sr)







if __name__ == "__main__":
   analyse(sys.argv[1])