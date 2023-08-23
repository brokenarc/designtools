# Design Tools

This is where I keep assorted Python scripts I write that support design tasks.

## Scripts

### extract_swatches

Extracts hexadecimal color codes from a text file and generates an SVG with
swatches of those colors.

#### Usage

`python -m designtools.extract_swatches [-h] text_file [swatch_file]`

#### Arguments

- `text_file` : The text file to extract color codes from. This may be any text
  file that contains hexadecimal color codes.
- `swatch_file` : Optional. The name of the SVG file to create. If the argument
  is not given, the script will create a file with the same base name as the
  input file and append the extension `.swatches.svg`.
- `-h`, `--help` : show the help message and exit.

### scale_sequence

Scales known numeric sequences around a given value and writes them as columns
in a CSV file with sequence names in the first row.

Known sequences: Golden powers (20 values), Fibonacci (41 values), Lucas (39
values), Pell (32 values), Pell-Lucas (31 values), Metallic means (20 values)

#### Usage

`python -m designtools.scale_sequence [-h] [--offset OFFSET] file value`

#### Arguments

- `file` : The name of the CSV file to generate. This file will be overwritten
  if it already exists.
- `value` : The number to scale the sequences around.
- `--offset OFFSET` : Optional. The index within the sequence that should equal
  the given value after scaling. If offset is not given, the offset will be set
  to half the middle of the shortest known sequence.
- `-h`, `--help` : show the help message and exit.

### make_sequence

Generates numeric sequences using known ratios and writes them as columns in a
CSV file with sequence names in the first row.

Known ratios: Golden ratio, Supergolden ratio, Silver ratio, Plastic number,
Minor second, Major second, Minor third, Major third, Perfect fourth, Augmented
fourth, Perfect fifth

#### Usage

`python -m designtools.make_sequence [-h] [--count COUNT] file seed`

#### Arguments

- `file` : The name of the CSV file to generate. This file will be overwritten
  if it already exists.
- `seed` : The value to build the sequence around. This value will be in the
  middle of the returned sequence. This value may be a float or integer.
- `--count COUNT` : The number of items to be created before and after the seed
  value in the sequences. The count will default to 5 if not given. The length
  of each generated sequence will always be `2 * count + 1`.
- `-h`, `--help` : show the help message and exit.

## Modules

- `designtools.color` contains utilities for converting, grouping, and sorting
  colors.
- `designtools.graphics` contains a utility for rendering color swatches as an
  SVG image.
- `designtools.mathutil` contains various mathematical constants, sequences,
  and utilities. This includes things like the Golden Ratio, Golden Angle, Pell
  numbers, and the Fibonacci sequence.
