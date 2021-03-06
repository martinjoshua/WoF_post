#!/bin/csh
#==================================================================

source ~/.tcshrc
set echo

#cd to directory where job was submitted from
#cd /scratch2/patrick.skinner/python_2019_verif
#cd /work/brian.matilla/python_2019_verif
cd /home/brian.matilla/work_backup/python_2019_verif

# User defined variables: 

set date = 20190618
#set base_dir = /oldscratch/skinnerp/2019_wofs_post/
set base_dir = /scratch/brian.matilla/

if ($date >= 20190617) then
########## WPC Cycling Start ################
   set times = (1600 1700 1800 1900 2000 2100 2200 2300 0000 0100 0200 0300 0400 0500 0600)
   set nt = (72 72 72 72 72 72 72 72 72 72 72 72 72 72 24)

else if ($date >= 20190429 && $date <= 20190616) then
########## SFE Cycling Start ################
   set times = (1700 1900 1930 2000 2030 2100 2130 2200 2230 2300 2330 0000 0030 0100 0130 0200 0230 0300)
   set nt = (36 72 36 72 36 72 36 72 36 72 36 72 36 72 36 72 36 72)

else
########## All other runs ###################
#   set times = (1900 2000 2100 2200 2300 0000 0100 0200 0300)
#   #   set nt = (72 72 72 72 72 72 72 72 72)
#   endif

endif

# Build directories needed: 

#set summary = "/scratch/skinnerp/2019_wofs_post/summary_files/"$date"/"
set summary = "/scratch/brian.matilla/WoFS_2019/summary_files/"$date"/"
set image = "/www/wof.nssl.noaa.gov/newse_images/"$date"/"
set flagdir = $base_dir"flags/"$date"/"
set mrmsdir = "/scratch/brian.matilla/MRMS_QPE_AGG/"$date"/"
set qpeqcdir = $base_dir"qpe_qc_2019/"$date"/"

if (! -d ${summary} ) then
   echo "Today's directories not created yet."
   exit(0)
endif
# Run wrapper script for forecast: 

sleep 5

set i = 1

foreach dir ($times)
   set tempsumdir = $summary$dir"/"
   echo $tempsumdir

   set tempmrmsdir = $mrmsdir$dir"/"
   echo $tempmrmsdir

   set tempqpeqcdir = $qpeqcdir$dir"/"
   echo $tempqpeqcdir

   set flagfile = $flagdir"/"$dir"_paint.txt"
   echo $flagfile

   set tempnt = $nt[$i]
   echo $tempnt

   set tempfiles=`ls -a ${tempsumdir} | wc | awk '{print $1}'`
   if ( "${tempfiles}" > 2) then #$ne ) then
      set imagedir = $image$dir"/"
      if ( ! -e $flagfile ) then
         touch $flagfile
         python wrapper_paintball_qpf.py -m $tempmrmsdir -d $tempsumdir -q $tempqpeqcdir -o $imagedir -e $tempnt -p $date
#         exit(0)
      endif 
   endif
   wait
   @ i++
end

sleep 10

