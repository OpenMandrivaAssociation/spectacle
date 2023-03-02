Summary:	The new screenshot capture utility, replaces KSnapshot
Name:		spectacle
Version:	22.12.3
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		https://www.kde.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	cmake(KF5Screen) >= 5.6.0-2
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KDEExperimentalPurpose)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(kImageAnnotator)
BuildRequires:	cmake(kColorPicker)
Obsoletes:	ksnapshot < 2:15.12.0
Provides:	ksnapshot = 2:15.12.0
Obsoletes:	ksnapshot-handbook < 2:15.12.0
Provides:	ksnapshot-handbook = 2:15.12.0
# For /usr/bin/qdbus
Requires:	qt5-qttools-qtdbus

%description
The new screenshot capture utility, replaces KSnapshot.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/spectacle.categories
%{_bindir}/spectacle
%{_datadir}/applications/org.kde.spectacle.desktop
%{_datadir}/metainfo/org.kde.spectacle.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_iconsdir}/*/*/*/*
%{_datadir}/knotifications5/spectacle.notifyrc
%{_libdir}/kconf_update_bin/spectacle-migrate-shortcuts
%{_libdir}/kconf_update_bin/spectacle-migrate-rememberregion
%{_datadir}/kconf_update/spectacle_rememberregion.upd
%{_datadir}/kconf_update/spectacle_newConfig.upd
%{_datadir}/kconf_update/spectacle_shortcuts.upd
%{_datadir}/kconf_update/50-clipboard_settings_change.py
%{_datadir}/kconf_update/spectacle_clipboard.upd
%{_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_prefix}/lib/systemd/user/app-org.kde.spectacle.service
%{_mandir}/man1/*.1*

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html --with-man
