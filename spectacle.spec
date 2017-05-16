Summary:	The new screenshot capture utility, replaces KSnapshot
Name:		spectacle
Version:	17.04.0
Release:	2
License:	GPLv2+
Group:		System/Base
URL:		https://www.kde.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5X11Extras)
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
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Kipi)
Obsoletes:	ksnapshot < 2:15.12.0
Provides:	ksnapshot = 2:15.12.0
Obsoletes:	ksnapshot-handbook < 2:15.12.0
Provides:	ksnapshot-handbook = 2:15.12.0

%description
The new screenshot capture utility, replaces KSnapshot.

%files -f %{name}.lang
%{_bindir}/spectacle
%{_datadir}/applications/org.kde.spectacle.desktop
%{_datadir}/metainfo/org.kde.spectacle.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_iconsdir}/*/*/*/*
%{_datadir}/khotkeys/spectacle.khotkeys
%{_datadir}/knotifications5/spectacle.notifyrc
%doc %{_docdir}/HTML/en/spectacle
%lang(ca) %doc %{_docdir}/HTML/ca/spectacle
%lang(es) %doc %{_docdir}/HTML/es/spectacle
%lang(it) %doc %{_docdir}/HTML/it/spectacle
%lang(nl) %doc %{_docdir}/HTML/nl/spectacle
%lang(pt_BR) %doc %{_docdir}/HTML/pt_BR/spectacle
%lang(sv) %doc %{_docdir}/HTML/sv/spectacle
%lang(uk) %doc %{_docdir}/HTML/uk/spectacle

#--------------------------------------------------------------------


%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}
