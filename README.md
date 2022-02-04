#Swen331 Fuzzer Project
Contributor: Amy Do

Installation:

   Python: 3.*
   pip3 install mechanicalsoup
   pip3 install argparse

  fuzz [discover | test] url OPTIONS

  COMMANDS:

    discover :  Output a comprehensive, human-readable list of all discovered inputs to the system. Techniques include both crawling and guessing.
    test    :  Discover all inputs, then attempt a list of exploit vectors on those inputs. Report anomalies that could be vulnerabilities.

  OPTIONS:
    Options can be given in any order.

    --custom-auth=string     Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa).

    Discover options:
      --common-words=file    Newline-delimited file of common words to be used in page guessing. Required.
      --extensions=file      Newline-delimited file of path extensions, e.g. ".php". Optional. Defaults to ".php" and the empty string if not specified
