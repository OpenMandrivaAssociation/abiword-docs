Name:       abiword-docs
Summary:    Documentation and helpfiles for Abiword
Version:    2.9.4
Release:    1
Group:      Office
URL:        http://www.abisource.com/
License:    GPLv2+
Source0:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
##########################################################################
# dirty hack: abiword cant generate part of its own docs under x86_64!!! #
source1:    abiword-docs-2.9.4.htmls.tar.gz
##########################################################################
BuildArch:  noarch
BuildRequires:	abiword-devel >= 2.9
BuildRequires:  pkgconfig(libglade-2.0)

%description
Documentation and helpfiles for Abiword.

#--------------------------------------------
%package en
Summary: English documentation and helpfiles for Abiword
Group: Office
Requires: locales-en
Provides: abiword-doc

%description en
English documentation and helpfiles for Abiword.

%files en
%{_datadir}/abiword*/help/en-US

#--------------------------------------------
%package fr
Summary: French documentation and helpfiles for Abiword
Group: Office
Requires: locales-fr
Provides: abiword-doc

%description fr
French documentation and helpfiles for Abiword.

%files fr
%{_datadir}/abiword*/help/fr-FR

#--------------------------------------------
%package pl
Summary: Polish documentation and helpfiles for Abiword
Group: Office
Requires: locales-pl
Provides: abiword-doc

%description pl
Polish documentation and helpfiles for Abiword.

%files pl
%{_datadir}/abiword*/help/pl-PL

#--------------------------------------------

%prep
%setup -q
##########################################################################
# dirty hack: abiword cant generate part of its own docs under x86_64!!! #
if [ "%{_build_arch}" == "x86_64" ]; then
tar -xf %{SOURCE1} -C ABW
fi
##########################################################################
 
%build
%configure2_5x
%make

%install
%makeinstall_std



%changelog
* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 2.8.6-1mdv2011.0
+ Revision: 633940
- update to new version 2.8.6

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.4-2mdv2011.0
+ Revision: 609904
- rebuild

* Sun Apr 18 2010 Funda Wang <fwang@mandriva.org> 2.8.4-1mdv2010.1
+ Revision: 536083
- new version 2.8.4

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 2.8.3-1mdv2010.1
+ Revision: 531236
- new version 2.8.3

* Sat Feb 13 2010 Funda Wang <fwang@mandriva.org> 2.8.2-1mdv2010.1
+ Revision: 505499
- New version 2.8.2

* Fri Oct 30 2009 Frederic Crozat <fcrozat@mandriva.com> 2.8.1-1mdv2010.0
+ Revision: 460236
- Release 2.8.1

* Wed Oct 28 2009 Frederic Crozat <fcrozat@mandriva.com> 2.8.0-1mdv2010.0
+ Revision: 459642
- Fix builrequires
- Release 2.8.0

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 2.7.8-1mdv2010.0
+ Revision: 419502
- import abiword-docs

