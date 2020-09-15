# If it is tizen, we can export Tizen API packages.
%bcond_with tizen

Name:		nnstreamer-extra
Summary:	Extra support for nnstreamer
Version:	0.0.1
Release:	0
Group:		Applications/Multimedia
Packager:	Parichay Kapoor <pk.kapoor@samsung.com>
License:	LGPL-2.1
Source0:	nnstreamer-extra-%{version}.tar.gz
Source1001:	nnstreamer-extra.manifest

BuildRequires: nnstreamer
Requires: nnstreamer
# Added to give error when installing on any other system other than CI
Conflicts: openssh

%description
This package provides extra utilities for nnstreamer.
For now, this modifies the installed nnstreamer.ini in the tizen,
setting enable_envvar to true, allowing running/testing of nnstreamer's
tensor filter extension not installed in the system.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install

%post
mv /etc/nnstreamer.ini /etc/nnstreamer.ini.bak

%postun
mv /etc/nnstreamer.ini.bak /etc/nnstreamer.ini

%files
%manifest nnstreamer-extra.manifest
%defattr(-,root,root,-)

%changelog
* Tue Sep 15 2020 Parichay Kapoor <pk.kapoor@samsung.com>
- Package editing of nnstreamer ini to allow envvar.
