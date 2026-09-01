%global __requires_exclude ^perl\\((the)
%define patch_set 1

Summary:	Command line system information script for console and IRC
Name:		inxi
Version:	3.3.41
Release:	1
License:	GPLv3
Group:		System/Configuration/Other
URL:		https://smxi.org/docs/inxi.htm
Source0:  https://codeberg.org/smxi/inxi/archive/%{version}-%{patch_set}/%{name}-%{version}-%{patch_set}.tar.gz
# GH source https://github.com/smxi/ is no longer used.

Requires:	glxinfo
Recommends:	perl(XML::Dumper)
Suggests:	lm_sensors
Suggests:	hddtemp
Suggests:	usbutils
Suggests:	xrandr
Suggests:	pciutils
Suggests:	procps
Suggests:	coreutils
Suggests:	gawk
Suggests:	sed
Suggests:	xprop
Suggests:	xset
BuildArch:	noarch
%rename inxi-konversation
%rename inxi-quassel

%description
inxi is a command line system information script built for console and IRC.
It is also used for forum technical support, as a debugging tool, to quickly
ascertain user system configuration and hardware.
inxi shows system hardware, CPU, drivers, Xorg, Desktop, kernel, GCC version,
processes, RAM usage, and a wide variety of other useful information.

%files
%doc inxi.changelog
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*

#---------------------------------------------------

%prep
%autosetup -p1 -n %{name}
#-n %{name}-%{version}-%{patch_set}

%build
# nothing here

%install
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
