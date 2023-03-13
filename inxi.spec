%global __requires_exclude ^perl\\((the)
%define patch_set 1

Summary:	Command line system information script for console and IRC
Name:		inxi
Version:	3.3.25
Release:	1
License:	GPLv3
Group:		System/Configuration/Other
URL:		http://smxi.org/docs/inxi.htm
Source0:	https://github.com/smxi/inxi/archive/%{version}-%{patch_set}/%{name}-%{version}-%{patch_set}.tar.gz

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
%package 	konversation
Summary:	Plugin for konversation
Group:		System/Configuration/Other
BuildRequires:	cmake(ECM)
Requires:       konversation
Requires:       %{name} = %{EVRD}

%description 	konversation
Plugin to allow %{name} to be easily used in konversation.

%files konversation
%{_kde5_datadir}/konversation/scripts/%{name}

#---------------------------------------------------
%package 	quassel
Summary:	Plugin for quassel
Group:		Development/KDE and Qt
BuildRequires:	cmake(ECM)
Requires:	quassel
Requires:	%{name} >= %{EVRD}

%description 	quassel
Plugin to allow %{name} to be easily used in quassel.

%files quassel
%{_kde5_datadir}/quassel/scripts/%{name}

#---------------------------------------------------

%prep
%autosetup -n %{name}-%{version}-%{patch_set}

%build
# nothing here

%install
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}%{_kde5_datadir}/konversation/scripts
cd %{buildroot}%{_kde5_datadir}/konversation/scripts/
ln -s %{_bindir}/%{name} %{name}
cd -
mkdir -p %{buildroot}%{_kde5_datadir}/quassel/scripts
cd %{buildroot}%{_kde5_datadir}/quassel/scripts/
ln -s %{_bindir}/%{name} %{name}
cd -
