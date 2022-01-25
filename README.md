#Swen331 Fuzzer Project
Contributor: Amy Do

Installation:
   Python: 3.*
   pip3 install mechanicalsoup
   pip3 install argparse

Command:
python3 fuzz.py [discover|test] URL OPTIONS

Options:
--custom-auth=string     Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa).
