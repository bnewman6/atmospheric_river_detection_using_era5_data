;--------------------------------------------------
; 
; These files are loaded by default in NCL V6.2.0 and newer
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
; load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
;
begin

;---Open netCDF file
  a = addfile("ivt2_h.nc","r")
  b = addfile("ivt2_v.nc","r")
;
  u = a->horizontal_data(:,:)
  v = b->vertical_data(:,:)
  lat_uv = b->latitude
  lon_uv = b->longitude

;---Create plot
  wks = gsn_open_wks("png","vector7")    ; send graphics to PNG file

  res = True     ; plot mods desired

  res@tiMainString       = "ERA5 Reanalysis Atmospheric River"
  res@gsnLeftString      = "Vertically Integrated Vector Vapor Transport"

  res@mpMinLonF          = 210.    ; select a subregion
  res@mpMaxLonF          = 270.
  res@mpCenterLonF       = 240.
  res@mpMinLatF          = 15.
  res@mpMaxLatF          = 55.

  res@vcMonoLineArrowColor   = False

  res@gsnAddCyclic           = False   ; regional data
  res@vcLevelPalette         = "cmocen_dense"    ; set color map
  res@vcLevelSelectionMode   = "ManualLevels"
  ; res@vcMinMagnitudeF       = 250.
  ; res@vcMaxMagnitudeF       = 1000.
  res@vcRefMagnitudeF        = 10.0    ; define vector ref mag
  res@vcExplicitLabelBarLabelsOn = True
  res@vcRefLengthF           = 0.045   ; define length of vec ref
  res@vcGlyphStyle           = "CurlyVector"    ; turn on curly vectors
  res@vcMinDistanceF         = 0.025

  plot=gsn_csm_vector_map(wks,u(:,:),v(:,:),res)
end
