Name:		inxi
Version:	1.9.18
Release:	2
License:	GPLv3
Group:		System/Configuration/Other
Summary:	A full featured system information script
URL:		http://code.google.com/p/inxi/
Source0:	inxi
Source1:	inxi.1
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
install -m644 %{SOURCE1} -D %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
