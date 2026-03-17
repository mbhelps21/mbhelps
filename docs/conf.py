project = 'MB Helps'
author = 'MB Helps'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    <meta name="google-site-verification" content="Cva8KgvW-eQpRtsdf8vIcSb023IJtLJfC8PxJAlQ0mc" />
     <meta name="msvalidate.01" content="B807FE4A03DB636D50EF7962DDBBE11F" />
    """
}

# Base URL for sitemap
html_baseurl = 'https://mbhelps1.readthedocs.io/en/latest/'
