
PRIMARY_TARGET = testall
PRIMARY_LOG = $(MAIN_TARGET).log
KERNELS_TARGET = geometries/kernels

$(PRIMARY_TARGET): $(KERNELS_TARGET)
	( find . -name '*.py' \
	| grep -v '_algorithm[.]py$$' \
	| sort \
	| while read i \
	; do echo;echo;echo ================ $$i ================ \
	; python $$i -s 2025-06-01T00:01:00 -e 2025-06-01T01:01:00 -h 600 \
	; done \
	&& echo "make $@ Succeeded" \
	|| ( echo "make $@ Failed" && false ) \
	) \
	| tee $(PRIMARY_LOG)

$(KERNELS_TARGET):
	cd $$(dirname $@) \
	&& git clone \
	     --quiet -b btc_review_202503 --depth 1 \
	     https://github.com/drbitboy/Aspera_SPICE_kernels.git \
	     $$(basename $@)

clean:
	$(RM) $(PRIMARY_LOG)
