import fitsio
import numpy as np

def load(input_file, hdu, bin_col, weight_col):
    #Load in data
    cols = [bin_col]
    if weight_col is not None:
        cols.append(weight_col)
    f = fitsio.FITS(input_file)
    data = f[hdu].read_columns(cols)
    n = len(data)
    if weight_col is None:
        weight = np.ones(n)
    else:
        weight = data[weight_col]
    z = data[bin_col]
    f.close()
    return z, weight

def compute_edges(z, weight, nbin, zmin, zmax):
    # compute the bin edges
    select = np.where((z>zmin) & (z<zmax) & (weight>0) )
    z_select = z[select]
    w_select = weight[select]
    index = np.argsort(z_select)
    z_select = z_select[index]
    w_select = w_select[index]
    w_cum = np.cumsum(w_select)
    w_cum /= w_cum[-1]
    edges = [zmin]
    for i in range(nbin-1):
        w_edge = np.where(w_cum>(1.0*(i+1))/(nbin))[0][0]
        z_edge = z_select[w_edge]
        edges.append(z_edge)
    edges.append(zmax)
    return edges

def bin_objects(z, weight, edges):
    n = len(z)
    nbin = len(edges)-1
    # Put objects in bins
    bins = np.repeat(-1, n)
    for i in range(nbin):
        z0 = edges[i]
        z1 = edges[i+1]
        select = np.where((z>z0) & (z<z1) & (weight>0) )
        bins[select] = i+1
    return bins

def summarize(nbin, bins):
    print("Object bin counts:")
    b = -1
    count = len(np.where(bins==b+1)[0])
    print("Unbinned: {}".format(count))
    for b in range(nbin):
        count = len(np.where(bins==b+1)[0])
        print("Bin {}: {}".format(b+1, count))

def save(output_file, nbin, bins):
    # save the results
    dt=np.dtype([('BIN', np.int32)])
    bins=bins.astype(dt)
    header = {"NBIN":nbin}
    fitsio.write(output_file, bins, header=header)


def main(input_file, output_file, bin_col, nbin, zmin, zmax, weight_col, hdu):
    z, weight = load(input_file, hdu, bin_col, weight_col)
    edges = compute_edges(z, weight, nbin, zmin, zmax)
    bins = bin_objects(z, weight, edges)
    summarize(nbin, bins)
    save(output_file, nbin, bins)

