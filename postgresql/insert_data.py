#read vcf file
#import gzip
# took 222 seconds :)

import psycopg2

try:
    conn = psycopg2.connect("dbname='bench' user='raony' host='localhost' password='raony'")
except:
    print("I am unable to connect to the database")
cur = conn.cursor()
with open('./input/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf', 'r') as f:
    #file_content = f.read()
    for j, line in enumerate(f):
        if not line.startswith('#'):
            row = line.split('\t')
            command = """INSERT INTO variant values ('{}','{}','{}', null, null, null, null, null, null, null, null)""".format(j, row[0],row[1]);
            # (22, 16050075, null, null, null, null, null, null, null, null, null, null)
            cur.execute(command)
            #print(command)
            # for genotype in row[9:]:
            #     pass
        else:
            if line.startswith('#CHROM'):
                individuals = line.strip().split('\t')[9:]
                #print(individuals)
                indvs = {}
                for i, individual in enumerate(individuals):
                    indvs[i] = individual
                    command = """INSERT INTO individual values ('{}','{}')""".format(i,individual);
                    #print(command)
                    cur.execute(command)

#read again and add individual variant
# command = """INSERT INTO individual_variant values ('{}','{}','{}', null, null, null, null, null, null, null, null)""".format(j, row[0],row[1]);