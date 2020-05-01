''' constants '''
RESOURCE_TYPES = [
    ('RASTER_DATA', 'Raster data'),
    ('TABULAR_DATA', 'Tabular data'),
    ('MAP', 'Map'),
    ('VISUALIZATION', 'Visualization'),
    ('DOCUMENTATION', 'Documentation'),
    ('REPORT', 'Report',)
]


DATA_SOURCES = [
    ('Sample based', [
        "NFI", "State of Europe's Forests", "Forest Resource Assessment"
    ]),
    ('Raster based',
        ["Forest Map / HRL Forest", "Corine Land Cover", "Global Forest Watch",
         "Maltese Planning Authority"]
     ),
]

NUTS_LEVELS = [
    ('nuts_level0', 'Level 0'),
    ('nuts_level1', 'Level 1'),
    ('nuts_level2', 'Level 2'),
    ('nuts_level3', 'Level 3'),
    ('nuts_level4', 'Level 4'),
]

DATASETS = ['NFI', 'FAO', 'FRA', 'GFW', 'Alpine Convention', 'SoEF']

GEOCOVERAGE_REGIONS = [
    'EEA39',
    'EU28',
    'FAO234',
    'SOEF46',
    # ... TODO: fill in with other countries
]

ACCESSIBILITY_LEVELS = [
    ('public', 'Publicly available',),
    ('registration', 'Download with registration or request'),
    ('restricted', 'Restricted')
]

INFO_LEVELS = ['A', 'B', 'C', 'D', 'E']
