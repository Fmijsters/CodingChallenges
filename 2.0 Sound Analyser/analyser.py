import numpy as np

# matplotlib for displaying the output
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
import sys
from pychord import Chord
# and IPython.display for audio output
import IPython.display

# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display

global path

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

def findChord(list_values):
	index_of_highest = -1
	highest_value = -1
	formatter = librosa.display.ChromaFormatter()
	for i,value in enumerate(list_values):
		if value > highest_value:
			index_of_highest = i
			highest_value = value
	if highest_value == 0:
		return "No Chord"
	return str(formatter.format_data(index_of_highest))
	
def clean_map(chords_map):
	teller= 0
	teller2 = 0
	array = list()
	for key,value in chords_map.items():
		if value == "No Chord":
			array.append(key)
	for value in array:
		del chords_map[value]
	return chords_map
	
def getMapByChromaOrig(chroma_orig,y,sr):
	frame_count = chroma_orig.shape[1]
	total_time= 0
	chord_by_time_map ={}
	for i in range(1,frame_count):
		times = librosa.core.frames_to_time([i-1,i],sr=sr,hop_length=512)
		total_time = total_time + (times[1] - times[0])
	rounded_time = round(total_time,2)
	teller = 0.00
	time_array = list()
	while teller != round(rounded_time + 0.01,2):
		time_array.append(teller)
		teller = round(teller + 0.01,2)
	prev_value = 0
	for i,value in enumerate(time_array):
		idx = [slice(None), slice(*list(librosa.time_to_frames([prev_value, value])))]
		if i == 0:
			continue
		if chroma_orig[idx].shape[1] == 0:
			continue
		chord = findChord(chroma_orig[idx])
		chord_by_time_map[prev_value] = chord
		prev_value = value

	return clean_map(chord_by_time_map)
def checkAllEqualInList(lst):
	if len(lst) == 0:
		return False
	return lst[1:] == lst[:-1]

def summarizeChords(chords_map):
	teller =0
	teller2 =0
	total_array = {}
	for key,value in chords_map.items():
		roundend_key = round(key,1)
		if roundend_key in total_array:
			array = total_array[roundend_key]
			array.append(value)
			total_array[roundend_key] = array
		else:
			new_array = list()
			new_array.append(value)
			total_array[roundend_key] = new_array
	cleanList = {}
	for key,value in total_array.items():
		if checkAllEqualInList(value):
			cleanList[key] = value[0]
	return cleanList

def generateChromagram(y,sr):
	global path
	y_harmonic, y_percussive = librosa.effects.hpss(y)
	chroma_orig = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr, hop_length=512)
	
	chords_map_by_time = getMapByChromaOrig(chroma_orig,y,sr)

	summarized_chords = summarizeChords(chords_map_by_time)

	for key,value in summarized_chords.items():
		c = Chord(value)
		c.transpose(-4)
		print(str(key) + ": " + str(c))



	plt.figure(figsize=(12,4))
	librosa.display.specshow(chroma_orig, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
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


def analyse(audio_path,analyse_method):
	global path
	path = audio_path
	y, sr = librosa.load(audio_path)
	print("Succes")

	if analyse_method == "meg":
		generateMegSpectogram(y,sr)
	elif analyse_method == "hpss":
		generateHarmonicPercussiveSourceSeperation(y,sr)
	elif analyse_method == "chromagram":
		generateChromagram(y,sr)
	elif analyse_method == "mfcc":
		generateMFCC(y,sr)
	elif analyse_method == "bt":
		generateBeatTracker(y,sr)

if __name__ == "__main__":
   if len(sys.argv) < 3:
   		print("please give a song path and an analyse method")
   		print("Choose between: ")
   		print("Meg spectogram: meg")
   		print("Generate harmonic percussive source spereration: hpss")
   		print("Generate Chromagram: chromagram")
   		print("Generate MFCC: mfcc")
   		print("Generate beat tracker: bt")
   		exit()
   else:
   		audio_path = sys.argv[1]
   		analyse_method = sys.argv[2].lower()
   		analyse(audio_path,analyse_method)
