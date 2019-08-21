# PHI-Hashing Anonymizer

```
usage: python anonymizer.py filename [$'delim']
```

For example, 

```
> python test.txt $'\t'
Select column indices (separated by comma) to hash:
 0. ClientName
 1. PatientName
 2. PatientGender
 3. DiagnosisCode
 4. ProcedureCode
(column indices): 1, 2
...
INFO: Anonymized data are in myfile_anonymized.csv
> 
```

