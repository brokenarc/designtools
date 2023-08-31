# Design Tools

This is where I keep assorted Python scripts I write that support design tasks.

- [Design Tools](#design-tools)
    - [Scripts](#scripts)
        - [extract\_swatches](#extract_swatches)
        - [scale\_sequence](#scale_sequence)
        - [make\_sequence](#make_sequence)
    - [Modules](#modules)
    - [Dependencies](#dependencies)

## Scripts

### extract_swatches

Extracts hexadecimal color codes from a text file and generates an SVG with
swatches of those colors.

Several styles of swatches are provided:

[![ball-grid swatches](./examples/img/example.ball-grid.png 'Sample of the "ball-grid" swatch style.')](./examples/example.ball-grid.svg)
`ball-grid` creates a grid of spheres for each color. The highlight has a
lighter, less saturated variation of the color. The shadow has a darker, more
saturated variant of the color.

[![circle-grid swatches](./examples/img/example.circle-grid.png 'Sample of the "circle-grid" swatch style.')](./examples/example.circle-grid.svg)
`circle-grid` creates a grid of circles for each color.

[![color-stack swatches](./examples/img/example.color-stack.png 'Sample of the "color-stack" swatch style.')](./examples/example.color-stack.svg)
`color-stack` groups colors by hue with overlapping color circles.

[![gradient-bar swatches](./examples/img/example.gradient-bar.png 'Sample of the "gradient-bar" swatch style.')](./examples/example.gradient-bar.svg)
`gradient-bar` groups colors by hue and creates a linear gradient using each
group. A stop is created for each color in the group and a group's stops are
equally spaced within that gradient.

[![square-grid swatches](./examples/img/example.square-grid.png 'Sample of the "square-grid" swatch style.')](./examples/example.square-grid.svg)
`square-grid` creates a grid of squares for each color.

#### Usage<!-- omit from toc -->

`python -m designtools.extract_swatches [-h] [--style {ball-grid,gradient-bar,square-grid,circle-grid,color-stack}] text_file [swatch_file]`

#### Arguments<!-- omit from toc -->

- `text_file` : The text file to extract color codes from. This may be any text
  file that contains hexadecimal color codes.
- `swatch_file` : Optional. The name of the SVG file to create. If the argument
  is not given, the script will create a file with the same base name as the
  input file and append the extension `.<style>.svg` where `<style>` is
  replaced with the swatch style ('`square-grid`' by default).
- `--style` : Optional. The style of swatches to render. Valid options are
  `ball-grid`, `gradient-bar`, `square-grid`, `circle-grid`, and `color-stack`.
- `-h`, `--help` : show the help message and exit.

### scale_sequence

Scales known numeric sequences around a given value and writes them as columns
in a CSV file with sequence names in the first row.

Known sequences: Golden powers (20 values), Fibonacci (41 values), Lucas (39
values), Pell (32 values), Pell-Lucas (31 values), Metallic means (20 values)

#### Usage<!-- omit from toc -->

`python -m designtools.scale_sequence [-h] [--offset OFFSET] file value`

#### Arguments<!-- omit from toc -->

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

#### Usage<!-- omit from toc -->

`python -m designtools.make_sequence [-h] [--count COUNT] file seed`

#### Arguments<!-- omit from toc -->

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
- `designtools.graphics.svg` contains a rudimentary (and very incomplete) SVG
  library based on `xml.etree.ElementTree`. It is not intended to be useful
  beyond the included scripts.
- `designtools.mathutil` contains various mathematical constants, sequences,
  and utilities. This includes things like the Golden Ratio, Golden Angle, Pell
  numbers, and the Fibonacci sequence.

## Dependencies

### Runtime<!-- omit from toc -->

None.

### Development<!-- omit from toc -->

- [pytest](https://pytest.org/) for tests
