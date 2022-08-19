Name:           wf-shell
Version:        0.7.0
Release:        0
Summary:        A GTK3-based panel for wayfire
License:        MIT
URL:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libpulse)
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
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -D -m 0644 wf-shell.ini.example %{buildroot}%{_datadir}/wayfire/wf-shell.ini.example
%fdupes %{buildroot}%{_prefix}

%files
%{_bindir}/wf-*
%{_bindir}/wayland-logout
%{_datadir}/wayfire/
%{_datadir}/wayfire/wf-shell.ini.example
%{_datadir}/wayfire/icons/*.png

%files devel
%{_libdir}/pkgconfig/wf-shell.pc
