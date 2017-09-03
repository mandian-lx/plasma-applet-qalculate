Summary:	Qalculate! applet for plasma desktop 
Name:		plasma-applet-qalculate
Version:	0.3.1
Release:	1
License:	GPLv2.0+ and CC0 and LGPLv2.1+
Group:		Graphical desktop/KDE
Url:		https://store.kde.org/p/1155946/
Source0:	https://github.com/dschopf/qalculate/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake >= 2.8.12
BuildRequires:	cmake(ECM) >= 5.4.0
BuildRequires:	cmake(KF5Plasma) >= 5.0.0
BuildRequires:	cmake(Qt5Core) >= 5.4.0
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	pkgconfig(libqalculate) >= 0.9.8
BuildRequires:	readline-devel

%description
A calculator plasma widget which uses the Qalculate! library to provide lots
of features like unit calculation or currency conversion.

%files  -f plasma_applet_org.kde.plasma.qalculate.lang
%dir %{_kde5_datadir}/plasma/plasmoids/org.kde.plasma.qalculate/
%{_kde5_datadir}/plasma/plasmoids/org.kde.plasma.qalculate/*
%{_kde5_datadir}/metainfo/org.kde.plasma.qalculate.appdata.xml
%{_kde5_qmldir}/org/kde/private/qalculate/libplasmoidplugin.so
%{_kde5_qmldir}/org/kde/private/qalculate/qmldir
%{_kde5_services}/plasma-applet-org.kde.plasma.qalculate.desktop

#---------------------------------------------------------------------------

%prep
%setup -q -n qalculate-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

# locales
%find_lang plasma_applet_org.kde.plasma.qalculate

