import qvdfile

qvd = qvdfile.QvdFile ("CMF.qvd")

# print(f"File has {qvd.attribs['NoOfRecords']} records")
# print(f"File has column {qvd.fields[0]['FieldName']}, {qvd.getFieldVal(qvd.fields[0]['FieldName'],0)})

# with open('CMF.csv', 'w') as f:
print(f"First row of the file is {qvd.getRow(0)}")