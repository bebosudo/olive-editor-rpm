%global shortname   olive
%global appname     org.olivevideoeditor.Olive
%global mimetype    application-vnd.olive-project

# RHEL 7 provides cmake 2 and cmake 3, so we force the use of cmake3
%if 0%{?rhel}
%global cmake       %cmake3
%endif

Name:       olive-editor
Version:    0.1.2
Release:    1%{?dist}
Summary:    Professional open-source NLE video editor
License:    GPLv3
URL:        https://www.olivevideoeditor.org
Source0:    https://github.com/%{name}/%{shortname}/archive/%{version}.tar.gz
Patch0:     olive.patch

%{?rhel:BuildRequires:      qt5-qtbase-devel, qt5-qtmultimedia-devel, qt5-qtsvg-devel, qt5-linguist}
%{?rhel:BuildRequires:      cmake3}
%{?fedora:BuildRequires:    cmake}
BuildRequires:              gcc, ffmpeg-devel, frei0r-devel
BuildRequires:              desktop-file-utils, libappstream-glib
BuildRequires:              mesa-libGL-devel,

%{?rhel:Requires:    qt5-qtbase}
%{?fedora:Requires:  qt5}

%description
Olive is a free non-linear video editor aiming to provide a fully-featured
alternative to high-end professional video editing software.


%package doc
Summary: Development documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
Olive is a free non-linear video editor aiming to provide a fully-featured
alternative to high-end professional video editing software.

This package contains doxygen-generated html API documentation for %{name}.


%prep
%autosetup -p1 -n %{shortname}-%{version}

%build
%cmake -DBUILD_DOXYGEN=ON .
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}
mv docs/ %{buildroot}%{_docdir}/%{name}

# RHEL uses /usr/share/appdata/ as metainfo dir, so move to it.
%{?rhel: mv %{buildroot}%{_datadir}/metainfo/ %{buildroot}%{_metainfodir}}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml


%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_metainfodir}/%{appname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.png
%{_datadir}/icons/hicolor/*/mimetypes/%{mimetype}.png

%files doc
%license LICENSE
%doc %{_docdir}/%{name}



%changelog
* Mon Nov 11 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 0.1.2-1
- Update to 0.1.2

* Sat Aug 24 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 0.1.0-2
- Use cmake3 macro for RHEL 7

* Fri May 10 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 0.1.0-1
- Update to 0.1.0 release
- No more need to explicitly compile with -DOpenGL_GL_PREFERENCE=LEGACY, see #810
- Move doxygen compilation inside cmake, see #759
- RHEL 6/7 build still not available due to cmake >= 3.9 requirement

* Sun Apr 21 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 20190420gitc5f63ec-1
- Update upstream to new nightly release

* Sat Apr 20 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 20190420git3251a42-1
- Update upstream
- Fix dependencies for rhel and derivatives

* Sat Apr 13 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 20190405git6264123-1
- Initial RPM release
