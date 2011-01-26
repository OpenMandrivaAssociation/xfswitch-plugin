Summary:	User switching plugin for Xfce desktop environment
Name:		xfswitch-plugin
Version:	0.0.1
Release:	%mkrel 8
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfswitch-plugin/
Source0:	http://goodies.xfce.org/releases/xfswitch-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4-panel-devel >= 4.7.0
BuildRequires:	libxfcegui4-devel
Requires:	gdm
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/%{name}.desktop
