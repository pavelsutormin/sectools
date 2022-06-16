# sectools
A tool for python to read and write sectors on a disc.
## examples
```python
import sectools
print('Current value of bootloader:\n'+str(sectools.readsec(disc='dev/sda1', sec=0)))
sectools.writesec(disc='dev/sda1', sec=0, data='\x00a new value\xaa')
print('New value of bootloader:\n'+str(sectools.readsec(disc='dev/sda1', sec=0)))
```
