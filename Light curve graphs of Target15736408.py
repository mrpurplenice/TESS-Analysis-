# -*- coding: utf-8 -*-

!pip install lightkurve
from lightkurve import TessTargetPixelFile
import lightkurve as lk
import numpy as np

tpf = TessTargetPixelFile("/content/tess2021258175143-s0043-0000000015736408-0214-s_tp.fits")
tpf.plot(aperture_mask=tpf.pipeline_mask);

lc = tpf.to_lightcurve()
lc.scatter();

flat_lc = lc.flatten()
flat_lc.scatter(s=1);

periodogram = flat_lc.to_periodogram(method="bls", period=np.arange(0.35, 3, 0.001))
periodogram.plot();

best_fit_period = periodogram.period_at_max_power
print('Best fit period: {:.3f}'.format(best_fit_period))

folded_lc = lc.fold(period=best_fit_period, t0=1355)
folded_lc.scatter(s=1);

binned_lc = folded_lc.bin(binsize=10) 
binned_lc.scatter();

pixelfile.plot_pixels();
