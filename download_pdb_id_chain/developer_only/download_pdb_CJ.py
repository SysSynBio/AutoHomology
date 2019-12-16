#!/usr/bin/python
# credit: Chang joon Lee?
import os
from os import popen, system
from os.path import exists, basename
import sys

remote_host = ''

def download_pdb(pdb_id, dest_dir):
    # print "downloading %s" % ( pdb_id )
    url = 'http://www.rcsb.org/pdb/files/%s.pdb.gz' % (pdb_id.upper())
    
    
    # both works well, but there is no size difference between .pdb.gz and .pdb
    
    #dest = '%s/%s.pdb.gz' % (os.path.abspath(dest_dir), pdb_id.lower())
    dest = '%s/%s.pdb' % (os.path.abspath(dest_dir), pdb_id.lower())
    
    
    wget_cmd = 'wget --quiet %s -O %s' % (url, dest)
    print wget_cmd
    if remote_host:
        wget_cmd = 'ssh %s %s' % (remote_host, wget_cmd)

    lines = popen(wget_cmd).readlines()
    if (exists(dest)):
        return dest
    else:
        print "Error: didn't download file!"


try:
       print "provided pdb_id_chain_file: ", sys.argv[1]
except:
       print "pdb_id_chain_file is not provided as an argument, so quit the program"
       sys.exit(0)
                 
files_to_unlink = []

with open(sys.argv[1]) as f:
    for line in f:
#        print line
        splited = line.split();
 #       print splited
#        print splited[0]
        if (splited[0] == "<id>"):
            continue
        id = splited[0]
        chain = splited[1]
        print id
        print chain
        
        netpdbname = download_pdb(id, '.')
        '''
        files_to_unlink.append(netpdbname)
    
        if len(files_to_unlink) > 0:
        for file in files_to_unlink:
        os.unlink(file)     
        '''
