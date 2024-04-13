# Directory Search Tool (FUZZER)

![FUZZER Logo](https://static.thenounproject.com/png/2221438-200.png)



> [!IMPORTANT]
> The current author does not own the repository. It is owned by [Shivang](https://github.com/shivangmauryaa/pytha-fuzz). This is just a module distribution instead of direct source code. Kindly star the original repository if you want to.



## Introduction

FUZZER is a simple pytha-fuzz tool developed by Shivang-Maurya It helps you discover directories on a target website by probing different paths. This tool is designed for security testing, web application analysis, and penetration testing.

## Features

- Fast and efficient directory scanning
- Customizable User-Agent header
- Option to follow HTTP redirects
- Verbose mode for detailed output
- Save results to an output file
- Colorful and user-friendly command-line interface

## Installation

1. Install from Build:
   ```shell
   git clone https://github.com/shivangmauryaa/pytha-fuzz.git
   cd pytha-fuzz
   python setup.py install
   ```
2. Install from PyPi as Module (Recommended):
   ```shell
   pip install pytha-fuzz
   ```

## Usage

Use the following command-line arguments to run pytha-fuzz:
```shell
-u or --url: The target URL to search (required).
-w or --wordlist: Wordlist file containing directories to check.
-t or --timeout: Timeout for HTTP requests (default: 5.0 seconds).
-ua or --user-agent: Custom User-Agent header for HTTP requests (default: DirectorySearchBot).
-f or --follow-redirects: Follow HTTP redirects (optional).
-v or --verbose: Enable verbose mode (optional).
-o or --output: Output file to save results (optional).
```

Example usage:
```shell
fuzz -u http://example.com -w wordlist.txt -o output.txt    // Custom
fuzz -u http://example.com // Auto
```



## Author
[Shivang Maurya](https://github.com/shivangmauryaa)
<br>
[![Linkden](https://github.com/halfstackpgr/pytha-fuzz/assets/118044992/5c0af136-eafa-4641-ae73-4b683c582f64)](https://www.linkedin.com/in/shivangmauryaa/)
<br>



#### Dist Maintainer:
[halfstackpgr](https://github.com/halfstackpgr/pytha-fuzz)


## License

This tool is licensed under the MIT License. See the LICENSE file for details.

## Support
For bug reports, feature requests, or general inquiries, please create an issue. for more good result use your self made wordlist 
