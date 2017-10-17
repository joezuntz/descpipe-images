import fitsio
import numpy as np


def iter_chunks(ext, chunk_size):
    n = ext.get_nrows()
    start = 0
    n_read = 0
    while start < n:
        end = start+chunk_size
        if end > n:
            end = n
        yield ext.read_slice(start, end)
        start = end

def pdf_sum(pdf_chunk, select, nz):
    output = np.zeros(nz)
    for i in range(nz):
        col = 'PDF_{}'.format(i)
        output[i] += pdf_chunk[col][select].sum()
    return output

def save(n_of_z, z_min, z_max, output_filename):
    nbin, nz = n_of_z.shape
    z_edge = np.linspace(z_min, z_max, nz+1)
    dz = z_edge[1]-z_edge[0]
    z_low = z_edge[:-1]
    z_high = z_edge[1:]
    z_mid = 0.5*(z_low + z_high)
    dt = [ ('z_mid', np.float64), ('z_low', np.float64), ('z_high', np.float64)   ]

    bin_cols =['BIN_{}'.format(b+1) for b in range(nbin)]
    dt += [(bc, np.float64) for bc in bin_cols]
    data = np.zeros(nz, dtype=dt)        
    data["z_mid"]=z_mid
    data["z_low"]=z_low
    data["z_high"]=z_high
    for b in range(nbin):
        data[bin_cols[b]] = n_of_z[b]
    header = {"ZMIN":z_min, "ZMAX":z_max, "NBIN":nbin, "NZ":nz, "DZ":dz}
    fitsio.write(output_filename, data, header=header)



def main(pdf_filename, tomography_filename, output_filename):
    pdf_file = fitsio.FITS(pdf_filename)
    pdf_ext = pdf_file[1]
    tomo_file = fitsio.FITS(tomography_filename)
    tomo_ext = tomo_file[1]

    nbin = tomo_ext.read_header().get('NBIN')
    pdf_header = pdf_ext.read_header()
    nz = pdf_header.get("NZ")
    z_min = pdf_header.get("ZMIN")
    z_max = pdf_header.get("ZMAX")
    counts = np.zeros(nbin)
    n_of_z = np.zeros((nbin,nz))

    chunk_size = 100000
    pdf_iter = iter_chunks(pdf_ext, chunk_size)
    tomo_iter = iter_chunks(tomo_ext, chunk_size)
    for pdf_chunk, tomo_chunk in zip(pdf_iter, tomo_iter):
        n = len(pdf_chunk)
        for b in range(nbin):
            select = np.where(tomo_chunk['BIN']==b+1)
            counts[b] += len(select[0])
            n_of_z[b] += pdf_sum(pdf_chunk, select, nz)
    for b in range(nbin):
        n_of_z[b]/=counts[b]


    save(n_of_z, z_min, z_max, output_filename)

