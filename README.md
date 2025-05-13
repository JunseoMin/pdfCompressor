# pdfCompressor
.pdf extention file compressor

# Dependency
OS: ubuntu22.04(tested)

## macOS
```
brew install ghostscript
```
## Ubuntu/Debian
```
 sudo apt-get install ghostscript
 ```

# Usage
**Options**  
-q : set quality  
printer (72  dpi)  
screen  (150 dpi)  
e-book  (300 dpi) (default)  

```
python3 pdfCompressor.py path/to/original.pdf path/to/compressed.pdf -q printer
```