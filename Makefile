
all: resources_rc.py

clean: 	
	rm -f resources_rc.py
	rm -f *.pyc *~

# sudo ln -s /usr/lib/qt6/libexec/rcc /usr/local/bin/rcc
# Make sure to replace a PySide6 import from resources_rc.py!
resources_rc.py: resources.qrc
	rcc -g python -o resources_rc.py resources.qrc
