STAGES=treecorr  tomography pz_stack 

OWNER=joezuntz
BASENAME=desc-pipe
VERSION=1.0


LOGS := $(STAGES:%=build/%.log) build/base.log

.DEFAULT_GOAL := all

all: $(STAGES)

.PHONY: base $(STAGES) clean all

base: build/base.log

$(STAGES): % :  build/%.log

build/base.log: base/Dockerfile
	docker build -t ${OWNER}/${BASENAME}-base:${VERSION} ./base 2>&1 | tee $@

build/%.log :  %/* build/base.log
	docker build -t ${OWNER}/${BASENAME}-$*:${VERSION} ./$* 2>&1 | tee $@

clean:
	rm -f $(LOGS)
