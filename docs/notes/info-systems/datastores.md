
# Datastores

## Machine Readable Data Formats

### CSV

Example CSV:

```csv
city,name,league
New York,Mets,Major
New York,Yankees,Major
Boston,Red Sox,Major
Washington,Nationals,Major
New Haven,Ravens,Minor
```

### JSON

Example JSON:

```js
[
  {"city": "New York", "name": "Yankees", "league":"Major"},
  {"city": "New York", "name": "Mets", "league":"Major"},
  {"city": "Boston", "name": "Red Sox", "league":"Major"},
  {"city": "Washington", "name": "Nationals", "league":"Major"},
  {"city": "New Haven", "name": "Ravens", "league":"Minor"}
]
```

### XML

Example XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<teams>
  <team>
    <city>New York</city>
    <league>Major</league>
    <name>Yankees</name>
  </team>
  <team>
    <city>New York</city>
    <league>Major</league>
    <name>Mets</name>
  </team>
  <team>
    <city>Boston</city>
    <league>Major</league>
    <name>Red Sox</name>
  </team>
  <team>
    <city>Washington</city>
    <league>Major</league>
    <name>Nationals</name>
  </team>
  <team>
    <city>New Haven</city>
    <league>Minor</league>
    <name>Ravens</name>
  </team>
</teams>
```
