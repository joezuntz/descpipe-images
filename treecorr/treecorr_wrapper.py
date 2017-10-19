import treecorr
import fitsio
import twopoint
import numpy as np

def main(config_file, tomo_file, cat_file, output_file):
        config = treecorr.read_config(config_file)
        
        tomo_data = fitsio.read(tomo_file)
        shear_data = fitsio.read(cat_file)
        tomo_header = fitsio.read_header(tomo_file, 1)
        nbin = tomo_header.get("NBIN")

        gg = treecorr.GGCorrelation(config)
        theta = []
        xip = []
        xim = []
        bin1 = []
        bin2 = []
        angbin = []

        print("Not doing the proper ngmix weighting in this test!")

        for b1 in range(nbin):
            w1 = np.where(tomo_data['BIN']==b1+1)
            d1 = shear_data[w1]
            cat1 = treecorr.Catalog(g1=d1['E_1'], g2=d1['E_1'],  w=d1['W'], 
                ra=d1['RA'], dec=d1['DEC'], ra_units='deg', dec_units='deg')
            for b2 in range(nbin):
                if b2<b1:
                    continue
                
                w2 = np.where(tomo_data['BIN']==b2+1)
                d2 = shear_data[w2]
                cat2 = treecorr.Catalog(g1=d2['E_1'], g2=d2['E_1'],  w=d2['W'], 
                    ra=d2['RA'], dec=d2['DEC'], ra_units='deg', dec_units='deg')
                gg.process(cat1, cat2)
                ntheta = len(gg.meanr)
                theta.append(gg.meanr)
                xip.append(gg.xip)
                xim.append(gg.xim)
                bin1.append(np.repeat(b1, ntheta))
                bin2.append(np.repeat(b2, ntheta))
                angbin.append(np.arange(ntheta, dtype=int))

        theta = np.concatenate(theta)
        xip = np.concatenate(xip)
        xim = np.concatenate(xim)
        bin1 = np.concatenate(bin1)
        bin2 = np.concatenate(bin2)
        angbin = np.concatenate(angbin)

        tp = twopoint.Types.galaxy_shear_plus_real
        tm = twopoint.Types.galaxy_shear_minus_real

        XIP = twopoint.SpectrumMeasurement("xip", (bin1,bin2), (tp,tp) , 
            ("source", "source"), "SAMPLE", angbin, xip, angle=theta, angle_unit="arcmin")
        XIM = twopoint.SpectrumMeasurement("xim", (bin1,bin2), (tm,tm) , 
            ("source", "source"), "SAMPLE", angbin, xim, angle=theta, angle_unit="arcmin")

        output = twopoint.TwoPointFile([XIP, XIM], [], [], None)
        output.to_fits(output_file)

