from datetime import datetime, date
import json
import logging
logger = logging.getLogger(__name__)

from DDR import converters



MODEL = 'collection'

STATUS_CHOICES = [['inprocess', 'In Progress'],
                  ['completed', 'Completed'],]

PERMISSIONS_CHOICES = [['1','Public'],
                       ['0','Private'],]
PERMISSIONS_CHOICES_DEFAULT = 1

RIGHTS_CHOICES = [["cc", "DDR Creative Commons"],
                  ["pcc", "Copyright, with special 3rd-party grant permitted"],
                  ["nocc", "Copyright restricted"],
                  ["pdm", "Public domain" ],]
RIGHTS_CHOICES_DEFAULT = 'cc'

LANGUAGE_CHOICES = [['',''],
                    ['eng','English'],
                    ['jpn','Japanese'],
                    ['chi','Chinese'],
                    ['fre','French'],
                    ['ger','German'],
                    ['kor','Korean'],
                    ['por','Portuguese'],
                    ['rus','Russian'],
                    ['spa','Spanish'],
                    ['tgl','Tagalog'],]

FIELDS = [
    
    {
        'model':      'collection',
        'name':       'id',
        'group':      '',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Collection ID',
            'help_text':  'The unique identifier for the collection. Automatically generated by the DDR Workbench when adding a new collection.',
            'max_length': 255,
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'index': 'not_analyzed',
            },
            'display': "string"
        },
        'xpath':      "",
        'xpath_dup':  ['/ead/archdesc/did/unitid',],
    },
    
    {
        'model':      'collection',
        'name':       'record_created',
        'group':      '',
        'model_type': datetime,
        'default':    datetime.now,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'DateTimeField',
        'form': {
            'label':      'Record Created',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "date",
                'index': "not_analyzed",
                'store': "yes",
                'format': converters.config.ELASTICSEARCH_DATETIME_MAPPING
            },
            'display': "datetime"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'record_lastmod',
        'group':      '',
        'model_type': datetime,
        'default':    datetime.now,
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'DateTimeField',
        'form': {
            'label':      'Record Modified',
            'help_text':  '',
            'widget':     'HiddenInput',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "date",
                'index': "not_analyzed",
                'store': "yes",
                'format': converters.config.ELASTICSEARCH_DATETIME_MAPPING
            },
            'display': "datetime"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'status',
        'group':      '',
        'model_type': int,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Production Status',
            'help_text':  '"In Progress" = the object is not ready for release on the DDR public website. (The object will not be published even if the collection has a status of "Complete".) "Complete" = the object is ready for release on the DDR public website. (The object can only be published if the collection has a status of "Complete".)',
            'widget':     '',
            'choices':    STATUS_CHOICES,
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'public',
        'group':      '',
        'model_type': int,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Privacy Level',
            'help_text':  '"Public" = the object is viewable through the DDR public website. (Any files under the object with a status of "Private" will not be viewable regardless of the object\'s privacy level. If the entire collection has a status of "Private" no objects or files will be viewable). "Private" = the object is restricted and not viewable through the DDR public website. (Any files under the object inherit this privacy level and will not be viewable either. If the entire collection has a status of "Public" the object will remain not viewable).',
            'widget':     '',
            'choices':    PERMISSIONS_CHOICES,
            'initial':    PERMISSIONS_CHOICES_DEFAULT,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': ""
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    # overview ---------------------------------------------------------
    {
        'model':      'collection',
        'name':       'title',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Title',
            'help_text':  'Titles are usually made up of two parts: 1) the name of the creator(s), collector(s), or topic and 2) the nature of the materials being described.* Use Chicago Manual of Style rules for titles.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      '/ead/eadheader/filedesc/titlestmt/titleproper',
        'xpath_dup':  ['/ead/archdesc/did/unittitle',],
    },
    
    {
        'model':      'collection',
        'name':       'unitdateinclusive',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Inclusive Dates',
            'help_text':  'Use the years separated by a dash: YYYY-YYYY. If exact dates are unknown use circa (c.).',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/unitdate[@type='inclusive']",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'unitdatebulk',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Bulk Dates',
            'help_text':  'Use the years separated by a dash: YYYY-YYYY. If exact dates are unknown use circa (c.). Can be the same as the inclusive dates if there are no predominant dates.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/unitdate[@type='bulk']",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'creators',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Creator',
            'help_text':  'When possible use the Library of Congress Name Authority Headings. For individuals use the following format: "Last Name, First Name: Creator Role" (e.g., Adams, Ansel:photographer). For organizations use the following format: "Organization Name: Creator Role" (e.g., Associated Press:publisher). Multiple creators are allowed, but must be separated using a semi-colon.',
            'max_length': 255,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "object",
                'properties': {
                    "namepart": {
                        "type": "string",
                        "store": "no",
                        "index": "not_analyzed"
                    },
                    'id': {
                        'type': "integer",
                        'store': "no",
                        'index': "not_analyzed"
                    },
                    "role": {
                        "type": "string",
                        "store": "no",
                        "index": "not_analyzed"
                    },
                }
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/origination",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'extent',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Physical Description',
            'help_text':  'Physical description is made up of two parts: 1) a number (quantity) and 2) an expression of the extent (items, containers, carriers) or material type.',
            'max_length': 255,
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/physdesc/extent",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'language',
        'group':      'overview',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'MultipleChoiceField',
        'form': {
            'label':      'Language',
            'help_text':  'The language that predominates in the original material being described.	Only needed for objects containing textual content (i.e. caption on a photograph, text of a letter). Use the Library of Congress Codes for the Representation of Names of Languages ISO 639-2 Codes (found here http://www.loc.gov/standards/iso639-2/php/code_list.php).',
            'choices':  LANGUAGE_CHOICES,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "facet"
        },
        'xpath':      "/ead/archdesc/did/langmaterial/language/@langcode",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'contributor',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Contributing Institution',
            'help_text':  "The name of the organization that owns the physical materials. In many cases this will be the partner's name unless the materials were borrowed from a different organization for scanning.",
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/repository",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'description',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Abstract',
            'help_text':  'A brief statement about the creator and the scope of the collection.	Brief free text following basic Chicago Manual style guidelines.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/abstract",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'notes',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Notes',
            'help_text':  'Additional information about the collection that is not appropriate for any other element.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': False,
            'properties': {
                'type': "string",
                'store': "no",
                'index': "no"
            },
            'display': ""
        },
        'xpath':      "/ead/archdesc/did/note",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'physloc',
        'group':      'overview',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Physical Location',
            'help_text':  'The place where the collection is stored.	Could be the name of a building, shelf location, etc.',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/archdesc/did/physloc",
        'xpath_dup':  [],
    },
    
    # administative ----------------------------------------------------
    {
        'model':      'collection',
        'name':       'acqinfo',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Acquisition Information',
            'help_text':  'Information about how the collection was acquired.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': False,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': ""
        },
        'xpath':      "/ead/descgrp/acqinfo",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'custodhist',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Custodial History',
            'help_text':  'Information about the provenance of the collection.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': False,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': ""
        },
        'xpath':      "/ead/descgrp/custodhist",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'accruals',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Accruals',
            'help_text':  'Can be used to note if there were multiple donations made at different times or if additional materials are expected in the future.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': False,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': ""
        },
        'xpath':      "/ead/descgrp/accruals",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'processinfo',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Processing Information',
            'help_text':  'Information about accessioning, arranging, describing, preserving, storing, or otherwise preparing the described materials for research use.	Free text field. Can include information about who processed the collection, who created/if there is a finding aid, deaccessioning, etc.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': False,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': ""
        },
        'xpath':      "/ead/descgrp/processinfo",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'rights',
        'group':      '',
        'model_type': str,
        'vocab':      True,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'ChoiceField',
        'form': {
            'label':      'Rights',
            'help_text':  'Setting will determine the initial default for objects in this collection.',
            'widget':     '',
            'choices':    RIGHTS_CHOICES,
            'initial':    RIGHTS_CHOICES_DEFAULT,
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "rights"
        },
        'xpath':      "",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'accessrestrict',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Restrictions on Access',
            'help_text':  'Can include more specific information about restrictions, such as duration of the restriction, the reasons for restrictions, authorized users, etc.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/descgrp/accessrestrict",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'userrestrict',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Restrictions on Use',
            'help_text':  'Should include information about copyright status, who owns copyright, contact information for requests for use, etc.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/descgrp/userrestrict",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'prefercite',
        'group':      'administative',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Preferred Citation',
            'help_text':  'Could identify the contributing institution, collection contributor and/or donor. This field is determined through deeds of gift or usage agreements for collection. Often begins with: "Courtesy of..."',
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   True,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/descgrp/prefercite",
        'xpath_dup':  [],
    },
    
    # bioghist ---------------------------------------------------------
    {
        'model':      'collection',
        'name':       'bioghist',
        'group':      'bioghist',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Biography and History',
            'help_text':  'Some of the elements that can be included are: biography/history of the individuals/families (dates; places of residence; education; occupations and life activities) and/or biography/history of corporate bodies (dates of founding or dissolution; geographical areas; mandates; functions; administrative structure; predecessor or successor bodies; administrative structure).',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/bioghist",
        'xpath_dup':  [],
    },
    
    # scopecontent -----------------------------------------------------
    {
        'model':      'collection',
        'name':       'scopecontent',
        'group':      'scopecontent',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Scope and Content',
            'help_text':  'Some of the elements that can be included are: functions, activities, processes that generated the materials being described; intellectual characteristics of the materials; content dates; geographic areas; subject matters; or any other relevant information that will help the researcher evaluate the relevance of the materials.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/scopecontent",
        'xpath_dup':  [],
    },
    
    # related ----------------------------------------------------------
    {
        'model':      'collection',
        'name':       'relatedmaterial',
        'group':      'related',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Related Materials',
            'help_text':  'Information about materials in other collections that might be of interest to researchers. Free text field. The addition of links will be available in the future.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/relatedmaterial",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'separatedmaterial',
        'group':      'related',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Separated Materials',
            'help_text':  'Information about materials that were pulled from this collection and added to another. Free text field. The addition of links will be available in the future.',
            'widget':     'Textarea',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "analyzed"
            },
            'display': "string"
        },
        'xpath':      "/ead/separatedmaterial",
        'xpath_dup':  [],
    },
    
    {
        'model':      'collection',
        'name':       'signature_id',
        'group':      '',
        'model_type': str,
        'default':    '',
        'csv': {
            'export': '',
            'import': '',
        },
        'form_type':  'CharField',
        'form': {
            'label':      'Signature',
            'help_text':  "DDR ID of the file to use as this object's thumbnail.",
            'max_length': 255,
            'widget':     '',
            'initial':    '',
            'required':   False,
        },
        'elasticsearch': {
            'public': True,
            'properties': {
                'type': "string",
                'store': "yes",
                'index': "not_analyzed"
            },
            'display': "string"
        },
    },

]

# List of FIELDS to be excluded when exporting and updating.
FIELDS_CSV_EXCLUDED = []



# jsonload_* --- load-from-json functions ----------------------------
#
# These functions take raw JSON and convert it to a Python data type.
#

def jsonload_record_created(text): return converters.text_to_datetime(text)
def jsonload_record_lastmod(text): return converters.text_to_datetime(text)
def jsonload_creators(text): return converters.text_to_rolepeople(text)



# jsondump_* --- export-to-json functions ------------------------------
#
# These functions take Python data and format it for JSON.
#

def jsondump_record_created(data): return converters.datetime_to_text(data)
def jsondump_record_lastmod(data): return converters.datetime_to_text(data)



# display_* --- Display functions --------------------------------------
#
# These functions take Python data from the corresponding Collection field
# and format it for display.
#


# id

def display_record_created(data):
    return converters.datetime_to_text(
        data, converters.config.PRETTY_DATETIME_FORMAT
    )
def display_record_lastmod(data):
    return converters.datetime_to_text(
        data, converters.config.PRETTY_DATETIME_FORMAT
    )

def display_status( data ):
    for c in STATUS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_public( data ):
    for c in PERMISSIONS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

def display_rights( data ):
    for c in RIGHTS_CHOICES:
        if data == c[0]:
            return c[1]
    return data

# title

DISPLAY_CREATORS = '{% if data.id %}' \
                   + '<a href="{{ data.id }}">{{ data.role }}: {{ data.namepart }}</a>' \
                   + '{% else %}' \
                   + '{{ data.role }}: {{ data.namepart }}' \
                   + '{% endif %}'

def display_creators( data ):
    return _display_multiline_dict(DISPLAY_CREATORS, data)

# extent

def display_language( data ):
    labels = []
    for c in LANGUAGE_CHOICES:
        if c[0] in data:
            labels.append(c[1])
    if labels:
        return ', '.join(labels)
    return ''

# organization
# description
# notes
# physloc
#
# acqinfo
# custodhist
# accruals
# processinfo
# accessrestrict
# userrestrict
# prefercite
#
# bioghist
#
# scopecontent
#
# relatedmaterial
# separatedmaterial

# The following are utility functions used by display_* functions.

def _display_multiline_dict( template, data ):
    t = []
    for d in data:
        if type(d) == type({}):
            t.append(converters.render(template, d))
        else:
            t.append(d)
    return '\n'.join(t)


# index_* --- format for Elasticsearch functions -----------------------
#
# These functions take Python data and format it for JSON.
#

def index_record_created(data):
    return converters.datetime_to_text(
        data, converters.config.ELASTICSEARCH_DATETIME_FORMAT
    )
def index_record_lastmod(data):
    return converters.datetime_to_text(
        data, converters.config.ELASTICSEARCH_DATETIME_FORMAT
    )



# formprep_* --- Form pre-processing functions.--------------------------
#
# These functions take Python data from the corresponding Collection field
# and format it so that it can be used in an HTML form.
#

# id

def formprep_record_created(data):
    if not data:
        data = datetime.now(converters.config.TZ)
    return data

def formprep_record_lastmod(data):
    if not data:
        data = datetime.now(converters.config.TZ)
    return data

# public
# rights
# title

def formprep_creators(data):
    return converters.rolepeople_to_text(data)

# extent
# language
# organization
# description
# notes
# physloc
#
# acqinfo
# custodhist
# accruals
# processinfo
# accessrestrict
# userrestrict
# prefercite
#
# bioghist
#
# scopecontent
#
# relatedmaterial
# separatedmaterial

# The following are utility functions used by formprep_* functions.

def _formprep_basic(data):
    if data:
        return json.dumps(data)
    return ''



# formpost_* --- Form post-processing functions ------------------------
#
# These functions take data from the corresponding form field and turn it
# into Python objects that are inserted into the Collection.
#

# id
# record_created
# record_lastmod
# public
# rights
# title
# unitdate_inclusive
# unitdate_bulk

def formpost_creators(text):
    return converters.text_to_rolepeople(text)

# extent
# language
# organization
# description
# notes
# physloc
#
# acqinfo
# custodhist
# accruals
# processinfo
# accessrestrict
# userrestrict
# prefercite
#
# bioghist
#
# scopecontent
#
# relatedmaterial
# separatedmaterial

# The following are utility functions used by formpost_* functions.

def _formpost_basic(data):
    if data:
        try:
            return json.loads(data)
        except:
            return data
    return ''
