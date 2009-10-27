Name:       abiword-docs
Summary:    Documentation and helpfiles for Abiword
Version:    2.8.0
Release:    %mkrel 1
Group:      Office
URL:        http://www.abisource.com/
License:    GPLv2+
Source0:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
BuildRoot:  %_tmppath/%name-%version-buildroot
BuildArch:  noarch
BuildRequires:	abiword-devel >= %{version}

%description
Documentation and helpfiles for Abiword.

#--------------------------------------------
%package en
Summary: English documentation and helpfiles for Abiword
Group: Office
Requires: locales-en
Obsoletes: abiword-doc-en < 2.7.8
Provides: abiword-doc

%description en
English documentation and helpfiles for Abiword.

%files en
%defattr(-,root,root)
%{_datadir}/abiword*/help/en-US

#--------------------------------------------
%package fr
Summary: French documentation and helpfiles for Abiword
Group: Office
Requires: locales-fr
Obsoletes: abiword-doc-fr < 2.7.8
Provides: abiword-doc

%description fr
French documentation and helpfiles for Abiword.

%files fr
%defattr(-,root,root)
%{_datadir}/abiword*/help/fr-FR

#--------------------------------------------
%package pl
Summary: Polish documentation and helpfiles for Abiword
Group: Office
Requires: locales-pl
Obsoletes: abiword-doc-pl < 2.7.8
Provides: abiword-doc

%description pl
Polish documentation and helpfiles for Abiword.

%files pl
%defattr(-,root,root)
%{_datadir}/abiword*/help/pl-PL

#--------------------------------------------

%prep
%setup -q -n %{name}-%{version}
 
%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

