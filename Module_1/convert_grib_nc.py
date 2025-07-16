import xarray

data = xarray.open_dataset('ERA5/htr_2018', engine='cfgrib')
data.to_netcdf('htr_2018.nc')