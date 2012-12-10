Name:		inxi
Version:	1.8.5
Release:	1
License:	GPLv3
Group:		System/Configuration/Other
Summary:	A full featured system information script
URL:		http://code.google.com/p/inxi/
Source0:	inxi
Source1:	inxi.8
BuildArch:	noarch

%description
Inxi: A full featured system information script

Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.
Check recommends to see what's needed for each extra feature. Check sources for
latest inxi version number.

%prep

%build

%install
install -m755 %{SOURCE0} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{SOURCE1} -D %{buildroot}%{_mandir}/man8/%{name}.8

%files
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Fri Jun 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.8.5-1
+ Revision: 805892
- imported package inxi


* Fri Jun  6 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.8.5-1
- initial release (requested by viking60)
