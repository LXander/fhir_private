import json
import requests

#r = requests.get('http://www.hl7.org/implement/standards/fhir/patient-example-a.json')




#example = r.json()


w = json.loads('''
{
  "resourceType": "Patient",
  "id": "f001",
  "text": {
    "status": "generated",
    "div": "<div><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>identifier</b>: 738472983 (USUAL), ?? (USUAL)</p><p><b>active</b>: true</p><p><b>name</b>: Pieter van de Heuvel </p><p><b>telecom</b>: ph: 0648352638(MOBILE), p.heuvel@gmail.com(HOME)</p><p><b>gender</b>: male</p><p><b>birthDate</b>: 17/11/1944</p><p><b>deceased</b>: false</p><p><b>address</b>: Van Egmondkade 23 Amsterdam 1024 RJ NLD (HOME)</p><p><b>maritalStatus</b>: Getrouwd <span>(Details : {http://hl7.org/fhir/v3/MaritalStatus code 'M' = 'Married', given as 'Married'})</span></p><p><b>multipleBirth</b>: true</p><h3>Contacts</h3><table><tr><td>-</td><td><b>Relationship</b></td><td><b>Name</b></td><td><b>Telecom</b></td></tr><tr><td>*</td><td>Partner <span>(Details : {http://hl7.org/fhir/patient-contact-relationship code 'partner' = 'Partner)</span></td><td>Sarah Abels </td><td>ph: 0690383372(MOBILE)</td></tr></table><h3>Communications</h3><table><tr><td>-</td><td><b>Language</b></td><td><b>Preferred</b></td></tr><tr><td>*</td><td>Nederlands <span>(Details : {urn:ietf:bcp:47 code 'nl' = '??', given as 'Dutch'})</span></td><td>true</td></tr></table><p><b>managingOrganization</b>: <a>Burgers University Medical Centre</a></p></div>"
  },
  "identifier": [
    {
      "use": "usual",
      "system": "urn:oid:2.16.840.1.113883.2.4.6.3",
      "value": "738472983",
      "_value": {
        "fhir_comments": [
          "    BSN identification system    "
        ]
      }
    },
    {
      "fhir_comments": [
        "    BSN identification system    "
      ],
      "use": "usual",
      "system": "urn:oid:2.16.840.1.113883.2.4.6.3"
    }
  ],
  "active": true,
  "name": [
    {
      "use": "usual",
      "family": [
        "van de Heuvel"
      ],
      "given": [
        "Pieter"
      ],
      "suffix": [
        "MSc"
      ]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "0648352638",
      "use": "mobile"
    },
    {
      "system": "email",
      "value": "p.heuvel@gmail.com",
      "use": "home"
    }
  ],
  "gender": "male",
  "birthDate": "1944-11-17",
  "deceasedBoolean": false,
  "address": [
    {
      "fhir_comments": [
        "    ISO 3166 Codes (Countries)    "
      ],
      "use": "home",
      "line": [
        "Van Egmondkade 23"
      ],
      "city": "Amsterdam",
      "postalCode": "1024 RJ",
      "country": "NLD"
    }
  ],
  "maritalStatus": {
    "coding": [
      {
        "system": "http://hl7.org/fhir/v3/MaritalStatus",
        "code": "M",
        "display": "Married"
      }
    ],
    "text": "Getrouwd"
  },
  "multipleBirthBoolean": true,
  "contact": [
    {
      "relationship": [
        {
          "coding": [
            {
              "system": "http://hl7.org/fhir/patient-contact-relationship",
              "code": "partner"
            }
          ]
        }
      ],
      "name": {
        "use": "usual",
        "family": [
          "Abels"
        ],
        "given": [
          "Sarah"
        ]
      },
      "telecom": [
        {
          "system": "phone",
          "value": "0690383372",
          "use": "mobile"
        }
      ]
    }
  ],
  "communication": [
    {
      "language": {
        "coding": [
          {
            "system": "urn:ietf:bcp:47",
            "code": "nl",
            "_code": {
              "fhir_comments": [
                "    IETF language tag    "
              ]
            },
            "display": "Dutch"
          }
        ],
        "text": "Nederlands"
      },
      "preferred": true
    }
  ],
  "managingOrganization": {
    "reference": "Organization/f001",
    "display": "Burgers University Medical Centre"
  }
}
''')

s = json.loads('''
  {
    "resourceType":"Patient",
    "id":"example",
    "identifier":[
        {
            "fhir_comments":[
                " MRN assigned by ACME healthcare on 6-May 2001 "
            ],
            "use":"usual",
            "type":{
                "coding":[
                    {
                        "system":"http://hl7.org/fhir/v2/0203",
                        "code":"MR"
                    }
                ]
            },
            "system":"urn:oid:1.2.36.146.595.217.0.1",
            "value":"12345",
            "period":{
                "start":"2001-05-06"
            },
            "assigner":{
                "display":"Acme Healthcare"
            }
        }
    ],
    "active":true,
    "name":[
        {
            "fhir_comments":[
                " Peter James Chalmers, but called 'Jim' "
            ],
            "use":"official",
            "family":[
                "Chalmers"
            ],
            "given":[
                "Peter",
                "James"
            ]
        },
        {
            "use":"usual",
            "given":[
                "Jim"
            ]
        }
    ],
    "telecom":[
        {
            "fhir_comments":[
                " home communication details aren't known "
            ],
            "use":"home"
        },
        {
            "system":"phone",
            "value":"(03) 5555 6473",
            "use":"work"
        }
    ],
    "gender":"male",
    "_gender":{
        "fhir_comments":[
            " use FHIR code system for male / female "
        ]
    },
    "birthDate":"1974-12-25",
    "_birthDate":{
        "extension":[
            {
                "url":"http://hl7.org/fhir/StructureDefinition/patient-birthTime",
                "valueDateTime":"1974-12-25T14:35:45-05:00"
            }
        ]
    },
    "deceasedBoolean":false,
    "address":[
        {
            "use":"home",
            "type":"both",
            "line":[
                "534 Erewhon St"
            ],
            "city":"PleasantVille",
            "district":"Rainbow",
            "state":"Vic",
            "postalCode":"3999",
            "period":{
                "start":"1974-12-25"
            }
        }
    ],
    "contact":[
        {
            "relationship":[
                {
                    "coding":[
                        {
                            "system":"http://hl7.org/fhir/patient-contact-relationship",
                            "code":"partner"
                        }
                    ]
                }
            ],
            "name":{
                "family":[
                    "du",
                    "Marc"
                ],
                "_family":[
                    {
                        "extension":[
                            {
                                "fhir_comments":[
                                    " the 'du' part is a family name prefix (VV in iso 21090) "
                                ],
                                "url":"http://hl7.org/fhir/StructureDefinition/iso21090-EN-qualifier",
                                "valueCode":"VV"
                            }
                        ]
                    },
                    null
                ],
                "given":[
                    "Bdicte"
                ]
            },
            "telecom":[
                {
                    "system":"phone",
                    "value":"+33 (237) 998327"
                }
            ],
            "gender":"female",
            "period":{
                "start":"2012",
                "_start":{
                    "fhir_comments":[
                        " The contact relationship started in 2012 "
                    ]
                }
            }
        }
    ],
    "managingOrganization":{
        "reference":"Organization/1"
    }
}
'''
)

p = json.loads('''
{"name":[
        {
            "fhir_comments":[
                " Peter James Chalmers, but called 'Jim' "
            ],
            "use":"official",
            "family":[
                "Chalmers"
            ],
            "given":[
                "Peter",
                "James"
            ]
        },
        {
            "use":"usual",
            "given":[
                "Jim"
            ]
        }
    ]
}
'''
)

d = [['fhir_comments'],['use']]

sequence = json.loads('''
{
    "resourceType": "Sequence",
    "observedAllele": "T",
    "text": {
        "status": "generated",
        "div": "<div>Genotype of rs2279363 is C/T</div>"
    },
    "coordinate": [
        {
            "start": 44959213,
            "end": 44959213,
            "genomeBuild": {
                "text": "GRCh37"
            },
            "chromosome": {
                "text": "11"
            }
        }
    ],
    "variationID": {
        "coding": [
            {
                "code": "rs2279363",
                "system": "http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi"
            }
        ]
    },
    "type": "DNA",
    "species": {
        "text": "Homo sapiens",
        "coding": [
            {
                "code": "337915000",
                "system": "http://snomed.info/sct"
            }
        ]
    },
    "referenceAllele": "C"
}
'''
)

form_test = ['name','gender'];

simple = json.loads('''
{
  "resourceType": "Patient",
  "id": "pat1",
  "text": {
    "status":"generated",
    "div":"<div>"
  },
  "identifier": [
    {
      "use": "usual",
      "type": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/v2/0203",
            "code": "MR"
          }
        ]
      },
      "system": "urn:oid:0.1.2.3.4.5.6.7",
      "value": "654321"
    }
  ],
  "active": true,
  "name": [
    {
      "use": "official",
      "family": [
        "Donald"
      ],
      "given": [
        "Duck"
      ]
    }
  ],
  "gender": "male",
  "photo": [
    {
      "contentType": "image/gif",
      "data": "R0lGODlhEwARAPcAAAAAAAAA/+9aAO+1AP/WAP/eAP/eCP/eEP/eGP/nAP/nCP/nEP/nIf/nKf/nUv/nWv/vAP/vCP/vEP/vGP/vIf/vKf/vMf/vOf/vWv/vY//va//vjP/3c//3lP/3nP//tf//vf///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAAEALAAAAAATABEAAAi+AAMIDDCgYMGBCBMSvMCQ4QCFCQcwDBGCA4cLDyEGECDxAoAQHjxwyKhQAMeGIUOSJJjRpIAGDS5wCDly4AALFlYOgHlBwwOSNydM0AmzwYGjBi8IHWoTgQYORg8QIGDAwAKhESI8HIDgwQaRDI1WXXAhK9MBBzZ8/XDxQoUFZC9IiCBh6wEHGz6IbNuwQoSpWxEgyLCXL8O/gAnylNlW6AUEBRIL7Og3KwQIiCXb9HsZQoIEUzUjNEiaNMKAAAA7"
    }
  ],
  "contact": [
    {
      "relationship": [
        {
          "coding": [
            {
              "system": "http://hl7.org/fhir/patient-contact-relationship",
              "code": "owner"
            }
          ]
        }
      ],
      "organization": {
        "reference": "Organization/1",
        "display": "Walt Disney Corporation"
      }
    }
  ],
  "managingOrganization": {
    "reference": "Organization/1",
    "display": "ACME Healthcare, Inc"
  },
  "link": [
    {
      "other": {
        "reference": "Patient/pat2"
      },
      "type": "seealso"
    }
  ]
}
'''
)

seq_ep = json.loads(
    '''
    {
    "referenceSeq": {
        "text": "ENSESTT00000085772.1",
        "coding": [
            {
                "code": "ENSESTT00000085772.1",
                "system": "http://www.ensembl.org"
            }
        ]
    },
    "repository": [
        {
            "url": "https://www.googleapis.com/genomics/v1beta2",
            "name": "ga4gh",
            "readGroupSetId": "B1B2",
            "variantId": "A1A2"
        }
    ],
    "resourceType": "Sequence",
    "observedAllele": "T",
    "species": {
        "text": "Homo sapiens",
        "coding": [
            {
                "code": "337915000",
                "system": "http://snomed.info/sct"
            }
        ]
    },
    "meta": {
        "versionId": 1,
        "lastUpdated": "2016-03-23T13:48:34.689681"
    },
    "text": {
        "status": "generated",
        "div": "<div><p><b>Generated Narrative with Details</b></p></div>"
    },
    "coordinate": [
        {
            "start": 55227976,
            "end": 55227977,
            "chromosome": {
                "coding": [
                    {
                        "code": "7"
                    }
                ]
            },
            "genomeBuild": "GRCh37"
        }
    ],
    "variationID": [
        {
            "text": "rs363358000",
            "coding": [
                {
                    "code": "363358000",
                    "system": "http://snomed.info/sct"
                }
            ]
        }
    ],
    "type": "DNA",
    "id": "example",
    "referenceAllele": "A"
}


    '''
)


ob_ep = json.loads(
    '''
    {
    "status": "final",
    "valueCodeableConcept": {
        "coding": [
            {
                "code": "10828004",
                "system": "http://snomed.info/sct",
                "display": "Positive"
            }
        ]
    },
    "code": {
        "coding": [
            {
                "code": "55233-1",
                "system": "http://loinc.org",
                "display": "Genetic analysis master panel"
            }
        ]
    },
    "extension": [
        {
            "url": "http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence",
            "valueReference": {
                "reference": "Sequence/example"
            }
        },
        {
            "url": "http://hl7.org/fhir/StructureDefinition/observation-geneticsSource",
            "valueCodeableConcept": {
                "coding": [
                    {
                        "code": "LA6684-0",
                        "system": "http://hl7.org/fhir/LOINC",
                        "display": "somatic"
                    }
                ]
            }
        },
        {
            "url": "http://hl7.org/fhir/StructureDefinition/observation-geneticsVariationHGVS",
            "extension": [
                {
                    "url": "genomeBuild",
                    "valueCodeableConcept": {
                        "text": "GRCh 38"
                    }
                },
                {
                    "url": "name",
                    "valueCodeableConcept": {
                        "text": "NG_007726.3:g.146252T>G"
                    }
                }
            ]
        },
        {
            "url": "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene",
            "valueCodeableConcept": {
                "coding": [
                    {
                        "code": "3236",
                        "system": "http://www.genenames.org",
                        "display": "EGFR"
                    }
                ]
            }
        },
        {
            "url": "http://hl7.org/fhir/StructureDefinition/observation-geneticsRegion",
            "valueCodeableConcept": {
                "text": "Exon 21"
            }
        }
    ],
    "resourceType": "Observation",
    "text": {
        "status": "generated",
        "div": "<div><p><b>Generated Narrative with Details</b></p></div>"
    },
    "specimen": {
        "display": "Molecular Specimen ID: MLD45-Z4-1234",
        "reference": "Specimen/genetics-example1-somatic"
    },
    "component": [
        {
            "valueCodeableConcept": {
                "text": "Lung cancer",
                "coding": [
                    {
                        "code": "363358000",
                        "system": "http://snomed.info/sct",
                        "display": "Malignant tumor of lung (disorder)"
                    }
                ]
            },
            "code": {
                "coding": [
                    {
                        "code": "51967-8",
                        "system": "http://loinc.org",
                        "display": "Genetic disease assessed"
                    }
                ]
            }
        },
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "code": "LA6669-1",
                        "display": "Pathogenic"
                    }
                ]
            },
            "code": {
                "coding": [
                    {
                        "code": "53037-8",
                        "system": "http://loinc.org",
                        "display": "Genetic disease sequence variation interpretation"
                    }
                ]
            }
        }
    ],
    "performer": [
        {
            "display": "Molecular Diagnostic Laboratory",
            "reference": "Practitioner/genetics-example1-somatic"
        }
    ],
    "meta": {
        "versionId": 1,
        "lastUpdated": "2016-03-22T14:11:12.235286"
    },
    "issued": "2013-03-11T10:28:00+01:00",
    "id": "ob-genetics-1",
    "subject": {
        "display": "Molecular Lab Patient ID: HOSP-23456",
        "reference": "Patient/genetics-example1-somatic"
    }
}
    '''
)

example = simple