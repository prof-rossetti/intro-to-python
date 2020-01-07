# The `fpdf` Package

> Thanks to @megc1 for surfacing the capabilities of this package

Reference:

  + [Homepage](https://pyfpdf.readthedocs.io/en/latest/)
  + [Official Tutorial](https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html)
  + [Source Code](https://github.com/reingart/pyfpdf)
  + [An unofficial Tutorial](http://www.blog.pythonlibrary.org/2018/06/05/creating-pdfs-with-pyfpdf-and-python/)

## Installation

First install the package using Pip, if necessary:

```sh
pip install fpdf
```

## Usage

A basic usage example to generate a new PDF document:

```py
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.output("my_generated_document.pdf", "F")
```

See the package documentation and tutorial for more examples.
