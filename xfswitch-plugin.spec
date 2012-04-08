Summary:	User switching plugin for Xfce desktop environment
Name:		xfswitch-plugin
Version:	0.0.1
Release:	%mkrel 9
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfswitch-plugin/
Source0:	http://goodies.xfce.org/releases/xfswitch-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4-panel-devel >= 4.7.0
BuildRequires:	libxfcegui4-devel
Requires:	gdm

%description
Xfswitch-plugin is a user switching plugin, which allows you 
to leave the current session opened and open a new session 
with another user.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/%{name}.desktop
