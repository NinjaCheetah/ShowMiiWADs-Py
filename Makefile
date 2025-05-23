CC=python -m nuitka
ARCH_FLAGS?=

all:
	# python build_translations.py
	$(CC) --show-progress --assume-yes-for-downloads ShowMiiWADs-Py.py $(ARCH_FLAGS) -o ShowMiiWADs-Py

install:
	rm -rd /opt/ShowMiiWADs-Py/
	install -d /opt/ShowMiiWADs-Py
	cp -r ./ShowMiiWADs-Py.dist/* /opt/ShowMiiWADs-Py/
	chmod 755 /opt/ShowMiiWADs-Py/
	install ./packaging/icon.png /opt/ShowMiiWADs-Py/ShowMiiWADs-Py.png
	install ./packaging/ShowMiiWADs-Py.desktop /usr/share/applications

clean:
	rm ShowMiiWADs-Py
	rm -rd ShowMiiWADs-Py.build/
	rm -rd ShowMiiWADs-Py.dist/
	rm -rd ShowMiiWADs-Py.onefile-build/
