Name:           wf-shell
Version:        0.7.0
Release:        1
Summary:        A GTK3-based panel for wayfire
License:        MIT
Group:          Wayfire
URL:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wf-config)

%description
wf-shell is a repository which contains the various components needed to built a fully functional DE based around wayfire. Currently it has only a GTK-based panel and background client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -D -m 0644 wf-shell.ini.example %{buildroot}%{_datadir}/wayfire/wf-shell.ini.example

%files
%{_bindir}/wf-*
%{_bindir}/wayland-logout
#{_datadir}/wayfire/
%{_datadir}/wayfire/wf-shell.ini.example
%{_datadir}/wayfire/icons/wayfire.png
%{_datadir}/wayfire/metadata/
%{_datadir}/wayfire/wallpaper.jpg

%files devel
%{_libdir}/pkgconfig/wf-shell.pc
