
KERNELS_DIR = geometries/kernels

pytestall: kernels_check
	( find . -name '*.py' \
	| grep -v '_algorithm[.]py$$' \
	| grep -v 'GeoDriverCSV[.]py$$' \
	| grep -v 'geometries/kernels/' \
	| sort \
	| xargs pytest $$i \
	&& echo "make $@ Succeeded" \
	|| ( echo "make $@ Failed" && false ) \
	) \
	| tee $@.log

testall: kernels_check
	( find . -name '*.py' \
	| grep -v '_algorithm[.]py$$' \
	| grep -v 'geometries/kernels/' \
	| sort \
	| while read i \
	; do echo;echo;echo ================ $$i ================ \
	; python $$i -s 2025-06-01T00:01:00 -e 2025-06-01T01:01:00 -h 600 \
	|| exit 1 \
	; done \
	&& echo "make $@ Succeeded" \
	|| ( echo "make $@ Failed" && false ) \
	) \
	| tee $@.log

kernels_check:
	cd $(KERNELS_DIR) && make

clean:
	$(RM) pytestall.log testall.log
