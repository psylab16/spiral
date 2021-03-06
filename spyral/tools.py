# -*- coding: utf-8 -*-

"""
Spiral Python functions.
"""
import numpy as np

fir_host = np.array([  5.58149986e-05,   8.75499973e-06,   9.35499975e-06,
         1.01559999e-05,   1.08249997e-05,   1.16840001e-05,
         1.24170001e-05,   1.33450003e-05,   1.41609999e-05,
         1.51759996e-05,   1.60950003e-05,   1.72000000e-05,
         1.81889991e-05,   1.93129999e-05,   2.03950003e-05,
         2.17550005e-05,   2.28459994e-05,   2.42660008e-05,
         2.55199993e-05,   2.70210003e-05,   2.83959998e-05,
         3.00089996e-05,   3.14999997e-05,   3.32199998e-05,
         3.48299982e-05,   3.66749991e-05,   3.84240011e-05,
         4.03980011e-05,   4.22480007e-05,   4.43690005e-05,
         4.63879987e-05,   4.86300014e-05,   5.07959994e-05,
         5.31910009e-05,   5.55129991e-05,   5.80619999e-05,
         6.05470013e-05,   6.32730007e-05,   6.59200014e-05,
         6.88090004e-05,   7.16409995e-05,   7.47180020e-05,
         7.77340028e-05,   8.09870035e-05,   8.42060035e-05,
         8.76609993e-05,   9.10739982e-05,   9.47399967e-05,
         9.83589998e-05,   1.02238002e-04,   1.06077001e-04,
         1.10177003e-04,   1.14249997e-04,   1.18586999e-04,
         1.22893995e-04,   1.27466003e-04,   1.32029003e-04,
         1.36862000e-04,   1.41672994e-04,   1.46766994e-04,
         1.51849003e-04,   1.57218004e-04,   1.62582000e-04,
         1.68233993e-04,   1.73883993e-04,   1.79829003e-04,
         1.85783996e-04,   1.92035004e-04,   1.98305002e-04,
         2.04869997e-04,   2.11455001e-04,   2.18354005e-04,
         2.25274998e-04,   2.32510007e-04,   2.39785004e-04,
         2.47368996e-04,   2.54999992e-04,   2.62954010e-04,
         2.70958000e-04,   2.79286993e-04,   2.87676987e-04,
         2.96401995e-04,   3.05191003e-04,   3.14319012e-04,
         3.23521992e-04,   3.33069998e-04,   3.42701009e-04,
         3.52684001e-04,   3.62758001e-04,   3.73190996e-04,
         3.83718987e-04,   3.94616014e-04,   4.05617000e-04,
         4.16994997e-04,   4.28483996e-04,   4.40356991e-04,
         4.52351000e-04,   4.64735000e-04,   4.77250986e-04,
         4.90163977e-04,   5.03219024e-04,   5.16681001e-04,
         5.30289020e-04,   5.44312992e-04,   5.58506988e-04,
         5.73111989e-04,   5.87892020e-04,   6.03110006e-04,
         6.18499005e-04,   6.34342025e-04,   6.50370028e-04,
         6.66852982e-04,   6.83541992e-04,   7.00692006e-04,
         7.18056981e-04,   7.35899026e-04,   7.53963017e-04,
         7.72518979e-04,   7.91310973e-04,   8.10600992e-04,
         8.30143981e-04,   8.50196986e-04,   8.70517979e-04,
         8.91360978e-04,   9.12487973e-04,   9.34143027e-04,
         9.56102973e-04,   9.78610944e-04,   1.00142905e-03,
         1.02481595e-03,   1.04852801e-03,   1.07282400e-03,
         1.09746703e-03,   1.12270599e-03,   1.14831002e-03,
         1.17453199e-03,   1.20113394e-03,   1.22837303e-03,
         1.25601899e-03,   1.28431595e-03,   1.31304201e-03,
         1.34243804e-03,   1.37228903e-03,   1.40283303e-03,
         1.43385294e-03,   1.46559998e-03,   1.49783504e-03,
         1.53082598e-03,   1.56433904e-03,   1.59863394e-03,
         1.63348799e-03,   1.66914600e-03,   1.70537794e-03,
         1.74245995e-03,   1.78016000e-03,   1.81873096e-03,
         1.85796595e-03,   1.89810200e-03,   1.93894701e-03,
         1.98072894e-03,   2.02325708e-03,   2.06677592e-03,
         2.11108499e-03,   2.15642899e-03,   2.20260792e-03,
         2.24988209e-03,   2.29804195e-03,   2.34734989e-03,
         2.39761197e-03,   2.44907290e-03,   2.50155502e-03,
         2.55531096e-03,   2.61015398e-03,   2.66634696e-03,
         2.72369408e-03,   2.78247893e-03,   2.84250802e-03,
         2.90405797e-03,   2.96695507e-03,   3.03146197e-03,
         3.09741497e-03,   3.16511095e-03,   3.23435711e-03,
         3.30546498e-03,   3.37825692e-03,   3.45304608e-03,
         3.52965295e-03,   3.60842003e-03,   3.68918502e-03,
         3.77225899e-03,   3.85749293e-03,   3.94526077e-03,
         4.03539790e-03,   4.12827684e-03,   4.22374904e-03,
         4.32221591e-03,   4.42355918e-03,   4.52814996e-03,
         4.63594496e-03,   4.74730087e-03,   4.86220419e-03,
         4.98104095e-03,   5.10382699e-03,   5.23099303e-03,
         5.36255492e-03,   5.49898995e-03,   5.64038800e-03,
         5.78722404e-03,   5.93966199e-03,   6.09824108e-03,
         6.26313686e-03,   6.43500686e-03,   6.61408901e-03,
         6.80112792e-03,   6.99645281e-03,   7.20086694e-03,
         7.41484808e-03,   7.63937784e-03,   7.87502527e-03,
         8.12298059e-03,   8.38398933e-03,   8.65942240e-03,
         8.95035267e-03,   9.25841928e-03,   9.58499312e-03,
         9.93213058e-03,   1.03017101e-02,   1.06962901e-02,
         1.11183496e-02,   1.15712602e-02,   1.20583801e-02,
         1.25840604e-02,   1.31531404e-02,   1.37714203e-02,
         1.44457202e-02,   1.51843401e-02,   1.59970503e-02,
         1.68958306e-02,   1.78955793e-02,   1.90145392e-02,
         2.02756505e-02,   2.17086095e-02,   2.33514309e-02,
         2.52543706e-02,   2.74853706e-02,   3.01383100e-02,
         3.33461203e-02,   3.73048782e-02,   4.23147716e-02,
         4.88610305e-02,   5.77816404e-02,   7.06595778e-02,
         9.08864737e-02,   1.27281800e-01,   2.12181106e-01,
         6.36611581e-01], dtype=np.float32)

def erb2hz(erb):
    """
    Convert equivalent rectangular bandwidth (ERB) to Hertz.
    """
    tmp = np.exp((erb - 43.) / 11.17)
    return (0.312 - 14.675 * tmp) / (tmp - 1.0) * 1000.

def hz2erb(hz):
    """
    Convert Hertz to equivalent rectangular bandwidth (ERB).
    """
    return 11.17 * np.log((hz + 312.) / (hz + 14675.)) + 43.

def generate_bands(lo, hi, n_bands):
    """
    Generates the upper and lower band cut-offs of a series of 'nbands' contiguous frequency bands,
    linearly spaced on an ERB scale, between the frequencies 'lo' and 'hi' (in Hz)
    """
    density = n_bands / (hz2erb(hi) - hz2erb(lo))
    bands = []
    for i in np.arange(1, n_bands + 1):
        bands.append([erb2hz(hz2erb(lo) + (i - 1) / density), erb2hz(hz2erb(lo) + i / density)])
    return bands


def generate_cfs(lo, hi, n_bands):
    """
    Generates a series of 'bands' frequencies in Hz, linearely distributed
    on an ERB scale between the frequencies 'lo' and 'hi' (in Hz).
    These would are the centre frequencies (on an ERB scale) of the bands
    specifications made by 'generate_bands' with the same arguments
    """
    density = n_bands / (hz2erb(hi) - hz2erb(lo))
    bands = []
    for i in np.arange(1, n_bands + 1):
        bands.append(erb2hz(hz2erb(lo) + (i - 0.5) / density))
    return bands


def make_fir_filter(lo, hi, sf):
    """
    Makes a 512-point band-pss FIR filter using the host-windowing method
    (Abed & Cain, 1978, The Radio and Electronic Engineer, 46, 293-300).
    The filter is zero-phase (i.e. symmetrical).

    Arguments:
        - lo (float): Lower limit of the band (Hz)
        - hi (float): Higher limit of the band (Hz)
        - sf (float): Sampling frequency (Hz)

    Returns:
        - out (np.array)
    """
    nspecs = 1000
    nyquist = sf / 2.
    n_stopband_lo = np.int32(lo/nyquist*nspecs)
    stopband_lo = np.zeros(n_stopband_lo)
    n_passband = np.int32(hi/nyquist*nspecs)-n_stopband_lo
    passband = np.ones(n_passband)
    n_stopband_hi = nspecs - n_stopband_lo - n_passband
    stopband_hi = np.zeros(n_stopband_hi)
    specs = np.hstack((stopband_lo, passband, stopband_hi))

    band_lo = 0
    win = np.zeros(256)
    b = np.arange(256) - 255.5
    for i in np.arange(1000):
        band_hi = np.pi * (i + 1) / nspecs
        win += specs[i] * (np.sin(b * band_hi) - np.sin(b * band_lo))
        band_lo = band_hi

    ar = np.transpose(fir_host) * win
    return np.hstack((ar, ar[::-1]))
