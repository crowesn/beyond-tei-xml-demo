# Python XML processing demo 
### Beyond TEI | DHSI 2017

Script demo to add reference attributes to TEI name tags

This script takes a TEI xml file with `name` tags and a csv file with two columns: matching-text and uri. 
It loops through the xml, matching on the name text and adding an ref attribute with URI to the name entity.

Execute script: 

```
$ python3 xml_add_attributes_demo.py xml_input_file url_csv_file
```
