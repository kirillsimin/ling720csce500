from os import listdir

files = listdir('.')
essayClasses = []

for file in files:
    if '__' not in file and 'pyc' not in file:
        module = file.replace('.py','')
        essayClasses.append(module)
    


__all__ = essayClasses

#print (__all__)