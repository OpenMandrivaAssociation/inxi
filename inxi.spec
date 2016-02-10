Name:		inxi
Version:	2.2.27
Release:	1
License:	GPLv3
Group:		System/Configuration/Other
Summary:	Command line system information script for console and IRC
URL:		http://code.google.com/p/inxi/
# obtaining source and version from svn :
# svn checkout http://inxi.googlecode.com/svn/trunk && cat trunk/inxi | grep "Version: "
# or if you know the version just: wget http://inxi.googlecode.com/svn/trunk/inxi.tar.gz -O %{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Source1:	README.urpmi

Requires:	glxinfo
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
BuildRequires:	kde4-macros
Requires:       konversation
Requires:       %{name} = %{EVRD}

%description 	konversation
Plugin to allow %{name} to be easily used in konversation.


%files konversation
%doc inxi.changelog
%{_kde_appsdir}/konversation/scripts/%{name}

#---------------------------------------------------
%prep
%setup -c
chmod -x inxi.changelog

%build
# nothing here

%install
# binary script
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
# man page
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1
# konversation-plugin
mkdir -p %{buildroot}%{_kde_appsdir}/konversation/scripts
pushd %{buildroot}%{_kde_appsdir}/konversation/scripts/
ln -s %{_bindir}/%{name} %{name}
popd

# inxi --recommends
install -m644 %{SOURCE1} README.urpmi
