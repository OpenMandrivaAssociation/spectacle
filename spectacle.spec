#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	The new screenshot capture utility, replaces KSnapshot
Name:		spectacle
Version:	6.4.4
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		System/Base
URL:		https://www.kde.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/spectacle/-/archive/%{gitbranch}/spectacle-%{gitbranchd}.tar.bz2#/spectacle-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/spectacle-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Svg)
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
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(kImageAnnotator-Qt6)
BuildRequires:	cmake(kColorPicker-Qt6)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(LayerShellQt) >= 5.27.80
BuildRequires:	cmake(KPipeWire) >= 5.27.60
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(ZXing)
BuildRequires:	cmake(OpenCV)
# For /usr/bin/qdbus
Requires:	qt6-qttools-dbus
# Renamed after 6.0 2025-05-03
%rename plasma6-spectacle

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
The new screenshot capture utility, replaces KSnapshot.

%patchlist

%files -f %{name}.lang
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
