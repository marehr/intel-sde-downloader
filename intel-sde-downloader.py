#! /bin/env python

import os
import sys
import mechanicalsoup

if sys.version_info >= (3, 0):
    from urllib.parse import urlparse
if sys.version_info < (3, 0) and sys.version_info >= (2, 5):
    from urlparse import urlparse

results = {}
download_filename = sys.argv[1] if 1 < len(sys.argv) else "[EMPTY: NO ARGUMENT GIVEN]"
download_filename = download_filename.strip("intel-http-accept://")

# Connect to protected Intel Download Page
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://software.intel.com/content/www/us/en/develop/articles/pre-release-license-agreement-for-intel-software-development-emulator-accept-end-user-license-agreement-and-download.html")

# # Fill-in the search form
# print("Accept license")
# form = browser.select_form('#intel-licensed-dls-step-1')
# form.set_checkbox({'accept_license': 1})
# browser.submit_selected()

download_link_attribute = "href" # "data-id-url"

# Collect results
for link in browser.get_current_page().select('a[' + download_link_attribute + '$=".tar.bz2"]'):
    if ".tar.bz2" not in link.text:
        continue

    url = urlparse(link.attrs[download_link_attribute])
    filename = os.path.basename(url.path)

    results[filename] = link

# Download file
if download_filename in results:
    link = results[download_filename]
    url = link.attrs[download_link_attribute]
    link['href'] = url # override URL (URL is in `data-id-url`)

    print("Attempt to download", url)

    browser.download_link(link, download_filename)

    print("Download written to", download_filename)

# Display found filenames for debug purposes
else:
    print ("Not found:", download_filename)
    print ("Found versions: ")
    for filename, url in results.items():
        print(filename, ':', url)
