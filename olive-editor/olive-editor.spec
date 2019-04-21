%global commit      c5f63ec2c5511e4af0f4a5a839dbfd995bd77fd4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global shortname   olive
%global appname     org.olivevideoeditor.Olive

Name:       olive-editor
Version:    20190420git%{shortcommit}
Release:    1%{?dist}
Summary:    Professional open-source NLE video editor

License:    GPLv3
URL:        https://www.olivevideoeditor.org
Source0:    https://github.com/%{name}/%{shortname}/archive/%{commit}/%{shortname}-%{shortcommit}.tar.gz

%{?rhel:BuildRequires:    qt5-qtbase-devel}
%{?fedora:BuildRequires:  qt5-devel}
BuildRequires:  ffmpeg-devel
BuildRequires:  frei0r-devel
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

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
%autosetup -n %{shortname}-%{commit}

%build
%cmake -DOpenGL_GL_PREFERENCE=LEGACY .
%make_build

%install
%make_install

doxygen
mkdir -p %{buildroot}%{_docdir}/%{name}
mv docs/ %{buildroot}%{_docdir}/%{name}

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

%files doc
%license LICENSE
%doc %{_docdir}/%{name}



%changelog
* Sun Apr 21 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 20190420gitc5f63ec-1
- Update upstream to new nightly release

* Sat Apr 20 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 20190420git3251a42-1
- Update upstream
- Fix dependencies for rhel and derivatives

* Sat Apr 13 2019 Alberto Chiusole <bebo.sudo@gmail.com> - 20190405git6264123-1
- Initial RPM release
