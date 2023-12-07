Summary:	The new screenshot capture utility, replaces KSnapshot
Name:		plasma6-spectacle
Version:	24.01.80
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		https://www.kde.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/spectacle-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(kImageAnnotator)
BuildRequires:	cmake(kColorPicker)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(KPipeWire) < 6.27.60
Obsoletes:	ksnapshot < 2:16.12.0
Provides:	ksnapshot = 2:16.12.0
Obsoletes:	ksnapshot-handbook < 2:16.12.0
Provides:	ksnapshot-handbook = 2:16.12.0
# For /usr/bin/qdbus
Requires:	qt6-qttools-qtdbus

%description
The new screenshot capture utility, replaces KSnapshot.

%files -f spectacle.lang
%{_datadir}/qlogging-categories6/spectacle.categories
%{_bindir}/spectacle
%{_datadir}/applications/org.kde.spectacle.desktop
%{_datadir}/metainfo/org.kde.spectacle.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_iconsdir}/*/*/*/*
%{_datadir}/knotifications6/spectacle.notifyrc
%{_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_mandir}/man1/*.1*
%{_libdir}/kconf_update_bin/*
%{_datadir}/kconf_update/*
%{_datadir}/dbus-1/services/org.kde.spectacle.service
%{_prefix}/lib/systemd/user/app-org.kde.spectacle.service

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n spectacle-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang spectacle --with-html --with-man
