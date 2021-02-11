# qvdfile

## QVD File reader and writer (exploratory version)

This is python3 object created to explore QVD file, it can be used 

* to read QVD file Metadata
* to read column values from QVD file
* to read rows from QVD file

Sample usage:

```
import qvdfile 

qvd = qvdfile.QvdFile ("test.qvd")

print(f"File has {qvd.attribs["NoOfRecords"]} records")

print(f"File has column {qvd.fields[0]['FieldName']}, {qvd.getFieldVal(qvd.fields[0]['FieldName']})
  
print(f"First row of the file is {qvd.getRow(0)}"
```

The structure of QVD file is described in [Wiki](../../wiki).

## Performance

This is explarotary version and it is not suited for production usage. Code simplicity is the first priority. If you need better performance please contact the author: QVD files can be read much much faster by other version of software.

### Reading fields

QVD file does not allow indexing - it is impossible to read field #N without reading (N-1) previous fields. This version contains no caching - if you read field #4 and then read field #5 you will read 4 fields first and then read 4 same fields again... This is done specificly for simplicity.

It is faster to read first fields then the last fields. It is nearly impossible to read field #10 000 000 (while it is OK to read field #1000).

### Reading rows

The same is true for rows: the smaller the index the faster it is read. The reason is simple - QVD files usually contain first symbols in the first rows. I would not try to read row #100 000 (and will not try #1000 as well).

For performance contact the author.

## Dependencies

Code is simple and depends only on bitstring module:

```pip install bitstring```

## Unit tests

Unit tests are provided as a sort of documentation - they describe what to expect from the code (or how it was supposed to be used by the author).
