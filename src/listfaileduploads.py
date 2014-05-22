import datetime
import boto
from optparse import OptionParser
import time
import datetime
import string

sumbytesall = 0
sumbytesolderthan = 0
now = datetime.datetime.now()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--clean", dest="cleanuploads",
                      action="store_true", default=False)
    parser.add_option("--printoldonly", dest="printoldonly",
                      action="store_true", default=False)
    parser.add_option("--olderthandays", dest="olderthandays",default="7")
    parser.add_option("--verbose", dest="verbose",default=False)
    (options, args) = parser.parse_args()

    defaultdays = datetime.timedelta(days=string.atoi(options.olderthandays))
    oneyearout = datetime.timedelta(days=365)

    print 'default days',defaultdays

    conn = boto.connect_s3(host='s3.amazonaws.com', is_secure=True)

    for bucket in conn.get_all_buckets():
        for ul in bucket.list_multipart_uploads():
            print ul
            print 'id',ul.id
            print 'owner name',ul.owner.display_name
            print 'owner id  ',ul.owner.id
            print 'storage class',ul.storage_class
            if options.verbose:
                print 'getallparts'
            youngest = oneyearout
            for parts in ul.get_all_parts():
                partdate = datetime.datetime.fromtimestamp(time.mktime(time.strptime(parts.last_modified[:19], "%Y-%m-%dT%H:%M:%S")))
                sumbytesall += parts.size

                if options.verbose:
                    if not options.printoldonly:
                        print '      bucket          ',parts.bucket
                        print '      last modified   ',parts.last_modified,' (',now-partdate,') ago'
                        print '      part number     ',parts.part_number
                        print '      size            ',parts.size
                        print ''

                if partdate-now < youngest:
                    youngest = now-partdate
                if now-partdate > defaultdays:
                    sumbytesolderthan += parts.size
                if options.verbose:
                    print ''

            if options.cleanuploads:
               if youngest > defaultdays:
                   print 'youngest upload part (',youngest,') is more than',defaultdays,'ago, cleaning'
                   ul.cancel_upload()
               else:
                   print 'not cleaning, youngest upload part (',youngest,') was before',defaultdays
            else:
               if youngest > defaultdays:
                   print 'youngest upload part (',youngest,') is more than',defaultdays,'ago, would be cleaned with --clean flag'
               else:
                   print 'not cleaning, youngest upload part (',youngest,') was before',defaultdays
            print ''
            print ''


    print ''
    print ''
    print 'sum bytes of all uploads',sumbytesall,'(%d gb)' % (sumbytesall/(1024*1024*1024))
    print 'sum bytes of uploads older than',defaultdays,'is',sumbytesolderthan,'(%d gb)' % (sumbytesolderthan/(1024*1024*1024))
