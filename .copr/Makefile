rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')
.PHONY: prepare srpm rpm

prepare:
	dnf -y install rpmdevtools rpm-build
	compgen -G "*.patch" >/dev/null && cp *.patch $(rpmbuild_src)
	spectool -g -R $(spec)

srpm: prepare
	rpmbuild -bs --define "_srcrpmdir $(outdir)" $(spec)

# Not used by COPR, but it's useful for local builds.
rpm: prepare
	rpmbuild -bb --define "_rpmdir $(outdir)" $(spec)
