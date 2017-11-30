STAGES=treecorr  tomography pz_stack
DM_STAGES=
OWNER=joezuntz
BASENAME=desc-pipe
VERSION=1.0



LOGS := $(STAGES:%=build/%.log) $(DM_STAGES:%=build/%.log) build/base.log
PUSHES := $(STAGES:%=build/.push-%) $(DM_STAGES:%=build/.push-%)
PULLS := $(STAGES:%=pull-%) $(DM_STAGES:%=pull-%)

# Decide how to pull
ifdef NERSC_HOST
	PULLCMD=shifterimg pull docker:
else
	PULLCMD=docker pull 
endif

.DEFAULT_GOAL := all

all: $(STAGES) $(DM_STAGES)

.PHONY: base $(STAGES) $(DM_STAGES) clean all push $(PULLS) pull

base: build/base.log
base-dm: build/base-dm.log

$(STAGES): % :  build/%.log
$(DM_STAGES): % :  build/%.log

build/base.log: base/Dockerfile ../dist/descpipe-1.2.tar.gz
	cp ../dist/descpipe-1.2.tar.gz base/
	docker build -t ${OWNER}/${BASENAME}-base:${VERSION} ./base 2>&1 | tee $@

build/base-dm.log: base/Dockerfile
	docker build -t ${OWNER}/${BASENAME}-base-dm:${VERSION} ./base 2>&1 | tee $@

build/%.log :  %/* build/base.log
	docker build -t ${OWNER}/${BASENAME}-$*:${VERSION} ./$* 2>&1 | tee $@

push:  $(PUSHES)

pull: $(PULLS)

$(PUSHES): build/.push-%: build/%.log
	docker push ${OWNER}/${BASENAME}-$*:${VERSION}
	touch build/.push-$*

$(PULLS): pull-%:
	$(PULLCMD)${OWNER}/${BASENAME}-$*:${VERSION}

clean:
	rm -f $(LOGS)
