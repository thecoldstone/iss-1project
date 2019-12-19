import os
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import spectrogram
from scipy.stats import pearsonr

"""To mean the input signal"""
def mean_signal(s):
    for i in range(len(s)):
        s[i] = s[i] - np.mean(s)

"""Get spectogram"""
def get_spec(signalData, fs, plot):
    f, t, sgr = spectrogram(signalData, fs, window=('tukey', .25), nperseg=400, noverlap=240, nfft=511)

    # (ve spektrogramu se obcas objevuji nuly, ktere se nelibi logaritmu, proto +1e-20)
    sgr_log = 10 * np.log10(sgr + 1e-20)

    if plot == 1:
        plot_spectogram(t,f,sgr_log)
        plot_show()

    return f, t, sgr_log

"""Find feature"""
def get_features(spec_data):
    return [sum(spec_data[i*16 : (i+1)*16 - 1]) for i in range(16)]

"""Find the scores of the input singals"""
def get_score(fS, fQ):
    #fS - sentence's features
    #fQ - query's features

    #Transpote matrices
    F = np.transpose(fS)
    Q = np.transpose(fQ)

    #List where we store scores
    score = list()

    #Find distance
    for pp in range(len(F) - len(Q)):
        rating = 0
        for x in range (len(Q)):
            rating += pearsonr(Q[x], F[x + pp])[0]
        score.append(rating / len(Q))

    #Add zeroes where is no number
    for i in range(len(Q)):
        score.append(np.nan)

    return score


def plot_spectogram(t, f, spec):
    plt.figure(figsize=(9,3))
    plt.pcolormesh(t, f, spec)
    plt.gca().set_xlabel('Time [s]')
    plt.gca().set_ylabel('Frequency [Hz]')
    cbar = plt.colorbar()
    cbar.set_label('Power spectral density [dB]', rotation=270, labelpad=15)
    plt.gca().set_title('Audio signal: ' + 'sa1.wav')

def plot_features(features, fs):
    plt.yticks(np.arange(17, step=4))
    plt.pcolormesh(features)

"""To draw it out"""
def plot_show():
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    #Path to the sentences and queries used in that project
    pathToDir = '../sentences/'
    pathToQueries = '../queries/'
    pathToOutPutImages = '../assets/signals&features&scores/'

    #Read queries
    qOne, qFsOne = sf.read(pathToQueries + 'q1.wav')
    qTwo, qFsTwo = sf.read(pathToQueries + 'q2.wav')

    #Analyse each wav file with two queries
    for filename in os.scandir(pathToDir):

        if filename.name.endswith('.wav'):

            pathToFile = pathToDir + filename.name

            #Cut the endings for changin to png
            spectogramePng = filename.name[:-4]

            #Read wav file
            s, fs = sf.read(pathToFile)
            duration = np.arange(s.size)/fs

            mean_signal(s)
            mean_signal(qOne)
            mean_signal(qTwo)

            """4.Task"""
            #For sentence
            specSen = get_spec(s, fs, 0)
            featuresSen = get_features(specSen[2])

            #For query one
            specQueryOne = get_spec(qOne, qFsOne, 0)
            featuresQueryOne = get_features(specQueryOne[2])

            #For query two
            specQueryTwo = get_spec(qTwo, qFsTwo, 0)
            featuresQueryTwo = get_features(specQueryTwo[2])

            """5.Task"""
            #Get score
            # print(len(featuresSen), len(featuresQueryOne), len(featuresQueryTwo))
            scoreSenQOne = get_score(featuresSen, featuresQueryOne)
            scoreSenQTwo = get_score(featuresSen, featuresQueryTwo)

            for i in scoreSenQOne:
                if i == 1:
                    print('Match')

            for i in scoreSenQTwo:
                if i == 1:
                    print('Match')

            # print(scoreSenQOne, scoreSenQTwo)

            # _, graph = plt.subplots(3, 1, figsize=(8, 6))
            #
            # graph[0].set_title('"downtown" and "examples vs ' + filename.name[:-4])
            # graph[0].plot(duration, s)
            # graph[0].set_xlabel('$t[s]$')
            # graph[0].set_ylabel('Signal')
            #
            # graph[1].pcolormesh(specSen[1], np.arange(16), featuresSen)
            # graph[1].set_xlabel('$t[s]$')
            # graph[1].set_ylabel('Features')
            # graph[1].invert_yaxis()
            #
            # downtown, = graph[2].plot(specSen[1], scoreSenQOne, label= 'downtown')
            # examples, = graph[2].plot(specSen[1], scoreSenQTwo, label= 'examples')
            # graph[2].legend(handles=[downtown, examples], loc='upper right')
            # graph[2].set_xlabel('$t[s]$')
            # graph[2].set_ylabel('Scores')
            #
            # plt.savefig(pathToOutPutImages + spectogramePng)