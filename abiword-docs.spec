Summary:	Documentation and help files for Abiword
Name:		abiword-docs
Version:	3.0.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		http://www.abisource.com/
Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
BuildRequires:	abiword-devel >= 3.0
BuildRequires:	pkgconfig(libglade-2.0)
# Exclude some pages pending http://bugzilla.abisource.com/show_bug.cgi?id=13459
Patch0:		abiword-docs-2.9.4-mga-temp_build_fix-en-US-Makefile.in.patch
Patch1:		abiword-docs-2.9.4-mga-temp_build_fix-pl-PL-Makefile.in.patch
Patch2:		abiword-docs-2.9.4-mga-temp_build_fix-fr-FR-Makefile.in.patch
BuildArch:	noarch

%description
Documentation and help files for Abiword.

#----------------------------------------------------------------------------

%package en
Summary:	English documentation and help files for Abiword
Requires:	locales-en
Provides:	abiword-doc = %{EVRD}
BuildArch:	noarch

%description en
English documentation and help files for Abiword.

%files en
%{_datadir}/abiword*/help/en-US
%dir %{_datadir}/abiword*/help/

#----------------------------------------------------------------------------

%package fr
Summary:	French documentation and help files for Abiword
Requires:	locales-fr
Provides:	abiword-doc = %{EVRD}
BuildArch:	noarch

%description fr
French documentation and help files for Abiword.

%files fr
%{_datadir}/abiword*/help/fr-FR
%dir %{_datadir}/abiword*/help/

#----------------------------------------------------------------------------

%package pl
Summary:	Polish documentation and help files for Abiword
Requires:	locales-pl
Provides:	abiword-doc = %{EVRD}
BuildArch:	noarch

%description pl
Polish documentation and help files for Abiword.

%files pl
%{_datadir}/abiword*/help/pl-PL
%dir %{_datadir}/abiword*/help/

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .abiword-docs-2.9.4-mga-temp_build_fix-en-US-Makefile.in.patch
%patch1 -p0 -b .abiword-docs-2.9.4-mga-temp_build_fix-pl-PL-Makefile.in.patch
%patch2 -p0 -b .abiword-docs-2.9.4-mga-temp_build_fix-fr-FR-Makefile.in.patch

%build
%configure2_5x
%make

%install
%makeinstall_std

