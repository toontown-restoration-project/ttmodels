import glob
import os
files = glob.glob('**', recursive=True)

for filename in files:
    if 'dna' not in filename and 'bam' not in filename:
        continue

    if '_english' not in filename:
        continue

    newFilename = filename.replace('_english', '')
    print(filename, '->', newFilename)

    os.system('cp %s %s' % (filename, newFilename))
