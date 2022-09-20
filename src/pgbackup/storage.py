
def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, fileleam):
    client.upload_fileobj(infile, bucket, filename)
