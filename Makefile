
all: resources_rc.py

clean: 	
	rm -f resources_rc.py
	rm -f *.pyc *~

# sudo ln -s /usr/lib/qt6/libexec/rcc /usr/local/bin/rcc
resources_rc.py: resources.qrc
	rcc -g python -o resources_rc.py resources.qrc
